# Crew_Scheduling
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

a. Crew Pairing

b. Crew Assignment

## Project Objectives

· Minimize crew costs (whilst maximizing preferences)

· Automate crew pairing and assignment based on predefined criteria such as flight schedules, crew availability, and seniority.

· Integration with existing crew management systems and databases.

· User-friendly interface for crew members and managers to view and manage schedules.

· The final model is developed using python and is deployed using frameworks like Streamlit or Flask.

## Project Scope

The team will obtain clarity on the various factors involved by conducting theoretical and industry based research. This process will be taken foward by documenting the variables and factors and formualing the components in the form of a mathematical model. Then the optimization model will be build using Python and Google OR Tools. Then the model is evaluated and validated for various scenarios and will be deployed (Web-UI Interface) using the Flask framework.

## Assumptions

1. The Flight Schedule/Time Table is already available inclusive of start and end times, layovers, destinations, aircraft type and capacity, and expected turnaround times (time between a flight's arrival and departure).

2. The Fleet Types are already assigned to specific flights.

## Literature Review
In the first phase, we did our exploratory research to understand the airline industry and drafted a business requirement document on crew scheduling. ​We tried to understand different algorithms such as dynamic programming, depth-first search, and nearest neighbor for pairing generation. On comparing, we found that depth-first search is best for pairing generation. Later, we will optimize crew pairing using a column generation algorithm to reduce the cost in terms of the time span of pairings, covering all unique flight legs.

## Pairing Generation
Initially, our focus was on a specific subset of the broader crew scheduling problem. 
We have generated hypothetical data for flight legs in crew pairings.
The Depth-First Search Algorithm is employed for pairing generation, which is divided into two main components: Duty Generation and Pairing Generation.
In Duty Generation, a flight schedule is provided as input. This schedule includes all non-stop flight legs and their associated attributes, such as departure and arrival airports, as well as start and end times.
Several legality constraints must be satisfied for generating flight duties:
Start-city and End-city Constraints: The first flight of a flight duty should commence from a crew base and conclude at the same crew base.
Sit-time Constraints: The sit-time between two consecutive flight legs in a flight duty should adhere to a minimum limit of 60 minutes.
