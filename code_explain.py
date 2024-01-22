import datetime  # Importing the datetime module for handling time-related tasks

class Garage:
    def __init__(self):
        # Initializing the Garage object with attributes:
        self.tickets = [True] * 121  # A list to represent 120 available tickets (0-120)
        self.parking_spaces = [True] * 121  # A list to represent 120 parking spaces
        self.active_tickets = {}  # A dictionary to store information about active tickets
        self.rate_per_hour = 2.0  # Setting the parking rate per hour
        
    def check_space_availability(self):
        # Method to check if there are any available tickets
        return True in self.tickets  # Returns True if there's at least one True (available ticket) in the tickets list

    def take_ticket(self):
        # Method for taking a ticket and allocating a parking space
        if self.check_space_availability():
            # If there's an available ticket
            ticket_index = self.tickets.index(True)  # Find the first available ticket
            self.tickets[ticket_index] = False  # Mark this ticket as taken
            self.parking_spaces[ticket_index] = False  # Mark the corresponding parking space as occupied
            # Record the ticket's status and entry time in active_tickets
            self.active_tickets[ticket_index] = {"paid": False, "entry_time": datetime.datetime.now()}
            # Inform the user of their ticket number and parking space
            print(f"Ticket #{ticket_index} taken. Please park at space #{ticket_index}.")
        else:
            # If no tickets are available
            print("No tickets available")

    def calculate_fee(self, ticket_number):
        # Method to calculate the parking fee for a given ticket number
        if ticket_number in self.active_tickets:
            # If the ticket is an active ticket
            entry_time = self.active_tickets[ticket_number]["entry_time"]  # Get the entry time for the ticket
            exit_time = datetime.datetime.now()  # Current time as exit time
            duration = exit_time - entry_time  # Calculate the parking duration
            hours = duration.total_seconds() / 3600  # Convert duration to hours
            return round(hours * self.rate_per_hour, 2)  # Calculate and return the fee
        else:
            # If the ticket number is not found in active tickets
            print("Error: Entry time not recorded for this ticket.")
            return 0

    def safe_input_ticket_number(self, prompt):
        # Utility method to safely get a ticket number input from the user
        while True:
            # Infinite loop to keep asking until valid input is given
            try:
                return int(input(prompt))  # Return the input after converting it to an integer
            except ValueError:
                # If the input is not a valid integer
                print("Invalid input. Please enter a valid ticket number.")
        
    def pay_for_parking(self, ticket_number=None):
        # Method for a user to pay for their parking
        if ticket_number is None:
            # If no ticket number is provided as an argument
            ticket_number = self.safe_input_ticket_number("Enter your ticket number: ")  # Get the ticket number safely
        if ticket_number in self.active_tickets:
            # If the ticket number is valid and active
            required_fee = self.calculate_fee(ticket_number)  # Calculate the fee
            print(f"Fee owed: ${required_fee}")  # Display the fee owed
            amount = float(input("Enter payment amount: "))  # Get the payment amount from user
            if amount >= required_fee:
                # If the paid amount is enough to cover the fee
                self.active_tickets[ticket_number]["paid"] = True  # Mark the ticket as paid
                print(f"Payment accepted for ticket number: {ticket_number}.")
            else:
                # If the paid amount is not enough
                print("Error in payment. Please try again.")
        else:
            # If the ticket number is invalid or not found
            print("Invalid ticket number or ticket not found.")

    def leave_garage(self, ticket_number=None):
        # Method for a user to leave the garage
        if ticket_number in self.active_tickets:
            # If the ticket number is valid and active
            if self.active_tickets[ticket_number].get("paid", False):
                # If the ticket has been paid for
                print("Thank you, have a nice day!")
                self.tickets[ticket_number] = True  # Mark the ticket as available again
                self.parking_spaces[ticket_number] = True  # Mark the parking space as available
                del self.active_tickets[ticket_number]  # Remove the ticket from active tickets
            else:
                # If the ticket has not been paid for
                print("Ticket not paid. Please pay for your parking.")
                self.pay_for_parking(ticket_number)  # Prompt the user to pay for the ticket
        else:
            # If the ticket number is invalid or not found
            print("Invalid ticket number or no ticket has been taken.")

    def display_garage_status(self):
        # Method to display the current status of the garage
        available_tickets = self.tickets.count(True)  # Count available tickets
        available_spaces = self.parking_spaces.count(True)  # Count available parking spaces
        print(f"Available Tickets: {available_tickets}, Available Spaces: {available_spaces}")  # Display the counts

    def extend_parking_time(self, ticket_number):
        # Method to extend the parking time for a given ticket
        if ticket_number in self.active_tickets:
            # If the ticket number is valid and active
            try:
                additional_time = int(input("How many minutes would you like to extend your parking? "))  # Get additional time from user
                current_entry_time = self.active_tickets[ticket_number]["entry_time"]  # Get the current entry time
                # Update the entry time to subtract the additional time
                self.active_tickets[ticket_number]["entry_time"] = current_entry_time - datetime.timedelta(minutes=additional_time)
                new_fee = self.calculate_fee(ticket_number)  # Calculate the new fee
                print(f"Parking time extended for ticket number: {ticket_number}. New fee: ${new_fee}")  # Display the new fee
            except ValueError:
                # If the input is not a valid integer
                print("Invalid input. Please enter a number.")
        else:
            # If the ticket number is invalid or not found
            print("Invalid ticket number or ticket not found.")
    
    def interactive_menu(self):
        # Interactive menu method for the user to interact with the garage system
        while True:
            # Infinite loop to keep the menu running until the user decides to exit
            print("\nWelcome to the Garage!")
            print("A. Take a ticket")  # Option to take a ticket
            print("B. Pay for parking")  # Option to pay for parking
            print("C. Extend parking")  # Option to extend parking time
            print("D. Leave garage")  # Option to leave the garage
            print("E. Exit program")  # Option to exit the program
            choice = input("Choose option A-E: ").upper()  # Get the user's choice and convert it to uppercase

            if choice == "A":
                self.take_ticket()  # Handle taking a ticket
            elif choice == "B":
                ticket_number = self.safe_input_ticket_number("Enter your ticket number: ")  # Get ticket number for payment
                self.pay_for_parking(ticket_number)  # Handle payment
            elif choice == "C":
                ticket_number = self.safe_input_ticket_number("Enter your ticket number to extend parking: ")  # Get ticket number for extending parking time
                self.extend_parking_time(ticket_number)  # Handle extending parking time
            elif choice == "D":
                ticket_number = self.safe_input_ticket_number("Enter your ticket number to leave: ")  # Get ticket number for leaving
                if ticket_number in self.active_tickets:
                    self.leave_garage(ticket_number)  # Handle leaving the garage
                else:
                    print("Can't leave without a valid ticket.")  # Message if no valid ticket
            elif choice == "E":
                print("Exiting the program. Have a nice day!")  # Exit message
                break  # Break the loop to exit the program
            else:
                print("Invalid option. Please try again.")  # Message for invalid option

# Create an instance of the Garage and start the interactive menu
garage = Garage()
garage.interactive_menu()  # Start the interactive menu for the garage
