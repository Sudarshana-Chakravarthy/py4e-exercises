n = 0
total = 0
average = 0
while True:
    
    user_input = input("Enter a number: ")
    if  user_input == "done":
        print(f" {total} {n} {average}")
        break

    try:
        number = int(user_input)
    except:
        print(f"Invalid input")
        continue

    total += number
    n += 1
    average = total / n
    

