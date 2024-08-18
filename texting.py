def division(a, b):
     try:
          return a/b
     except:
          return "Sorry, It's not dividable!"
     
user_input = int(input("Please enter a nuber to be divided with 50: "))
print(f"{user_input}/50 = ", division(50,user_input))