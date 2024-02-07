# AirBnB Clone Project

## Project Description

The AirBnB Clone project aims to create a simplified version of the popular vacation rental platform, allowing users to manage and interact with various objects related to property rentals. This project is a multi-step endeavor, starting with the implementation of a command-line interface (CLI) for managing AirBnB objects.

To start building the command interpreter for your AirBnB clone project, you can follow these steps. We'll start with the implementation of the `BaseModel` class, serialization/deserialization, and then move on to creating classes for AirBnB objects, and finally, the file storage engine.

1. **BaseModel class:**
   - Create a file named `base_model.py`.
   - Define the `BaseModel` class with methods for initialization, serialization, and deserialization.
   ```python
   import uuid
   from datetime import datetime
   import json

   class BaseModel:
       def __init__(self, *args, **kwargs):
           self.id = str(uuid.uuid4())
           self.created_at = datetime.now()
           self.updated_at = datetime.now()

       def to_dict(self):
           """Convert object attributes to a dictionary."""
           obj_dict = self.__dict__.copy()
           obj_dict['__class__'] = self.__class__.__name__
           obj_dict['created_at'] = self.created_at.isoformat()
           obj_dict['updated_at'] = self.updated_at.isoformat()
           return obj_dict

       def __str__(self):
           """Return the string representation of the object."""
           return "[{}] ({}) {}".format(
               self.__class__.__name__, self.id, self.__dict__)

       def save(self):
           """Update the 'updated_at' attribute and save to a file."""
           self.updated_at = datetime.now()
           models.storage.save()

   ```

2. **Serialization and Deserialization:**
   - Create a folder named `models`.
   - Inside the `models` folder, create a file named `__init__.py`.
   - Create a file named `file_storage.py` in the `models` folder for the file storage engine.
   - Define methods for serialization and deserialization in `file_storage.py`.
   ```python
   import json

   class FileStorage:
       __file_path = "file.json"
       __objects = {}

       def all(self):
           """Return the dictionary of all objects."""
           return FileStorage.__objects

       def new(self, obj):
           """Add a new object to the dictionary."""
           key = "{}.{}".format(obj.__class__.__name__, obj.id)
           FileStorage.__objects[key] = obj

       def save(self):
           """Serialize and save the objects to a file."""
           objects_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
           with open(FileStorage.__file_path, 'w') as file:
               json.dump(objects_dict, file)

       def reload(self):
           """Deserialize and load objects from a file."""
           try:
               with open(FileStorage.__file_path, 'r') as file:
                   objects_dict = json.load(file)
                   for key, obj_dict in objects_dict.items():
                       class_name = obj_dict['__class__']
                       obj = globals()[class_name](**obj_dict)
                       FileStorage.__objects[key] = obj
           except FileNotFoundError:
               pass
   ```

3. **Create AirBnB Classes:**
   - In the `models` folder, create files for each AirBnB class (e.g., `user.py`, `state.py`, `city.py`, `place.py`).
   - In each file, define a class that inherits from `BaseModel`.
   ```python
   from models.base_model import BaseModel

   class User(BaseModel):
       def __init__(self, *args, **kwargs):
           super().__init__(*args, **kwargs)
           # Additional attributes for User class

   # Repeat the above for other classes (State, City, Place, etc.)
   ```

4. **Command Interpreter:**
   - Create a file named `console.py` for your command interpreter.
   - Implement a loop to continuously accept user input and process commands.
   ```python
   import cmd

   class HBNBCommand(cmd.Cmd):
       prompt = '(hbnb) '

       def do_quit(self, arg):
           """Exit the command interpreter."""
           return True

       def do_EOF(self, arg):
           """Exit the command interpreter at EOF."""
           print()
           return True

       def emptyline(self):
           """Do nothing on an empty line."""
           pass

   if __name__ == '__main__':
       HBNBCommand().cmdloop()
   ```

   Extend the `HBNBCommand` class with methods to handle various commands like create, show, destroy, update, etc.

5. **Unit Tests:**
   - Create a folder named `tests` to store your unit tests.
   - Write unit tests for each class and functionality.

6. **Running the Command Interpreter:**
   - Run the `console.py` file to start the command interpreter.
   ```
   $ python console.py
   ```

## Command Interpreter Description

### How to Start the Command Interpreter

To start the AirBnB Clone Command Interpreter, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/Mutai05/AirBnB_clone.git
    ```

2. Navigate to the project directory:

    ```bash
    cd AirBnBClone
    ```

3. Run the command interpreter:

    ```bash
    ./console.py
    ```

### How to Use the Command Interpreter

The command interpreter allows users to manage various objects within the AirBnB Clone project. Here are some key commands and functionalities:

- **Create a new object:**
    ```
    (hbnb) create <class_name>
    ```

- **Retrieve an object:**
    ```
    (hbnb) show <class_name> <object_id>
    ```

- **Do operations on objects (e.g., count, compute stats, etc.):**
    ```
    (hbnb) <class_name>.<operation>()
    ```

- **Update attributes of an object:**
    ```
    (hbnb) update <class_name> <object_id> <attribute_name> "<new_value>"
    ```

- **Destroy an object:**
    ```
    (hbnb) destroy <class_name> <object_id>
    ```

- **Exit the command interpreter:**
    ```
    (hbnb) quit
    ```

### Examples

Here are some examples of using the AirBnB Clone Command Interpreter:

- **Creating a new User:**
    ```
    (hbnb) create User
    ```

- **Showing details of a User:**
    ```
    (hbnb) show User <user_id>
    ```

- **Updating the name of a User:**
    ```
    (hbnb) update User <user_id> name "John Doe"
    ```

- **Counting the number of Users:**
    ```
    (hbnb) User.count()
    ```

- **Exiting the command interpreter:**
    ```
    (hbnb) quit
    ```
