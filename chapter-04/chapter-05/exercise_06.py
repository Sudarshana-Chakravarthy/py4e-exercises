hours = int (input("enter hours: "))
rate = float (input("Enter Rate: "))

def computepay(hours,rate):
    if hours>40:
        pay = rate * 40 + ((hours - 40) * 1.5 * rate)
        print(f"Pay: {pay}")
    else:
        pay = rate *hours
        print(f"Pay: {pay}")

computepay(hours,rate)
