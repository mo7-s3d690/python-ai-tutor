#task 1 
p1 =int(input("enter the first num"))
p2 = int(input("enter the second num"))
t_b = p1 + p2
cost = int(input("enter the cost"))
if cost > t_b:
    a = cost - t_b
    print(f"we still need {a} pounds")
else:
    a =t_b - cost

    print(f"we still have {a} pounds")
'''----------------------------------------------------------'''
# task 2 part 1
x = int (  input ( "enter ur temperature in celsius: " ) )

if x >= 30:
    print ( "its a hot day , stay hydrated" )
elif x >= 20 and x < 30:
    print ( "its a nice day , enjoy the weather" )
elif x >= 10 and x < 20:
    print ( "its a bit cold , wear a jacket" )
else:
    print ( "its cold , dont go outside" )

# task 2 part 2
x = list(range(1 , 21))

for i in x :
    if i % 3 == 0:
        print(f"{i} is divisible by 3")
'''----------------------------------------------------------'''
