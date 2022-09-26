# name = input("Enter name: ")
file_obj = open("User.txt", "w")
file_obj.writelines("Name : "+ input("Enter name: ") + " ")
file_obj.close()