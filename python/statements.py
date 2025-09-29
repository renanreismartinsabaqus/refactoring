import math


def format_as_dollars(amount):
    return f"${amount:0,.2f}"


def statement(invoice, plays):
    data = statement_data(invoice, plays)
    return generate_text_report(data)


def statement_data(invoice, plays):
    statement_data = {
        "customer": invoice["customer"],
        "performances":[],
        "total_amount": 0,
        "total_credits": 0,
    }

    for performance in invoice["performances"]:
        play = plays[performance['playID']]
        statement_data["performances"].append(
            {
                **performance,
                "play_name": play["name"],
                "play_type": play["type"],
                
            }
        )

    for performance in statement_data["performances"]:
        performance["amount"] = amount_for(performance)

    statement_data["total_amount"] = sum([p["amount"] for p in statement_data["performances"]])
    
    statement_data["total_credits"] = total_volume_credits(statement_data["performances"])
    
    
    return statement_data

def generate_html_report(invoice: dict, plays: dict):
    # Generates a pretty html report
    pass

def generate_text_report(data: dict):
    strings_perf_result = [f' {perf["play_name"]}: {format_as_dollars(perf["amount"]/100)} ({perf["audience"]} seats)\n' for perf in data["performances"]]
    result = f'Statement for {data["customer"]}\n'
    result += "".join(strings_perf_result)
    result += f'Amount owed is {format_as_dollars(data["total_amount"]/100)}\n'
    result += f'You earned {data["total_credits"]} credits\n'
    
    return result



def tragedy_amount_calculator(performance):
    performance_amount = 40000
    if performance['audience'] > 30:
        performance_amount += 1000 * (performance['audience'] - 30)

    return performance_amount


def comedy_amount_calculator(performance):
    performance_amount = 30000
    if performance['audience'] > 20:
        performance_amount += 10000 + 500 * (performance['audience'] - 20)
    performance_amount += 300 * performance['audience']

    return performance_amount


def comedy_credits_calculator(performance):
    performance_volume_credits = max(performance['audience'] - 30, 0)
    performance_volume_credits += math.floor(performance['audience'] / 5)
    
    return performance_volume_credits


def tragedy_credits_calculator(performance):
    performance_volume_credits = max(performance['audience'] - 30, 0)
    
    return performance_volume_credits
    


PLAY_TYPE_CALCULATORS = {
    "comedy": {
        "amount":comedy_amount_calculator,
        "credits":comedy_credits_calculator,
    },
    "tragedy": { 
        "amount": tragedy_amount_calculator,
        "credits": tragedy_credits_calculator,
    },
}




def total_volume_credits(performances):
    volume_credits = 0
    for performance in performances: 
        play_type = performance["play_type"]
        volume_credits += PLAY_TYPE_CALCULATORS[play_type]["credits"](performance)
        
    return volume_credits


def amount_for(performance):
    play_type = performance["play_type"]
    if play_type in PLAY_TYPE_CALCULATORS:
        return PLAY_TYPE_CALCULATORS[play_type]["amount"](performance)
    else:
        raise ValueError(f'unknown type: {performance["play_type"]}')
