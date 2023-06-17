import os

name_list = os.listdir(r"D:\python\Project\Pyhthons")
print(name_list)
for item in name_list:
    if item.endswith(".py"):
        print(item)