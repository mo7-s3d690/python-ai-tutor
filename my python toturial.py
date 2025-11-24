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