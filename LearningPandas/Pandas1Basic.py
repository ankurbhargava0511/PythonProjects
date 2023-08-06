import pandas as pd

data=pd.read_csv("weather_data.csv")
print (data)

print (type(data)) # dataframe

temp= data["temp"]

print (type(temp)) # series


print(data.head(2))#top row
print(data.tail(2))#bottom rows

# Data type of each column
print(data.dtypes)


# technical information of frame
print(data.info())

print(data.to_dict()) # creating dict series can be converted to list


print (temp.tolist())


#Average

print (sum(temp)/len(temp))

print(temp.mean())

print (temp.max())

#selecting a column

print (data["condition"])

print (data.condition)



#selecting rows

print(data[data.day=="Monday"])


print (data[data.temp==data.temp.max()])


#creating a dataframe from data



data_dict={
    "students": ["Amy", "James", "Angela"],
    "scores":[76,56,65]
}

student_data= pd.DataFrame(data_dict)

print (student_data)



data= pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

print (data.head(5))



#iterate over panda Df



student_dict ={
    "student": ["Angela", "James", "Lily"],
    "score": [56,76,98]
}

import pandas


df= pandas.DataFrame(student_dict)

#print( df)

#iterate through rows

for (index,row ) in df.iterrows():
    #print(row)
    print(row.student)
    print(row.score)

