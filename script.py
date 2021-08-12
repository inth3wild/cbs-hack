import requests
import json



headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.io)"
}


# categories = [
#     "fashionablemale", 
#     "nextgenmale", 
#     "entrepreneurmale", 
#     "facemale", 
#     "sociablemale",
#     "sportspersonmale",
#     "innovativemale",

#     "fashionablefemale",
#     "nextgenfemale", 
#     "entrepreneurfemale", 
#     "facefemale", 
#     "sociablefemale",
#     "sportspersonfemale",
#     "innovativefemale"
# ]

categories = ["facemale", "facefemale"]

db = []
list_of_contestants = []

def run(categories):
    for category in categories:
        reqUrl = f"http://cbsvote.lmu.edu.ng/api/category/{category}"
        response = requests.request("GET", reqUrl, headers=headersList)
        response = response.json()

        for i in response:
            # list_of_contestants = []

            id = i.get("_id").get("$oid")
            name = i["name"]
            votes = i.get("category")[0].get("votes")
            department =  i["department"]
            constestant =  { "name": name, "votes": votes, "department": department, "id":id }
            list_of_contestants.append(constestant)

            # db[category] = 1
            category_dict = {category:list_of_contestants}
    db.append(category_dict)




run(categories)

print(db)