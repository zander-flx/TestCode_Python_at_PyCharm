path = "C://text_file/temp.txt"

file = open(path, "r")
content = file.read()
print(content)
file.close()
