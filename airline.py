from queue import PriorityQueue
from typing import Dict, List, Union


class Passenger:
    def __init__(self, name, passport_number, dob, membership_status):
        self.name = name
        self.passport_number = passport_number
        self.dob = dob
        self.membership_status = membership_status


class Flight:
    def __init__(self, flight_number, max_capacity, departure, arrival):
        self.flight_number = flight_number
        self.max_capacity = max_capacity
        self.departure = departure
        self.arrival = arrival
        self.confirmed_passengers = []
        self.waiting_list = {
            "gold": PriorityQueue(),
            "silver": PriorityQueue(),
            "non_member": PriorityQueue()
        }

    def get_passengers_info(self) -> List[Passenger]:
        return self.confirmed_passengers

    def add_passenger(self, passenger:Passenger):

        # if there is space in the confirmed_passengers list, add passengers to the list.
        # Else, add passengers to the queue

        if len(self.confirmed_passengers) < self.max_capacity:
            self.confirmed_passengers.append(passenger)
        else:
            membership_status = passenger.membership_status
            self.waiting_list[membership_status].put(passenger)

    def assign_seat_to_waiting_list(self):
        # Assign seats to passengers on waiting lists based on membership
        for status in ["gold", "sliver", "non_member"]:
            if not self.waiting_list[status].empty():
                next_passenger = self.waiting_list[status].get()
                self.confirmed_passengers.append(next_passenger)
                print(f"Seat assigned to {next_passenger.name} on flight {self.flight_number}")

    def occupany_rate(self) -> float:
        return len(self.confirmed_passengers)/self.max_capacity

    class AirLineReservationSystem:
        pass


def main():
    # Create flights
    flight1 = Flight("F001", 200, "CityA", "CityB")
    flight2 = Flight("F002", 150, "CityC", "CityD")


if __name__ == "__main__":
    main()
