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

def ReadUpdatedFile():
    with open('updatedValues.csv') as file_obj: 
    # Create reader object by passing the file 
    # object to DictReader method 
        article_read = csv.DictReader(file_obj) 

        yesMale = []
        yesFemale = []
        maleYesOver40 = []
        maleYesUnder40 = []
        femaleYesOver40 = []
        femaleYesUnder40 = []

        noMale = []
        noFemale = []
        maleNoOver40 = []
        maleNoUnder40 = []
        femaleNoOver40 = []
        femaleNoUnder40 = []
        

        for x in article_read:
            if(x['EverBenched'] == 'Yes'):
                if x['Gender'] == '1':
                    yesMale.append(x)
                elif x['Gender'] == '0':
                    yesFemale.append(x)
                """
                if x['Age'] == '1':
                    yesOver40.append(x)
                elif x['Age'] == '0':
                    yesUnder40.append(x)
                """
            elif(x['EverBenched'] == 'No'):
                if x['Gender'] == '1':
                    noMale.append(x)
                elif x['Gender'] == '0':
                    noFemale.append(x)
                """
                if x['Age'] == '1':
                    noOver40.append(x)
                elif x['Age'] == '0':
                    noUnder40.append(x)
                """
        
        for x in yesMale:
            if x['Age'] == '1':
                maleYesOver40.append(x)
            elif x['Age'] == '0':
                maleYesUnder40.append(x)

        for x in noMale:
            if x['Age'] == '1':
                maleNoOver40.append(x)
            elif x['Age'] == '0':
                maleNoUnder40.append(x)
        
        for x in yesFemale:
            if x['Age'] == '1':
                femaleYesOver40.append(x)
            elif x['Age'] == '0':
                femaleYesUnder40.append(x)

        for x in noFemale:
            if x['Age'] == '1':
                femaleNoOver40.append(x)
            elif x['Age'] == '0':
                femaleNoUnder40.append(x)

    return(yesMale)



#updatedValues = ReadFile()
#WriteFile('updatedValues',updatedValues)

vals = ReadUpdatedFile()


