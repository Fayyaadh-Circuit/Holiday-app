# Divider input
SYMBOL = "-"
WIDTH = 30

# location input list
location_options = ["d", "l", "p", "x"]


def plane_cost(city_flight):
    """
    Takes a input for location and assigns a value based on location.
    """

    if city_flight == "d":
        return 7500
    elif city_flight == "l":
        return 9800
    elif city_flight == "p":
        return 6700
    elif city_flight == "x":
        return False
    else:
        return False


def hotel_cost(num_nights):
    """
    Returns the total cost for a hotel for a given number of days.
    """
    if num_nights < 0:
        return False
    return num_nights * 1500


def car_rental(rental_days):
    """
    Returns the total cost for renting a car for a given number of days.
    """
    if rental_days < 0:
        return False
    return rental_days * 500


def holiday_cost(city_flight, num_nights, rental_days):
    """
    Returns the total cost for the holiday based on the 3 functions given.
    """
    total_cost = (plane_cost(city_flight) +
                  hotel_cost(num_nights) +
                  car_rental(rental_days))
    return total_cost


def options(city_flight, num_nights, rental_days):
    """Displays the main menu."""
    all_selected = city_flight and num_nights and rental_days
    print("Holiday calculator")
    print(f"f = flights {"✔️" if city_flight else ""}")
    print(f"a = accommodation {"✔️" if num_nights else ""}")
    print(f"r = rental car days {"✔️" if rental_days else ""}")
    print(f"t = total holiday cost {"" if all_selected else "❌"}")
    print("q = quit")


def location():
    """Displays the locations."""
    print("select a location")
    print("d = Dubai")
    print("l = London")
    print("p = paris")
    print("x = return")


def currency(value):
    """Converts the vale given to a correct currency format."""
    return f"R{value:,.2f}".replace(",", " ")


# Assigning bol to variables
num_nights = False
city_flight = False
rental_days = False

# Main loop for options
while True:
    print(SYMBOL * WIDTH)
    options(city_flight, num_nights, rental_days)
    choice = input("Please enter your choice: ").lower()
    print(SYMBOL * WIDTH)

    # Selecting location and assign vale
    if choice == "f":
        location()

        location_choice = input("select a location : ").lower()
        if location_choice == "x":
            city_flight = False
            print("returning")
            continue

        if location_choice not in location_options:
            input("select a location : ")
            continue

        city_flight = location_choice
        print(SYMBOL * WIDTH)
        cost = plane_cost(city_flight)
        if cost:
            print("Your flight will be", currency(cost))
            continue
        if cost is False:
            print("Returning")
        else:
            print("Invalid selection")

    # Calculate accommodation cost
    elif choice == "a":
        num_nights = int(input("how many nights will you be staying : "))
        print(SYMBOL * WIDTH)
        if num_nights >= 0:
            print("Accommodation cost for is",
                  currency(hotel_cost(num_nights)))
            continue
        print("Invalid selection")
        num_nights = False

    # Calculate rental car cost
    elif choice == "r":
        rental_days = int(input("How many day would u like a rental car : "))
        print(SYMBOL * WIDTH)
        if rental_days > num_nights:
            print(
                  "Warning  - Car rental longer than days booked for hotel")
        if rental_days >= 0:
            print("Your rental cost is", currency(car_rental(rental_days)))
            continue

        print("Invalid selection")
        rental_days = False


    # exit function
    elif choice == "q":
        print("Exiting...")
        break

    # Calculate total holiday cost
    elif choice == "t":

        # Calculate if all details have been provided
        if city_flight and num_nights and rental_days:
            total = holiday_cost(city_flight, num_nights, rental_days)
            print("Flights cost:", currency(plane_cost(city_flight)))
            print("Accommodation cost :", currency(hotel_cost(num_nights)))
            print("Rental car cost :", currency(car_rental(rental_days)))
            print("Your total is :", currency(total))
            print("Safe Travels q to exit or select what you'd like to edit")
            continue
        print("Please ensure that you have provided a destination,",
              "as well as a valid number of nights and days",
              sep="\n")

    # Handle invalid inputs
    else:
        print("Unrecognized option.")
         
