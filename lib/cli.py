from lib.actions import (
    sign_up_user,
    log_in_user,
    car_availability,
    rent_car,
    return_car,
    admin_add,
    admin_update_car,
    admin_remove_car,
    admin_remove_rental,
    admin_update_rental,
)
from lib.model import Customer, Rental
from lib.database import session


def main():
    print("\n🚗 Welcome to the Car Rental System!")

    user = None
    while not user:
        print("\n1. Sign Up")
        print("2. Log In")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter your name: ").strip()
            password = input("Enter a password: ").strip()
            role = input("Enter your role (manager/customer): ").strip().lower()

            user = sign_up_user(name, password, role)

        elif choice == "2":
            name = input("Enter your name: ").strip()
            password = input("Enter your password: ").strip()
            user = log_in_user(name, password)
            if user:
                print(f"\nWelcome, {user.name}! ({user.role})")
                if user.role == "manager":
                    admin_menu(user)
                else:
                    customer_menu(user)

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


def customer_menu(user):
    """Handles Customer Actions"""
    while True:
        print("\n👤 Customer Menu")
        print("1. View Available Cars")
        print("2. Rent a Car")
        print("3. Return a Car")
        print("4. Logout")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            car_availability()
        elif choice == "2":
            car_id = input("Enter Car ID to rent: ").strip()
            if car_id.isdigit():
                rent_car(int(car_id), user.id)
            else:
                print("Invalid Car ID.")
        elif choice == "3":
            car_id = input("Enter the Car ID to return: ").strip()
            if car_id.isdigit():
                return_car(user.id, int(car_id))  # Fixed argument order
            else:
                print("Invalid Car ID.")
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid option. Try again.")


def admin_menu(admin):
    """Handles Admin Actions"""
    while True:
        print("\n🔧 Admin Menu")
        print("1. Add a New Car")
        print("2. Update Car Details")
        print("3. Remove a Car")
        print("4. View Available Cars")
        print("5. View Rentals")
        print("6. Update Rental")
        print("7. Remove Rental")
        print("8. Logout")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            make = input("Enter Car Make: ").strip()
            model = input("Enter Car Model: ").strip()
            year = input("Enter Year: ").strip()
            price = input("Enter Price: ").strip()
            if year.isdigit() and price.isdigit():
                admin_add(admin, make, model, int(year), int(price), available=True)
            else:
                print("Year and Price must be numbers.")

        elif choice == "2":
            car_id = input("Enter Car ID to update: ").strip()
            if car_id.isdigit():
                make = (
                    input("Enter new Make (or press Enter to skip): ").strip() or None
                )
                model = (
                    input("Enter new Model (or press Enter to skip): ").strip() or None
                )
                year = input("Enter new Year (or press Enter to skip): ").strip()
                price = input("Enter new Price (or press Enter to skip): ").strip()

                admin_update_car(
                    admin,
                    int(car_id),
                    make=make,
                    model=model,
                    year=int(year) if year.isdigit() else None,
                    price=int(price) if price.isdigit() else None,
                )
            else:
                print("Invalid Car ID.")

        elif choice == "3":
            car_id = input("Enter Car ID to remove: ").strip()
            if car_id.isdigit():
                admin_remove_car(admin, int(car_id))
            else:
                print("Invalid Car ID.")

        elif choice == "4":
            car_availability()

        elif choice == "5":
            print("\n📋 Viewing Rentals...")
            rentals = session.query(Rental).all()
            if rentals:
                for rental in rentals:
                    print(
                        f"Rental ID: {rental.id}, Car ID: {rental.car_id}, Customer ID: {rental.customer_id}, "
                        f"Rental Date: {rental.rental_date}, Return Date: {rental.return_date or 'Not Returned'}"
                    )
            else:
                print("No rentals found.")

        elif choice == "6":
            rental_id = input("Enter Rental ID to update: ").strip()
            if rental_id.isdigit():
                car_id = (
                    input("Enter new Car ID (or press Enter to skip): ").strip() or None
                )
                customer_id = (
                    input("Enter new Customer ID (or press Enter to skip): ").strip()
                    or None
                )
                return_date = (
                    input(
                        "Enter return date (YYYY-MM-DD) or press Enter to skip: "
                    ).strip()
                    or None
                )

                admin_update_rental(
                    admin,
                    int(rental_id),
                    car_id=int(car_id) if car_id and car_id.isdigit() else None,
                    customer_id=int(customer_id) if customer_id and customer_id.isdigit() else None,
                    return_date=return_date,
                )
            else:
                print("Invalid Rental ID.")

        elif choice == "7":
            rental_id = input("Enter Rental ID to remove: ").strip()
            if rental_id.isdigit():
                admin_remove_rental(admin, int(rental_id))
            else:
                print("Invalid Rental ID.")

        elif choice == "8":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()