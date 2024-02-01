# Indian Airline Sector

The Indian airline sector is currently experiencing a boom with an annual growth rate of 47.05%.

## Types of Airline Planning

1. Schedule Design Problem  

2. Fleet Assignment Problem  

3. Maintenance Routing Problem  

4. Crew Scheduling Problem -
   -  Crew Pairing
   - Crew Assignment 

## Crew Scheduling

Crew Scheduling is defined as the problem of assigning a group of workers (a crew) to a set of tasks. 

### Why Crew Scheduling?

In the airline industry crew costs are second only to fuel costs and any reduction in crew costs will result in saving millions of dollars for the company.

## Project Objectives

   1. Minimize crew costs (whilst maximizing preferences)

   2. Automate crew pairing and assignment based on predefined criteria such as flight schedules, crew availability, and seniority.

   3. Integration with existing crew management systems and databases.

   4. User-friendly interface for crew members and managers to view and manage schedules.

   5. The final model is developed using python and is deployed using frameworks like Streamlit.

## Project Scope

The team will obtain clarity on the various factors involved by conducting theoretical and industry based research. This process will be taken foward by documenting the variables and factors and formualing the components in the form of a mathematical model. Then the optimization model will be build using Python and Google OR Tools. Then the model is evaluated and validated for various scenarios and will be deployed (Web-UI Interface) using the Streamlit framework.

## Assumptions

