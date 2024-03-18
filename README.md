# Indian Airline Sector
The Indian airline sector is currently experiencing a boom with an annual growth rate of 75% in terms of flights and passengers.

# Project's Title
Airline Planning - Crew Scheduling

## Crew Scheduling
1. Crew Scheduling is defined as the problem of assigning a group of workers (a crew) to a set of tasks. 
2. Crew Scheduling is done into two steps-
- Crew Pairing             
- Crew Rostering/Assignment

# Project Description
In the airline industry, crew cost is the second highest variable cost and any reduction in crew costs will save the company millions of rupees. Crew Scheduling is a larger problem in many industries like healthcare, airlines, railways etc. Our scope revolves around developing a python-based optimisation model deployed using Streamlit framework to efficiently schedule crew pairings by mimimising the cost and maximising crew utilisation.

## Project Objectives
   1. Minimize crew costs - (whilst maximizing preferences)​
   2. Cover all Flight Legs - (whilst maximizing preferences)​
   3. Generate a User-Friendly Roster - (based on predefined criteria, crew availability, and regulatory requirements)​
   4. Deploy the Python Model - (using Streamlit library)

# Crew Pairing
A crew pairing is a sequence of flight legs, within the same fleet, that starts and ends at the same crew base. 

## Pairing Generation
The pairing generation process uses depth first search algorithm and is divided into two principal components: Duty Generation and Pairing Generation.

# Data Collection
The data is collected from airline aggregrators by using a web scraper extension. These extensions are typically browser add-ons or plugins that enhance the functionality of web browsers, allowing users to gather information from websites without manual copying and pasting.

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

RMP: Solves the Restricted Master Problem (RMP) to assign flights to pairs based on binary allocation variables.
    
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



   sub_problem: Solves the sub-problem to generate the reduced cost matrix and identifies the indices of the least reduced cost pairs.
   
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
Array-based architecture is able to provide a 2.4x decrease in time taken to final the optimal set of pairings. The use of column generation leads 40% decrease in computational time.

This implementation of the Column Generation algorithm provides an efficient approach to solving crew pairing optimization problems. It can be adapted to different scenarios by adjusting input data and parameters. The algorithm aims to find an optimal solution while considering constraints and minimizing overall costs.

# How to install and run the project
** Hosted the application on GitHub**  
  
   **Clone the Repository**
The Streamlit application is hosted in a repository, clone it to your local machine using Git:  
  
  git clone <https://github.com/AbisheakJacob/Crew_Scheduling>

**Navigate to the Project Directory**
Open a terminal or command prompt and navigate to the directory where the Streamlit application code is located.

**Install Dependencies**
If the application has additional dependencies, install them using pip:  
    
    pip install -r requirements.txt

**Run the Application**
Execute the Streamlit application by running the following command:  
    
    streamlit run main.py

**Access the Application**
Once the application is running, you can access it by opening a web browser and navigating to the URL provided in the terminal.


# Recommendations
- Numba, cuda integration for nopython and parallel processing.​
- Using shortest path algorithm for column generation sub problem.​
- Increase the robustness of the model.​
- Use code optimization techniques.

# Streamlit for Web Application
**STARTING THE APPLICATION**
Open the link to get start with the application.  
  **Link to the application: https://team1-crewscheduling.streamlit.app/**

**INITIATING DATA UPLOADS**
Users have the option to choose the method of data input and can either upload the data via a CSV file by browsing their desktop or by using the drag and drop feature.

**DATA DISPLAY**
Users have the option to select how the data is presented: either the beginning (head) or the end (tail), or they can choose not to display it at all.
 
**GENERATION OF DUTIES AND PAIRINGS** 
The application utilizes a depth-first search algorithm to generate both duties and pairings. There is no requirement to store the pairings and the cost matrix separately as they are generated simultaneously in real-time.
 
**CREW PAIRING**
The application employs column generation to solve crew pairing, resulting in the determination of the set of pairings.
 
**OUTPUT**
The output can be visualized on the network plot by choosing either the Flight Leg ID or the airport as reference points.
 

	
