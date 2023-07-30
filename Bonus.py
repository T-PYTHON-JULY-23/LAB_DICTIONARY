import re
print("fill the dictionary")
city_name= input("Fill in the  name of city : ")
for char in city_name:
    if char.isalpha() == True:
        continue
    else:
        print("this is invalid city name, try again ")
        quit()
        
date= input("Fill in the date in the following format(day-month-year) : ")
"""pattern_date = r'%d-%m-%Y'
if re.match(pattern_date, date)!= True:
    print("this is invalid date format, try again ")
    quit()"""

temperature= input("Fill in the temperature  : ")
if temperature.isdigit()!= True:
     print("this is invalid temperature value, try again ")
     quit()

humidity= input("Fill in the  humidity  True or False: ")
if humidity =="True" or humidity =="False":
    pass

else:
    print("this is invalid humidity value , try again ")
    quit()

weather_condition= input("Fill in the  weather condition : ")
for char in weather_condition:
    if char.isalpha() == True:
        continue
    else:
        print("this is invalid weather condition, try again ")
        quit()
        

nested_dict = { city_name: {date: {temperature: {humidity:weather_condition}}},
               
               }

user_ch = input("Enter the name of city you want data weather: ")
user_d = nested_dict.get(user_ch,"Sorry, the name of city not found ")
print(f"The data weather for  {user_ch} is: {user_d}")