import requests

pet_id = 180720251400
pet_name = "pisec_obiknovenniy"
pet_status = "last_chance"

# Функция для создания нового питомца (POST /pet) 
def createPet():
    pet_data = {
        "id": pet_id,
        "name": pet_name,
        "status": pet_status
    }

    responce = requests.post("https://petstore.swagger.io/v2/pet", 
                             json = pet_data)