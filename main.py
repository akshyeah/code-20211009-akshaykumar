   
#defined a different module for opening of json files
from jsonfile import *

global sum
sum=0

#to calculate BMI using hight and weight
def bmi_calculator(hightcm, weightkg):
    hightm = hightcm/100
    bmi = weightkg/hightm**2    #BMI cal formula BMI(kg/m ) = mass(kg) / height(m) squared
    return bmi

#dictionary for categories, BMI_Category and Health Risk
bmi_category =  {1:["Underweight","MalnutritionRisk"],
                 2:["NormalWeight","LowRisk"],
                 3:["OverWeight","EnhancedRisk"],
                 4:["ModeratelyObese","MediumRisk"],
                 5:["SeverelyObese","HighRisk"],
                 6:["VerySeverelyObese","VeryHighRisk"] }

#Function for range and return a value respectively, which will be used in final result function 
def bmi_range(bmi_val):
    if bmi_val <= 18.4:
        return 1
    elif bmi_val >=18.5 and bmi_val <= 24.9:
        return 2
    elif bmi_val >=25 and bmi_val <= 29.9:
        return 3
    elif bmi_val >=30 and bmi_val <= 34.9:
        return 4
    elif bmi_val >=35 and bmi_val <= 39.9:
        return 5
    else:
        return 6

#Returned value from bmi_range will be passed here to return bmi_category dict values
def result(count):
    return bmi_category[count]


jsonInput = read("data.json")

#adding bmi bmi_category, healthRisk as 3 new coloums to the file object
for i in jsonInput:
    i["BMI"]=bmi_calculator(i["HeightCm"], i["WeightKg"])
    i["BMI_Category"]=result(bmi_range(i["BMI"]))[0]
    if i["BMI_Category"]=="OverWeight":
        sum=sum+1
    i["HealthRisk"]=result(bmi_range(i["BMI"]))[1]

#writing into the dataUpdated.json file
try: 
    write("dataUpdated.json",jsonInput)
    print("File Updated, Please check \'dataUpdated.json\'.")

except:
    print("File updation failed. Please Check for errors")

print("Count of \"OverWeight\" people: ",sum)