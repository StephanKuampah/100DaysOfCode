with open("file1.txt") as files1:
    file1 = files1.readlines()
new_file1 = [int(n.strip('\n')) for n in file1]




with open("file2.txt") as files2:
    file2 = files2.readlines()
new_file2 = [int(n.strip('\n')) for n in file2]


result = [n for n in new_file1 if n in new_file1 and n in new_file2]
# # # # Write your code above 👆

print(result)


