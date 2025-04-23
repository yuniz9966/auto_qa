import requests

#  Получение списка всех сотрудников
# def all_user_info():
#   user_id = 1
#   base_url = "http://5.101.50.27:8000"
#
#   while True:
#     response = requests.get(f"{base_url}/employee/info/{user_id}")
#
#     if response.status_code == 200:
#       print(f"User {user_id}:", response.json())
#       user_id += 1
#     else:
#       break
#
#
# all_user_info()


# Задание 1. Создание нового сотрудника
class TestEmployeeApi:
    base_url = "http://5.101.50.27:8000"
    client_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJoYXJyeXBvdHRlciIsInJvbGUiOiJhZG1pbiIsImV4cCI6MTc0NTQzMzU5OH0.2T3kIWgZc1SFXNtwebfQgahY35ONyJS3Uo60BQb6x6w"
    def test_user_create(self):
        data_json = {
            "first_name": "Jack",
            "last_name": "Richer",
            "middle_name": "Hudson",
            "company_id": 6,
            "email": "user6@net.com",
            "phone": "+49123456789",
            "birthdate": "1993-03-06",
            "is_active": True
        }

        response = requests.post(f"{self.base_url}/employee/create", json=data_json)
        assert response.status_code == 200

# Задание 2. Получение информации о работнике
    def test_user_info(self):
        user_id = 23

        response = requests.get(f"{self.base_url}/employee/info/{user_id}")
        assert response.status_code == 200
        print(response.text)

# Задание 3. Изменение данных о работнике
    def test_user_update(self):
        data_json = {
            "first_name": "Jack",
            "last_name": "Richer",
            "email": "user6@net.com",
            "phone": "+49987654321",
        }

        response = requests.patch(f"{self.base_url}/employee/change/15/?client_token={self.client_token}", json=data_json)
        print(response.status_code)
        print(response.text)
        assert response.status_code == 200





