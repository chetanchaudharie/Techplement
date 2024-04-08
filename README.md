# Techplement
# Weather Checking Application

This Python script allows you to check the weather for a specific city using the WeatherAPI. It retrieves current weather data including temperature, humidity, and wind speed in metric units.

## Usage

- **Real-time Weather Data:** Utilizes a weather API to fetch real-time weather information for specified cities.
- **CRUD Operations:** Allows users to manage their list of favorite cities, including adding and removing cities.
- **Auto-refresh:** Automatically updates weather information at regular intervals to ensure users receive the latest data.
- **Command-line Interface:** Simple command-line interface for ease of use.

### Prerequisites

- Python 3.x
- Requests library (`pip install requests`)

### Getting Started

1. Clone or download this repository.

2. Install the required dependencies:
   ```sh
   pip install requests

1. Obtain an API key from WeatherAPI and replace "YOUR_API_KEY" in the script with your actual API key.

2. Run the script by executing the following command in your terminal:

   ```sh
   python weather_checker.py <city>

3. Replace <city> with the name of the city you want to check the weather for.

    ```sh
    python weatherapp.py London

4. To add <city> in favourite list.
     ```sh
    python weatherapp.py add <city>

5. To remove <city> from favourite list.
     ```sh
    python weatherapp.py remove <city>

6. To retrieve fresh data or refresh data for specific city.
     ```sh
    python weatherapp.py refresh <city>
