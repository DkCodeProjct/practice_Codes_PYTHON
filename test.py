"""
user_input = input("type_here* ")
output = user_input.replace(" ", "..")
print(f"slow_down! {output}")
"""

def convert(name):
    if name % 2 == 0 and name * 2 > 20:
        print("evenOdd")
    elif name % 2 == 0:
        print("odd")
    elif name * 2 > 20:
        print("even")
get_num = int(input("enter here "))
change = convert(get_num)
print(f"convert {change}")