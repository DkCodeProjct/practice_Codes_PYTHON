while True:
    def fizzBuzz(num):
        
        if num % 3 == 0 and num % 5 == 0:
            print(f"<fizzBuzz>")
        
        elif num % 3 == 0:
            print("fizz")
        
        elif num % 5 == 0:
            print("Buzz")
        
        else:
            print(num)
    
    User_num = int(input("enter_num* " ))
    fizzBuzz(User_num)

    another_round = input("D0_An0ther_R0und:_type(y/n) ")
    if another_round == "n":
        break
print("<thank you for participating>")
    
        