#Question 1

def parallel(resistors):
    total = sum(1/r for r in resistors)
    result = round(1/total,3)
    print(f"{result} ohms")

parallel([330, 1000, 2200])