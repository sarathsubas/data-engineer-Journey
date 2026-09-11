import json

employee = {
    "name" : "sarath",
    "age"  : 27,
    "skill" : ('plsql','python'),
    "exp" : True,
    "issues" : None 
}

j_emp = json.dumps(employee)

with open("datasets\\employee.json","w") as file:
    file.write(j_emp)

with open("datasets\\employee.json","r") as file1:
    json_data=file1.read()
    diction_data = json.loads(json_data)
    print(diction_data["name"])
    print(diction_data["age"])
    print(diction_data["skill"])
    print(diction_data["exp"])