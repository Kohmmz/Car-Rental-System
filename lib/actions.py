"function and CRUD operations"
# sign up user admin or customer = done
# log in user = done
# check if cars are available for renting = done
# allow ther uer to rent a car = done
# update the car's availability when rented = done
# check if the car is rented using the database =done
# manage sysytem for the car rental(admin) = done
# make it soo that the function to manage the car rental system is only available to the admin = done
# menu = To do
# add admin can add new cars to the system = done
# add admin can remove cars from the system =done
# add admin can update the car's details =done
# add admin can update the rental details =done

from lib.model import Car, Customer, Rental
from datetime import datetime
from functools import wraps
from lib.database import session

def sign_up_user(name, password, role):
    """Check if user already exists; if not, create a new user."""
    existing_user = session.query(Customer).filter_by(name=name).first()
    if existing_user:
        print("User already exists")
        return None

    new_user = Customer(name=name, password=password, role=role)
    session.add(new_user)
    session.commit()
    print("User created successfully")
    return new_user

def log_in_user(name, password):
    """Authenticate user login."""
    user = session.query(Customer).filter_by(name=name, password=password).first()
    if user:
        print(f"Welcome Back {user.name}! ({user.role})")
        return user
    else:
        print("Invalid credentials, please try again")
        return None

def car_availability():
    """Check available cars for renting."""
    available_cars = session.query(Car).filter(Car.available.is_(True)).all()

    if available_cars:
        print("Available Cars:")
        for car in available_cars:
            print(f"ID: {car.id}, Make: {car.make}, Model: {car.model}, Year: {car.year}, Price: {car.price}")
    else:
        print("No cars available for rent")

def rent_car(car_id, customer_id):
    """Allow a customer to rent a car."""
    car_rent = session.query(Car).filter_by(id=car_id, available=True).first()
    if not car_rent:
        print("Car not available for rent")
        return None

    new_rental = Rental(car_id=car_rent.id, customer_id=customer_id, rental_date=datetime.now())
    car_rent.available = False

    session.add(new_rental)
    session.commit()

    print(f"Car ID {car_id} has been rented successfully!")
    return new_rental

def return_car(customer_id, car_id):
    """Process returning a rented car."""
    rental = session.query(Rental).filter_by(car_id=car_id, return_date=None).first()

    if rental and rental.customer_id == customer_id:
        rental.return_date = datetime.now()
        car = session.query(Car).filter(Car.id == rental.car_id).first()
        if car:
            car.available = True
        session.commit()
        print(f"Car ID {car_id} has been successfully returned.")
    else:
        print("Error: Either the car was not rented or does not belong to you.")

def admin_only(func):
    """Admin Privileges Decorator"""

    @wraps(func)
    def wrapper(customer, *args, **kwargs):
        if customer.role.lower() != "manager":
            print("Access Denied: manager only!")
            return None
        return func(customer, *args, **kwargs)

    return wrapper

@admin_only
def admin_add(customer, make, model, year, price, available=False):
    """Add a new car to the database."""
    add_car = Car(make=make, model=model, year=year, price=price, available=available)
    session.add(add_car)
    session.commit()
    print(f"Car {make} {model} added successfully.")

@admin_only
def admin_update_car(customer, car_id, make=None, model=None, year=None, price=None, available=None):
    """Update Car details."""
    car = session.query(Car).filter(Car.id == car_id).first()
    if car:
        if make:
            car.make = make
        if model:
            car.model = model
        if year:
            car.year = year
        if price:
            car.price = price
        if available is not None:
            car.available = available

        session.commit()
        print(f"Car ID {car_id} updated successfully!")
    else:
        print("Car not found.")

@admin_only
def admin_update_rental(admin, rental_id, car_id=None, customer_id=None, return_date=None, rental_date=None):
    """Update rental details."""

    rental = session.query(Rental).filter(Rental.id == rental_id).first()

    if not rental:
        print("Rental not found.")
        return

    updated = False

    if car_id is not None:
        rental.car_id = car_id
        updated = True

    if customer_id is not None:
        rental.customer_id = customer_id
        updated = True

    if return_date:
        try:
            rental.return_date = datetime.strptime(return_date, "%Y-%m-%d").date()
            updated = True
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return
    if rental_date:
        try:
            rental.rental_date = datetime.strptime(rental_date, "%Y-%m-%d").date() 
            updated = True
        except ValueError:
            print(" Invalid date format. Please use YYYY-MM-DD.")
            return

    if updated:
        session.commit()
        print(f"Rental ID {rental_id} updated successfully!")
    else:
        print(" No updates were made.")

@admin_only
def admin_remove_car(customer, car_id):
    """Remove a car from the database."""
    car = session.query(Car).filter(Car.id == car_id).first()
    if car:
        session.delete(car)
        session.commit()
        print(f"Car with ID {car_id} has been removed.")
    else:
        print(f"Car with ID {car_id} not found.")

@admin_only
def admin_remove_rental(customer, rental_id):
    """Remove a rental from the database."""
    rental = session.query(Rental).filter(Rental.id == rental_id).first()
    if rental:
        session.delete(rental)
        session.commit()
        print(f"Rental with ID {rental_id} has been removed.")
    else:
        print(f"Rental with ID {rental_id} not found.")
