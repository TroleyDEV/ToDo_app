file = open("members.txt", "r")
content = file.readlines()
file.close()

member = input("Enter name of a new member: ") + "\n"

file = open("members.txt", "w")

content.append(member)

file.writelines(content)
file.close()