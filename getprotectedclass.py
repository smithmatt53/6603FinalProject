import csv
import random

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

def WriteTrainingAndTestingFile(name, values):
    with open(name+'.csv', 'w', newline='') as file:
            fields = ['Education',	'JoiningYear',	'City',	'PaymentTier',	'Age',	'Gender',	'EverBenched',	'ExperienceInCurrentDomain',	'LeaveOrNot', 'ID']
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


#Step 4 Divide Dataset
def ReadAndSplitDataSet(fileName):
    with open(fileName + '.csv') as file_obj: 
    # Create reader object by passing the file 
    # object to DictReader method 
        article_read = csv.DictReader(file_obj) 
        allRows = []
        for x in article_read:
            allRows.append(x)

        val = len(allRows)
        val = val/2
        val = int(val)
        train = random.sample(allRows, val)
        numbersOnly = []
        for x in train:
            numbersOnly.append(x['ID'])



        test = []
        for x in allRows:
            val = x['ID']
            if (val not in numbersOnly):
                test.append(x)

    return(train, test)

#Step 4 Method
def ReadTrainingTestingData(fileName):
    with open(fileName + '.csv') as file_obj: 
    # Create reader object by passing the file 
    # object to DictReader method 
        article_read = csv.DictReader(file_obj) 
        scores = []
        notTier23 = []
        for x in article_read:
            score = 100

            if(x['Education']=='PHD'):
                score = 110
                scores.append({'Score': score,'Education': x['Education'], 'JoiningYear': x['JoiningYear'], 'City': x['City'], 'PaymentTier': x['PaymentTier'], 'Age': x['Age'], 'Gender': x['Gender'], 'EverBenched': x['EverBenched'], 'ExperienceInCurrentDomain': x['ExperienceInCurrentDomain'], 'LeaveOrNot': x['LeaveOrNot'], 'ID': x['ID']})
            
            elif (int(x['ExperienceInCurrentDomain']) >= 5):
                score = 110
                scores.append({'Score': score,'Education': x['Education'], 'JoiningYear': x['JoiningYear'], 'City': x['City'], 'PaymentTier': x['PaymentTier'], 'Age': x['Age'], 'Gender': x['Gender'], 'EverBenched': x['EverBenched'], 'ExperienceInCurrentDomain': x['ExperienceInCurrentDomain'], 'LeaveOrNot': x['LeaveOrNot'], 'ID': x['ID']})
            else:
                if(int(x['JoiningYear']) >= 2017):
                    score = score - 30
                if(x['LeaveOrNot'] == '1'):
                    score = score - 45
            
                if(x['City'] == 'Bangalore'):
                    score = score - 10
                
                if(x['EverBenched'] == '1'):
                    score = score - 20
                scores.append({'Score': score,'Education': x['Education'], 'JoiningYear': x['JoiningYear'], 'City': x['City'], 'PaymentTier': x['PaymentTier'], 'Age': x['Age'], 'Gender': x['Gender'], 'EverBenched': x['EverBenched'], 'ExperienceInCurrentDomain': x['ExperienceInCurrentDomain'], 'LeaveOrNot': x['LeaveOrNot'], 'ID': x['ID']})
                
        return scores

def WriteTier3(name, values):
    with open(name+'.csv', 'w', newline='') as file:
            fields = ['Score','Education',	'JoiningYear',	'City',	'PaymentTier',	'Age',	'Gender',	'EverBenched',	'ExperienceInCurrentDomain',	'LeaveOrNot', 'ID']
            writer = csv.DictWriter(file, fieldnames = fields)
            writer.writeheader() 
            #for x in newValues:
            writer.writerows(values)
#updatedValues = ReadFile()
#WriteFile('updatedValues',updatedValues)

def FindTrainingResults(trainingResults):
    falsePositive = []
    falseNegative = []
    right = []

    for x in trainingResults:
        if x['PaymentTier'] == '3' and int(x['Score']) >= 45:
            right.append(x)
        elif x['PaymentTier'] == '3' and int(x['Score']) < 45:
            falseNegative.append(x)
        elif x['PaymentTier'] != '3' and int(x['Score']) < 45:
            right.append(x)
        elif x['PaymentTier'] != '3' and int(x['Score']) >= 45:
            falsePositive.append(x)

    print('accuracy', len(right))
    print('false positive', len(falsePositive))
    print('false negative', len(falseNegative))

