import os

dir = "./data"
if (os.path.exists(dir)) is not True:
    os.mkdir(dir)

with open("./data/ar1.txt", "w") as file:
    file.write("alo2")
