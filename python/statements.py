import math


def format_as_dollars(amount): # Maybe move this outside
    return f"${amount:0,.2f}"


def statement(invoice, plays):
    # Invoice iteration
    statement_data = {
        "customer": invoice["customer"],
        "performances":[],
        "total_amount": 0,
        "total_credits": total_volume_credits(invoice["performances"], plays),
    }

    for performance in invoice["performances"]:
        play = plays[performance['playID']]
        statement_data["performances"].append(
            {
                **performance,
                "play_name": play["name"],
                "play_type": play["type"],
                "amount":  amount_for(performance, play),
                
            }
        )
    
    statement_data["total_amount"] = sum([p["amount"] for p in statement_data["performances"]])
        
    strings_perf_result = [f' {perf["play_name"]}: {format_as_dollars(perf["amount"]/100)} ({perf["audience"]} seats)\n' for perf in statement_data["performances"]]
    result = f'Statement for {invoice["customer"]}\n'
    result += "".join(strings_perf_result)
    result += f'Amount owed is {format_as_dollars(statement_data["total_amount"]/100)}\n'
    result += f'You earned {statement_data["total_credits"]} credits\n'
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