def FindTestingResults(testingResults):
    falsePositiveTest = []
    falseNegativeTest = []
    rightTest = []
    for x in testingResults:
        if x['PaymentTier'] == '3' and int(x['Score']) >= 45:
            rightTest.append(x)
        elif x['PaymentTier'] == '3' and int(x['Score']) < 45:
            falseNegativeTest.append(x)
        elif x['PaymentTier'] != '3' and int(x['Score']) < 45:
            rightTest.append(x)
        elif x['PaymentTier'] != '3' and int(x['Score']) >= 45:
            falsePositiveTest.append(x)

    print('accuracy',len(rightTest))
    print('false positive',len(falsePositiveTest))
    print('false negative', len(falseNegativeTest))

    # get protected class percentage

    malefalsePositiveTest = []
    malefalseNegativeTest = []
    malerightTest = []


    femalefalsePositiveTest = []
    femalefalseNegativeTest = []
    femalerightTest = []
    femaletherTest = []

    falsePositiveTest40 = []
    falseNegativeTest40 = []
    rightTest40 = []
    femaletherTest40 = []

    falsePositiveTestnot40 = []
    falseNegativeTestnot40 = []
    rightTestnot40 = []
    femaletherTestnot40 = []

    maleScore45 = []
    femaleScore45 = []
    over40Score45 = []
    under40Score45 = []

    for x in testingResults:
        if x['Gender'] == '1':
            if int(x['Score']) >= 45:
                maleScore45.append(x)
            if x['PaymentTier'] == '3' and int(x['Score']) >= 45:
                malerightTest.append(x)
            elif x['PaymentTier'] == '3' and int(x['Score']) < 45:
                malefalseNegativeTest.append(x)
            elif x['PaymentTier'] != '3' and int(x['Score']) < 45:
                malerightTest.append(x)
            elif x['PaymentTier'] != '3' and int(x['Score']) >= 45:
                malefalsePositiveTest.append(x)
        
        elif x['Gender'] == '0':
            if int(x['Score']) >= 45:
                femaleScore45.append(x)
            if x['PaymentTier'] == '3' and int(x['Score']) >= 45:
                femalerightTest.append(x)
            elif x['PaymentTier'] == '3' and int(x['Score']) < 45:
                femalefalseNegativeTest.append(x)
            elif x['PaymentTier'] != '3' and int(x['Score']) < 45:
                femalerightTest.append(x)
            elif x['PaymentTier'] != '3' and int(x['Score']) >= 45:
                femalefalsePositiveTest.append(x)

        if x['Age'] == '1':
            if int(x['Score']) >= 45:
                over40Score45.append(x)
            if x['PaymentTier'] == '3' and int(x['Score']) >= 45:
                rightTest40.append(x)
            elif x['PaymentTier'] == '3' and int(x['Score']) < 45:
                falseNegativeTest40.append(x)
            elif x['PaymentTier'] != '3' and int(x['Score']) < 45:
                rightTest40.append(x)
            elif x['PaymentTier'] != '3' and int(x['Score']) >= 45:
                falsePositiveTest40.append(x)

        elif x['Age'] == '0':
            if int(x['Score']) >= 45:
                under40Score45.append(x)
            if x['PaymentTier'] == '3' and int(x['Score']) >= 45:
                rightTestnot40.append(x)
            elif x['PaymentTier'] == '3' and int(x['Score']) < 45:
                falseNegativeTestnot40.append(x)
            elif x['PaymentTier'] != '3' and int(x['Score']) < 45:
                rightTestnot40.append(x)
            elif x['PaymentTier'] != '3' and int(x['Score']) >= 45:
                falsePositiveTestnot40.append(x)

    print('male false positive:', len(malefalsePositiveTest))
    print('male false negative:', len(malefalseNegativeTest))
    print('male right:', len(malerightTest))

    print('female false positive:', len(femalefalsePositiveTest))
    print('female false negative:', len(femalefalseNegativeTest))
    print('female right:', len(femalerightTest))
    print(len(femaletherTest))

    print('40 false positive:', len(falsePositiveTest40))
    print('40 false negative:', len(falseNegativeTest40))
    print('40 right:', len(rightTest40))
    print(len(femaletherTest40))

    print('not 40 false positive:', len(falsePositiveTestnot40))
    print('not 40 false negative:', len(falseNegativeTestnot40))
    print('not 40 right:', len(rightTestnot40))
    print(len(femaletherTestnot40))

    print('male score 45',len(maleScore45))
    print('female score 45',len(femaleScore45))
    print('over 40 score 45',len(over40Score45))
    print('under 40 score 45',len(under40Score45))

def NewFindTrainingResults(trainingResults):
    falsePositive = []
    falseNegative = []
    right = []

    for x in trainingResults:
        if x['PaymentTier'] == '1' and int(x['Score']) >= 45:
            right.append(x)
        elif x['PaymentTier'] == '1' and int(x['Score']) < 45:
            falseNegative.append(x)
        elif x['PaymentTier'] == '0' and int(x['Score']) < 45:
            right.append(x)
        elif x['PaymentTier'] == '0' and int(x['Score']) >= 45:
            falsePositive.append(x)

    print('accuracy', len(right))
    print('false positive', len(falsePositive))
    print('false negative', len(falseNegative))

