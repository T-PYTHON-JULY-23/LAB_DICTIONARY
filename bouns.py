"""# Bonus (use a new file)

### Exercise: Weather Data Aggregation

**Objective:** Write a Python program that aggregates weather data for different cities and provides weather data based on user queries.

#### Requirements:

1. **Input Weather Data:** Allow the user to input weather data for different cities. Each entry should include the city name, date, temperature, humidity, and weather condition (e.g., sunny, rainy).
2. **Store Data in a Dictionary:** Use a nested dictionary to store the weather data. The outer dictionary's keys will be the city names, and the values will be another dictionary containing date and weather details.
3. **Query by City:** Allow the user to query the weather data by city name, displaying all the recorded weather data for that city.

#### Guidelines:

- Use nested dictionaries to store the weather data efficiently.
- Implement separate functions for inputting data, querying by city.
- Validate user inputs to ensure correctness.

#### Challenge:

- Extend the program to allow the user to update or delete weather data for a specific city and date.


"""
weather_dict={}

def add_data():
    city=input("Enter city name or -1 to leave  : ").lower()
    if city =="-1" :
        return False 
    date=input("Enter the date : ") 
    if city not in weather_dict :
        weather_dict[city]={}
        
    temperature=input("Enter temprture :")
    humidity=input("Enter the humidity : ")
    weather_condition=input("Enter the weather condtion : ")
    
    weather_dict[city][date]={
            "tempt":temperature,
            "hum":humidity,
            "cond":weather_condition
        }
                        
    print("data insterted into weather status.")
    return True  


def search_city():
    city_to_search = input("Enter city name to search for weather deatil : ").lower()   
    city_data=weather_dict.get(city_to_search, "City not found")
    if city_data=='City not found':
        print(city_data)
        return
    date_data=input("Enter date  to search for weather deatil : ")  
    date_to_edit=city_data.get(date_data,'day data is not exit')
    if date_to_edit=="day data is not exit":
        print(date_to_edit)
        return
    print(f"Weather in {city_to_search} for day {date_data} is ")
    print(f"Teamprute : {date_to_edit['tempt']} c , Humidity : {date_to_edit['hum']}, Weather condtion : {date_to_edit['cond']}")    


    
def print_all_info():
    city_to_search = input("Enter city name to search for weather deatil : ").lower()   
    city_data=weather_dict.get(city_to_search, "City not found")
    if city_data=='City not found':
        print("\n",city_data,"\n")
        return
    for key,value in city_data.items():
        print(f'date : {key},temperature : {value["tempt"]} c, humidity : {value["hum"]} ,Weather condtion : {value["cond"]}')

def delete_one():
    city_to_search = input("Enter city name : ").lower()   
    city_data=weather_dict.get(city_to_search, "City not found")
    if city_data=='City not found':
        print("\n",city_data,"\n")
        return
    date_data=input("Enter date to delete data : ")  
    if date_data in weather_dict[city_to_search]:

        del weather_dict[city_to_search][date_data]
        print(f"\ndate {date_data} for {city_to_search} has been deleted\n")
    else:
        print("\nDate doesnt exist\n")

def delete_all_city():
    city_to_search = input("Enter city name : ").lower()   
    city_data=weather_dict.get(city_to_search, "City not found")
    if city_data=='City not found':
        print("\n",city_data,"\n")
        return
    else:
        del weather_dict[city_to_search]
        print(f"\nAll {city_to_search}'s date have been deleted\n")

functions={
    1:add_data,
    2:search_city,
    3:print_all_info,
    4:delete_one,
    5:delete_all_city,
    "Add/Update data for one city ":1,
    "Print one day data ":2,
    "Print all city's data":3,
    "Delete one day data ":4,
    "Delete all city's data" : 5,
}


city =None 
date=None 
temperature=None
humidity=None
weather_condition=None

print("Welcome to waether app ")
print('---------------------------')
while True:
    print('***********************************************')
    for key, value in functions.items():
        if isinstance(key,int):
            continue
        print(str(value),key)
    
    print('***********************************************\n')
    user_input=int(input("Choose the option ->: "))
    if user_input==-1:
        break
    functions.get(user_input,"Invlid input")()


