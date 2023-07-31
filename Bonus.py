
def input_weather_data(weather_data):
    city = input("Enter city name: ")
    date = input("Enter date (YYYY-MM-DD): ")
    temperature = float(input("Enter temperature (in Celsius): "))
    humidity = int(input("Enter humidity (in percentage): "))
    weather_condition = input("Enter weather condition: ")

    if city not in weather_data:
        weather_data[city] = {}

    weather_data[city][date] = {
        "temperature": temperature,
        "humidity": humidity,
        "weather_condition": weather_condition,
    }
    print(f"Weather data for {city} on {date} recorded successfully.\n")


def query_by_city(weather_data):
    city = input("Enter city name to query: ")

    if city in weather_data:
        print(f"Weather data for {city}:")
        for date, data in weather_data[city].items():
            print(f"Date: {date}, Temperature: {data['temperature']}°C, Humidity: {data['humidity']}%, Weather Condition: {data['weather_condition']}")
    else:
        print("City not found in the weather data.")


def main():
    weather_data = {}

    while True:
        print("\nMenu:")
        print("1. Input Weather Data")
        print("2. Query by City")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            input_weather_data(weather_data)
        elif choice == "2":
            query_by_city(weather_data)
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()