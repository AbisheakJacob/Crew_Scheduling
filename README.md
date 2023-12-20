# Indian Airline Sector
The indian airline sector is currently experiencing a boom with an annual growth rate of 47.05%.

# Crew Scheduling
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

