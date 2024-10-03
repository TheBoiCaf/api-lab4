#calling in request to use api
import requests as rq

class APIHandler:
    #this should have the link to api
    #a method for getting characters
    #a method for searching for character
    #a method for filter characters by epidsode and name
 BASE_URL = 'https://gravity-falls-api.vercel.app/api'
 #take measn im taking 5 at a time, and skip mean im skiping the 0 character starting with first character
 def get_characters(self, take=5, skip=0):
    print('')

class Favorites:
    print('something here')
    #this should have an array to hold the favorite characters or dictionary wtv works
    #a add to favorite method
    #a remove favorite method
    #a show list of favoite method

class mainApp:
    print('somehting here')
    # call on the class something like self.api_Handler = APIHandler
    #a while loop with an option list
    #if option chosen then run the methods that will be made in the main class to connect to the other classes
    #need a search character to connect to the method in APIHandler printing out the character user searched for
    # after searching and finding a character ask if they wwant to add to favorite if yes then add using add_favorite method in Favorites
    #a browse character method just for the user to look throught the characters we have
    #a filter by name and ep method to connect to method in APIHandler
    # a view_favorite method connect to list favorite methid in Favorites
    #after listing as if they want to remove a favorite using the remove_favorite method in Favorites
    