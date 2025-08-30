# f = open("demo.txt", "r")
# data = f.read()
# print(data)
# # print(type(data))
# f.close()
# f = open("demo.txt", "rt")
# line1 = f.readline()
# print(line1)

# f.close()
# f = open("damo.txt", "w")
# f.write("hello world.")
# f.close()
# f = open("demo.txt", "r")
# data = f.read()
# print(data)
# f.close()
# f = open("demo.txt", "a")
# f.write("\n i am learning python from apnacollage.")
# f = open("sample.txt", "w")
# f.close()
# f = open("demo.txt", "r+")
# f.write("abc")
# f.close()
# 
# with open("demo.txt", "w") as f:
#     f.write("hello world.")
#     f.write("\n i am learning python from apnacollage")
# import os

# os.remove("damo.txt")
# with open("practice.txt", "w") as f:
#     f.write("hello world.")
#     f.write("\n i am learning python from apnacollage\n")
#     f.write("using Java.\ni like programming in Java.")
# with open("practice.txt", "r") as f:
#     data = f.read()
    
# new_data = data.replace("Java", "Python")
# print(new_data)
# with open("practice.txt", "w") as f:
#     f.write(new_data)

# def check_for_word():
#     word = "learning"
#     with open("practice.txt", "r") as f:
#         data = f.read()
#         if(data.find(word) != -1):
#             print("found")
#         else:
#             print("not found")
    
# check_for_word()
# def check_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if (word in data) :
#                 print(line_no)
#                 return
#             line_no += 1
    
#     return -1
# check_line()
