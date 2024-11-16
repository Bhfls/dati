# BEGIN: 5ycj4j9d0n8c
def calculate_new_grass_sufficiency(initial_grass, daily_growth, total_days):
    total_grass_consumed = 0
    for day in range(total_days):
        total_grass_consumed += initial_grass + daily_growth * day
    return total_grass_consumed / total_days

initial_grass = 15 * 20 - 20 * 10
daily_growth = (15 * 20 - 20 * 10) / (20 - 10)
sufficiency = calculate_new_grass_sufficiency(initial_grass, daily_growth, 1)

print(int(sufficiency))
# END: 5ycj4j9d0n8c
