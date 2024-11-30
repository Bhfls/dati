# BEGIN: 969j093kf09
def calculate_ticket_price(quantity):
    if quantity >= 30:
        return quantity * (50 - 2)
    else:
        return quantity * 50

try:
    num_tickets = int(input())
    total_cost = calculate_ticket_price(num_tickets)
    print(f"{total_cost} ")
except ValueError:
    print("输入无效，请输入一个正整数。")
# END: 969j093kf09
