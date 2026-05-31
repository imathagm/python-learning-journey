b = float (input("ENTER BASIC SALARY AMOUNT:"))
d = int(input("ENTER NUM OF DAYS:"))
t = int(input("ENTER EXTRA HOURS:"))

tot=b+(d*(b*0.05))+t*250
tax=tot*0.12

salary=tot-tax

print("salary is", salary)  