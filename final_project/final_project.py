import json
import requests
import uuid
from datetime import datetime, time

class User:
    def __init__(self, user_id, username, email, city):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.city = city

class Scooter:
    def __init__(self, scooter_id, battery_percentage, range_km):
        self.scooter_id = scooter_id
        self.battery_percentage = battery_percentage
        self.range_km = range_km

class RentalSystem:
    def __init__(self):
        self.users = []
        self.load_users()
        self.scooters = []
        self.load_scooters()

    def register_user(self, username, email, city):
        user_id = str(uuid.uuid4())
        user = User(user_id, username, email, city)
        self.users.append(user)
        self.save_users()
        return user

    def get_user_by_id(self, user_id):
        return next((u for u in self.users if u.user_id == user_id), None)

    def get_weather(self, city):
        # Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
        api_key = 'YOUR_API_KEY'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response = requests.get(url)

        if response.status_code == 200:
            weather_data = response.json()
            return weather_data.get('weather', [])[0].get('main', 'Unknown')
        else:
            return 'Unknown'

    def rent_scooter(self, user_id, scooter_id):
        user = self.get_user_by_id(user_id)
        scooter = next((s for s in self.scooters if s.scooter_id == scooter_id), None)

        if not user or not scooter:
            print("User or scooter not found.")
            return

        weather = self.get_weather(user.city)
        rental_price = self.calculate_rental_price(weather)

        print(f"\nScooter Details:")
        print(f"Scooter ID: {scooter.scooter_id}")
        print(f"Battery Percentage: {scooter.battery_percentage}%")
        print(f"Range: {scooter.range_km} km")

        print(f"\nWeather Conditions in {user.city}: {weather}")
        print(f"Rental Price: {rental_price} tenge/minute")

    # def calculate_rental_price(self, weather):
    #     if weather.lower() == 'rain':
    #         return 70
    #     elif weather.lower() == 'clear':
    #         return 47
    #     else:
    #         return 50  # Default price for unknown weather

    def calculate_rental_price(self, weather):
        base_price = 50  # Default base price for unknown weather
        time_adjustment = 10  # Adjustment to be added during specific time periods

        current_time = datetime.now().time()
        print(current_time)

        # Define the time ranges for adjustments
        time_ranges = [(time(7, 0), time(10, 0)),
                       (time(13, 0), time(14, 0)),
                       (time(17, 50), time(21, 30))]

        # Check if the current time falls within any of the specified ranges
        for start_time, end_time in time_ranges:
            if start_time <= current_time <= end_time:
                if weather.lower() == 'rain':
                    return 70 + time_adjustment
                elif weather.lower() == 'clear':
                    return 47 + time_adjustment
                else:
                    return base_price + time_adjustment

        # If the current time doesn't fall within any time range, use the base price
        if weather.lower() == 'rain':
            return 70
        elif weather.lower() == 'clear':
            return 47
        else:
            return base_price

    def load_users(self):
        try:
            with open("users.json", "r") as file:
                user_data = json.load(file)
                self.users = [User(**u) for u in user_data]
        except FileNotFoundError:
            pass

    def save_users(self):
        with open("users.json", "w") as file:
            json.dump([vars(u) for u in self.users], file)

    def load_scooters(self):
        try:
            with open("scooters.json", "r") as file:
                scooter_data = json.load(file)
                self.scooters = [Scooter(**s) for s in scooter_data]
        except FileNotFoundError:
            pass

    def save_scooters(self):
        with open("scooters.json", "w") as file:
            json.dump([vars(s) for s in self.scooters], file)

if __name__ == "__main__":
    rental_system = RentalSystem()

    # User registration
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    city = input("Enter your city: ")

    user = rental_system.register_user(name, email, city)

    # Display available scooters
    print("\nAvailable Scooters:")
    for idx, scooter in enumerate(rental_system.scooters, 1):
        print(f"{idx}. Scooter ID: {scooter.scooter_id}")

    # Scooter rental
    if rental_system.scooters:
        scooter_number = int(input("\nEnter the number of the scooter you want to rent: "))
        if 1 <= scooter_number <= len(rental_system.scooters):
            selected_scooter = rental_system.scooters[scooter_number - 1]
            rental_system.rent_scooter(user.user_id, selected_scooter.scooter_id)
        else:
            print("Invalid scooter number.")
    else:
        print("No scooters available in the system.")

