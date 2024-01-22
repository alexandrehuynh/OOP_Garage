import datetime

class Garage:
    def __init__(self):
        self.tickets = [True] * 121 # Initial ticket
        self.parking_spaces = [True] * 121 # Initial parking spaces
        self.current_ticket = {}
        self.entry_time = {}
        self.exit_time = {}
        self.rate_per_hour = 2.0
        
    def take_ticket(self):
        if self.check_space_availability():
            ticket_index = self.tickets.index(True)
            self.tickets[ticket_index] = False
            self.parking_spaces[ticket_index] = False
            self.current_ticket = {"ticket_number": ticket_index, "paid": False}
            self.entry_time[ticket_index] = datetime.datetime.now()  # Record entry time
            print(f"Ticket #{ticket_index} taken. Please park at space #{ticket_index}.")
        else:
            print("No tickets available")
     
    def display_garage_status(self):
        available_tickets = self.tickets.count(True)
        available_spaces = self.parking_spaces.count(True)
        print(f"Available Tickets: {available_tickets}, Available Spaces: {available_spaces}")
        
    def check_space_availability(self):
        return True in self.tickets

    def calculate_fee(self, ticket_number):
        if ticket_number in self.entry_time:
            entry_time = self.entry_time[ticket_number]
            exit_time = datetime.datetime.now()
            duration = exit_time - entry_time
            hours = duration.total_seconds() / 3600
            return round(hours * self.rate_per_hour, 2)
        else:
            print("Error: Entry time not recorded for this ticket.")
            return 0

    def pay_for_parking(self, ticket_number=None):
        if ticket_number is None:
            ticket_number = self.current_ticket.get("ticket_number")

        if ticket_number is not None and ticket_number in self.entry_time:
            required_fee = self.calculate_fee(ticket_number)
            amount = float(input("Enter payment amount: "))
            if amount >= required_fee:
                print(f"Payment accepted for ticket number: {ticket_number}.")
                self.current_ticket = {}  # Clear current ticket
                self.exit_time[ticket_number] = datetime.datetime.now()
            else:
                print("Error in payment. Please try again.")
        else:
            print("Invalid ticket number or ticket not found.")
            
    def leave_garage(self, ticket_number=None):
        if ticket_number is None:
            ticket_number = self.current_ticket.get("ticket_number")

        if ticket_number in self.entry_time:
            if not self.current_ticket.get("paid", False):
                print("Ticket not paid. Please pay for your parking.")
                self.pay_for_parking(ticket_number)

            if self.current_ticket.get("paid"):
                print("Thank you, have a nice day!")
                self.tickets[ticket_number] = True
                self.parking_spaces[ticket_number] = True
                self.current_ticket = {}
        else:
            print("Invalid ticket number or no ticket has been taken.")

# Garage class containing:
# - tickets: List to track available tickets.
# - parking_spaces: List to track available parking spaces.
# - current_ticket: Dictionary to track the status of the current ticket.
# - rate_per_hour: Attribute to store the hourly parking rate.
# - entry_time: Dictionary to track the entry time for each ticket.
# - exit_time: Dictionary to track the exit time for each ticket.

# Methods:
# - take_ticket()
# - pay_for_parking()
# - leave_garage()
# - calculate_fee()
# - check_space_availability()
# - display_garage_status()
# - extend_parking()
# - generate_report()