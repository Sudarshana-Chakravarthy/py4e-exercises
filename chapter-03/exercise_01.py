hours = int (input ("Enter Hours: "))
rate = int(input("Enter Rate: "))

if hours>40:
    pay = 40 * rate + ((hours - 40) * 1.5 * rate)
    print(f"Pay : {pay}")
else:
    pay= hours * rate
    print(f"Pay: {pay}")
