weather_data = {}

def add_weather_data():
    city = input("Please enter the city name: ")
    date = input("Please enter the date (YYYY-MM-DD): ")
    temp = input("Please enter the temperature (in Celsius): ")
    humidity = input("Please enter the humidity (in percentage): ")
    weather_cond = input("Please enter the weather condition: ")
    
    if city not in weather_data:
        weather_data[city] = {}
    
    weather_data[city][date] = {
        "temperature": temp,
        "humidity": humidity,
        "weather_condition": weather_cond
    }
    
    print(f"Weather data for {city} on {date} has been added successfully.")

def query_by_city():
    city = input("Please enter the city name: ")
    
    if city not in weather_data:
        print(f"No weather data found for {city}.")
    else:
        print(f"Weather data for {city}:")
        for date, data in weather_data[city].items():
            print(f"Date: {date}, Temperature: {data['temperature']}, Humidity: {data['humidity']}, Weather Condition: {data['weather_condition']}")
    
while True:
    print("Please select an option:")
    print("1. Add weather data")
    print("2. Query by city")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        add_weather_data()
    elif choice == "2":
        query_by_city()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")