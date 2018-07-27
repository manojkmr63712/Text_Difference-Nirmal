import difflib

employeeNames = ['Colton','Coltron','Colty','Jayne','Barb','Carlene','Dick','Despina']
employeeNames.sort()
userEmpName = raw_input("Please enter the employee name you're searching for. We'll return the best match on record.")
global Answer
while True:
    pickedName = difflib.get_close_matches(userEmpName, employeeNames, 1)

    print(pickedName)
    print employeeNames

    if len(pickedName)==0:
        break

    userNameOK = raw_input("Is this the name of the person you're looking for?\n\n Type 'Y' or 'N'.\n\n")

    if (userNameOK=='n' or userNameOK=='N'):
        employeeNames.remove(pickedName[0])

    else:
        Answer=pickedName[0]
        break

print Answer+" is the right choice"
