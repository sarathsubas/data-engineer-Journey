def validation_data(data_rec):
    x=0
    validation_result=[]
    for line in data_rec:
        if line[0] == "":
            x=1
        if int(line[4]) <=0:
            x=1
        if int(line[5]) <=0:
            x=1
        if line[6] == "":
            x=1
        validation_result.append(x)
        x=0
       
    return validation_result