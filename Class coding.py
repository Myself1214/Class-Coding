#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Animals

'''Animal Class'''

    def __init__(self, name):
            print('Initializing name')
            self.__name = name
            self.__kind = kind
            
        
    @property
    def name(self):
        print('Getting name')
        return self.__name

    @property
    def kind(self):
        print('Getting kind')
        return self.__kind

    @name.setter
    def name(self, new_name):
        print('Setting name')
        self.__name = new_name

    @kind.setter
    def type(self, new_kind):
        print('Setting kind')
        self.__name = new_kind
        
    def move(self):
        print('Moving')
        
    def attack(self):
        print('Attacking')

        
class Book

'''Book Class'''

    def __init__(self, name):
            print('Initializing name')
            self.__name = name
            self.__kind = kind
            
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
    def type(self, new_type):
        print('Setting type')
        self.__name = new_type
        
    @pages.setter
    def pages(self, new_pages):
        print('Setting pages')
        self.__name = new_pages
        
class Vehicle

'''Vehicle class'''

    @property
    def color(self):
        print('Getting color')
        return self.__color

    @property
    def engine-size(self):
        print('Getting engine-size')
        return self.__engine-size
    
    @property
    def year(self):
        print('Getting year')
        return self.__year
    
    def drive(self):
        print('Driving')
    
        

