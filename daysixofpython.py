# def calc_sum(a, b):
#     sum = a + b
#     print(sum)
#     return sum

# calc_sum(3, 5)

# calc_sum(10, 20)
# def calc_sum(a, b):
#     return a + b

# sum = calc_sum(3, 5)
# print(sum)
# def print_hello():
#     print("hello ")
# print_hello()
# print_hello()
# print_hello()

# output = print_hello()
# print(output)
# def calc_avg(a , b, c):
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)
#     return avg
# calc_avg(3, 5, 7)
# calc_avg(10, 20, 30)    
# print("gold",end="$")
# print("silver",end="$")
# print("bronze")
# def calc_prod(a=1 , b=1):
#     print(a * b)
#     return a * b

# calc_prod()
# cities = ["karachi", "lahore", "islamabad", "quetta", "peshawar"]
# heroes = ["superman", "batman", "spiderman", "ironman", "captain america","thor",]
# print(heroes[0],end="")
# print(heroes[1])

# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(heroes)
# def cal_fact(n):
#     fact= 1
#     for i in range(1,n+1):
#         fact*= i
#     print(fact)

# cal_fact(6)
# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n - 1)
#     print("ended")

# show(5)
# print("end")
# def fact(n):
#     if (n==1 or n==0):
#         return 1
#     return fact(n-1) * n
     
# print(fact(6))

# def fact(n):
#     if (n == 1 or n == 0):
#         return 1
#     return fact(n-1) * n
# print(fact(5))
def calc_sum(n):
    if(n==0):
        return 0
    print(n)
    return calc_sum(n-1) + n               

sum = calc_sum(5)
print(sum)