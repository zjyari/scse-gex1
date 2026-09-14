######################## IMPORTANT ########################
""" Do not rename the variables or functions.
Do not change the function parameters.
Do not add input() calls inside airport_manager.py.
The file must be importable by the tests. """
###########################################################

airport_info = ("OUL", "1", "14-09-2026")
allowed_gates = {"A1", "A2", "A3", "A4", "B1", "B2"}
restricted_destinations = {"Moscow", "Pyongyang"}
flights = {
    "AY450": {
        "destination": "Helsinki",
        "departure": "08:30",
        "gate": "A2",
        "capacity": 5,
        "passengers": ["Alice Wong", "David Kim", "Fatima Ali"]
    },
    "SK271": {
        "destination": "Stockholm",
        "departure": "10:15",
        "gate": "B1",
        "capacity": 4,
        "passengers": ["Chen Wei", "George Smith"]
    },
    "LH2491": {
        "destination": "Munich",
        "departure": "12:40",
        "gate": "A4",
        "capacity": 5,
        "passengers": ["Hana Lee", "Maria Garcia", "Noah Wilson"]
    }
}


def find_flight(flights, flight_number):
    if not isinstance(flights, dict):
        return None
    search_val = flight_number.strip().upper()
    for real_key in flights:
        if real_key.upper() == search_val:
            return real_key
    return None


def passenger_exists(passengers, passenger_name):
    target = passenger_name.strip().lower()
    for p in passengers:
        if p.strip().lower() == target:
            return True
    return False


def check_in_passenger(
    flights,
    flight_number,
    passenger_name,
    restricted_destinations
):
    flight_key = find_flight(flights, flight_number)
    if flight_key is None:
        return "FLIGHT_NOT_FOUND"

    raw_name = passenger_name.strip()
    if len(raw_name) == 0:
        return "EMPTY_NAME"

    flight = flights[flight_key]
    if flight["destination"] in restricted_destinations:
        return "RESTRICTED"

    passenger_list = flight["passengers"]
    if passenger_exists(passenger_list, raw_name):
        return "DUPLICATE"

    capacity = flight["capacity"]
    if len(passenger_list) >= capacity:
        return "FULL"

    import string
    fixed_name = string.capwords(raw_name)
    passenger_list.append(fixed_name)
    return "OK"


def remove_passenger(
    flights,
    flight_number,
    passenger_name
):
    flight_key = find_flight(flights, flight_number)
    if flight_key is None:
        return "FLIGHT_NOT_FOUND"

    flight = flights[flight_key]
    passenger_list = flight["passengers"]
    target_low = passenger_name.strip().lower()

    found_index = None
    for idx, person in enumerate(passenger_list):
        if person.strip().lower() == target_low:
            found_index = idx
            break
    if found_index is None:
        return "PASSENGER_NOT_FOUND"

    del passenger_list[found_index]
    return "OK"


def change_gate(
    flights,
    flight_number,
    new_gate,
    allowed_gates
):
    flight_key = find_flight(flights, flight_number)
    if flight_key is None:
        return "FLIGHT_NOT_FOUND"
    if new_gate.upper() not in allowed_gates:
        return "INVALID_GATE"
    flights[flight_key]["gate"] = new_gate.upper()
    return "OK"


def flight_status(flight):
    cap = flight["capacity"]
    count = len(flight["passengers"])
    ratio = count / cap * 100
    if ratio >= 100:
        return "FULL"
    elif ratio >= 75:
        return "ALMOST FULL"
    else:
        return "AVAILABLE"


def sorted_manifest(
    flights,
    flight_number
):
    flight_key = find_flight(flights, flight_number)
    if flight_key is None:
        return None
    passenger_list = flights[flight_key]["passengers"]
    return sorted(passenger_list.copy())


def total_passengers(flights):
    total = 0
    for flight_data in flights.values():
        total += len(flight_data["passengers"])
    return total


def any_full_flight(flights):
    for f_data in flights.values():
        if flight_status(f_data) == "FULL":
            return True
    return False


def all_flights_have_passengers(flights):
    for f_data in flights.values():
        if len(f_data["passengers"]) < 1:
            return False
    return True
