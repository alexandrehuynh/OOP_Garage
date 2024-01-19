class Garage:
    def __init__(self):
        self.tickets = [True] * 100  # Assuming 100 tickets initially
        self.parking_spaces = [True] * 100  # Assuming 100 parking spaces initially
        self.current_ticket = {}

    def take_ticket(self):
        if True in self.tickets:
            ticket_index = self.tickets.index(True)
            self.tickets[ticket_index] = False
            self.parking_spaces[ticket_index] = False
            self.current_ticket = {"ticket_number": ticket_index, "paid": False}
            print(f"Ticket #{ticket_index} taken. Please park at space #{ticket_index}.")
        else:
            print("No tickets available.")

    def pay_for_parking(self):
        pass

    def leave_garage(self):
        pass


#####   TESTING    ####
garage = Garage()
garage.take_ticket()
garage.pay_for_parking()
garage.leave_garage()