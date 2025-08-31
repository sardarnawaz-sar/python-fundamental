# a = 10
# b = 20

# sum = a + b
# print(sum)
# diff = b - a
# print(diff)
# class student :
#     name = "karan"

# s1 = student()
# print(s1.name)
# s2 = student()
# print(s2.name)
# class car :
#     colour = "blue"
#     brand = "BMW"
# car1 = car()
# print(car1.colour)
# print(car1.brand)
# class student :
#     name = "karan"
#     def __init__(self):
#         print(self)
#         print("adding new student in database")
# s1 = student()
# print(s1)

# class student :
    
#     def __init__(self, fullname):
#         self.name = fullname
#         print("adding new student in database")
# s1 = student("karan")
# print(s1.name)

# s2 = student("rahul")
# print(s2.name)
# class student :
    
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in database")
# s1 = student("karan", 90)
# print(s1.name, s1.marks)

# s2 = student("rahul", 98)
# print(s2.name, s2.marks)

# class student :
#     collage_name = "apnacollage"
    
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in database")
# s1 = student("karan", 90)
# print(s1.name, s1.marks)
# print(s1.collage_name)
# s2 = student("rahul", 98)
# print(s2.name, s2.marks)

# print(s2.collage_name)
# class student :
#     collage_name = "apnacollage"
    
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in database")
    
#     def welcome(self):
#         print("welcome student,", self.name)
#     def get_marks(self):
#         return self.marks
    
# s1 = student("karan",97)
# s1.welcome()
# print(s1.get_marks())

# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum += val
#         print("hi", self.name, "your avg score is:",sum/3)
# s1 = student("tony stark", [99, 98, 97])
# s1.get_avg()
# s1.name = "ironman"
# s1.get_avg()

# class student :
#     collage_name = "apnacollage"
    
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in database")
    
#     def welcome(self):
#         print("welcome student,", self.name)
#     def get_marks(self):
#         return self.marks
    
# s1 = student("karan",97)
# s1.welcome()
# print(s1.get_marks())

# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     @staticmethod
#     def hello():
#         print("hello")

#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum += val
#         print("hi", self.name, "your avg score is:",sum/3)
# s1 = student("tony stark", [99, 98, 97])
# s1.get_avg()
# s1.name = "ironman"
# s1.get_avg()

# class car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("car started")

# car1 = car()
# car1.start()

# class account:
#     def __init__(self, bal , acc):
#         self.balance = bal
#         self.account_no = acc

#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs",amount, "debited from your account")
#         print("total balance =", self.get_balance())

#     def credit(self, amount):
#         self.balance += amount
#         print("Rs",amount, "credited to your account")
#         print("total balance =", self.get_balance())

#     def get_balance(self):
#         return self.balance
    

# acc1 = account(10000, "12345")
# acc1.debit(1000)
acc1.credit(500)

        

