# BEGIN: 9ycx9j04wxr4
def calculate_average(scores):
    total = sum(scores)
    return total / len(scores)

def main():
    scores = [9.6, 9.4, 9.8]
    average = calculate_average(scores)
    print("%5.2f" % average)

if __name__ == "__main__":
    main()
# END: 9ycx9j04wxr4
