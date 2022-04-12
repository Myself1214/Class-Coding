#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Animals

'''Animal Class(base class)'''

    def __init__(self, name):
            print('Initializing name')
            self.__name = name
               
    @property
    def name(self):
        print('Getting name')
        return self.__name


    @name.setter
    def name(self, new_name):
        print('Setting name')
        self.__name = new_name
        
    def move(self):
        print('Moving')
        
    def attack(self):
        print('Attacking')
        
class Fish(Animals)

'''Fish class(other class)'''

    def __init__(self, name, type):
                super().__init__(name)
                self.__fishtype = type
    
    @Property
    def type(self):
        return self.__fishtype
    
    @type.setter
    def name(self, new_type):
        self.__fishtype = new_type
        

class Snake(Animals)

'''Snake class(other class)'''

    def __init__(self, name, type, poisoneous):
        super().__init__(name)
        self.__type = type
        self.__snakepoisoneous = poisoneous
        
    @Property
    def type(self):
        return self.__type
    
    @type.setter
    def name(self, new_type):
        self.__type = new_type
        
    @Property
    def poisoneous(self):
        return self.__sneakpoisoneous
    
    @poinoseous.setter
    def name(self, new_poisoneous):
        self.__sneskpoisoneous = new_poisoneous
        
class Person(Animals)

'''Person class(other class)'''

    def __init__(self, name, gender):
        super().__init__(name)
        self.__persongender = gender
        
    @Property
    def gender(self):
        return self._persongender
    
    @gender.setter
    def name(self, new_gender):
        self._persongender = new_gender
        
    
#-----------------------------------------------------------------------------------
        
class Book

'''Book Class(base class)'''

    def __init__(self, name, type, pages):
            print('Initializing name')
            self.__name = name
            self.__type = type
            self.__pages = pages
            
    @property
    def name(self):
        print('Getting name')
        return self.__name

    @property
    def type(self):
        print('Getting type')
        return self.__type
    
    @property
    def pages(self):
        print('Getting pages')
        return self.__pages
    

    @name.setter
    def name(self, new_name):
        print('Setting name')
        self.__name = new_name

    @type.setter
    def name(self, new_type):
        print('Setting type')
        self.__type = new_type
        
    @pages.setter
    def name(self, new_pages):
        print('Setting pages')
        self.__pages = new_pages
        

class Textbook(Book)

'''Textbook class(other class)'''

    def __init__(self, name, type, pages, color):
        super().__init__(name)
        super().__init__(type)
        super().__init__(pages)
        self.__textbookcolor = color
        
    @Property
    def color(self):
        return self.__textbookcolor
    
    @color.setter
    def name(self, new_color):
        self.__textbookcolor = new_color
        
class Adressbook(Book)

'''Adressbook class(other class)'''

    def __init__(self, name, type, pages, color):
        super().__init__(name)
        super().__init__(type)
        super().__init__(pages)
        self.__adressbookcolor = color
        
    @Property
    def color(self):
        return self.__adressbookcolor
    
    @color.setter
    def name(self, new_color):
        self.__adressbookcolor = new_color
        
        
#--------------------------------------------------------------------------------------------------
        
class Vehicle

'''Vehicle class(base class)'''

    def __init__(self, color, year):
        print(Initializing color, year)
        self.__color = color
        self.__year = year

    @property
    def color(self):
        print('Getting color')
        return self.__color

    
    @property
    def year(self):
        print('Getting year')
        return self.__year
    
    def drive(self):
        print('Driving')
        

class Car(Vehicle)

'''Car class(other class)'''

    def __init__(self, color, year, engine-size):
        super().__init__(color)
        super.__init__(year)
        self.__carengine-size = engine-size
        
    @Property
    def engine-size(self):
        return self.__carengine-size
    
    @engine-size.setter
    def name(self, new_engine-size):
        self.__carengine-size = new_engine-size
        
class Bicycle(Vehicle)

'''Bicycle class(other class)'''

    def __init__(self, color, year, size):
        super().__init__(color)
        super().__init__(year)
        self.__size = size
        
    @Property
    def size(self):
        return self.__size
    
    @size.setter
    def name(self, new_size):
        self.__size = new_size
        
class Boat(Vehicle)

'''Boat class(other class)'''

    def __init__(self, color, year, type):
        super().__init__(color)
        super().__init__(year)
        self.__type = type
        
    @Property
    def type(self):
        return self.__type
    
    @type.setter
    def name(self, new_type):
        self.__type = new_type
        

