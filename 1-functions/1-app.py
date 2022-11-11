# def sum(num1, num2):
#     result = num1 + num2
#     return result


# n1 = float(input("Enter num1: "))
# n2 = float(input("Enter num2: "))
# print(sum(n1, n2))


# lambda function >> annonimous function

sum_lambda = lambda n1, n2: n1+n2
print(f"The result is: {sum_lambda(2,3)}")

n1=3
n2=5
math_lambda_tuple = lambda n1, n2: (n1+n2, n1-n2)
math_lambda_dict = lambda n1, n2: {"sum":n1 + n2, "diff":n1 - n2}
print(math_lambda_tuple(n1, n2))
print(math_lambda_dict(n1, n2))


print("###################################")

li = ["iman", "saman", "jack"]
li_upper = []
for i in li:
    li_upper.append(i.upper())
print(li_upper)


print("############### MAP ####################")
# map got two input: one function and one list

li = ["iman", "saman", "jack"]
li_upper1 = list(map(str.upper, li))
print(li_upper1)




# n1 = float(input("Enter num1: "))
# n2 = float(input("Enter num2: "))
# max_num = lambda n1, n2: max(n1, n2)
# print(max_num(n1, n2))



#######################
li=[3,3,23,54,6767,56]
li_up = list(map(lambda x: x>10, li))
print(li_up)

#######################

li=[3,3,23,54,6767,56]
li_up = list(filter(lambda x: x>10, li))
print(li_up)




li_name = ['ali', 'iman', 'JACK', 'JOK']
li_up = list(filter(lambda name: name.isupper(), li_name))
li_lower = list(filter(lambda name: name.islower(), li_name))
print(li_up)
print(li_lower)


##########################

name = "ali"
li_name = list(name)
print(li_name)
li_name.reverse()
print(li_name)
print(''.join(li_name))


name = "iman"
print(name[::-1])



##############################
list1 = ["aba", "bnb","ADA", "sdf", 'asf']
filterd = list(filter(lambda x: x[::-1] == x, list1))
print(filterd)