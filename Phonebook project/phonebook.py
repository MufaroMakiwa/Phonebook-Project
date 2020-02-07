# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 16:17:41 2019

@author: Mufaro Makiwa
"""

import datetime

class Contact:
    '''Represents a contact in  phonebook'''
    
    def __init__(self, title, name, surname, address, email, number, counter):
        '''This initializes the contact object with the stated attributes'''
        
        self.title=title
        self.name=name
        self.surname=surname
        self.address=address
        self.number=number
        self.email=email
        self.favorite='No'
        self.family='No'
        self.blacklisted='No'
        self.date_created=datetime.date.today()
        self._counter=counter #this is to be used when sorting
    
    def match(self, text):
        '''This is used to match the various attributes of the contact
        object with the filter text given by the user'''
        
        if self.email==None:
            return text in self.title or text in self.name or text in self.surname\
                or text in self.address or text in self.number
            
        else:
            return text in self.title or text in self.name or text in self.surname\
                or text in self.address or text in self.number or text in self.email
   

class Phonebook:
    '''This is a collection of all the contacts in the phonebook
    It contains the various actions that can be done on a contact'''
    
    def __init__(self):
        '''This initializes a list of all contacts as well as a list of al the
        favorite contacts'''
        
        self.all_contacts=[]
        self.favorite_contacts=[]
        self.blacklisted_contacts=[]
        self.family_contacts=[]
        
    def _find_contacts(self, text):
        '''This is used to find a partiular contact as according the filter
        text from the user'''
        
        return [contact for contact in self.all_contacts if contact.match(text)]
    
    def particular_contact(self, text, value):
        '''This is used to fish out a contact from those filtered
        The value is what the user enters when prompted from the menu interface'''
        
        filtered_dict={}
        for i in range(len(self._find_contacts(text))):
            filtered_dict[str(i+1)]=self._find_contacts(text)[i]
            
        return filtered_dict[value]  
    
    def create_new(self, title, name, surname, address, email, number, counter):
        '''This is used to add a new contact to the phonebook'''
        
        self.all_contacts.append(Contact(title, name, surname, address, email, number, counter))
  
    def delete_contact(self, text, value):
        '''This is used to delete a specific contact selected by the user'''
        
        contact=self.particular_contact(text, value)
        self.all_contacts.remove(contact)
        if contact in self.favorite_contacts:
            self.favorite_contacts.remove(contact)
        if contact in self.blacklisted_contacts:
            self.blacklisted_contacts.remove(contact)
        if contact in self.family_contacts:
            self.family_contacts.remove(contact)
               
    def add_blacklist_contact(self, text, value):
        '''This is used to add contacts to the phonebook's blacklist'''
        
        self.blacklisted_contacts.append(self.particular_contact(text, value))
        self.particular_contact(text, value).blacklisted='Yes'
        
    def add_family_contact(self, text, value):
        '''This is used to add contacts to the family list'''
        
        self.family_contacts.append(self.particular_contact(text, value))
        self.particular_contact(text, value).family='Yes'
        
    def add_favorite_contact(self, text, value):
        '''This is used to add contacts to the favorites list'''
        
        self.favorite_contacts.append(self.particular_contact(text, value))
        self.particular_contact(text, value).favorite='Yes'
        
    def remove_favorite(self, text, value):
        '''This is used to remove a contact from the favorites list'''
        
        self.favorite_contacts.remove(self.particular_contact(text, value))
        
    def remove_family(self, text, value):
        '''This is used to remove a contact from the favorites list'''
        
        self.family_contacts.remove(self.particular_contact(text, value))
        
    def remove_blacklist(self, text, value):
        '''This is used to remove a contact from blaklist'''
        
        self.blacklisted_contacts.remove(self.particular_contact(text, value))
    
    def modify_title(self, text, value, title):
        '''This is used to modify the title of a particular contact'''
        
        self.particular_contact(text, value).title=title
        
    def modify_name(self, text, value, name):
        '''This is used to modify the name of a particular contact'''
        
        self.particular_contact(text, value).name=name
    
    def modify_surname(self, text, value, surname):
        '''This is used to modify the surname of a particular contact'''
        
        self.particular_contact(text, value).surname=surname
        
    def modify_email(self, text, value, email):
        '''This is used to modify the email address of a particular contact'''
        
        self.particular_contact(text, value).email=email
        
    def modify_address(self, text, value, address):
        '''This is used to modify the physical address of a particular contact'''
        
        self.particular_contact(text, value).address=address
        
    def modify_number(self, text, value, number):
        '''This is used to modify the physical address of a particular contact'''
        
        self.particular_contact(text, value).number=number
        
    def delete_all_contacts(self):
        '''This is used to erase all contacts in the phonebook'''
        
        self.all_contacts=[]
    
    def add_to_existing(self, text, value, number):
        '''This is used to add contacts to an existing one'''
        
        self.particular_contact(text, value).number.append(number)
