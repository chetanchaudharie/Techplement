import argparse
import requests
import time

FAVORITES_FILE = "favorites.txt"
REFRESH_INTERVAL = 15  # in seconds


# Function to fetch weather information by city name
def get_weather(city):
    """
    Get weather data from weather API
    :param city: city name
    """
    try:
        # Use an API to fetch weather data for the city
        # Replace 'API_KEY' with your actual API key
        API_KEY = "f963305bdfd2479085d81036240404"
        url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&units=metric"
        response = requests.get(url)
        data = response.json()
        if 'error' in data:
            print("Error:", data['error']['message'])
        else:
            print(f"Weather in {city}:")
            print(f"Description: {data['current']['condition']['text']}")
            print(f"Temperature: {data['current']['temp_c']}°C")
            print(f"Humidity: {data['current']['humidity']}%")
            print(f"Wind Speed: {data['current']['wind_kph']} km/h")
    except Exception as e:
        print("An error occurred:", e)


# Function to add a city to the favorite list
def add_to_favorites(city):

    try:
        with open(FAVORITES_FILE, "a") as f:
            f.write(city + "\n")
        print(f"{city} added to favorites.")
    except IOError as e:
        print(f"Error: {e}")


# Function to remove a city from the favorite list
def remove_from_favorites(city):
    try:
        with open(FAVORITES_FILE, "r") as f:
            lines = f.readlines()
        with open(FAVORITES_FILE, "w") as f:
            for line in lines:
                if line.strip() != city:
                    f.write(line)
        print(f"{city} removed from favorites.")
    except IOError as e:
        print(f"Error: {e}")


# Function to auto-refresh weather information
def auto_refresh(city):
    """
    Automatically refresh
    :param city: city to refresh
    :return: None
    """
    while True:
        get_weather(city)
        time.sleep(REFRESH_INTERVAL)


# Main function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description="Weather Checking Application")

    # Subparsers for different commands
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Command to check weather
    weather_parser = subparsers.add_parser("weather", help="Check weather by city")
    weather_parser.add_argument("city", help="Name of the city")

    # Command to add a city to favorites
    add_parser = subparsers.add_parser("add", help="Add city to favorites")
    add_parser.add_argument("city", help="Name of the city")

    # Command to remove a city from favorites
    remove_parser = subparsers.add_parser("remove", help="Remove city from favorites")
    remove_parser.add_argument("city", help="Name of the city")

    # Command to auto-refresh weather
    refresh_parser = subparsers.add_parser("refresh", help="Auto-refresh weather information")
    refresh_parser.add_argument("city", help="Name of the city")

    args = parser.parse_args()

    if args.command == "weather":
        get_weather(args.city)
    elif args.command == "add":
        add_to_favorites(args.city)
    elif args.command == "remove":
        remove_from_favorites(args.city)
    elif args.command == "refresh":
        auto_refresh(args.city)
    else:
        print("Invalid command. Use -h or --help for usage information.")


if __name__ == "__main__":
    main()
