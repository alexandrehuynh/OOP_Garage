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
        if True in self.tickets:
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

    def calculate_fee(self):
        if "ticket_number" in self.current_ticket:
            ticket_number = self.current_ticket["ticket_number"]
            if ticket_number in self.entry_time:
                entry_time = self.entry_time[ticket_number]
                exit_time = datetime.datetime.now()
                duration = exit_time - entry_time
                hours = duration.total_seconds() / 3600
                fee = round(hours * self.rate_per_hour, 2)
                return fee
            else:
                print("Error: Entry time not recorded.")
                return 0  # Default fee or appropriate handling
        else:
            print("Error: No current ticket.")
            return 0  # Default fee or appropriate handling

    def pay_for_parking(self):
        amount = float(input("Enter payment amount: "))
        required_fee = self.calculate_fee()
        if required_fee is not None and amount >= required_fee:
            self.current_ticket["paid"] = True
            print(f"Your ticket number: {self.current_ticket['ticket_number']} is now paid")
        else:
            print("Error in payment. Please try again.")

    
    def leave_garage(self): 
        if "ticket_number" in self.current_ticket:
            if self.current_ticket.get("paid"):
                print("Thank you, Have a nice day!")
                ticket_number = self.current_ticket['ticket_number']
                self.parking_spaces[ticket_number] = True
                self.tickets[ticket_number] = True
                self.current_ticket = {}

            else:
                print("You have not paid your ticket.")
                self.pay_for_parking() 
                if self.current_ticket.get("paid"):
                    print("Thank you, Have a nice day!")
                    ticket_number = self.current_ticket['ticket_number']
                    self.parking_spaces[ticket_number] = True
                    self.tickets[ticket_number] = True
                    self.current_ticket = {}
                
        else:
            print("Yoooo we need a ticket home boy/girl!")


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