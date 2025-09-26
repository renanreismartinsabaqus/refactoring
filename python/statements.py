import math


def format_as_dollars(amount): # Maybe move this outside
    return f"${amount:0,.2f}"


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'

    # Invoice iteration
    for perf in invoice['performances']: # Maybe move this outside
        play = plays[perf['playID']]

        this_amount = amountFor(perf, play)

        # add volume credits
        volume_credits += max(perf['audience'] - 30, 0)
        # add extra credit for every ten comedy attendees
        if "comedy" == play["type"]:
            volume_credits += math.floor(perf['audience'] / 5)
        # print line for this order
        result += f' {play["name"]}: {format_as_dollars(this_amount/100)} ({perf["audience"]} seats)\n'
        total_amount += this_amount

    result += f'Amount owed is {format_as_dollars(total_amount/100)}\n'
    result += f'You earned {volume_credits} credits\n'
    return result


def amountFor(performance, play):
    if play['type'] == "tragedy":
        this_amount = 40000
        if performance['audience'] > 30:
            this_amount += 1000 * (performance['audience'] - 30)
    elif play['type'] == "comedy":
        this_amount = 30000
        if performance['audience'] > 20:
            this_amount += 10000 + 500 * (performance['audience'] - 20)

        this_amount += 300 * performance['audience']
    else:
        raise ValueError(f'unknown type: {play["type"]}')

    return this_amount

def calculation(invoice: dict, plays: dict):
    pass

def generate_html_report(invoice: dict, plays: dict):
    calcuation = calculation()
    # Generates a pretty html report
    pass

def generate_text_report(invoice: dict, plays: dict):
    calcuation = calculation()
    # Generates a pretty text report
    pass



#1) I need o be able o render the stament in html and text
#2) Extend the calculations by play type
#3) Make the code more readable and more sclable


# Coding plan
#1 taking notes of the calculation logic
#2 define main functions to code
#3 



# Functions

# calcualtion()
    # 
# renders_html
# renders_text

