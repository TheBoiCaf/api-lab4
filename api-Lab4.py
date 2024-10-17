#calling in request to use api
import requests as rq
import sys
import json
from collections import defaultdict

# api_url = 'https://dattebayo-api.onrender.com/characters'
# response = rq.get(api_url)
# response.raise_for_status()  # raises exception when not a 2xx response
# if response.status_code != 204:
#    response.json()
# if (
#     response.status_code != 204 and
#     response.headers["content-type"].strip().startswith("application/json")
# ):
#     try:
#         response.json()
#     except ValueError:
#       print("Womp")
#         # decide how to handle a server that's misbehaving to this extent



#class APIHandler:
BASE_URL = 'https://dattebayo-api.onrender.com'
def GetCharacter(searchCharacter):

    response = rq.get(f"{BASE_URL}/characters?name={searchCharacter}")

    return response.json()
#     #this should have the link to api
#     #a method for getting characters
#     #a method for searching for character
#     #a method for filter characters by epidsode and name
    # BASE_URL = 'https://gravity-falls-api.vercel.app/api/'
  #take measn im taking 5 at a time, and skip mean im skiping the 0 character starting with first character
    # def get_characters(self):
    #  response = rq.get(f"{self.BASE_URL}/characters")
    #  return response.json() if response.status_code == 200 else None
#  def search_Characters(): 
#     print('')
#  def filter_Characters():
#     print('')

# class Favorites:
#     print('something here')
    #this should have an array to hold the favorite characters or dictionary wtv works
    #a add to favorite method
    #a remove favorite method
    #a show list of favoite 

def CharacterSearch(): 

    newCharacter = input('Enter the name of the character you want to search: ')
    returnedCharacters = GetCharacter(newCharacter)
    filteredCharacters = []
    for char in returnedCharacters["characters"]:
        try:
            newData = defaultdict(lambda: 'Not Available', {
            "name": char["name"],
            "debut": char["debut"],
            "personal": char["personal"]
            })
            filteredCharacters.append(newData)
        except KeyError:
            newData = defaultdict(lambda: 'Not Available', {
            "name": char["name"],
            "personal": char["personal"]
            })


    # counter = 0
    # for c in filteredCharacters:
    #     print(f"{counter + 1}. {c["name"]}\n")
    #     counter += 1


    # answer = int(input("choose the number of which charcater you want more info on: "))
    # pickedCharacter = []
    # pickedCharacter.append(filteredCharacters[answer-1])
    # characterInfo = []

    # for picked in pickedCharacter["personaln"]:
    #     personalData = {
    #         "clan": picked["clan"]
    #     }
    #     characterInfo.append(personalData)
    
    for idx, c in enumerate(filteredCharacters):
        print(f"{idx + 1}. {c['name']}\n")

    answer = int(input("Choose the number of the character you want more info on: "))
    
    # Access the selected character
    pickedCharacter = filteredCharacters[answer - 1]
    
    # Extract the "personal" data
    characterInfo = {
        "clan": pickedCharacter["personal"].get("clan"), 
        "anime": pickedCharacter["debut"].get("anime"),
        "manga": pickedCharacter["debut"].get("anime")
    }

    
    print(f"Name: {pickedCharacter["name"]}")
    print(f"Clan: {characterInfo["clan"]}")
    print(f"Anime: {characterInfo["anime"]}")
    print(f"Manga: {characterInfo["manga"]}")
    

    
    # for key in characters:{
    #     print(key,":", characters[key])
    # }
    # print(characters)

def tailBeast():
    newTailedBeast = input('Enter the name of the character you want to search: ')
    returnedTailedBeast = GetCharacter(newTailedBeast)
    filteredTailedBeast = []
    for char in returnedTailedBeast["characters"]:
        try:
            newData = defaultdict(lambda: 'Not Available', {
            "name": char["name"],
            "debut": char["debut"],
            "personal": char["personal"],
            "uniqueTraits": char["uniqueTraits"]
            })
            filteredTailedBeast.append(newData)
        except KeyError:
            newData = defaultdict(lambda: 'Not Available', {
            "name": char["name"],
            "personal": char["personal"]
            })
    
    for idx, c in enumerate(filteredTailedBeast):
        print(f"{idx + 1}. {c['name']}\n")

    answer = int(input("Choose the number of the character you want more info on: "))

    pickedTailedBeast = filteredTailedBeast[answer - 1]
    
    # Extract the "personal" data
    BeastInfo = {
        "jinchūriki": pickedTailedBeast["personal"].get("jinchūriki"), 
        "anime": pickedTailedBeast["debut"].get("anime"),
        "manga": pickedTailedBeast["debut"].get("anime"),
        
    }

    
    print(f"Name: {pickedTailedBeast["name"]}")
    print(f"Anime: {BeastInfo["anime"]}")
    print(f"Manga: {BeastInfo["manga"]}")
    print(f"uniqueTraits: {pickedTailedBeast["uniqueTraits"]}")


def main():
    tailBeast()
    CharacterSearch()

if __name__ == "__main__":
    main()
    # call on the class something like self.api_Handler = APIHandler
    #a while loop with an option list
    #if option chosen then run the methods that will be made in the main class to connect to the other classes
    #need a search character to connect to the method in APIHandler printing out the character user searched for
    # after searching and finding a character ask if they wwant to add to favorite if yes then add using add_favorite method in Favorites
    #a browse character method just for the user to look throught the characters we have
    #a filter by name and ep method to connect to method in APIHandler
    # a view_favorite method connect to list favorite methid in Favorites
    #after listing as if they want to remove a favorite using the remove_favorite method in Favorites
    