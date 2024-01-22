import datetime  # Import datetime module for time operations

class Garage:
    def __init__(self):
        # Initialize Garage with 120 tickets and parking spaces, and an hourly rate
        self.tickets = [True] * 121
        self.parking_spaces = [True] * 121
        self.active_tickets = {}  # Dictionary to track the status of active tickets
        self.rate_per_hour = 2.0  # Set hourly parking rate
        


#### -------- CALLABLE METHODS -------- #####    

    def take_ticket(self):
        # Issue a ticket if available and mark parking space as occupied
        if self.check_space_availability():
            ticket_index = self.tickets.index(True)
            self.tickets[ticket_index] = False
            self.parking_spaces[ticket_index] = False
            # Record the ticket's issue time
            self.active_tickets[ticket_index] = {"paid": False, "entry_time": datetime.datetime.now()}
            print(f"Ticket #{ticket_index} taken. Please park at space #{ticket_index}.")
        else:
            print("No tickets available")
            
    def pay_for_parking(self, ticket_number=None):
        # Process payment for parking
        if ticket_number is None:
            ticket_number = self.safe_input_ticket_number("Enter your ticket number: ")
        if ticket_number in self.active_tickets:
            required_fee = self.calculate_fee(ticket_number)
            print(f"Fee owed: ${required_fee}")
            amount = float(input("Enter payment amount: "))
            if amount >= required_fee:
                self.active_tickets[ticket_number]["paid"] = True
                print(f"Payment accepted for ticket number: {ticket_number}.")
            else:
                print("Error in payment. Please try again.")
        else:
            print("Invalid ticket number or ticket not found.")            
            
    def extend_parking_time(self, ticket_number):
        # Allow users to extend their parking time
        if ticket_number in self.active_tickets:
            try:
                additional_time = int(input("How many minutes would you like to extend your parking? "))
                current_entry_time = self.active_tickets[ticket_number]["entry_time"]
                self.active_tickets[ticket_number]["entry_time"] = current_entry_time - datetime.timedelta(minutes=additional_time)
                new_fee = self.calculate_fee(ticket_number)
                print(f"Parking time extended for ticket number: {ticket_number}. New fee: ${new_fee}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("Invalid ticket number or ticket not found.") 

    def leave_garage(self, ticket_number=None):
        # Handle the process of a car leaving the garage
        if ticket_number in self.active_tickets:
            if self.active_tickets[ticket_number].get("paid", False):
                print("Thank you, have a nice day!")
                self._reset_ticket_and_space(ticket_number)
            else:
                print("Ticket not paid. Please pay for your parking.")
                self.pay_for_parking(ticket_number)
                if self.active_tickets[ticket_number].get("paid", False):
                    print("Thank you, have a nice day!")
                    self._reset_ticket_and_space(ticket_number)
                else:
                    print("Payment not completed. You cannot leave the garage.")
        else:
            print("Invalid ticket number or no ticket has been taken.")          
            
    def display_garage_status(self):
        # Display the current availability of tickets and parking spaces
        available_tickets = self.tickets.count(True)
        available_spaces = self.parking_spaces.count(True)
        print(f"Available Tickets: {available_tickets}, Available Spaces: {available_spaces}")
    
    def interactive_menu(self):
        # Interactive menu for users to interact with the garage system
        while True:
            print("\nWelcome to the Garage!")
            print("A. Take a ticket")
            print("B. Pay for parking")
            print("C. Extend parking")
            print("D. Leave garage")
            print("E. Exit program")
            print("F. Display garage status")
            choice = input("Choose option A-F: ").upper()

    def interactive_menu(self):
        while True:
            print("\nWelcome to the Garage!")
            print("A. Take a ticket")
            print("B. Pay for parking")
            print("C. Extend parking")
            print("D. Leave garage")
            print("E. Exit program")
            print("F. Display garage status")
            choice = input("Choose option A-F: ").upper()

            if choice == "A":
                self.take_ticket()
            elif choice == "B":
                ticket_number = self.safe_input_ticket_number("Enter your ticket number: ")
                self.pay_for_parking(ticket_number)
            elif choice == "C":
                ticket_number = self.safe_input_ticket_number("Enter your ticket number to extend parking: ")
                self.extend_parking_time(ticket_number)
            elif choice == "D":
                ticket_number = self.safe_input_ticket_number("Enter your ticket number to leave: ")
                if ticket_number in self.active_tickets:
                    self.leave_garage(ticket_number)
                else:
                    print("Can't leave without a valid ticket.")
            elif choice == "E":
                print("Exiting the program. Have a nice day!")
                break
            elif choice == "F":
                self.display_garage_status()
            else:
                print("Invalid option. Please try again.")



#### -------- HELPER METHODS -------- #####        
            
    def check_space_availability(self):
        # Check if there is at least one available ticket
        return True in self.tickets

    def calculate_fee(self, ticket_number):
        # Calculate the fee based on the duration of parking
        if ticket_number in self.active_tickets:
            entry_time = self.active_tickets[ticket_number]["entry_time"]
            exit_time = datetime.datetime.now()
            duration = exit_time - entry_time
            hours = duration.total_seconds() / 3600
            return round(hours * self.rate_per_hour, 2)
        else:
            print("Error: Entry time not recorded for this ticket.")
            return 0

    def safe_input_ticket_number(self, prompt):
        # Parse ticket number input, checking if it is a valid integer
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid ticket number.")
    
    def _reset_ticket_and_space(self, ticket_number):
        # Reset the ticket and parking space status after a car leaves
        self.tickets[ticket_number] = True
        self.parking_spaces[ticket_number] = True
        del self.active_tickets[ticket_number]

        

# Create an instance of the Garage and start the interactive menu
garage = Garage()
garage.interactive_menu()
