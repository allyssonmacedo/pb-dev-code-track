class Ticket: 
    def __init__(self, price_ticket) -> None:
        self.value = price_ticket
    
    def print_value(self):
        return f"Esse ticket custa {self.value}" 
    
class VIP(Ticket):
    def __init__(self, price_ticket) -> None:
        super().__init__(price_ticket) 
        self.plus_vip = 10 
    
    def print_value(self): 
        return f"Esse ticket custa {self.value + self.plus_vip}" 
    
ticket = Ticket(120) 
print(ticket.print_value()) 
ticket_vip = VIP(120) 
print(ticket_vip.print_value())