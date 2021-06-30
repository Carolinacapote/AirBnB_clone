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

