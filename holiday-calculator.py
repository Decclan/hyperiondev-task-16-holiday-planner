
"""Unidecode for converting accented characters.
Tabulate for formatting display options for user."""

from unidecode import unidecode
from tabulate import tabulate

def city_options():
    """Dictionary flight options function for dynamic changeability"""
    city_dict =	{
        "London": 132.98,
        "Cape Town": 586.57,
        "Auckland": 812.76,
        "Sydney": 786.55,
        "Glasgow": 233.31,
        "New Delhi": 671.42,
        "Shanghai": 713.96,
        "Tokyo": 901.95,
        "Taipei": 887.97,
        "Hong Kong": 724.96,
        "Moscow": 564.88,
        "Madrid": 156.39,
        "Lisbon": 149.98,
        "Paris": 132.59,
        "Berlin": 102.69,
        "Rome": 121.99,
        "Warsaw": 178.67,
        "Athens": 156.23,
        "Mexico City": 685.97,
        "Bogota": 783.93,
        "Santiago": 901.95,
        "Buenos Aires": 887.35,
        "Bangkok": 712.99,
        "Washington": 564.88,
        "New York": 468.49,
        "Toronto": 589.55,
        "San José": 698.88,
        }
    return city_dict


def get_integer(prompt):
    """Fetch valid integer function"""
    while True:
        try:
            user_input = input(prompt)
            user_input = int(user_input) # Try to convert input to an integer
            # Validation: Ensure the input meets additional criteria
            if user_input < 0:
                print("Please enter a non-negative integer.")
            else:
                return user_input # Return valid input if all conditions are met

        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def city_choice(city_dict):
    """Fetch valid city choice from user"""
    while True:
        try:
            user_city = input("Where would you like to travel?\n")
            if user_city.isalpha:
                # Cast to lower case and change accents if present
                user_city = unidecode(user_city).lower()

            for city, price in city_dict.items():
                # Unidecode changes accent characters to non accented characters (e.g San José)
                if user_city == city.lower() or user_city == unidecode(city).lower():
                    print(f"\nYou chose: {city} for {chr(163)}{price}.")
                    # Returns tuple of lowered city, price float, original city key for display
                    return user_city, price, city
            print("Invalid input.")

        except ValueError:
            print("Please enter a valid option.")


def hotel_cost(num_nights):
    """Calculates the cost of the hotel"""
    hotel_total = num_nights * 150.00 + 2.95 # Price, booking fee
    return hotel_total


def plane_cost(city_flight):
    """Assigns second tuple value from user choice as the flight cost"""
    # Set tax for flight of 7.5%
    flight_tax = city_flight[1] * 0.075
    # Round to 2 decimal points, fetch cost from dictionary, add booking fee and tax
    flight_total = round(city_flight[1] + 5.99 + flight_tax, 2)
    return flight_total


def car_rental(rental_days):
    """Calculates car rental total based on rental days"""
    car_total = round(rental_days * 45.00 + 11.50, 2) # add insurance
    return car_total


def holiday_cost(num_nights, city_flight, rental_days):
    """Calculates total holiday cost"""
    holiday_total = round(hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days), 2)
    return holiday_total


def main():
    """Main logic sequence of events"""
    print("\nWelcome to the Holiday Application. Your options are:")
    # Tabulate display user options from city options dictionary
    headers = ["- City -", "- Price -"]
    print(tabulate(city_options().items(), headers = headers, tablefmt='grid'))
    # Cast tuple of user input choice
    city_flight = city_choice(city_options())

    num_nights = get_integer("How many nights will you stay at the hotel?\n")
    rental_days = get_integer("How many days will you rent a car for?\n")

    horizontal_line = str(84 * chr(9135))

    print(f"""
    {chr(8226)} Your hotel stay for {num_nights} nights in {city_flight[2]} including a booking fee will cost: {chr(163)}{hotel_cost(num_nights)}.
    {horizontal_line}
    {chr(8226)} Your total flight cost including tax and a booking fee will be: {chr(163)}{plane_cost(city_flight)}.
    {horizontal_line}
    {chr(8226)} Your car rental cost for {rental_days} days with insurance will be: {chr(163)}{car_rental(rental_days)}.
    {horizontal_line}
    {chr(8226)} The total cost of your holiday to {city_flight[2]} will be: {chr(163)}{holiday_cost(num_nights, city_flight, rental_days)}
    """)


main()
