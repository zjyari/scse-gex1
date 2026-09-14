import copy
import random

import airport_manager as am


RANDOM_SEED = 48391
rng = random.Random(RANDOM_SEED)


def make_random_name():
    first_names = [
        "Alice",
        "Bob",
        "Chen",
        "David",
        "Emma",
        "Fatima",
        "George",
        "Hana",
        "Ivan",
        "Julia"
    ]

    last_names = [
        "Wong",
        "Lee",
        "Smith",
        "Kim",
        "Ali",
        "Brown",
        "Chen",
        "Garcia",
        "Wilson",
        "Martin"
    ]

    first = rng.choice(first_names)
    last = rng.choice(last_names)

    return f"{first} {last}"


def make_random_flight_number():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    prefix = (
        rng.choice(letters)
        + rng.choice(letters)
    )

    number = rng.randint(100, 999)

    return f"{prefix}{number}"


def make_random_flight(
    capacity=None,
    passenger_count=None
):
    if capacity is None:
        capacity = rng.randint(2, 15)

    if passenger_count is None:
        passenger_count = rng.randint(0, capacity)

    passengers = []

    while len(passengers) < passenger_count:
        name = make_random_name()

        if name not in passengers:
            passengers.append(name)

    return {
        "destination": rng.choice([
            "Paris",
            "Berlin",
            "Oslo",
            "Madrid",
            "Rome",
            "Vienna",
            "Prague",
            "Tallinn"
        ]),
        "departure": f"{rng.randint(0, 23):02d}:{rng.randint(0, 59):02d}",
        "gate": rng.choice([
            "A1", "A2", "A3",
            "B1", "B2", "B3"
        ]),
        "capacity": capacity,
        "passengers": passengers
    }


def make_random_flights(count=5):
    flights = {}

    while len(flights) < count:
        flight_number = make_random_flight_number()

        if flight_number not in flights:
            flights[flight_number] = make_random_flight()

    return flights



def test_airport_info_structure():
    assert isinstance(am.airport_info, tuple)
    assert len(am.airport_info) == 3


def test_allowed_gates_is_set():
    assert isinstance(am.allowed_gates, set)


def test_restricted_destinations_is_set():
    assert isinstance(am.restricted_destinations, set)


def test_flights_is_dictionary():
    assert isinstance(am.flights, dict)

    for flight in am.flights.values():
        assert isinstance(flight, dict)
        assert isinstance(flight["passengers"], list)




def test_find_flight_randomized():
    flights = make_random_flights(8)

    for flight_number in flights:

        lower_case = flight_number.lower()
        padded = f"   {lower_case}   "

        result = am.find_flight(
            flights,
            padded
        )

        assert result == flight_number

    assert am.find_flight(
        flights,
        "ZZ999"
    ) is None




def test_passenger_exists_randomized():
    passengers = []

    for _ in range(6):
        name = make_random_name()

        if name not in passengers:
            passengers.append(name)

    target = rng.choice(passengers)

    assert am.passenger_exists(
        passengers,
        target.lower()
    ) is True

    assert am.passenger_exists(
        passengers,
        target.upper()
    ) is True

    assert am.passenger_exists(
        passengers,
        "Definitely Not Present"
    ) is False





def test_check_in_random_success():
    flights = make_random_flights(4)

    flight_number = rng.choice(
        list(flights.keys())
    )

    flight = flights[flight_number]

    flight["passengers"] = []
    flight["capacity"] = 10
    flight["destination"] = "Paris"

    new_passenger = "Random Test Person"

    result = am.check_in_passenger(
        flights,
        flight_number.lower(),
        f"   {new_passenger.lower()}   ",
        {"Moscow", "Pyongyang"}
    )

    assert result == "OK"

    assert "Random Test Person" in flight["passengers"]


def test_check_in_duplicate_randomized():
    flights = make_random_flights(3)

    flight_number = rng.choice(
        list(flights.keys())
    )

    flight = flights[flight_number]

    flight["capacity"] = 10
    flight["destination"] = "Paris"

    passenger = "Alice Example"

    flight["passengers"] = [
        passenger
    ]

    before = copy.deepcopy(flights)

    result = am.check_in_passenger(
        flights,
        flight_number,
        "ALICE EXAMPLE",
        set()
    )

    assert result == "DUPLICATE"
    assert flights == before


def test_check_in_full_randomized():
    capacity = rng.randint(2, 8)

    flight_number = make_random_flight_number()

    passengers = [
        f"Passenger {i}"
        for i in range(capacity)
    ]

    flights = {
        flight_number: {
            "destination": "Berlin",
            "departure": "10:00",
            "gate": "A1",
            "capacity": capacity,
            "passengers": passengers
        }
    }

    before = copy.deepcopy(flights)

    result = am.check_in_passenger(
        flights,
        flight_number,
        "New Passenger",
        set()
    )

    assert result == "FULL"
    assert flights == before


