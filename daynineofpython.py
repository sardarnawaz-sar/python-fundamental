# class student:
#     def __init__(self,name):
#         self.name = name

# s1 = student("karan")
# del s1
# print(s1.name)
# class account:
#     def __init__(self,acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass
#     def reset_pass(self):
#         print(self.__acc_pass)



# acc1 = account("12345","abcd")
# print(acc1.acc_no)
# # print(acc1.__acc_pass)
# print(acc1.reset_pass())

# class person:
#     __name = "karan"

#     def __hello(self):
#         print("welcome person")

#     def welcome(self):
#         self.__hello()

# p1 =person()
# print(p1.welcome())

# class car:
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stoped..")

# class toyotacar(car):
#     def __init__(self,brand):
#         self.name = brand

# car1 = toyotacar("fortuner")
# car2 = toyotacar("prius")

# print(car1.name)
# print(car1.start())

# class fortuner(toyotacar):
#     def __init__(self, type):
#         self.type = type
# car1 = fortuner("diesel")
# car1.start()

# class A:
#     varA = "welcome to class A"

# class B:
#     varB = "welcome to class B"

# class C(A,B):
#     varC = "welcome to class C"

# c1 = C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

# class car:
#     def __init__(self, type):
#         self.type = type
    
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stoped..")

# class toyotacar(car):
#     def __init__(self,name,type):
#         self.name = name
#         super().__init__(type)
#         super().start()

# car1 = toyotacar("prius","electric")
# print(car1.type)

# class person:
#     name = "anonymous"

#     @classmethod
#     def changename(cls, name):
#         cls.name = name 

    # def changename(self, name):
    #     self.name = name
        #self.__class__.name = "rahul"

# p1 = person()
# p1.changename("rahul")
# print(p1.name)
# print(person.name)

# class student:
#     def __init__(self, phy, che, math):
#         self.phy = phy
#         self.che = che
#         self.math = math


#     @property
#     def percentage(self):
#         return str((self.phy + self.che + self.math)/3) + "%"
    
# stu1 = student(97, 98, 99)
# print(stu1.percentage)

# stu1.phy = 100
# print(stu1.percentage)


# class complex:
#     def __init__(self, real , img):
#         self.real = real
#         self.img = img
#     def shownumber(self):
#         print(self.real,"i +", self.img,"j")

#     def __add__(self, num2):
#         newreal = self.real + num2.real
#         newimg = self.img + num2.img
#         return complex(newreal, newimg)

# num1 = complex(1, 3)
# num1.shownumber()

# num2 = complex(4, 6)
# num2.shownumber()

# num3 =num1 + num2
# num3.shownumber()


