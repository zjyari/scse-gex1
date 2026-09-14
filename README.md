
EXERCISE REQUIREMENTS:
1. Create airport_manager.py using appropriate Python data structures. 
2. Your solution must meaningfully use a list, tuple, dictionary and set. 
3. You must also implement the required functions exactly as specified. 
4. Your functions will be tested with data different from the examples given here, so do not hard-code the provided flight numbers, passenger names, capacities, gates, or destinations.


PROGRAM DATA REQUIREMENTS:

Airport:
Code: OUL
Terminal: 1
Date: 14-09-2026

Allowed gates:
A1, A2, A3, A4, B1, B2

Restricted destinations:
Moscow
Pyongyang

Flight details and passenger list:
AY450
Destination: Helsinki
Departure: 08:30
Gate: A2
Capacity: 5

Passengers:
Alice Wong
David Kim
Fatima Ali

--------------

SK271

Destination: Stockholm
Departure: 10:15
Gate: B1
Capacity: 4

Passengers:
Chen Wei
George Smith

--------------

LH2491

Destination: Munich
Departure: 12:40
Gate: A4
Capacity: 5

Passengers:
Hana Lee
Maria Garcia
Noah Wilson

----------------------------------------------------------------------------------------------------------------


ALL THE CORRECTLY WORKING FUNCTIONS MUST RETURN THE FOLLOWING:

find_flight(...): Return normalized flight key or None

passenger_exists(...): Return True/False, case-insensitive

check_in_passenger(...): Return one of OK, FLIGHT_NOT_FOUND, EMPTY_NAME, DUPLICATE, FULL, RESTRICTED

remove_passenger(...): Return OK, FLIGHT_NOT_FOUND, or PASSENGER_NOT_FOUND

change_gate(...): Return OK, FLIGHT_NOT_FOUND, or INVALID_GATE

flight_status(...): Return AVAILABLE, ALMOST FULL, or FULL

sorted_manifest(...): Return a sorted copy of passenger names, or None

total_passengers(...): Return total passenger count

any_full_flight(...): Return True/False

all_flights_have_passengers(...): Return True/False


----------------------------------------------------------------------------------------------------------------

SETUP AND TESTING:
- Create and activate a virtual environment
- Install requirements using: uv pip install -r requirements.txt
    -- The above command will install pytest, which is required for testing
- Once you have finished your program, test it using: uv run python -m pytest -v
- Once all the tests pass, then commit to your GitHub and submit only the GitHub link in Moodle



IMPORTANT:
Do not try to create a program that works for the given data only. The solution should be usable across any available dataset.
