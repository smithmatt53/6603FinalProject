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


def ReadUpdatedFile():
    with open('updatedValues.csv') as file_obj: 
    # Create reader object by passing the file 
    # object to DictReader method 
        article_read = csv.DictReader(file_obj) 

        Male1 = []
        Female1 = []
        Male2 = []
        Female2 = []
        Male3 = []
        Female3 = []

        pay1Over40 = []
        pay2Over40 = []
        pay3Over40 = []

        pay1Under40 = []
        pay2Under40 = []
        pay3Under40 = []
        


        male1Over40 = []
        male1Under40 = []
        female1Over40 = []
        female1Under40 = []

       
        male2Over40 = []
        male2Under40 = []
        female2Over40 = []
        female2Under40 = []

        male3Over40 = []
        male3Under40 = []
        female3Over40 = []
        female3Under40 = []
        #Age = 0 under 40
        #Age = 1 Over 40

        for x in article_read:
            if(x['PaymentTier'] == '1'):
                if x['Gender'] == '1':
                    Male1.append(x)
                elif x['Gender'] == '0':
                    Female1.append(x)
                
                if x['Age'] == '1':
                    pay1Over40.append(x)
                elif x['Age'] == '0':
                    pay1Under40.append(x)
                
            elif(x['PaymentTier'] == '2'):
                if x['Gender'] == '1':
                    Male2.append(x)
                elif x['Gender'] == '0':
                    Female2.append(x)
                if x['Age'] == '1':
                    pay2Over40.append(x)
                elif x['Age'] == '0':
                    pay2Under40.append(x)

            elif(x['PaymentTier'] == '3'):
                if x['Gender'] == '1':
                    Male3.append(x)
                elif x['Gender'] == '0':
                    Female3.append(x)
                if x['Age'] == '1':
                    pay3Over40.append(x)
                elif x['Age'] == '0':
                    pay3Under40.append(x)
        

        #Male1 = []
        #Female1 = []
        #Male2 = []
        #Female2 = []
        #Male3 = []
        #Female3 = []

        male1Over40 = []
        male1Under40 = []
        female1Over40 = []
        female1Under40 = []

       
        male2Over40 = []
        male2Under40 = []
        female2Over40 = []
        female2Under40 = []

        male3Over40 = []
        male3Under40 = []
        female3Over40 = []
        female3Under40 = []
        
        for x in Male1:
            if x['Age'] == '1':
                male1Over40.append(x)
            elif x['Age'] == '0':
                male1Under40.append(x)

        for x in Female1:
            if x['Age'] == '1':
                female1Over40.append(x)
            elif x['Age'] == '0':
                female1Under40.append(x)
        
        for x in Male2:
            if x['Age'] == '1':
                male2Over40.append(x)
            elif x['Age'] == '0':
                male2Under40.append(x)

        for x in Female2:
            if x['Age'] == '1':
                female2Over40.append(x)
            elif x['Age'] == '0':
                female2Under40.append(x)

        for x in Male3:
            if x['Age'] == '1':
                male3Over40.append(x)
            elif x['Age'] == '0':
                male3Under40.append(x)

        for x in Female3:
            if x['Age'] == '1':
                female3Over40.append(x)
            elif x['Age'] == '0':
                female3Under40.append(x)
        

    return(Male1,
        Female1,
        Male2 ,
        Female2,
        Male3,
        Female3,

        pay1Over40,
        pay2Over40,
        pay3Over40,

        pay1Under40,
        pay2Under40,
        pay3Under40,
        
        male1Over40,
        male1Under40,
        female1Over40,
        female1Under40,

        male2Over40,
        male2Under40,
        female2Over40,
        female2Under40,

        male3Over40,
        male3Under40,
        female3Over40,
        female3Under40)




#updatedValues = ReadFile()
#WriteFile('updatedValues',updatedValues)

vals = ReadUpdatedFile()


print('male 1:', len(vals[0]))
print('female 1:', len(vals[1]))
print('male 2:' , len(vals[2]))
print('female 2:' , len(vals[3]))
print('male 3:' , len(vals[4]))
print('female 3:' , len(vals[5]))

print('pay 1 over 40:',  len(vals[6]))
print('pay 2 over 40:' , len(vals[7]))
print('pay 3 over 40:' , len(vals[8]))

print('pay 1 under 40:',  len(vals[9]))
print('pay 2 under 40:' , len(vals[10]))
print('pay 3 under 40:' , len(vals[11]))

print('male 1:', len(vals[12]))
print('female 1:', len(vals[13]))
print('male 2:' , len(vals[14]))
print('female 2:' , len(vals[15]))
print('male 3:' , len(vals[16]))
print('female 3:' , len(vals[17]))

print('pay 1 over 40:',  len(vals[18]))
print('pay 2 over 40:' , len(vals[19]))
print('pay 3 over 40:' , len(vals[20]))

print('pay 1 under 40:',  len(vals[21]))
print('pay 2 under 40:' , len(vals[22]))
print('pay 3 under 40:' , len(vals[23]))


