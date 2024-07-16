name = input("Customer Name: ")
bill = input("Bill Amount: Rs.")
tip = int(bill)/10
gst = int(bill)*(1+20/100)
total_bill = int(bill) + tip + gst
print("Total Bill: Rs.",total_bill)
cash_received = input("Cash received: Rs.")
change = int(cash_received) - total_bill
print("-----------------------------------------")
print("                    RECEIPT")
print("-----------------------------------------")
print("Name:",name)
print("Sub-total: Rs.",bill)
print("10% Tip: Rs.",tip)
print("Sales Tax 20% Amount: Rs.",gst)
print("-----------------------------------------")
print("Total bill: Rs.",total_bill)
print("Cash received: Rs.",cash_received)
print("Change: Rs.",change)
print("-----------------------------------------")
thnx="Thank You For Shopping!"
print("            ",thnx)

