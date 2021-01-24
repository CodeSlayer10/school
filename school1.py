Ticket_Price = 42
Glasses3D_Price = 5



def Total_Price_Calculator(Ticket_Amount, Glasses3D_Amount):
    return Ticket_Price*Ticket_Amount+Glasses3D_Price*Glasses3D_Amount

ticket_requested_amount = int(input("Enter Number of tickets: "))
glasses3d_requested_amount = int(input("Enter Number of 3D glasses: "))
total_cost = Total_Price_Calculator(ticket_requested_amount, glasses3d_requested_amount)
print("your total cost will be {}".format(total_cost))
