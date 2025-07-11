try:
    score = float(input("Enter score: "))
except:
    print(f"Bad score")
    quit()

def computegrade(score):
    if score < 0.6:
        return "F"
    elif score >= 0.6 and score < 0.7:
        return "D"
    elif score >= 0.7 and score < 0.8:
        return "C"
    elif score >= 0.8 and score < 0.9:
        return "B"
    elif score >= 0.9 and score < 1.0:
        return "A"
    else:
        return "Bad Score"
        

print(f"{computegrade(score)}")
