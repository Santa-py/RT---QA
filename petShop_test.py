import requests
import pytest
import petShop

# Тест для получения информации о питомце по ID (GET /pet/{petId}) 
def test_getPetById():
    responce = requests.get(f"https://petstore.swagger.io/v2/pet/{petShop.pet_id}")

    assert responce.status_code == 200
    assert responce.json()["id"] == petShop.pet_id
    assert responce.json()["name"] == petShop.pet_name
    assert responce.json()["status"] == petShop.pet_status


# Тест для обновления информации о существующем питомце (PUT /pet) 
def test_renamePet():
    pet_changed_data = {
        "id": 180720251400,
        "name": "pisec_okonchatelnniy",
        "status": "game_over"
    }

    responce = requests.put("https://petstore.swagger.io/v2/pet", 
                            json = pet_changed_data)
    
    assert responce.json()["id"] == pet_changed_data["id"]
    assert responce.json()["name"] == pet_changed_data["name"]
    assert responce.json()["status"] == pet_changed_data["status"]


# Тест для удаления питомца (DELETE /pet/{petId}) 
def test_deletePet():
    responce = requests.delete(f"https://petstore.swagger.io/v2/pet/{petShop.pet_id}")

    assert responce.status_code == 200
    assert responce.json()["type"] == "unknown"
    assert responce.json()["message"] == f"{petShop.pet_id}"


# Вызов функции для создания питомца 
petShop.createPet()