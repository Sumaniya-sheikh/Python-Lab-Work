
# Average salary of each department

employee_file = open("Employee.txt", "r")

employees = employee_file.readlines()
employee_file.close()

salary = {}

for line in employees[1:]:
    data = line.strip().split(",")

    name = data[0]
    eid = data[1]
    sal = float(data[2])
    did = data[3]

    if did not in salary:
        salary[did] = []

    salary[did].append(sal)

for did in salary:
    average = sum(salary[did]) / len(salary[did])
    print(did, "Average Salary =", average)