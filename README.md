Django Dish Search Application
This project is a Django-based web application designed to search through a list of dishes and recommend the best match based on the user's input. The application uses a file-based SQLite database and leverages Django’s powerful admin interface for easy management of the dataset.

Features
Django Framework: Built using Django, this application takes advantage of its robust features, including the admin interface for managing the database and models.
SQLite Database: The application uses a file-based SQLite database, making it lightweight and easy to set up without requiring a separate database server.
Search Functionality: Users can search through the names of dishes, with the application providing a list of the best matches based on the input query.
Data Source: The dataset used in this application is sourced from a CSV file containing information about various dishes. This file can be found here.
Admin Interface: Django’s built-in admin interface allows easy management of the dish data, including adding, editing, and deleting entries.

How It Works
1. Data Import: The CSV file is imported into an SQLite database using Django’s ORM. Each row in the CSV file corresponds to a dish, which is stored in the database with relevant attributes.
2. Search and Recommendation: The application features a search bar where users can input the name of a dish. The system then searches the database for matching entries and returns the best match, based on relevance.
3. Admin Management: The Django admin interface provides a backend view for administrators to manage the dish data. They can view the full list of dishes, perform searches, and manage the dataset.
