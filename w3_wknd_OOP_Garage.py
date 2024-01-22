import datetime

class Garage:
    def __init__(self):
        self.tickets = [True] * 121 # Initial ticket
        self.parking_spaces = [True] * 121 # Initial parking spaces
        self.active_tickets = {} 
        self.entry_time = {}
        self.exit_time = {}
        self.rate_per_hour = 2.0
        
    def take_ticket(self):
        if self.check_space_availability():
            ticket_index = self.tickets.index(True)
            self.tickets[ticket_index] = False
            self.parking_spaces[ticket_index] = False
            self.active_tickets[ticket_index] = {"paid": False, "entry_time": datetime.datetime.now()}
            self.entry_time[ticket_index] = datetime.datetime.now()  # Ensure this line is working correctly
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
        if ticket_number in self.active_tickets and ticket_number in self.entry_time:
            required_fee = self.calculate_fee(ticket_number)
            amount = float(input("Enter payment amount: "))
            if amount >= required_fee:
                self.active_tickets[ticket_number]["paid"] = True
                print(f"Payment accepted for ticket number: {ticket_number}.")
            else:
                print("Error in payment. Please try again.")
        else:
            print("Invalid ticket number or ticket not found.")
            
    def leave_garage(self, ticket_number=None):
        if ticket_number in self.active_tickets and ticket_number in self.entry_time:
            if self.active_tickets[ticket_number].get("paid", False):
                print("Thank you, have a nice day!")
                self.tickets[ticket_number] = True
                self.parking_spaces[ticket_number] = True
                del self.active_tickets[ticket_number]  # Remove the ticket from active_tickets
            else:
                print("Ticket not paid. Please pay for your parking.")
                self.pay_for_parking(ticket_number)
        else:
            print("Invalid ticket number or no ticket has been taken.")

# Garage class containing:
# - tickets: List to track available tickets.
# - parking_spaces: List to track available parking spaces.
# - active_tickets: Dictionary to track the status of the current ticket.
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