#Question 1

def parallel(resistors):
    total = sum(1/r for r in resistors)
    result = round(1/total,3)
    print(f"{result} ohms")

parallel([330, 1000, 2200])


#Question 2

def potential_divider(voltage, resistors):
    total_resistance = sum(resistors)
    for r in resistors:
        voltage_drop = round(voltage * (r / total_resistance), 2)
        print(f"{voltage_drop}v")

potential_divider(9, [3000, 1000])