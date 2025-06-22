from functions.get_files_info import get_files_info, get_file_content, write_file

# print(f"{get_files_info("calculator", ".")}")
# print(f"{get_files_info("calculator", "pkg")}")
# print(f"{get_files_info("calculator", "/bin")}")
# 

#print(f"{get_file_content("calculator", "lorem.txt")}")
# print(f"{get_file_content("calculator", "main.py")}")
# print(f"{get_file_content("calculator", "pkg/calculator.py")}")
# print(f"{get_file_content("calculator", "/bin/cat")}")

print(f"{write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")}")
print(f"{write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")}")
print(f"{write_file("calculator", "/tmp/temp.txt", "this should not be allowed")}")