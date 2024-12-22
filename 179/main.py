# BEGIN: 9ycx9r9944wx
def calculate_investment_return(rate, principal, years):
    return int(principal * (1 + rate / 100) ** years)

R, M, Y = map(int, input().split())
result = calculate_investment_return(R, M, Y)
print(result)
# END: 9ycx9r9944wx
