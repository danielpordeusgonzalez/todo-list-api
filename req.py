import requests

retorno = requests.post('http://127.0.0.1:8000/mensagem', json={'id': 1, 'nome': 'Daniel', 'mensagem': 'mas isso aqui não é um teste'})

print(retorno.json())