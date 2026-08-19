from linux.files import (
    get_file_info,
    search_files,
    find_large_files,
    get_directory_info
)


home_directory = "/home/shrivardhan_patil"


print("Directory Information:")
print(get_directory_info(home_directory))


print("\nFile Information:")
print(get_file_info("linux/files.py"))


print("\nSearching for Python files:")
python_files = search_files(home_directory, "*.py")

for file in python_files[:10]:
    print(file)


print("\nLarge Files:")
large_files = find_large_files(home_directory, 100)

for file in large_files[:10]:
    print(file)
