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
            f"It will take {years} years for your investment of {message_two} to double")
