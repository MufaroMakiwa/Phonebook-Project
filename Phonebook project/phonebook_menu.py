# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 18:09:13 2019

@author: Mufaro Makiwa
"""

import sys
from phonebook import Phonebook
import time


#to have a global sort variable for sorting contacts
#to have a settings function that includes the sort criterion and how to view
#contacts either name or surname first


class PhonebookMenu:
    '''This provides a list of options for the user to pick from and allows
    interaction with the phonebook menu interface'''
    
    sort_by='First Name'
    display_fields=[1, 2, 3, 4, 5]
    
    def __init__(self):
        '''This creates a phonebook object from the Phonebook class as well as
        initializes the various options available for interaction with the 
        phonebook'''
        
        self.phonebook=Phonebook()
        self.options={'1':self.display_all_contacts,
                      '2':self.search_contacts,
                      '3':self.create_new_contact,
                      '4':self.edit_contact,
                      '5':self.erase_a_contact,
                      '6':self.modify_groups,
                      '7':self.display_group_contacts,
                      '8':self.about_contacts,
                      '9':self.settings,
                     '10':self.quit_use}
    
    def display_options(self):
        '''This method contains a list of the various methods and displays them
        as they are on the screen for user selection'''
        
        print('''\n\n
{:^30s}
|________________________________|
|                                |
| 1. Display all contacts        |
| 2. View particular contact(s)  |
| 3. Create a new contact        |
| 4. Modify an existing contact  |
| 5. Delete a contact            |
| 6. Modify phonebook groups     |
| 7. Display group contacts      |
| 8. About contacts              |
| 9. Settings                    |
|10. Quit use                    |
|                                |
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'''.format('| <<<<____PHONEBOOK MENU____>>>> |'))        
    def run(self):
        '''This repeatedly prompts the user to perform various actions on the 
        choice from the list of options
        
        The current password to the phonebook is the word pass'''
        
        count=3
        prompt='''
You are about to access your phonebook. Please enter your password:
    
>\t'''
        while True:
            password=input(prompt)
            if password=='pass':
                print('\n<__ACCESS GRANTED!!__>\n')
                for i in range(78):
                    print('.', end='') 
                    time.sleep(3/78)
                break
            else:
                count-=1
                prompt='''
You have {} chances left. Enter the correct password:
    
>\t'''.format(count)
                if count==0:
                    print('\n<__You have run out of chances, try again later__>\n'.upper())
                    time.sleep(1)
                    print('<<__ABORTING__>>\n')
                    for i in range(78):
                        print('.', end='')
                        time.sleep(3/78)
                    print('\n')
                    sys.exit(0)
        
        while True:
            self.display_options()
            while True:
                option=input('Enter the number corresponding to the option you want:\n\n>\t')
                if option in self.options:
                    action=self.options[option]
                    action()
                    print('\n')
                    for i in range(78):
                        print('.', end='')
                        time.sleep(3/78)
                    break
                else:
                    print('\n<__Enter a valid option!!__>\n'.upper())
                    time.sleep(1)
                    
    def settings(self):
        '''This function presents the user with a means to set a specific 
        sort method for his or her contacts.
        
        It also provides an option to decide whether to view contacts with name
        or surname first'''
        
        time.sleep(1)
        prompt='''
Select the required option:
    
1. Sort contacts by
2. Display options

>\t'''

        while True:
            choice=input(prompt)
        
            if choice in ['1', '2']:
                break
            else:
                prompt='Select a valid option, 1 or 2\n\n>\t'
                
        if choice=='1':
            print('\n')
            prompt='''
Select the sort criterion:
    
1. First Name
2. Surname

>\t'''
            while True:
                option=input(prompt)
                if option in ['1', '2']:
                    break
                
                else:
                    prompt='Enter a valid option, 1 or 2\n\n>\t'
                    
            if option=='1':
                self.sort_by='First Name'
                
            elif option=='2':
                self.sort_by='Surname'
                
            print('\n<__THE SORT CRITERION WAS SUCCESSFULLY CHANGED!!__>\n')
            time.sleep(1)
                
        elif choice=='2':
            print('''\n
The following fields are optional at contacts display:
    
1. Home Address
2. Contact in favorites
3. Family contact
4. Blacklisted
5. Date created\n''')
            time.sleep(2)
            
            print('''
<__ENTER THE NUMBERS CORRESPONDING TO THE FIELDS YOU WOULD LIKE TO BE \
DISPLAYED e.g 1,2,4,5__>
          Press zero if you do not want any of these fields to be displayed
          
   (<__Press enter when you no longer want to edit the contact fields to be displayed__>)''')
            
            prompt='\n>\t'
            while True:
                values=input(prompt)
                
                if not values:
                    fields=0
                    print('\n<__Display options were not modified!!__>'.upper())
                    break
                
                if len(values)==1:
                    try:
                        fields=int(values)
                    
                    except:
                       prompt='\n<__ENTER VALID OPTIONS!!__>\n\n>\t'
                       continue
                    
                    if fields not in range(1, 6):
                        if fields==0:
                            self.display_fields=[]
                            print('\n<__THE DISPLAY FIELDS WHERE SUCCESSFULLY MODIFIED!!__>\n')
                            break
                        
                        else:
                            prompt='\n<__ENTER VALID OPTIONS!!__>\n\n>\t'
                            continue
                        
                    else:
                        break
                
                elif len(values)>1:
                    try:
                        fields=list(eval(values))
                        
                    except:
                        error=True
                        prompt='\n<__ENTER VALID OPTIONS!!__>\n\n>\t'
                        continue
                    
                    for i in fields:
                        if type(i)!=int:
                            error=True
                            prompt='\n<__ENTER VALID OPTIONS!!__>\n\n>\t'
                            break
                        
                        else:
                            error=False
                        
                    for i in fields:
                        if i not in range(1, 6):
                            error=True
                            prompt='\n<__ENTER VALID OPTIONS!!__>\n\n>\t'
                            break
                        
                        else:
                            error=False
                        
                    if error: 
                        continue
                    
                    elif not error:
                        break
            
            if fields!=0:
                if type(fields)==int:
                    self.display_fields=[]
                    self.display_fields.append(fields)
                
                else:
                    self.display_fields=fields
                    
                print('\n<__THE DISPLAY FIELDS WHERE SUCCESSFULLY CHANGED!!__>\n')
                    
                    
    def about_contacts(self):
        '''This serves to display the details about all the contacts in the 
        phonebook, that is, the total number of contacts and the numbers of 
        contacts in each group'''
        
        print('''\n
                 <__YOUR PHONEBOOK CONTACTS STATISTICS__>''')
        
        print('''\n              
                  Number of contacts in phonebook  :  {}
                  Number of contacts in favorites  :  {}
                  Number of family contacts        :  {}
                  Number of backlisted contacts    :  {}
                  
'''.format(len(self.phonebook.all_contacts), len(self.phonebook.favorite_contacts),\
len(self.phonebook.family_contacts), len(self.phonebook.blacklisted_contacts)))   
            
        time.sleep(3)
        
    def _sort_contacts(self, contacts):
        '''This is for intenal purposes only, used to sort contacts as
        per user's request'''
        
        sort_dict={} #contains an integer index and the contact object as value
        sort_criterion={} #contains an integer index and the name or surname
        sorted_list=[] #collects all the contacts aftert they  have been sorted  
        
        if self.sort_by=='First Name':
            for i in range(len(contacts)):
                sort_dict[i+1]=contacts[i]                   
                sort_criterion[i+1]=contacts[i].name+contacts[i].surname+str(contacts[i]._counter)
              
        elif self.sort_by=='Surname':
            for i in range(len(contacts)):
                sort_dict[i+1]=contacts[i]                   
                sort_criterion[i+1]=contacts[i].surname+contacts[i].name+str(contacts[i]._counter)
                         
        for i in sorted(sort_criterion.values()):
            for j in sort_criterion:
                if sort_criterion[j]==i:
                    index=j
            sorted_list.append(sort_dict[index])
            
        return sorted_list
            
    def display_contacts_search(self, contacts):
        '''This is for displaying searched contacts'''
        
        print('\n')
        for i in range(len(contacts)):
            print('{:<4s}{:<22s}:\t{}'.format(str(i+1)+'.', '-Title', contacts[i].title))
            print('    {:<22s}:\t{}'.format('-Name', contacts[i].name))
            print('    {:<22s}:\t{}'.format('-Surname', contacts[i].surname))
            print('    {:<22s}:\t{}'.format('-Phone number(s)', contacts[i].number[0]))
            if len(contacts[i].number)>1:
                for j in range(1, len(contacts[i].number)):
                    print('    {:<22s}:\t{}'.format(' ', contacts[i].number[j]))
            print('    {:<22s}:\t{}'.format('-Email address', contacts[i].email))
            print('    {:<22s}:\t{}'.format('-Home address', contacts[i].address))
            print('    {:<22s}:\t{}'.format('-Contact in favorites', contacts[i].favorite))
            print('    {:<22s}:\t{}'.format('-Family contact', contacts[i].family))
            print('    {:<22s}:\t{}'.format('-Blacklisted', contacts[i].blacklisted))
            print('    {:<22s}:\t{}'.format('-Date created', contacts[i].date_created))
            print('\n\n')
            time.sleep(1)
            
    def display_all_contacts(self, contacts=None):
        '''This is for displaying all the contacts in a fixed way'''
        
        if not contacts:
            if len(self.phonebook.all_contacts)==0:
                print('\n<__There are no contacts in your phonebook!!__>'.upper())
                
            else:
                print('\n')
                contacts=self._sort_contacts(self.phonebook.all_contacts)
#                self.display_contacts_search(contacts)
        else:
            print('\n')
            contacts=self._sort_contacts(contacts)
#            self.display_contacts_search(contacts)
            
        if contacts:
            print('\n')
            for i in range(len(contacts)):
                print('{:<4s}{:<22s}:\t{}'.format(str(i+1)+'.', '-Title', contacts[i].title))
                print('    {:<22s}:\t{}'.format('-Name', contacts[i].name))
                print('    {:<22s}:\t{}'.format('-Surname', contacts[i].surname))
                print('    {:<22s}:\t{}'.format('-Phone number(s)', contacts[i].number[0]))
                if len(contacts[i].number)>1:
                    for j in range(1, len(contacts[i].number)):
                        print('    {:<22s}:\t{}'.format(' ', contacts[i].number[j]))
                print('    {:<22s}:\t{}'.format('-Email address', contacts[i].email))
                
                if 1 in self.display_fields:                    
                    print('    {:<22s}:\t{}'.format('-Home address', contacts[i].address))
                
                if 2 in self.display_fields:
                    print('    {:<22s}:\t{}'.format('-Contact in favorites', contacts[i].favorite))
                
                if 3 in self.display_fields:
                    print('    {:<22s}:\t{}'.format('-Family contact', contacts[i].family))
                
                if 4 in self.display_fields:
                    print('    {:<22s}:\t{}'.format('-Blacklisted', contacts[i].blacklisted))
                
                if 5 in self.display_fields:
                    print('    {:<22s}:\t{}'.format('-Date created', contacts[i].date_created))
                print('\n\n')
                time.sleep(1)
        
    def display_group_contacts(self):
        '''This is for displaying a specific group of contacts in a fixed way'''
        
        if len(self.phonebook.all_contacts)==0:
            print('\n<__THERE ARE NO CONTACTS IN YOUR PHONEBOOK!!__>\n')
        else:
            prompt='''
Select the option corresponding to the group of contacts you want to display:
    
1. Favorite contacts
2. Family contacts
3. Blacklisted contacts

>\t'''
            while True:
                group=input(prompt)
                if group=='1':
                    if len(self.phonebook.favorite_contacts)==0:
                        print('\n<__You do not have contacts in the favorites list!!__>'.upper())
                        time.sleep(1)
                        
                    else:
                        contacts=self._sort_contacts(self.phonebook.favorite_contacts)
                        self.display_all_contacts(contacts)
                        time.sleep(1)
                    break
                
                elif group=='2':
                    if len(self.phonebook.family_contacts)==0:
                        print('\n<__YOU DO NOT HAVE CONTACTS IN THE FAMILY LIST!!__>')
                        time.sleep(1)
                        
                    else:
                        contacts=self._sort_contacts(self.phonebook.family_contacts)
                        self.display_all_contacts(contacts)
                        time.sleep(1)
                    break
                
                elif group=='3':
                    if len(self.phonebook.blacklisted_contacts)==0:
                        print('\n<__You do not have blacklisted contacts!!__>'.upper())
                        time.sleep(1)
                        
                    else:
                        contacts=self._sort_contacts(self.phonebook.blacklisted_contacts)
                        self.display_all_contacts(contacts)
                        time.sleep(1)
                    break
                
                else:
                    print('\n<__Enter a valid option!!__>\n'.upper())
                    time.sleep(1)
                    
    def create_new_contact(self):
        '''This is for providing the user with fields to add the various attributes
        of a contact object'''

        print('''
Fill in all the required fields. Press enter if there is nothing to add \
(This only applies to email, home address and when adding phone numbers more than once):''')
        time.sleep(3)
        print('\n')
        
        while True:
            title=input('{:21s}:\t'.format('Enter Title'))
            if title:
                break
        while True:
            name=input('{:21s}:\t'.format('Enter Name'))
            if name:
                break
        while True:
            surname=input('{:21s}:\t'.format('Enter Surname'))
            if surname:
                break
        
        counter=1
        for contact in self.phonebook.all_contacts:
            if name+surname==contact.name+contact.surname:
                counter+=1
            
        while True:
            address=input('{:21s}:\t'.format('Enter Home Address'))
            if address:
                break
            else:
                address='N/A'
                break
        count=1
        numbers=[]
        while True:
            number=input('{:21s}:\t'.format('Enter Phone Number '+str(count)))
            if number=='':
                if count>1:
                    break
                else:
                    continue
                
            elif len(self.phonebook.all_contacts)==0:
                error=False
                
            else:
                for i in self.phonebook.all_contacts:
                    if number in i.number:
                        error=True
                        prompt='''
The number you entered is already saved under {} {} {}.         
Do you want to add more numbers to this new contact:

1. YES
2. NO

>\t'''.format(i.title.upper(), i.name.upper(), i.surname.upper())

                        while True:
                            choice=input(prompt)
                            
                            if choice in ['1', '2']:
                                break
                            
                            else:
                                prompt='Enter a valid option, 1 or 2:\n\n>\t'
                                
                        if choice=='1':
                            break
                            
                        elif choice=='2':
                            if len(numbers)==0:
                                print('''
\n<__NEW CONTACT CREATION WAS UNSUCCESSFUL__>\n''')
                                return
                            
                            else:
                                break
                        
                    else:
                        error=False
                        
            if error:
                if choice=='2' and len(numbers)>0:
                    break
                
            else:
                if number in numbers:
                    print('\n<__{} has already been entered!!__>\n'.format(number))
                    time.sleep(1)
                    
                else:
                    numbers.append(number)
                    count+=1
                
        
        while True:
            email=input('{:21s}:\t'.format('Enter Email Address'))
            if email=='':
                self.phonebook.create_new(title, name, surname, address, None, numbers, counter)
                break
            
            elif len(self.phonebook.all_contacts)==0:
                new_email=False
                
            else:
                for i in self.phonebook.all_contacts:
                    if email==i.email:
                        prompt=('''\n
The email you entered is already saved under {} {} {}. 
Do you want to enter a different email address to this new contact:

1. YES
2. NO

>\t'''.format(i.title, i.name, i.surname))
                        while True:
                            choice=input(prompt)
                            if choice=='1':
                                new_email=True
                                break
                            elif choice=='2':
                                new_email=False
                                email=None
                                break
                            else:
                                prompt='Enter a valid option, 1 or 2:\n\n>\t'
                                
                        if choice=='1' or choice=='2':
                            break
                    else:
                        new_email=False
                        
            if not new_email:
                self.phonebook.create_new(title, name, surname, address, email, numbers, counter)  
                break
                
        print('\n\n<__Your contact was successfully created!!!__>'.upper())
        
    def _find_particular_contacts(self):
        '''This function serves to prompt the user to get the required contacts'''
        
        print('''
\n<__ALL CONTACTS THAT MATCH THE SEARCH KEYWORD WILL BE DISPLAYED!!__>
 (Any tiny detail of any contact can be used as the search keyword)''')
        time.sleep(2)
        
        text=input('''
Type the search key word for a contact:
(Press enter to display all contacts)
    
>\t''')
        contacts=self.phonebook._find_contacts(text)
        
        if len(contacts)==0:
            print('\n<__THERE IS NO CONTACT FOUND THAT MATCHES THE SEARCH KEYWORD!!__>\n')
            value=None
            
        elif len(contacts)>0:
            values=[]
            for i in range(len(contacts)):
                values.append(str(i+1))
                
            if len(contacts)==1:
                print('\nThe following contact has been found:\n')
                self.display_contacts_search(contacts)
                value='1' 
                
            elif len(contacts)>1:
                print('\nThe following {} contacts have been found:\n'.format(len(contacts)))
#                contacts=self._sort_contacts(contacts)
                self.display_contacts_search(contacts)
                print('\n')
                while True:
                    value=input('''
Type in the number corresponding to the contact you want:
    
>\t''')
                    if value in values:
                        break
                    
                    else:
                        print('\n<__Enter a valid option!!__>\n'.upper())
                        time.sleep(1)
                        
        return contacts, text, value
                           
    def search_contacts(self):
        '''This is used to display particular contacts as required by the user'''
        
        if len(self.phonebook.all_contacts)==0:
            print('\n<__There are no contacts in your phonebook!!__>\n'.upper())
            
        else:
            print('''
\n<__ALL CONTACTS THAT MATCH THE SEARCH KEYWORD WILL BE DISPLAYED!!__>
 (Any tiny detail of any contact can be used as the search keyword)''')
            
            time.sleep(2)
            text=input('''
Type the search key word for a contact:
(Press enter to display all contacts)
    
>\t''')
            contacts=self.phonebook._find_contacts(text)
            
            if len(contacts)==0:
                print('\n<__THERE IS NO CONTACT FOUND THAT MATCHES THE SEARCH KEYWORD!!__>\n')
            
            elif len(contacts)>0:
                if len(contacts)==1:
                    print('\nThe following contact has been found:\n')
                    self.display_contacts_search(contacts)
                    
                else:
                    print('\n{} contacts have been found:\n'.format(len(contacts)))
                    contacts=self._sort_contacts(contacts)
                    self.display_all_contacts(contacts)
                    time.sleep(1)
                    print('\n')
        
    def edit_contact(self):
        '''This provides the user with various options to edit one attribute
        of a particular contact'''
        
        if len(self.phonebook.all_contacts)==0:
            print('\n<__There are no contacts in your phonebook!!__>'.upper())
            
        else:
            contacts, text, value=self._find_particular_contacts()
            
            if len(contacts)>0:
                the_contact=self.phonebook.particular_contact(text, value)
                time.sleep(1)
            
                while True:
                    print('''
Select the field you want to edit: 1 - Title
                                   2 - Name
                                   3 - Surname
                                   4 - Phone number(s)
                                   5 - Email address
                                   6 - Home address
                                   7 - Phonebook Menu''')
            
                    valid_options=[]
                    for i in range(1, 8):
                        valid_options.append(str(i))
                    
                    while True:
                        choice=input('\n>\t')
                        
                        if choice in valid_options[:-1]:
                            print('''\n
(<__Press enter when you no longer want to edit the selected field__>)\n''')
                        time.sleep(1)
                        
                        if choice=='1':
                            title=input('Type in the new title:\n\n>\t')
                            
                            if title:
                                self.phonebook.modify_title(text, value, title)
                                print('\n<__The title was successfully changed!!__>'.upper())                            
                                time.sleep(1)
                                
                            else:
                                print('\n<__The title was not changed!!__>'.upper())
                                time.sleep(1)
                            
                        elif choice=='2':
                            name=input('Type in the new name:\n\n>\t')
                            
                            if not name:
                                print('\n<__The name was not changed!!__>'.upper())
                                time.sleep(1)
                            
                            elif name==the_contact.name:
                                print('\n<__The name was successfully changed!!__>'.upper())
                                time.sleep(1)
                                
                            else:
                                for contact in self.phonebook.all_contacts:
                                    if name+the_contact.surname==contact.name+contact.surname:
                                        the_contact._counter+=1
                                    
                                self.phonebook.modify_name(text, value, name)
                                print('\n<__The name was successfully changed!!__>'.upper())
                            
                        elif choice=='3':
                            surname=input('Type in the new surname:\n\n>\t')
                            
                            if not surname:
                                print('\n<__The surname was not changed!!__>'.upper())
                                time.sleep(1)
                            
                            elif surname==the_contact.surname:
                                print('\n<__The surname was successfully changed!!__>'.upper())
                                
                            else:
                                for contact in self.phonebook.all_contacts:
                                    if the_contact.name+surname==contact.name+contact.surname:
                                        the_contact._counter+=1
                                        
                                self.phonebook.modify_surname(text, value, surname)
                                print('\n<__The surname was successfully changed!!__>'.upper())
                            
                        elif choice=='4':
                                
                            while True:
                                action=input('''
Select the required option:
        
1. Add more phone numbers
2. Modify existing phone numbers
3. Delete an existing phone number

>\t''')
                                
                                if not action:
                                    print('\n<__The contact phone numbers were not modified!!__>\n'.upper())
                                    time.sleep(1)
                                    break
                                    
                                    
                                elif action=='1':
                                    print('\n<__Press \'enter\' when you no longer want to enter the new number!!__>\n'.upper())
                                    time.sleep(2)                
                                    count=len(the_contact.number)+1
                                    
                                    while True:
                                        new_number=input('{:21s}:\t'.format('Enter phone number '+str(count)))
                                        if new_number=='':
                                            error=True
                                            print('''\n
<__NO NEW PHONE NUMBER WAS ADDED TO THIS CONTACT__>\n''')
                                            time.sleep(1)
                                            break
                                        
                                        elif new_number in the_contact.number:
                                            print('\n<__{} IS ALREADY SAVED!!__>\n'.format(new_number))
                                            error=True
                                            break
                                                                                
                                        else:
                                            for contact in self.phonebook.all_contacts:
                                                if new_number in contact.number:
                                                    error=True
                                                    
                                                    prompt='''
The number you entered is already saved under {} {} {}.         
Do you want to add more numbers to this new contact:
        
1. YES
2. NO
        
>\t'''.format(contact.title.upper(), contact.name.upper(), contact.surname.upper())
        
                                                    while True:
                                                        choice=input(prompt)
                                                        if choice=='1':
                                                            break
                                                        
                                                        elif choice=='2':
                                                            print('''\n\n
<__NO NEW NUMBERS WERE ADDED TO THIS CONTACT!!__>\n''')
                                                            break
                                                        else:
                                                            prompt='Enter a valid option, 1 or 2:\n\n>\t'
                                                     
                                                    if choice:
                                                        break
                                                        
                                                else:
                                                    error=False
                                                    
                                            if choice=='2' and error:
                                                break
                                                    
                                            elif not error:                             
                                                self.phonebook.add_to_existing(text, value, new_number)
                                                print('\n<__Your contact has been updated successfully!!__>\n'.upper())
                                                time.sleep(1)
                                                break    
                                        
                                elif action=='2':
                                    print('\n<__The following numbers have already been saved:__>\n'.upper())
                                    
                                    for i in the_contact.number:
                                        print('>   {}'.format(i))
                                    print('''\n
<__ENTER THE NEW MODIFIED PHONE NUMBER BELOW FOR EACH OF THE ABOVE PHONE NUMBERS!!__>
               (Press enter if you do not want to edit the old number)\n''')
                                    
                                    time.sleep(2)
                                    numbers=[]
                                    print('\n    {:10s} | {:10s}'.format('OLD NUMBER', 'NEW NUMBER'))
                                    print('   ', '_'*23)
                                    
                                    for i in range(len(the_contact.number)):
                                        old_number=the_contact.number[i]
                                        number=input('>\t{:10s} | '.format(old_number))
                                        
                                        if number=='':
                                            numbers.append(old_number)
                                            error=True
                                        
                                        elif number in the_contact.number:
                                            if number in numbers:
                                                print('''\n
<__{} has already been entered.
   The Phone Number {} will remain unchanged!!__>'''.format(number, old_number))
                                                numbers.append(old_number)
                                                continue
                                            
                                            else:
                                                error=False
                                                             
                                        else:
                                            for contact in self.phonebook.all_contacts:
                                                if number in contact.number:
                                                    error=True
                                                    print('''\n
<__The number you entered is already saved under {} {} {}
   The Phone Number {} will remain uchanged!!__>
'''.format(contact.title.upper(), contact.name.upper(), contact.surname.upper(), old_number))
                                                    numbers.append(old_number)
                                                    time.sleep(1)
                                                    break
                                            
                                                else:
                                                    error=False
                                        
                                        if not error:
                                            numbers.append(number)
                                            
                                    numbers=list(set(numbers))        
                                    self.phonebook.modify_number(text, value, numbers)
                                    print('\n\n<__Your contact has been updated successfully!!__>\n'.upper())
                                    
                                elif action=='3':
                                    if len(the_contact.number)==1:
                                        print('''\n
<__THIS OPTION ONLY APPLIES TO CONTACTS WITH MORE THAN ONE PHONE NUMBER ADDED TO THEM!!__>
          (To delete this contact, return to Phonebook Menu and select the 
                          'Delete a contact' option)''')
                                        time.sleep(3)
                                        break
                                        
                                    else:                                    
                                        print('\n<__The following numbers have already been saved:__>\n'.upper())
                                        
                                        for i in range(len(the_contact.number)):
                                            print('{}.  {}'.format(i+1, the_contact.number[i]))
                                        time.sleep(1)
                                        
                                        valid_choices=[]
                                        for i in range(0, len(the_contact.number)):
                                            valid_choices.append(str(i+1))
                                                
                                        while True:
                                            to_delete=input('''\n
Enter the number corresponding to the number you want to delete:
        
>\t''')
                                            if to_delete not in valid_choices:
                                                print('\n<__Enter a valid option!!__>\n'.upper())
                                                
                                            else:
                                                break
                                        
                                        while True:                                        
                                            confirm=input('''\n
Are you sure you want to delete {} from {} {} {}'s contact details?
    
1. YES
2. NO
    
>\t'''.format(the_contact.number[int(to_delete)-1], the_contact.title.upper(), the_contact.name.upper(), the_contact.surname.upper()))
                                            
                                            if confirm=='1':
                                                print('\n<__{} WAS SUCCESSFULLY ERASED!!__>\n'.format(the_contact.number[int(to_delete)-1]))
                                                del the_contact.number[int(to_delete)-1]
                                                time.sleep(1)
                                                break
                                                
                                            elif confirm=='2':
                                                break
                                            
                                            else:
                                                print('\n<__Enter a valid option!!__>\n'.upper())
                                    
                                if action in ['1', '2', '3']:
                                    break
                                
                                else:
                                    print('\n<__Enter a valid option!!__>\n'.upper())
                            
                        elif choice=='5':
                            email=input('Type in the new email address:\n\n>\t')
                            
                            if not email:
                                new_email=False
                                print('\n<__The email address was not changed!!__>'.upper())
                                time.sleep(1)
                            
                            elif email==the_contact.email:
                                new_email=False
                                print('\n<__The email address was successfully changed!!__>\n'.upper())
                                time.sleep(1)
                                
                            else:
                                new_email=True
                                
                                for i in self.phonebook.all_contacts:
                                    if email==i.email:
                                        new_email=False
                                        print('''\n
The email you entered is already saved under {} {} {}'''.format(i.title.upper(), i.name.upper(), i.surname.upper()))
                                        print('\n<__The email address was not changed!!__>'.upper())
                                        print('\n')
                                        time.sleep(1)
                            
                            if new_email:           
                                self.phonebook.modify_email(text, value, email)
                                print('\n<__The email address was successfully changed!!__>\n'.upper())
                            
                        elif choice=='6':
                            address=input('Type in the new home address:\n\n>\t')
                            
                            if address:
                                self.phonebook.modify_address(text, value, address)
                                print('\n<__The address was successfully changed!!__>'.upper())
                                
                            else:
                                print('\n<__The home address was not changed!!__>'.upper())
                                time.sleep(1)
                            
                        if choice in valid_options:
                            break
                        
                        else:
                            print('\n<__Enter a valid option!!__>\n'.upper())
                            
                    if choice=='7':
                        break
        
    def erase_a_contact(self):
        '''This is for deleting a contact from the phonebook as specified by the
        use'''
        
        if len(self.phonebook.all_contacts)==0:
            print('\n<__There are no contacts in your phonebook!!__>'.upper())
            return        
        
        prompt='''
Select the required option:

1. Erase all contacts
2. Erase one contact

>\t'''
        while True:
            
            num=input(prompt)
            if num=='1':
                while True:
                    choice=input('''
Are you sure you want to erase all contacts from your phonebook:

1. YES
2. NO

>\t''')
                    if choice=='1':
                        self.phonebook.delete_all_contacts()
                        print('\n<__ALL CONTACTS HAVE BEEN DELETED!!__>')
                        break 
                       
                    elif choice=='2':
                        break
                    
                    else:
                        print('\n<__Enter a valid option!!__>\n'.upper())
                
                if choice in ['1', '2']:
                    break
                            
            elif num=='2':
                contacts, text, value=self._find_particular_contacts()
                
                if len(contacts)>0:
                    title=self.phonebook.particular_contact(text, value).title
                    name=self.phonebook.particular_contact(text, value).name
                    surname=self.phonebook.particular_contact(text, value).surname
                    
                    while True:
                        choice=input('''\n
Are you sure you want to erase {} {} {} from your phonebook:
    
1. YES
2. NO

>\t'''.format(title.upper(), name.upper(), surname.upper()))
                        if choice=='1':
                            self.phonebook.delete_contact(text, value)
                            break
                        
                        elif choice=='2':
                            break
                        
                        else:
                            print('\n<__Enter a valid option!!__>\n'.upper())
                break
            
            else:
                prompt='Enter a valid option, 1 or 2:\n\n>\t'
               
    def _add_to_groups(self):
        '''This is for adding a contact to any of the three groups, that is,
        family, favorites or blacklist'''
        
        contacts, text, value=self._find_particular_contacts()
        time.sleep(1)
        
        if len(contacts)>0:
            title=self.phonebook.particular_contact(text, value).title
            name=self.phonebook.particular_contact(text, value).name
            surname=self.phonebook.particular_contact(text, value).surname
            the_contact= self.phonebook.particular_contact(text, value)
            
            while True:
                group=input('''
Select the option corresponding to the required group:
        
1. Favorite contacts
2. Family contacts
3. Blacklisted contacts

>\t''')
           
                if group=='1':
                    if the_contact in self.phonebook.favorite_contacts:
                        print('''\n
<__{} {} {} is already in favorites!!__>'''.format(title.upper(), name.upper(), surname.upper()))
                        time.sleep(1)
                        
                    else:
                        self.phonebook.add_favorite_contact(text, value)
                        print('''\n
<__{} {} {} was successfully added to favorites!!__>'''.format(title.upper(), name.upper(), surname.upper()))
                        time.sleep(1)    
                    break
                    
                elif group=='2':
                    if the_contact in self.phonebook.family_contacts:
                        print('''
<__{} {} {} is already in family contacts!!__>'''.format(title.upper(), name.upper(), surname.upper()))
                        time.sleep(1)
                        
                    else:
                        self.phonebook.add_family_contact(text, value)
                        print('''\n
<__{} {} {} was successfully added to family contacts!!__>'''.format(title.upper(), name.upper(), surname.upper()))
                        time.sleep(1)
                    break
                
                elif group=='3':
                    if the_contact in self.phonebook.blacklisted_contacts:
                        print('''\n
<__{} {} {} is already blacklisted!!__>'''.format(title.upper(), name.upper(), surname.upper()))
                        time.sleep(1)
                        
                    else:
                        self.phonebook.add_blacklist_contact(text, value)
                        print('''\n
<__{} {} {} was successfully blacklisted!!__>'''.format(title.upper(), name.upper(), surname.upper()))       
                        time.sleep(1)
                    break
                
                else:
                    print('\n<__Enter a valid option!!__>\n'.upper())
                    time.sleep(1)
                    
    def _remove_from_groups(self):
        '''This is for removing a contact from a particular group if it exists in 
        any one of the three groups'''
        
        contacts, text, value=self._find_particular_contacts()
        time.sleep(1)
        
        if len(contacts)>0:
            title=self.phonebook.particular_contact(text, value).title
            name=self.phonebook.particular_contact(text, value).name
            surname=self.phonebook.particular_contact(text, value).surname
            the_contact= self.phonebook.particular_contact(text, value)
            
            while True:
                group=input('''
Select the option corresponding to the required group:
    
1. Favorite contacts
2. Family contacts
3. Blacklisted contacts

>\t''')      
            
                if group=='1':
                    if the_contact not in self.phonebook.favorite_contacts:
                        print('''\n
<__{} {} {} is not in favorites!!__>'''.format(title.upper(), name.upper(), surname.upper()))
                        time.sleep(1)
                    
                    else:
                        self.phonebook.remove_favorite(text, value)
                        print('''\n
<__{} {} {} was successfully romoved from favorites!!__>'''.format(title.upper(), name.upper(), surname.upper()))
                        time.sleep(1)
                        
                    break
                    
                elif group=='2':
                    if the_contact not in self.phonebook.family_contacts:
                        print('''
<__{} {} {} is not in family contacts!!__>'''.format(title.upper(), name.upper(), surname.upper()))
                        time.sleep(1)
                    
                    else:
                        print("surprise!")
                        self.phonebook.remove_family(text, value)
                        print('''\n
<__{} {} {} was successfully removed from family contacts!!__>'''.format(title.upper(), name.upper(), surname.upper()))
                        time.sleep(1)
                        
                    break
                
                elif group=='3':
                    if the_contact not in self.phonebook.blacklisted_contacts:
                        print('''\n
<__{} {} {} is not blacklisted!!__>'''.format(title.upper(), name.upper(), surname.upper()))
                        time.sleep(1)
                        
                    else:
                        self.phonebook.remove_blacklist(text, value)
                        print('''\n
<__{} {} {} was successfully removed from blacklist!!__>'''.format(title.upper(), name.upper(), surname.upper()))       
                        time.sleep(1)
                    break
                
                else:
                    print('\n<__Enter a valid option!!__>\n'.upper())
                    time.sleep(1)
                
    def modify_groups(self):
        '''This is used to add or remove contacts from any of the three groups,
        that is family, favorites and blacklist'''
        
        if len(self.phonebook.all_contacts)==0:
            print('\n<__There are no contacts in your phonebook groups!!__>'.upper())
            
        else:
            while True:
                while True:
                    option=input('''
Select the option corresponding to the required action:
    
1. Add contacts to groups
2. Remove contacts from groups
3. Phonebook menu

>\t''')
                    
                    if option=='1':
                        self._add_to_groups()
                        break
                    
                    elif option=='2':
                        self._remove_from_groups()
                        break
                    
                    elif option=='3':
                        break
                    
                    else:
                        print('\n<__Enter a valid option!!__>\n'.upper())
                        time.sleep(1)
                
                if option=='3':
                    break
        
    def quit_use(self):
        '''This is used to exit the phonebook'''
        
        prompt='''\n
Leave Phonebook?

<__ALL YOUR CONTACTS WILL BE ERASED!!__>
    
1. EXIT
2. NOPE

>\t'''
        while True:
            option=input(prompt)
            
            if option=='1':
                print('\n<<__EXITING__>>\n')
                for i in range(75):
                    print('.', end='')
                    time.sleep(3/75)
                print('\n')
                sys.exit(0)
            
            elif option=='2':
                break
            
            else:
                 prompt='Enter a valid option, 1 or 2:\n\n>\t'
                 
                 
        
if __name__=='__main__':
    PhonebookMenu().run()
    