1. The Flight Schedule/Time Table is already available inclusive of start and end times, layovers, destinations, aircraft type and capacity, and expected turnaround times (time between a flight's arrival and departure).

2. The Fleet Types are already assigned to specific flights.

## Literature Review

1. Harry Kornilakis and Panagiotis Stamatopoulos, Crew Pairing Optimization with Genetic Algorithms, Department of Informatics and Telecommunications, University of Athens, Panepistimiopolis, 157 84 Athens, Greece.​

2. Xin Wen, Xuting Sun, Yige Sun, Xiaohang Yue, Airline crew scheduling: Models and algorithms, Transportation Research Part E 149 (2021)​

3. Cynthia Barnart, Ellis L. Johnson, Diego Klabjan, George L. Nemhauser, Airline Crew Scheduling, Researchgate Publication number: 227105914, January 2003​

4. Niklas Kohl and Stefan E. Karisch, Airline Crew Rostering: Problem Types, Modelling, and Optimization, Annals of Operations Research 127, 223-257, 2004​

5. Shengzhi Shao, Integrated Aircraft Fleeting, Routing, and Crew Pairing Models and Algorithms for the Airline Industry, Virginia Polytechnic Institute and State University, 2012

6. Divyam Aggarwal, Dhish Kumar Saxena, Thomas Back, and Michael Emmerich: Real-World Airline Crew Pairing Optimization: Customized Genetic Algorithm versus Column Generation Method. arXiv:2003.03792v2 [cs.NE], 27 May 2023

7. Jonathan Nillius: Deep Learning in State of the Art Airline Crew Rostering Algorithms. Department of Computer Science and Engineering, CHALMERS UNIVERSITY OF TECHNOLOGY, UNIVERSITY OF GOTHENBURG, Gothenburg, Sweden 2022

## Crew Pairing

A crew pairing is a sequence of flight legs, within the same fleet, that starts and ends at the same crew base. 

![Crew Pairing flowchart](/00_resources/images/Crew_Pairing.png)

## Pairing Generation

The pairing generation process uses depth first search algorithm and is divided into two principal components: Duty Generation and Pairing Generation.
![Pairing_Generation_Steps](/00_resources/images/Pairing_Generation.png)

## Terminologies

- **Flight leg** - A nonstop flight segment. Each flight leg is characterized by five features: the flight number, the origin airport, the destination airport, the departure time, and the arrival time.

- **Flight Duty** - A sequence of consecutive air legs comprising a working day for a single crew member. Two consecutive duties should begin and end at the same airport. Legs are separated by sit time to a minimum limit of 60 minutes.

- **Pairing** -  A sequence of duties for an unspecified crew member that starts and ends at a base. Pairings typically last 4–5 days.

- **Duty Generation** -  In the Duty Generation phase, a flight schedule serves as input, encompassing all non-stop flight legs and their relevant attributes such as departure and arrival airports, as well as start and end times to ensure comprehensive coverage of all flight legs, adhering to various legality constraints.

- **Pairing Generation** - Following the duty generation, possible pairings are generated from flight duties, ensuring that each flight leg is covered by at least one pairing, adhering to the constraints.

- **Cost Matrix** - It is the cost associated with each possible pairing quantified in terms of time (flying time and sit time) in hours.

## Depth First Search

The DFS algorithm is a recursive algorithm that uses the idea of backtracking. It involves exhaustive searches of all the nodes (flight legs) by going ahead, if possible, else by backtracking. 

### Depth-First Search Algorithm
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

## Algorithms for the Optimization of Crew Pairing

The objective is to minimise the time span of pairing, covering all the flight legs.

### Set Partitioning

An approach for optimization problems where the goal is to select the subset of pairings to minimize a cost function while satisfying the constraint of covering each flight leg exactly once.

### Column Generation

Column Generation is the most widely adopted technique which is proven for efficiency solving large scale crew pairing optimization problems. Column Generation involves iteratively generating and adding crew pairings (columns) to the solution, focusing on a reduced cost. The initial set may consist of basic crew pairings that meet legal and operational requirements. Subsequently, the algorithm identifies and adds new pairings that enhance the overall schedule, converge to an optimal solution.
![Column_Generation_flowchart](/00_resources/images/Column_Generation.png)

### Genetic Algorithm

Population-based probabilistic-search heuristics, for which enumeration and handling of the entire pairing set is computationally-tractable.

![Genetic_Algorithm_Steps](/00_resources/images/Genetic_Algorithm.png)

### Machine Learning
Machine learning is gradually making its way into crew pairing optimization within the airline sector. While it may not be widely adopted at this point, it represents a significant advancement in the efficient scheduling of airline crews. Our preliminary research offered valuable insights into optimizing airline crew pairing through machine learning. 
For further details, check **CrewML**, which is an open-source ML python package.

## Column Generation
We implemented column generation algorithm using ortools in python for crew pairing optimization.
![Column Generation](/00_resources/images/Column_Generation_Algorithm.png)

The algorithm consists of two main components: the Restricted Master Problem (RMP) and the Sub-Problem.

**1. Restricted Master Problem (RMP):**
The RMP is a mixed-integer linear programming problem that aims to find an optimal combination of flight pairs from a reduced set. It creates binary allocation variables for each pair and includes constraints to ensure that each flight is assigned exactly once. The objective is to minimize the total cost of the selected pairs.

Input:
- index: The indices of the initial set of pairs.
- num_flights: The total number of flights.
- pairings: A list of flight pairings.
- cost_matrix: The cost matrix representing the cost of each pairing.

Output:
- status: The status of the solver (0 if solved successfully).
- objective_value: The optimal objective value.
- optimal_index: The indices of the final selected pairs.

**2. Sub-Problem:**
The Sub-Problem is a linear programming problem that aims to find the reduced cost matrix and the index of the pair with the least reduced cost. It uses dual values from the RMP solution to calculate the reduced costs.

Input:
- pairings: A list of flight pairings.
- cost_matrix: The cost matrix representing the cost of each pairing.
- index: The indices of the current set of pairs.
- num_pairs: The total number of pairs.
- num_flights: The total number of flights.

Output:
- red_cost_mtx: The reduced cost matrix.
- least_red_cost_index: The index of the pair with the least reduced cost.

**Column Generation Loop:**
The column generation process involves iteratively solving the RMP and Sub-Problem until all reduced costs are non-negative. The algorithm initializes with a reduced set of pairs and dynamically adds pairs with negative reduced costs until convergence.

**Initialization:**
The algorithm starts with an initial set of pairs (controlled by ini_pair and increment) to ensure at least one feasible solution.

**Main Loop:**
1. The RMP is solved to obtain an optimal solution and identify the indices of the selected pairs.
2. The Sub-Problem is solved to calculate the reduced cost matrix and find the pair with the least reduced cost.
3. The index is updated by adding the pair with the least reduced cost.
4. The loop continues until all reduced costs are non-negative or a timeout limit is reached.

**Usage:**
To use the algorithm, provide the necessary data, such as the flight legs, pairings, and cost matrix, and then execute the main loop of the column generation algorithm. Adjust parameters like the initial pair size (ini_pair), increment, and timeout as needed.

This implementation of the Column Generation algorithm provides an efficient approach to solving crew pairing optimization problems. It can be adapted to different scenarios by adjusting input data and parameters. The algorithm aims to find an optimal solution while considering constraints and minimizing overall costs.


