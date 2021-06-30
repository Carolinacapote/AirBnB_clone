
# Models

## Description
This folder contains the modules of all the classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel and the **BaseModel** class. Here you can also find a folder called **engine** where is stored a file called file_storage.

### Files description
- **base_model.py:**  
It contains a class BaseModel that defines all common attributes/methods for other classes.
- **user.py:**  
Class User that inherits from BaseModel. This class manages the users of the website.
- **amenity.py:**  
Class Amenity that inherits from BaseModel. This class manages all the amenities a place has.
- **place.py:**  
Class Place that inherits from BaseModel. This class manages the places(houses, flats, rooms) inscribed on the website
- **review.py:**  
Class Review that inherits from BaseModel. This class manages all the reviews given to the places inscribed on the website.
- **city.py:**  
Class City that inherits from BaseModel. This class manages the cities where the user can search a place.
- **state.py:**  
Class State that inherits from BaseModel. This class manages the states where the user can find a place in a specific city.
- **engine:**  
In this folder is stored a file called **file_storage.py** that contains a class called FileStorage which serializes instances to a JSON file and deserializes JSON file to instances.

## Authors

| Name | GitHub username |
| ------ | ------ |
| Carolina Capote | [Carolinacapote](https://github.com/Carolinacapote) |
| William Rodríguez | [williamzborja](https://github.com/williamzborja) |
