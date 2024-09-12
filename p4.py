# Get user inputs
while True:
    p = input("Enter the initial principal amount ($P): ")
    if 0 < float(p) < 100_000:
        break
while True:
    r = input("Enter the annual interest rate (r%): ")
    if 0 < float(r) < 10:
        break
while True:
    n = input("Enter the number of compounding periods per year (n = 1, 2, 4, 12): ")
    if int(n) == 1 or int(n) == 2 or int(n) == 4 or int(n) == 12:
        break
t = input("Enter the number of years (t): ")

# Convert the annual interest rate from percentage to decimal
r = float(r)/100
coeff = pow(1.0 + (r / int(n)), int(n))

# @return the amount after a period
def calculate_and_print (year: int, principal: float):
    # Divide
    if year < 1:
        return principal
    a_previous = calculate_and_print(year - 1, principal)
    a = a_previous * coeff
    # Conquer, Print the year and amount and interest earned
    print(f"{year:>4} | ${a:>12.2f} | ${(a - a_previous):>14.2f}")
    return a

print("Year |     Amount    | Interest Earned")
print("-"*40)

total_amount = calculate_and_print(int(t), int(p))

# Print the summary
print("Summary:")
print(f"Total interest earned: ${total_amount - int(p):.2f}")
print(f"Final account balance: ${total_amount:.2f}")
