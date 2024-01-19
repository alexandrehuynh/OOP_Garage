class Garage:
    def __init__(self):
        self.tickets = [True] * 121 # Initial ticket
        self.parking_spaces = [True] * 121 # Initial parking spacesw
        self.current_ticket = {}
        
    def take_ticket(self):
        if True in self.tickets:
            
            ticket_index = self.tickets.index(True)
            
            self.tickets[ticket_index] = False
            self.parking_spaces[ticket_index] = False
            self.current_ticket = {"ticket number": ticket_index, "paid": False}
            print(f"Ticket #{ticket_index} taken. Please park at space #{ticket_index}.")
        
        else:
            print("No tickets available")
            
    def pay_for_parking(self):   
        amount = float(input("Enter amount to pay: "))
        
        if amount > 0:
            self.current_ticket["paid"] = True
            print(f"Your ticket number: {self.current_ticket['ticket number']} is now paid")
    
    def leave_garage():
        pass

#####   TESTING    ####
garage = Garage()
garage.take_ticket()
garage.pay_for_parking()
garage.leave_garage()