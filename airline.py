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

def main():
    pass

if __name__ == "__main__":
    main()