def NewFindTestingResults(testingResults):
    falsePositiveTest = []
    falseNegativeTest = []
    rightTest = []
    for x in testingResults:
        if x['PaymentTier'] == '1' and int(x['Score']) >= 45:
            rightTest.append(x)
        elif x['PaymentTier'] == '1' and int(x['Score']) < 45:
            falseNegativeTest.append(x)
        elif x['PaymentTier'] == '0' and int(x['Score']) < 45:
            rightTest.append(x)
        elif x['PaymentTier'] == '0' and int(x['Score']) >= 45:
            falsePositiveTest.append(x)

    print('accuracy',len(rightTest))
    print('false positive',len(falsePositiveTest))
    print('false negative', len(falseNegativeTest))

    # get protected class percentage

    malefalsePositiveTest = []
    malefalseNegativeTest = []
    malerightTest = []


    femalefalsePositiveTest = []
    femalefalseNegativeTest = []
    femalerightTest = []
    femaletherTest = []

    falsePositiveTest40 = []
    falseNegativeTest40 = []
    rightTest40 = []
    femaletherTest40 = []

    falsePositiveTestnot40 = []
    falseNegativeTestnot40 = []
    rightTestnot40 = []
    femaletherTestnot40 = []

    maleScore45 = []
    femaleScore45 = []
    over40Score45 = []
    under40Score45 = []

    for x in testingResults:
        if x['Gender'] == '1':
            if int(x['Score']) >= 45:
                maleScore45.append(x)
            if x['PaymentTier'] == '1' and int(x['Score']) >= 45:
                malerightTest.append(x)
            elif x['PaymentTier'] == '1' and int(x['Score']) < 45:
                malefalseNegativeTest.append(x)
            elif x['PaymentTier'] == '0' and int(x['Score']) < 45:
                malerightTest.append(x)
            elif x['PaymentTier'] == '0' and int(x['Score']) >= 45:
                malefalsePositiveTest.append(x)
        
        elif x['Gender'] == '0':
            if int(x['Score']) >= 45:
                femaleScore45.append(x)
            if x['PaymentTier'] == '1' and int(x['Score']) >= 45:
                femalerightTest.append(x)
            elif x['PaymentTier'] == '1' and int(x['Score']) < 45:
                femalefalseNegativeTest.append(x)
            elif x['PaymentTier'] == '0' and int(x['Score']) < 45:
                femalerightTest.append(x)
            elif x['PaymentTier'] == '0' and int(x['Score']) >= 45:
                femalefalsePositiveTest.append(x)

        if x['Age'] == '1':
            if int(x['Score']) >= 45:
                under40Score45.append(x)
            if x['PaymentTier'] == '1' and int(x['Score']) >= 45:
                rightTestnot40.append(x)
            elif x['PaymentTier'] == '1' and int(x['Score']) < 45:
                falseNegativeTestnot40.append(x)
            elif x['PaymentTier'] == '0' and int(x['Score']) < 45:
                rightTestnot40.append(x)
            elif x['PaymentTier'] == '0' and int(x['Score']) >= 45:
                falsePositiveTestnot40.append(x)
            

        elif x['Age'] == '0':
            if int(x['Score']) >= 45:
                over40Score45.append(x)
            if x['PaymentTier'] == '1' and int(x['Score']) >= 45:
                rightTest40.append(x)
            elif x['PaymentTier'] == '1' and int(x['Score']) < 45:
                falseNegativeTest40.append(x)
            elif x['PaymentTier'] == '0' and int(x['Score']) < 45:
                rightTest40.append(x)
            elif x['PaymentTier'] == '0' and int(x['Score']) >= 45:
                falsePositiveTest40.append(x)

    print('male false positive:', len(malefalsePositiveTest))
    print('male false negative:', len(malefalseNegativeTest))
    print('male right:', len(malerightTest))

    print('female false positive:', len(femalefalsePositiveTest))
    print('female false negative:', len(femalefalseNegativeTest))
    print('female right:', len(femalerightTest))
    print(len(femaletherTest))

    print('40 false positive:', len(falsePositiveTest40))
    print('40 false negative:', len(falseNegativeTest40))
    print('40 right:', len(rightTest40))
    print(len(femaletherTest40))

    print('not 40 false positive:', len(falsePositiveTestnot40))
    print('not 40 false negative:', len(falseNegativeTestnot40))
    print('not 40 right:', len(rightTestnot40))
    print(len(femaletherTestnot40))

    print('male score 45',len(maleScore45))
    print('female score 45',len(femaleScore45))
    print('over 40 score 45',len(over40Score45))
    print('under 40 score 45',len(under40Score45))


"""
# Step 2
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
"""


#step 4 - SPlit Original data sets
"""
train, test = ReadAndSplitDataSet('updatedValues')
WriteTrainingAndTestingFile('training', train)
WriteTrainingAndTestingFile('testing', test)
"""

#step 4 - Split threshold data sets
"""
train, test = ReadAndSplitDataSet('threshhold')
WriteTrainingAndTestingFile('thresholdTraining', train)
WriteTrainingAndTestingFile('thresholdTesting', test)
"""

"""
trainingResults = ReadTrainingTestingData('training')
WriteTier3('training23', trainingResults)
testingResults = ReadTrainingTestingData('testing')
WriteTier3('testing23', testingResults)

FindTrainingResults(trainingResults)

FindTestingResults(testingResults)
"""

thresholdTrainingResults = ReadTrainingTestingData('thresholdTraining')

thresholdTestingResults = ReadTrainingTestingData('thresholdTesting')

NewFindTrainingResults(thresholdTrainingResults)

NewFindTestingResults(thresholdTestingResults)

