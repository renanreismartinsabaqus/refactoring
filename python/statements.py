import math


def format_as_dollars(amount): # Maybe move this outside
    return f"${amount:0,.2f}"


def statement(invoice, plays):

    data = statement_data(invoice, plays)
    
    return generate_text_report(data)


def statement_data(invoice, plays):
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
    return statement_data



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

def generate_text_report(data: dict):
    strings_perf_result = [f' {perf["play_name"]}: {format_as_dollars(perf["amount"]/100)} ({perf["audience"]} seats)\n' for perf in data["performances"]]
    result = f'Statement for {data["customer"]}\n'
    result += "".join(strings_perf_result)
    result += f'Amount owed is {format_as_dollars(data["total_amount"]/100)}\n'
    result += f'You earned {data["total_credits"]} credits\n'
    
    return result
