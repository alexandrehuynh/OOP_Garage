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