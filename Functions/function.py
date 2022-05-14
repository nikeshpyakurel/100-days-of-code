def add(x,y):   #function decalration
    return x+y
def subtract(x,y):
    return x-y




user = input("Subtract or Add?") 
z = int(input("Enter your first number :"))
a = int(input("Enter your second number :"))
if user == 'subtract': 
    print(f"Subtraction between {z} and {a}", subtract(z,a))
elif user == 'add':
    print(f"Addition between {z} and {a}", add(z,a))
else:
    print("Your input is wrong")