import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "Secret"
TOKEN = "Secret"
GRAPHID = "graph1"

headers = {
    "X-USER-TOKEN":TOKEN,
}
pixela_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

#Creating a pixel account
# response = requests.post(url=pixela_endpoint, json=pixela_params)
# print(response.text)

graph_config = {
    "id":GRAPHID,
    "name":"Coding Time Tracker",
    "unit":"Hours",
    "type":"float",
    "color":"ajisai",
    "timezone":"US/Central",
}

#Creating a pixela graph
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# time_quantity = str(input("How much coding did you study today: "))
todays_date = datetime.now().strftime("%Y%m%d")
print(todays_date)
# pixel_config = {
#     "date":todays_date,
#     "quantity":time_quantity,
# }

#Adding data to the pixela
# pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

yesterdays_date = str(int(todays_date) - 1)
update_quantity = input("What should the amount be changed to: ")
put_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{yesterdays_date}"
put_config = {
    "quantity":update_quantity
}

#Updating a pixela date
# response = requests.put(url=put_pixel_endpoint, headers=headers, json=put_config)
# print(response.text)

#Deleting a pixela date data
response = requests.delete(url=put_pixel_endpoint, headers=headers)
print(response.text)