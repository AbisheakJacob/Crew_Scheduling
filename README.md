# Indian Airline Sector
The indian airline sector is currently experiencing a boom with an annual growth rate of 47.05%.

## Crew_Scheduling
Crew Scheduling is defined as the problem of assigning a group of workers (a crew) to a set of tasks. Crew scheduling is used in various industries where there is a need to efficiently manage and schedule the work shifts and tasks of a workforce, especially in industries with shift-based or continuous operations. Some industries that heavily rely on crew scheduling for their operations include, Airlines, Railways, Hospitals, Hospitality, etc.

The Airline industry is a primary example for crew scheduling because of the following reasons:

1. They have many elements that are common to many crew scheduling problems.

2. They are true planning problems

3. The impact of better crew scheduling is very high because of very high salaries in this sector.

Crew Scheduling Problem is a part of the complex Airline Planning Problem. Because of the complexity of the size and complexity of this rich problem, they are solved in the order of,

1. Schedule Design Problem

2. Fleet Assignment Problem

3. Maintenance Routing Problem

4. Crew Scheduling Problem
    - Crew Pairing
    - Crew Assignment

## Project Objectives

  -  Minimize crew costs (whilst maximizing preferences)

  - Automate crew pairing and assignment based on predefined criteria such as flight schedules, crew availability, and seniority.

  - Integration with existing crew management systems and databases.

  - User-friendly interface for crew members and managers to view and manage schedules.

  - The final model is developed using python and is deployed using frameworks like Streamlit or Flask.

## Project Scope

The team will obtain clarity on the various factors involved by conducting theoretical and industry based research. This process will be taken foward by documenting the variables and factors and formualing the components in the form of a mathematical model. Then the optimization model will be build using Python and Google OR Tools. Then the model is evaluated and validated for various scenarios and will be deployed (Web-UI Interface) using the Flask framework.

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


### Crew Pairing
A crew pairing is a sequence of flight legs, within the same fleet, that starts and ends at the same crew base. The DFS algorithm is a recursive algorithm that uses the idea of backtracking. 
Additionally, we explored the optimization of crew pairing through set partitioning, involving a master problem and a column generation subproblem. The objective was to minimize costs associated with the time span of pairings, ensuring comprehensive coverage of all unique flight legs.
Initially, our focus is directed towards a specific subset within the broader scope of crew scheduling - Crew Pairing. 
Hypothetical data for the flight legs within crew pairings has been generated.
The pairing generation process utilizes the Depth-First Search Algorithm and is divided into two principal components: Duty Generation and Pairing Generation.
In the Duty Generation phase, a flight schedule serves as input, encompassing all non-stop flight legs and their relevant attributes such as departure and arrival airports, as well as start and end times. 
To ensure comprehensive coverage of all flight legs, various legality constraints must be met during the generation of flight duties:
Start-city and End-city Constraints: The initial flight of a flight duty must commence from a crew base and terminate at the same crew base.
Sit-time Constraints: The sit-time between two consecutive flight legs in a flight duty must adhere to a minimum limit of 60 minutes.
Following the duty generation, pairings are generated from flight duties, ensuring that each flight leg is covered by at least one pairing.
A web user interface has been designed and implemented using Streamlit. This interface showcases flight duties, pairings, and a cost matrix quantified in terms of time (flying time and sit time in hours). The data is sourced from an Excel file, incorporating information about all the flight legs.

### Depth First Search
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
