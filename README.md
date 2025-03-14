Car Rental System CLI

Description

The Car Rental System CLI is a Python-based command-line interface application that allows users to manage a car rental business efficiently. It provides functionalities for managing customers, vehicles, and rental transactions using SQLAlchemy ORM for database management.

Features

Customer Management: Add, update, and remove customers.

Vehicle Management: Add, update, and remove vehicles.

Rental Transactions: Rent and return vehicles with automatic tracking.

Database Management: Uses SQLAlchemy ORM and Alembic for migrations.

Technologies Used

Python

SQLAlchemy ORM

Alembic (for database migrations)

SQLite (default database, but can be configured for PostgreSQL/MySQL)

Installation

Clone the Repository:

git clone https://github.com/Kohmmz/Car-Rental-System.git
cd Car-Rental-System

Set Up the Virtual Environment and Install Dependencies:

pipenv install
pipenv shell

Set Up the Database:

alembic upgrade head

Start the CLI:

python lib/cli.py

🎉 You're ready to go! 🚗💨



Usage

Follow the on-screen prompts in the CLI to navigate and perform operations.

Ensure that the database is properly migrated before usage.

Future Enhancements

Implement a GUI version of the application.

Add authentication and user roles.

Integrate with an external API for real-time pricing and availability.

Contributing

Contributions are welcome! To contribute:

Fork the repository.

Create a feature branch.

Commit your changes.

Push to your fork and submit a pull request.

License

This project is licensed under the MIT License. See LICENSE for more details.

Contact

For any inquiries, reach out via GitHub Issues.