import math


def format_as_dollars(amount): # Maybe move this outside
    return f"${amount:0,.2f}"


def statement(invoice, plays):
    # Invoice iteration
    perf_results = []
    total_amount = 0


    performances = []
    for performance in invoice["performances"]:
        play = plays[performance['playID']]
        performances.append(
            {
                **performance,
                "play_name": play["name"],
                "play_type": play["type"],
                "amount": amount_for(performance, play)
            }
        )
        
    
    for perf in performances: # Maybe move this outside
        total_amount += perf["amount"]
        perf_results.append({"name": perf["play_name"], "amount": format_as_dollars(perf["amount"]/100), "seats":perf["audience"]})
        

    volume_credits = total_volume_credits(invoice["performances"], plays)


    strings_perf_result = [f' {perf["name"]}: {perf["amount"]} ({perf["seats"]} seats)\n' for perf in perf_results]
    result = f'Statement for {invoice["customer"]}\n'
    result += "".join(strings_perf_result)
    result += f'Amount owed is {format_as_dollars(total_amount/100)}\n'
    result += f'You earned {volume_credits} credits\n'
    return result


def amount_for(performance, play):
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


def total_volume_credits(performances, plays):
    volume_credits = 0
    for performance in performances: 
        play = plays[performance['playID']]
        volume_credits += calculate_volume_credits_for(performance, play)
        
    return volume_credits


def calculate_volume_credits_for(performance, play):
    performance_volume_credits = 0
    performance_volume_credits += max(performance['audience'] - 30, 0)
    if "comedy" == play["type"]:
        performance_volume_credits += math.floor(performance['audience'] / 5)

    return performance_volume_credits



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

