def div(x, y):
    return x / y

def mul(x, y):
    return x * y

def pow(x, y):
    return x ** y

def rem(x, y):
    return x % y

while True:
    print("1. div => Division /")
    print("2. mul => Multiplication *")
    print("3. pow => Power **")
    print("4. rem => Remainder %")

    user = input("CH00SE: (1/ 2/ 3/ 4)")
    if user not in ("(1/2/3/4)"):
        print("invalid")
        continue
    
    try:
        num_x = int(input("x "))
        num_y = int(input("y "))
    
    except ValueError:
        pass
    
    else:
        if user == "1":
            result = div(num_x, num_y)
            print(f"x / y == {result}")
        
        elif user == "2":
            result = mul(num_x, num_y)
            print(f"x * y == {result}")
        
        elif user == "3":
            result = pow(num_x, num_y)
            print(f"x ** y == {result}")
        
        elif user == "4":
            result = rem(num_x, num_y)
            print(f"x % y == {result}")
        
        
    
    do_n = input("D0_An0ther_cal:_type(n/y) ").lower()
    if do_n == "n":
        break
print("thanks")


