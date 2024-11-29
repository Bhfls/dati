# BEGIN: 5ycx4j094f4
def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

def calculate_time_difference(start_time, end_time):
    start_seconds = time_to_seconds(start_time)
    end_seconds = time_to_seconds(end_time)
    return end_seconds - start_seconds

start_time = input()
end_time = input()

time_difference = calculate_time_difference(start_time, end_time)
print(time_difference)
# END: 5ycx4j094f4
