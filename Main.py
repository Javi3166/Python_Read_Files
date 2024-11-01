"""
Everytime a read function is used, it "eats up"/uses up what was read. Will need to re-open the document to the variable
again to have access to everything again.
"""

employee_file = open("Employees.txt", "r")

print(".Readable()")
print(employee_file.readable()) #Returns True or False on whether the file can be read. That's it.

print("\n.Read()")
print(employee_file.read()) #Shows the info in the file.

employee_file = open("Employees.txt", "r")
print("\n.Readline()")
print(employee_file.readline()) #Only shows one line at a time.

employee_file = open("Employees.txt", "r")
print("\n.Readlines()")
print(employee_file.readlines()) #Prints them as an ArrayList
employee_file = open("Employees.txt", "r")
print("\n.Readlines()[1]")
print(employee_file.readlines()[1])

print("\nFor loop with .Readlines()[1]")
employee_file = open("Employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)

employee_file.close()