# importing the packages
import numpy as np
from ortools.linear_solver import pywraplp
import time
from warnings import filterwarnings

filterwarnings("ignore")


# define the restricted master problem
def RMP(index, num_flights, pair_matrix, cost_matrix):
    pair_matrix = pair_matrix[index]
    cost_matrix = cost_matrix[index].reshape(-1, 1)

    # Initializing the MIP Solver
    solver = pywraplp.Solver.CreateSolver("SAT")

    # creating the binary allocation variable
    x = np.array([solver.BoolVar("") for i in range(len(index))]).reshape(-1, 1)

    # create a matrix that is the product of the decision variable and the pair matrix
    result_matrix = x * pair_matrix

    # declaring the constraints
    # Uniqueness of flight legs and all flight legs covered
    for i in range(num_flights):
        solver.Add(solver.Sum(result_matrix[:, i]) == 1)

    # declaring the objective function
    solver.Minimize(np.sum(cost_matrix * x))

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
def sub_problem(pair_matrix, cost_matrix, index, num_pairs, num_flights):
    pair_matrix_idx = pair_matrix[index]
    cost_matrix_idx = cost_matrix[index].reshape(-1, 1)

    # Initializing the LP Solver
    solver = pywraplp.Solver.CreateSolver("GLOP")

    # creating the binary allocation variable
    x = np.array([solver.NumVar(0, 1, f"x_{i}") for i in range(len(index))]).reshape(
        -1, 1
    )

    # create a matrix that is the product of the decision variable and the pair matrix
    result_matrix = x * pair_matrix_idx

    # declaring the constraints
    # Uniqueness of flight legs and all flight legs covered
    for i in range(num_flights):
        solver.Add(solver.Sum(result_matrix[:, i]) == 1)

    # declaring the objective function
    solver.Minimize(np.sum(cost_matrix_idx * x))

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
            cost_matrix[i] - np.sum(pair_matrix[i] * dual_values, axis=0)
        )

    return red_cost_mtx, np.argsort(red_cost_mtx)[:50].tolist()


# function to generate the columns
def column_gen():
    # reading the cost_matrix and the pair_matrix
    cost_matrix = np.loadtxt("data/cost_matrix/cost.txt")
    pair_matrix = np.genfromtxt(
        "data/pairings/pair_array.txt", delimiter=",", dtype="int"
    )

    # determining the number of flights and tasks
    num_pairs = pair_matrix.shape[0]
    num_flights = pair_matrix.shape[1]

    # coloumn generation

    # initialization huerestics
    ini_pair, increment = 5000, 1000

    while True:
        # create a reduced pair array that contains atleast one feasible solution
        index = np.argsort(cost_matrix)[:ini_pair].tolist()

        status, obj, idx = RMP(index, num_flights, pair_matrix, cost_matrix)

        if obj != 0.0:
            break

        ini_pair += increment

    status, obj, index = RMP(index, num_flights, pair_matrix, cost_matrix)

    # setting the timer
    start_time = time.time()
    timeout_seconds = 300

    # the column generation problem
    while True:
        # the RMP solves the problem for a small number of pairs
        status, obj, idx = RMP(index, num_flights, pair_matrix, cost_matrix)

        # the sub problem finds the reduced cost matrix and the index of the least reduced cost
        red_cost_mtx, least_red_cost_index = sub_problem(
            pair_matrix, cost_matrix, index, num_pairs, num_flights
        )

        index = index + least_red_cost_index

        if all(x >= 0 for x in red_cost_mtx) == True:
            break

        if time.time() - start_time >= timeout_seconds:
            break

        return idx
