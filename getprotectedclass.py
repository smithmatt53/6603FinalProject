import csv

def ReadFile():
    with open('Employee.csv') as file_obj: 
    # Create reader object by passing the file 
    # object to DictReader method 
        article_read = csv.DictReader(file_obj) 

        updatedValues = []
        

        for x in article_read:
            if(x['Gender'] == 'Male'):
                x['Gender'] = 1
            elif(x['Gender'] == 'Female'):
                x['Gender'] = 0
            if(int(x['Age']) >= 40):
                x['Age'] = 1
            elif(int(x['Age']) < 40):
                x['Age'] = 0
            updatedValues.append(x)

    return(updatedValues)

def WriteFile(name, values):
    with open(name+'.csv', 'w', newline='') as file:
            fields = ['Education',	'JoiningYear',	'City',	'PaymentTier',	'Age',	'Gender',	'EverBenched',	'ExperienceInCurrentDomain',	'LeaveOrNot']
            writer = csv.DictWriter(file, fieldnames = fields)
            writer.writeheader() 
            #for x in newValues:
            writer.writerows(values)



updatedValues = ReadFile()
WriteFile('updatedValues',updatedValues)
"""
malesOver40 = []
malesUnder40= []
femalesOver40 = []
femalesUnder40= []
males,females = ReadFile()

for x in males:
    if(int(x['Age']) >= 40):
        malesOver40.append(x)
    elif(int(x['Age']) < 40):
        malesUnder40.append(x)

for x in females:
    if(int(x['Age']) >= 40):
        femalesOver40.append(x)
    elif(int(x['Age']) < 40):
        femalesUnder40.append(x)
"""
