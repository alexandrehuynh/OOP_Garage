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
        amount = float(input("Enter payment amount: "))
        if amount > 0:
            self.current_ticket["paid"] = True
            print("Your ticket has been paid. You have 15 minutes to leave.")

    def leave_garage(self):
        if self.current_ticket.get("paid"):
            print("Thank you, have a nice day!")
            ticket_number = self.current_ticket["ticket_number"]
            self.tickets[ticket_number] = True
            self.parking_spaces[ticket_number] = True
        else:
            print("Ticket not paid. Please pay for your parking.")
            self.pay_for_parking()
            print("Thank you, have a nice day!")
            ticket_number = self.current_ticket["ticket_number"]
            self.tickets[ticket_number] = True
            self.parking_spaces[ticket_number] = True
