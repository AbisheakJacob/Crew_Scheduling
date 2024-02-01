# importing the packages
import numpy as np
import pandas as pd
from itertools import chain
from ortools.linear_solver import pywraplp
import time
from warnings import filterwarnings

filterwarnings("ignore")


# define the restricted master problem
def RMP(index, num_flights, pairings, cost_matrix):
    pairings_rmp = [pairings[i] for i in index]
    cost_matrix_rmp = cost_matrix[index].reshape(-1, 1)

    # Initializing the MIP Solver
    solver = pywraplp.Solver.CreateSolver("SAT")

    # creating the binary allocation variable
    x = np.array([solver.BoolVar("") for i in range(len(index))]).reshape(-1, 1)

    # Adding the constraints
    for i in range(num_flights):
        solver.Add(
            solver.Sum(
                [x[j][0] * 1.0 for j in range(len(index)) if i in pairings_rmp[j]]
            )
            == 1.0
        )

    # Objective function
    solver.Minimize(sum(cost_matrix_rmp[i][0] * x[i][0] for i in range(len(index))))

    # Solve the problem
    status = solver.Solve()

    # find the values of the decision variable
    x_values = [x[i][0].solution_value() for i in range(len(index))]

    # find the indices of the final selected pairs
    optimal_index = [
        value for value, binary_value in zip(index, x_values) if binary_value == 1
    ]

    return status, solver.Objective().Value(), optimal_index


# function to find the reduced cost matrix
def sub_problem(pairings, cost_matrix, index, num_pairs, num_flights):
    pairings_sp = [pairings[i] for i in index]
    cost_matrix_sp = cost_matrix[index].reshape(-1, 1)

    # Initializing the LP Solver
    solver = pywraplp.Solver.CreateSolver("GLOP")

    # creating the binary allocation variable
    x = np.array([solver.NumVar(0, 1, f"x_{i}") for i in range(len(index))]).reshape(
        -1, 1
    )

    # create a matrix that is the product of the decision variable and the pair matrix
    for i in range(num_flights):
        solver.Add(
            solver.Sum(
                [x[j][0] * 1.0 for j in range(len(index)) if i in pairings_sp[j]]
            )
            == 1.0
        )

    # Objective function
    solver.Minimize(sum(cost_matrix_sp[i][0] * x[i][0] for i in range(len(index))))

    # Solve the problem
    status = solver.Solve()

    # find the values of the decision variable
    dual_values = np.array(
        [constraint.dual_value() for constraint in solver.constraints()]
    )

    # find the reduced cost matrix
    red_cost_mtx = []

    for i in range(num_pairs):
        red_cost_mtx.append(
            cost_matrix[i]
            - sum([1 * dual_values[j] for j in range(num_flights) if j in pairings[i]])
        )

    return red_cost_mtx, np.argsort(red_cost_mtx)[:50].tolist()


# coloumn generation
def column_gen():
    # Reading the dataframe and converting it to a numpy array
    np_arr = pd.read_csv(
        "data/flight_legs/data.csv",
        parse_dates=["start_time", "end_time"],
    ).to_numpy()

    # read the duties from the txt file
    with open("data/pairings/pairings.txt") as file:
        pairings = [list(chain.from_iterable(eval(line))) for line in file]

    # calculate the cost matrix from pair list
    cost_matrix = np.array(
        [
            (np_arr[pair[-1]][4] - np_arr[pair[0]][3]).total_seconds() / 3600
            for pair in pairings
        ]
    )

    # determining the number of flights and tasks
    num_pairs = len(pairings)
    num_flights = len(np_arr)

    # initialization huerestics
    ini_pair, increment = 15000, 1000

    while True:
        # create a reduced pair array that contains atleast one feasible solution
        ini_index = np.argsort(cost_matrix)[:ini_pair].tolist()

        status, obj, index = RMP(ini_index, num_flights, pairings, cost_matrix)

        if status == 0.0:
            break

        ini_pair += increment
    # setting the timer
    start_time = time.time()
    timeout_seconds = 10

    # the column generation problem
    while True:
        # the RMP solves the problem for a small number of pairs
        status, obj, idx = RMP(index, num_flights, pairings, cost_matrix)

        # the sub problem finds the reduced cost matrix and the index of the least reduced cost
        red_cost_mtx, least_red_cost_index = sub_problem(
            pairings, cost_matrix, index, num_pairs, num_flights
        )

        index = index + least_red_cost_index

        if all(x >= 0 for x in red_cost_mtx) == True:
            break

        if time.time() - start_time >= timeout_seconds:
            break

    return idx
