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

#Question 3

def temperature_check(temp, unit):
    if unit == "C":
        if temp < 35:
            print("The patient is hypothermic")
        elif temp > 37.5:
            print("The patient is hyperthermic")
        else:
            print("The patient's temperature is normal")
    elif unit == "F":
        if temp < 95:
            print("The patient is hypothermic")
        elif temp > 99.5:
            print("The patient is hyperthermic")
        else:
            print("The patient's temperature is normal")
    else:
        print("Invalid unit. Use 'C' or 'F'.")

temperature_check(14, "C")
temperature_check(37, "C")
temperature_check(37, "F")