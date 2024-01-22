class Garage:
    def __init__(self):
        self.tickets = [True] * 121 # Initial ticket
        self.parking_spaces = [True] * 121 # Initial parking spaces
        self.current_ticket = {}
        
    def take_ticket(self):
        if True in self.tickets:
            
            ticket_index = self.tickets.index(True)
            
            self.tickets[ticket_index] = False
            self.parking_spaces[ticket_index] = False
            self.current_ticket = {"ticket_number": ticket_index, "paid": False}
            print(f"Ticket #{ticket_index} taken. Please park at space #{ticket_index}.")
        
        else:
            print("No tickets available")
            
    def pay_for_parking(self):   
        amount = float(input("Enter amount to pay: "))
        
        if amount > 0:
            self.current_ticket["paid"] = True
            print(f"Your ticket number: {self.current_ticket['ticket_number']} is now paid")

    def extend_parking_time(self):
        if ticket_number in self.current_ticket:
            ticket_number = self.current_ticket.get("paid")
            print(f"How many minutes would you like to extend your parking {ticket_number}?")

        else:
            print("You did not add time to your ticket!")
            self.pay_for_parking()

    
    def leave_garage(self): 
        if "ticket_number" in self.current_ticket:
            if self.current_ticket.get("paid"):
                print("You may leave the Batcave!")
                ticket_number = self.current_ticket['ticket_number']
                self.parking_spaces[ticket_number] = True
                self.tickets[ticket_number] = True
                self.current_ticket = {}

            else:
                print("You have not paid your ticket.")
                self.pay_for_parking() 
                if self.current_ticket.get("paid"):
                    print("You may leave the Batcave!")
                    ticket_number = self.current_ticket['ticket_number']
                    self.parking_spaces[ticket_number] = True
                    self.tickets[ticket_number] = True
                    self.current_ticket = {}
                
        else:
            print("Yoooo we need a ticket home boy/girl!")

    def interactive_menu(self):
        while True:
            print("Welcome to the BatCave! ")
            print("A. Take a ticket")
            print("B. pay for paking ")
            print("C. Extend parking")
            print("D. Leave garage")
            person = input("Choose option A-D to access the BatCave!")

            if person == "A":
                self.take_ticket()
            elif person == "B":
                self.pay_for_parking()
            elif person == "C":
                self.extend_parking_time()
            elif person == "D":
                self.leave_garage()
                break
            else:
                print("Access denied to the Bat Cave!")



garage = Garage()
garage.interactive_menu()

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