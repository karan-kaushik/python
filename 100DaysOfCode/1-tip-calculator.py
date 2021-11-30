bill_amount = input("What is the bill amount? ")
tip_percent = int(input("What is the tip percentage? "))
number_of_people = int(input("How many people are splitting the bill? "))

def calculate_tip(bill_amount, tip_percent, number_of_people):
    tip_amount = float(bill_amount) * tip_percent / 100
    total_amount = float(bill_amount) + tip_amount
    final_amount_per_person = round(total_amount / number_of_people, 2)
    return final_amount_per_person

print(calculate_tip(bill_amount, tip_percent, number_of_people))