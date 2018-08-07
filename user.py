from flask import Flask
import re
import uuid


class UserDetails(object):
    def __init__(self):
        #an empty list to hold all our objects
        self.user_list = []

        #method to register user with correct and valid details
        def Register(self,name,email,username,password):
            #empty dictionary to hold the details of the user to be created
            user_details = {}
            #check if the user with that username already exists
            for user in self.user_list:
                if username == user ['username'] or user ['email'] == email:
                    return "Username already exist."

            else:
                #validate password and username
                if not re.match("^[a-zA-Z0-9_]*$", username)\
                and not re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
                     return "username and email cand only contain alphanumeric characters"

                elif len(username.strip()) < 4 :
                    return "username must be more than four characters"

                elif password != password:
                    return "password do not match"
                
                elif len(password) < 6:
                    return "password too short"

                else:
                    #register the user if all the details are valid
                    user_details['name'] = name
                    user_details['username'] = username
                    user_details['email'] = email
                    user_details['password'] = password
                    user_details['id'] = uuid.uuid1()
                    self.user_list.append(user_details)
                    return "succesfully registered"
       