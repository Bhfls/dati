# BEGIN: 9ycj0c9ukx4x
def format_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

input_seconds = int(input())
formatted_time = format_time(input_seconds)
print(formatted_time)
# END: 9ycj0c9ukx4x
