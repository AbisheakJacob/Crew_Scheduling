# Crew_Scheduling


## Pairing Generation
# Depth-First Search Algorithm is used for the generation of pairings. The pairing generation is separated into two parts Duty Generation and Pairing Generation.
**In Duty Generation, a flight schedule is given as input. This flight schedule contains all the non-stop flight legs and their associated attributes such as flights’ departure and arrival airport, their start and end times.**
**Subjected to several legality constraints which must be satisfied for genearting flight duties -**
**Start-city and End-city Constraints: 1st flight of a flight duty should start from a crew-base and should end at the same crew-base only.**
**Sit-time Constraints: Sit-time between two consecutive flight legs in a flight duty should be restricted by minimum limit of 60 minutes.**
