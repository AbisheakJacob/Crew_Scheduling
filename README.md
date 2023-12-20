# Indian Airline Sector
The indian airline sector is currently experiencing a boom with an annual growth rate of 47.05%.

## Types of Airline Planning
1. Schedule Design Problem  

2. Fleet Assignment Problem  

3. Maintenance Routing Problem  

4. Crew Scheduling Problem - 
   - Crew Pairing
   - Crew Assignment 

## Crew Scheduling
Crew Scheduling is defined as the problem of assigning a group of workers (a crew) to a set of tasks. 

### Why Crew Schedulung?
In the airline industry crew costs are second only to fuel costs and any reduction in crew costs will result in saving millions of dollars for the company.

## Project Objectives

  -  Minimize crew costs (whilst maximizing preferences)

  - Automate crew pairing and assignment based on predefined criteria such as flight schedules, crew availability, and seniority.

  - Integration with existing crew management systems and databases.

  - User-friendly interface for crew members and managers to view and manage schedules.

  - The final model is developed using python and is deployed using frameworks like Streamlit.

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

## Terminologies
- **Flight leg** - A nonstop flight segment. Each flight leg is characterized by five features: the flight number, the origin airport, the destination airport, the departure time, and the arrival time.

- **Flight Duty** - A sequence of consecutive air legs comprising a working day for a single crew member. Two consecutive duties should begin and end at the same airport. Legs are separated by sit time to a minimum limit of 60 minutes.

- **Pairing** -  A sequence of duties for an unspecified crew member that starts and ends at a base. Pairings typically last 4–5 days.

- **Duty Generation** -  In the Duty Generation phase, a flight schedule serves as input, encompassing all non-stop flight legs and their relevant attributes such as departure and arrival airports, as well as start and end times to ensure comprehensive coverage of all flight legs, adhering to various legality constraints.

- **Pairing Generation** - Following the duty generation, possible pairings are generated from flight duties, ensuring that each flight leg is covered by at least one pairing, adhering to the constraints.

- **Cost Matrix** - It is the cost associated with each possible pairing quantified in terms of time (flying time and sit time) in hours.


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

### Pairing Generation
The pairing generation process uses depth first search algorithm and is divided into two principal components: Duty Generation and Pairing Generation.
![Pairing_Generation_Steps](/00_resources/images/Pairing_Generation.png)

## Algorithms for Optimization of Crew Pairing
The objective is to minimise the time span of pairing, covering all the flight legs.

### Column Generation
Column Generation is the most widely adopted technique which is proven for efficiency solving large scale crew pairing optimization problems. Column Generation involves iteratively generating and adding crew pairings (columns) to the solution, focusing on a reduced cost. The initial set may consist of basic crew pairings that meet legal and operational requirements. Subsequently, the algorithm identifies and adds new pairings that enhance the overall schedule, converge to an optimal solution.
![Column_Generation_flowchart](/00_resources/images/Column_Generation.png)

### Genetic Algorithm
Population-based probabilistic-search heuristics, for which enumeration and handling of the entire pairing set is computationally-tractable.
![Genetic_Algorithm_Steps](/00_resources/images/Genetic_Algorithm.png)

