import os
i = input("shutdown? y/n: ")
if i == "y":
    os.system('shutdown -s')