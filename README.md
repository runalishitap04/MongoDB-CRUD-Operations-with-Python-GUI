# MongoDB-CRUD-Operations-with-Python-GUI:

This application provides a user-friendly graphical interface to perform CRUD (Create, Read, Update, Delete) operations on a MongoDB database using Python. The GUI is built with Tkinter, Python’s standard GUI toolkit, while PyMongo is used to interact with MongoDB.

The interface allows users to manage records within a MongoDB collection effortlessly. On launch, users can connect to a local or remote MongoDB database by entering the connection URI and specifying the desired database and collection names.

The Create functionality enables users to insert new documents into the collection. The form provides input fields for entering data in key-value format. On submission, the data is validated and stored in the MongoDB collection.

For the Read operation, the GUI displays all documents from the collection in a scrollable text area or table. Users can refresh this view at any time to retrieve the latest data.

The Update feature allows users to modify existing documents. Users can select a document by ID or search criteria, then enter new values for any fields they wish to update. The changes are applied immediately after confirmation.

The Delete functionality lets users remove records by specifying the document’s ID or matching conditions. Safety prompts prevent accidental deletions.

The GUI is designed to be intuitive, with clear labels, buttons, and real-time feedback for each action. Error messages and success notifications are also displayed for better user experience.

This project is ideal for developers and database administrators who want a simple yet powerful tool to interact with MongoDB without using command-line tools. It also serves as a great educational project for learning database operations, GUI development, and Python-MongoDB integration.
