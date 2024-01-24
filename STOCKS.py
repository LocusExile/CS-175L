purchased = int(input("How many stocks did you buy? "))
buyValue = float(input("How much did you spend per stock "))
commission = float(input("What is the percent that you pay your broker? "))
sellValue = float(input("What was the sell value of your stocks? "))
sold = int(input("How many stocks did you sell? "))

amountPaid = purchased * buyValue

purchCommission = amountPaid * commission

amountReceived = sold * sellValue

sellCommission = amountReceived * commission

amountLeft = amountReceived - sellCommission - purchCommission - amountPaid

print("Joe paid", amountPaid, "dollars for his stocks")

print("His broker was paid", purchCommission, "dollars during the purchase")

print("Joe's stocks sold for", amountReceived, "dollars")

print("The broker was paid", sellCommission, "dollars during the sale")

if amountLeft < 0:
    print("Joe lost", abs(amountLeft), "dollars")
else:
    print("Joe made", amountLeft, "dollars")
