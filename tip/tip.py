print("Hello there! Welcome to the tip calculator!\n")
bill = float(input("What was the total bill?\n"))
tip = int(input("How much do you want to tip? 10, 12, 15, 20 (in %)?\n"))
people = int(input("How many people are splitting the bill?\n"))
tip = float(tip/100)
total_bill = bill * (1+tip)
final_bill = round(float(total_bill/people),2)
print(f"Each person should pay ${final_bill}")