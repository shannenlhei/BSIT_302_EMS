class Employee:
 def __init__(self,name,department,job,rate):
        self.name = name
        self.department = department
        self.job = job
        self.rate = rate
     
    
start = True

employees = []



while start:
    print("""
        ****************************
        [1] Add new Employee
        [2] Enter hourly of Employee
        [3] Show Employees' data
        [4] Exit
        ****************************
        """)

    choice = input("Enter your choice: ")
 
    if choice == "1":
        Name = (input("Enter name of new Employee: "+"\n"))
        Department = (input("Enter Department of Employee: "+"\n"))
        Job = (input("Enter Job of Employee: "+"\n"))
        rate = int (input("Enter rate of Employee: " + "\n"))

        employees.append(Employee(Name,Department,Job,rate))
        print("Done!")

    elif choice == "2":
          index = int (input("Index no. of Employee: "))
          print(employees[index].name,"is selected!")
          hourly = int (input("Hourly of Employee: "))
          print("Employee's Salary: " , employees[index].rate * hourly)

    elif choice == "3":
        for e in employees:
          print("*********************************")
          print(employees.index(e),"\n","Name:", e.name,"\n","Department:", e.department,"\n","Job:", e.job,"\n","Rate:", e.rate,"\n")
    

    elif choice == "4":
    
          start = False
          print("You've exited")

    else:
         print("Invalid number, please try again")
          
          
          
            
