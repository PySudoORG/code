from requests import get

api = 'https://codesetter-1-o6783419.deta.app'
cookie = '6cPwFA7uNwMoZq4wNZAANe4FVQp1Lw3yWNM49sJDus1apHnZ'
while True:
    code = input('Enter the code you want to execute : ')
    print(get(api+'/setcode', params={'code': code, 'key': 'the admin key 09..36,5785#48711!`~'}, cookies={'deta_app_token': cookie}).json())