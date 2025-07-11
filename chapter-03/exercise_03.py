try:
    score = float (input("Enter score: "))
except:
    print(f"Bad score")
    quit()
if score < 0.6 and score >= 0:
    print(f"F")
elif score >= 0.6 and score < 0.7:
    print(f"D")
elif score >= 0.7 and score < 0.8:
    print(f"C")
elif score >=0.8 and score < 0.9:
    print(f"B")
elif score >=0.9 and score <= 1.0:
    print(f"A")
else:
    print(f"Bad score")

