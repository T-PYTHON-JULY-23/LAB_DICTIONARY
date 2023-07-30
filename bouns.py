
weather_data= {}

size = int(input("how many cities you want to add?: "))
for i in range(size):
    city_name = input("Enter the name of the city: ")

    weather_data[city_name] = {}
    date= input("Enter the date: ")
 
    temperature= int(input("Enter the temperature: "))
    humidity = int(input("Enter the humidity level: "))
    weather_condition = str(input("Enter the weather_condition:"))

    weather_data[city_name]["date"] = date
    weather_data[city_name]["temperature"] = temperature
    weather_data[city_name]["humidity"] = humidity
    weather_data[city_name]["weather_condition"] = weather_condition

print(weather_data)

def Query_by_City():
 print("Search For City Weather")
 query= input("City:")
 if query in weather_data:
    print(weather_data[query])

Query_by_City()