def test_check_in_restricted_randomized():
    restricted = {
        "Moscow",
        "Pyongyang",
        "Restricted City"
    }

    restricted_destination = rng.choice(
        list(restricted)
    )

    flight_number = make_random_flight_number()

    flights = {
        flight_number: {
            "destination": restricted_destination,
            "departure": "14:00",
            "gate": "B2",
            "capacity": 5,
            "passengers": []
        }
    }

    result = am.check_in_passenger(
        flights,
        flight_number,
        "Alice Test",
        restricted
    )

    assert result == "RESTRICTED"

    assert flights[flight_number]["passengers"] == []




def test_gate_change_randomized():
    flights = make_random_flights(4)

    allowed_gates = {
        "A1", "A2", "A3",
        "B1", "B2", "B3"
    }

    flight_number = rng.choice(
        list(flights.keys())
    )

    new_gate = rng.choice(
        list(allowed_gates)
    )

    result = am.change_gate(
        flights,
        flight_number.lower(),
        new_gate.lower(),
        allowed_gates
    )

    assert result == "OK"

    assert (
        flights[flight_number]["gate"]
        == new_gate
    )


def test_invalid_gate_does_not_modify():
    flights = make_random_flights(3)

    flight_number = rng.choice(
        list(flights.keys())
    )

    before = copy.deepcopy(flights)

    result = am.change_gate(
        flights,
        flight_number,
        "Z99",
        {"A1", "A2"}
    )

    assert result == "INVALID_GATE"
    assert flights == before




def test_remove_passenger_randomized():
    flight_number = make_random_flight_number()

    passengers = [
        "Alice Wong",
        "Bob Lee",
        "Chen Wei",
        "David Kim"
    ]

    flights = {
        flight_number: {
            "destination": "Paris",
            "departure": "10:00",
            "gate": "A1",
            "capacity": 10,
            "passengers": passengers.copy()
        }
    }

    target = rng.choice(passengers)

    result = am.remove_passenger(
        flights,
        flight_number.lower(),
        target.upper()
    )

    assert result == "OK"

    assert target not in flights[flight_number]["passengers"]




def test_flight_status_randomized():
    for _ in range(100):

        capacity = rng.randint(1, 30)

        passenger_count = rng.randint(
            0,
            capacity
        )

        passengers = [
            f"P{i}"
            for i in range(passenger_count)
        ]

        flight = {
            "capacity": capacity,
            "passengers": passengers
        }

        percentage = (
            passenger_count
            / capacity
            * 100
        )

        if percentage == 100:
            expected = "FULL"

        elif percentage >= 75:
            expected = "ALMOST FULL"

        else:
            expected = "AVAILABLE"

        assert (
            am.flight_status(flight)
            == expected
        )




def test_sorted_manifest_randomized():
    flight_number = make_random_flight_number()

    passengers = []

    while len(passengers) < 8:
        name = make_random_name()

        if name not in passengers:
            passengers.append(name)

    rng.shuffle(passengers)

    flights = {
        flight_number: {
            "destination": "Madrid",
            "departure": "13:00",
            "gate": "A1",
            "capacity": 20,
            "passengers": passengers.copy()
        }
    }

    original = copy.deepcopy(flights)

    result = am.sorted_manifest(
        flights,
        flight_number
    )

    assert result == sorted(passengers)

    assert flights == original




def test_total_passengers_randomized():
    flights = make_random_flights(10)

    expected = 0

    for flight in flights.values():
        expected += len(
            flight["passengers"]
        )

    assert (
        am.total_passengers(flights)
        == expected
    )




def test_any_full_flight_randomized():
    flights = make_random_flights(6)

    for flight in flights.values():

        if (
            len(flight["passengers"])
            == flight["capacity"]
        ):
            flight["passengers"].pop()

    assert (
        am.any_full_flight(flights)
        is False
    )

    chosen = rng.choice(
        list(flights.values())
    )

    chosen["passengers"] = [
        f"P{i}"
        for i in range(
            chosen["capacity"]
        )
    ]

    assert (
        am.any_full_flight(flights)
        is True
    )


def test_all_flights_have_passengers_randomized():
    flights = make_random_flights(6)

    # Force all to contain at least one.
    for flight in flights.values():

        if len(flight["passengers"]) == 0:
            flight["passengers"].append(
                "Test Passenger"
            )

    assert (
        am.all_flights_have_passengers(
            flights
        )
        is True
    )

    chosen = rng.choice(
        list(flights.values())
    )

    chosen["passengers"] = []

    assert (
        am.all_flights_have_passengers(
            flights
        )
        is False
    )