# double interest rate calculator using 72 rule

rate = "\n Please enter the annualized interest rate or enter 'quit' to end the program: "

investment = "\n Please enter initial investment amount: "

message = ""

while True:

    message = input(rate)

    if message == 'quit':
        break
    else:
        years = 72 / int(message)
        message_two = input(investment)
        print(
            f"It will take {years} years for your investment of ${message_two} to double")

            

# rate = input(
#     "\n Please enter the annualized interest rate or enter 'quit' to end the program: ")

# if rate == 'quit':
#     exit()

# investment = input("\n Please enter initial investment amount: ")

# years = 0
# amount = int(investment)


# while amount < 2 * int(investment):

#     amount = amount + (amount * (int(rate)/100))
#     years += 1
# print(f"It will take {years} years for your investment to double")


