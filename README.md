# 🚗 Car Rental System CLI

## 📌 Description
The **Car Rental System CLI** is a Python-based command-line interface application that allows users to manage a car rental business efficiently. It provides functionalities for managing customers, vehicles, and rental transactions using **SQLAlchemy ORM** for database management.

---

## ✨ Features
✅ **Customer Management**: Add, update, and remove customers.
✅ **Vehicle Management**: Add, update, and remove vehicles.
✅ **Rental Transactions**: Rent and return vehicles with automatic tracking.
✅ **Database Management**: Uses **SQLAlchemy ORM** and **Alembic** for migrations.

---

## 🛠️ Technologies Used
| Technology  | Purpose |
|------------|---------|
| 🐍 Python | Core Programming Language |
| 🗄️ SQLAlchemy ORM | Database Management |
| 🔄 Alembic | Database Migrations |
| 🗃️ SQLite | Default Database (Can be changed) |

---

## 🚀 Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/Kohmmz/Car-Rental-System.git
cd Car-Rental-System
```

### 2️⃣ Set Up the Virtual Environment & Install Dependencies
```sh
pipenv install
pipenv shell
```

### 3️⃣ Set Up the Database
```sh
alembic upgrade head
```

### 4️⃣ Start the CLI
```sh
python lib/cli.py
```
🎉 **You're ready to go!** 🚗💨

---

## 📂 Managing Database Migrations
If you've made changes to your SQLAlchemy models (**Car, Customer, Rental**), generate a new migration:
```sh
alembic revision --autogenerate -m "describe your change here"
```
🔹 **Example:**
```sh
alembic revision --autogenerate -m "Added new field to Car model"
```
This creates a migration file inside `migrations/versions/`.

### 📌 Apply New Migrations
```sh
alembic upgrade head
```
This updates your database schema to match your models.

### 📌 Check Applied Migrations
```sh
alembic history  # View migration history
alembic current  # Check current database version
```

### 🔄 Undoing a Migration
```sh
alembic downgrade -1  # Roll back last migration
```
📌 To go back multiple steps, replace `-1` with `-2`, `-3`, etc.

---

## 🔧 Usage
1. Follow the on-screen prompts in the CLI to navigate and perform operations.
2. Ensure that the database is **migrated** before using the system.

---

## 🔮 Future Enhancements
🔹 **GUI Version** - Implement a graphical interface.
🔹 **External API Integration** - Fetch real-time car pricing & availability.

---

## 🤝 Contributing
We welcome contributions! 🎉
1. **Fork** the repository.
2. **Create** a feature branch.
3. **Commit** your changes.
4. **Push** to your fork & submit a pull request.

---

## 📜 License
This project is licensed under the **MIT License**. See `LICENSE` for details.

---

## 📞 Contact
For any inquiries, open an issue on **[GitHub Issues](https://github.com/Kohmmz/Car-Rental-System/issues)** ✉️

