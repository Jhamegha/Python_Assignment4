#Method-1

filename = input("Enter the file name: ")
try:
    with open(filename, 'r') as file:
        for line in file:
            print(line, end='')
except FileNotFoundError:
    print("Error: The file ",filename,"was not found.")



#Method-2

''' filename=input("Enter a file name that you want to read: ")
if filename=="Sample.txt":
    file=open(filename,'r')
    for word in file:
        print(word,end="")
else:
    print(f"Error: The file '{filename}' was not found.") '''





