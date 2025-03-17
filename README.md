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

Installation and Setup

1️⃣ Clone the Repository

git clone https://github.com/Kohmmz/Car-Rental-System.git
cd Car-Rental-System

2️⃣ Set Up the Virtual Environment and Install Dependencies

pipenv install
pipenv shell

3️⃣ Apply Database Migrations

alembic upgrade head

4️⃣ Start the CLI

python lib/cli.py

🎉 You're ready to go! 🚗💨

Managing Database Migrations

If you've made any changes to your SQLAlchemy models (Car, Customer, Rental), you need to generate a new migration:

alembic revision --autogenerate -m "describe your change here"

Example:

alembic revision --autogenerate -m "Added new field to Car model"

This command will scan your lib/model.py file and create a new migration file inside the migrations/versions/ folder.

Apply the New Migration to Your Database

After generating the migration, apply it using:

alembic upgrade head

This updates your SQLite database schema to match the latest version of your SQLAlchemy models.

Checking Applied Migrations

To see all migrations that have been applied, use:

alembic history

To check the current version of the database, run:

alembic current

Undoing a Migration

If the migration breaks something and you need to go one step back, use:

alembic downgrade -1

If you need to go back multiple steps, replace -1 with the number of steps (e.g., -2, -3, etc.).

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