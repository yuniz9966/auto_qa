import requests

base_url = 'http://5.101.50.27:8000'

# def test_simple_req():
#  resp = requests.get('http://5.101.50.27:8000/company/list')
#
#  response_body = resp.json() # Преобразуем ответ в JSON
#  first_company = response_body[0] # Получаем первую компанию из списка
#
#  assert first_company["name"] == "QA Студия 'ТестировщикЪ'"
#  assert resp.status_code == 200
#  assert resp.headers["Content-Type"] == "application/json"
#
#  print(response_body)


def test_simple_req():
  resp = requests.get(f'{base_url}/company/list')
  assert resp.status_code == 200
  response_body = resp.json() # Преобразуем ответ в JSON

  for i in response_body:
    print(i)


# import requests
#
# base_url = 'http://5.101.50.27:8000/company/create'
#
# def test_created_co_status_201():
#     new = {
#   "name": "the sun",
#   "description": "make erth great again"
# }
#     response = requests.post(base_url, json=new)
#     assert response.status_code == 201


# import requests
#
# base_url = 'http://5.101.50.27:8000'
#
# def test_company_count():
#     company_list = requests.get(base_url + "/company/list")
#     before_count = len(company_list.json())
#
#     new_company = {
#     "name": "Test Company",
#     "description": "Automated test creation"
#     }
#
#     response_create = requests.post(base_url + "/company/create", json=new_company)
#     company_list = requests.get(base_url + "/company/list")
#     after_count= len(company_list.json())
#
#     assert after_count == before_count + 1

