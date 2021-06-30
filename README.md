# 0x00. AirBnB clone - The console

## Description

This repository contains the first steps of the AirBnB clone project made for Holberton School students.
During this first part of the project we had to::
- Put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances.
- Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- Create the first abstracted storage engine of the project: File storage.
- Create all unittests to validate all our classes and storage engine


### Files description

- **AUTHORS**  
 This file has a list of all individuals having contributed content to the repository. 

- **console.py**  
It contains a command line interpreter limited to a specific use-case. In our case, we want to be able to manage the objects of our project using this console.
The file contains the valid commands that you will find below:
  - do_EOF(): exits the program typing Ctrl + d.
  - emptyline(): an empty line + ENTER do not execute anything.
  - do_quit(): exits the program.
  - do_create(): Creates a new instance of a specific class and saves it (to the JSON file).
  - do_show(): Prints the string representation of an instance based on the class name and id.
  - do_destroy(): Deletes an instance based on the class name and id
  - do_all(): Shows all the instances that are alocated into the file.json based or not on the class name
  - do_update(): Updates an instance based on the class name and id by adding or updating an attribute
  - do_clear(): Clears the console.
 
- **models**  
This folder contains all the Class modules of the project, and a folder called engine. Click on [models](https://github.com/williamzborja/AirBnB_clone/tree/main/models) to know more about it.

- **tests**  
This folder contains all the UNITTEST of every module stored in the models folder and the TEST of the console.py file.


## Features

- **Programming language:** python3
- **Style:** All modules use the **PEP 8** style
- **Documentation:** All modules have documentation, including the functions, classes,etc.


## Usage

The console (console.py) works like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit  create  destroy  show  all  update

(hbnb)
(hbnb)
(hbnb) quit
$
```

But also in non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit  create  destroy  show  all  update
$
```

### Commands Usage

The commands of the console stored in **console.py** have 2 different usages.

#### - Calling the command first:
  - **quit**, **help**, **all** and **clear** can be called without any argument `<command>`
    - **help** and **all** accept arguments as well.
      To read the documentation of a command use `<help> <command>`.
      To print all the instances of a specific class type `<all> <class_name>`
  - **create** receives only 1 valid argument. `<create> <class_name>`
  - **show** and **destroy** receive only 2 valid arguments `<show> <class_name> <id>` or `<destroy> <class_name> <id>`
  - **update** needs 4 valid arguments to work. To update or add an attribute to the instance type `<update> <class_name> <id> <attribute name> "<attribute value>"` (do not forget the quots for the attribute value)

#### - Calling the class name first and then the command (`<class_name>.<command>()`)

- **quit**, **help** and **clear** Do not have this Usage, just the first one.
- **all** has this usage to print all the instances of a specific class. Usage: `<class_name>. all()`
- **create** usage: `<class_name>.create()`
- **show** and **destroy** must use the id argument to work. Usage: `<class_name>.show("<id>")` or `<class_name>.destroy("<id>")` (do not forget the quotes for the arguments insede the parentheses)
- **update** receives the id, atrribute name and attributr value inside the (). Usage: `<class_name>.update("<id>", "<attribute name>", "<attribute value>")` (do not forget the quotes for the arguments insede the parentheses)

Some examples of the usage:
```
$ ./console.py
(hbnb) create User
49faff9a-6318-451f-87b6-910505c55907
(hbnb) update User 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) User 49faff9a-6318-451f-87b6-910505c55907
[User] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) User.all()
[[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@holbertonshool.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}]
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'first_name': 'Betty', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@holbertonshool.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
(hbnb) quit
$
```
