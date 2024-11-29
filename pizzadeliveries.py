print("Welcome to Python Pizza Deliveries!")
size = input("What size do you want? Small, Medium, or Large: ").lower()
add_pepperoni = input("Do you want to add pepperoni? (yes or no): ").lower()
extra_cheese = input("Do you want to add extra cheese? (yes or no): ").lower()

bill = 0

# Set the base price based on size
if size == "small":
    bill = 15
elif size == "medium":
    bill = 20
elif size == "large":
    bill = 25
else:
    print("Invalid size. Please choose Small, Medium, or Large.")
    exit()

# Add cost for pepperoni
if add_pepperoni == "yes":
    bill += 3

# Add cost for extra cheese
if extra_cheese == "yes":
    bill += 1

# Print the final bill
print(f"Your total bill is ${bill}.")
