# Indian Airline Sector
The Indian airline sector is currently experiencing a boom with an annual growth rate of 47.05%.

# Project's Title
Airline Planning - Crew Scheduling

## Crew Scheduling
1. Crew Scheduling is defined as the problem of assigning a group of workers (a crew) to a set of tasks. 
2. Crew Scheduling is done into two steps-
- Crew Pairing             
- Crew Rostering/Assignment

# Project Description
In the airline industry, crew cost is the highest variable cost and any reduction in crew costs will save the company millions of rupees. Crew Scheduling is a larger problem in many industries like healthcare, airlines, railways etc.

## Project Objectives
   1. Minimize crew costs - (whilst maximizing preferences)​
   2. Cover all Flight Legs - (whilst maximizing preferences)​
   3. Generate a User-Friendly Roster - (based on predefined criteria, crew availability, and regulatory requirements)​
   4. Deploy the Python Model - (using Streamlit library)

# Crew Pairing
A crew pairing is a sequence of flight legs, within the same fleet, that starts and ends at the same crew base. 

## Pairing Generation
The pairing generation process uses depth first search algorithm and is divided into two principal components: Duty Generation and Pairing Generation.

# Depth First Search
The DFS algorithm is a recursive algorithm that uses the idea of backtracking. It involves exhaustive searches of all the nodes (flight legs) by going ahead, if possible, else by backtracking. 

## Depth-First Search Algorithm
```
function generate_duties(current_duty, duties):  
  if current_duty is valid:
    duties.append(current_duty)
  else:
    for each flight leg that is valid:
      current_duty.append(flight leg)
      generate_duties(current_duty, duties)
      current_duty.pop()
```

# Algorithm for Crew Pairing Optimization

The objective is to minimise the time span of pairing, covering all the flight legs.

## Column Generation

Column Generation is the most widely adopted technique which is proven for efficiency solving large scale crew pairing optimization problems. Column Generation involves iteratively generating and adding crew pairings (columns) to the solution, focusing on a reduced cost. The initial set may consist of basic crew pairings that meet legal and operational requirements. Subsequently, the algorithm identifies and adds new pairings that enhance the overall schedule, converge to an optimal solution.

### Column Generation Algorithm
The algorithm consists of two main components: the Restricted Master Problem (RMP) and the Sub-Problem.

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

**Results:**
Column Generation is able to provide a 2.4x decrease in time taken to final the optimal set of pairings. The use of limited number of pairings reduces the computation requirements tremendously. 

This implementation of the Column Generation algorithm provides an efficient approach to solving crew pairing optimization problems. It can be adapted to different scenarios by adjusting input data and parameters. The algorithm aims to find an optimal solution while considering constraints and minimizing overall costs.

# Recommendations
- Numba, cuda integration for nopython and parallel processing.​
- Using shortest path algorithm for column generation sub problem.​
- Increase the robustness of the model.​
- Use code optimization techniques.

# Fine-Tuning the Model
1. Elimination of Redundant Variables
2. In Time Generation of Pair Matrix and Cost Matrix
3. Streamlit Deployment
4. Real-Time Data Testing
5. Scalability
6. Parallel Processing
7. Web Scrapping Bot
8. Pyomo implementation

The initial fine-tuning of the model has resulted in 5x increase in the speed of the model, significant reduction in memory usage.

# Streamlit for Web Application

