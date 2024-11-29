# BEGIN: 9ycx4r9j4bf
def calculate_discounted_price(original_price, discount_rate):
    discounted_price = original_price * discount_rate / 10
    rounded_price = round(discounted_price / 10) * 10
    return rounded_price

original_price, discount_rate = map(float, input().split())
original_price = int(original_price)

discounted_price = calculate_discounted_price(original_price, discount_rate)
print(int(discounted_price))
# END: 9ycx4r9j4bf
