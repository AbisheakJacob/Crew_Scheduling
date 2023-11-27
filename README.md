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

## Pairing Generation
Depth-First Search Algorithm is used for the generation of pairings. The pairing generation is separated into two parts Duty Generation and Pairing Generation.
In Duty Generation, a flight schedule is given as input. This flight schedule contains all the non-stop flight legs and their associated attributes such as flights’ departure and arrival airport, their start and end times.
Subjected to several legality constraints which must be satisfied for genearting flight duties -
Start-city and End-city Constraints: 1st flight of a flight duty should start from a crew-base and should end at the same crew-base only.
Sit-time Constraints: Sit-time between two consecutive flight legs in a flight duty should be restricted by minimum limit of 60 minutes.
