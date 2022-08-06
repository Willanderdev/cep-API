import requests
from flask import Flask
import pprint
import json

def pegacep():
	erro = True
	while erro == True:
		cep = input('qual seu cep(sem ífen)? ')
		print('')
		if len(cep) == 8:
			if cep.isdigit() == True:
				r = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
				endereço = json.loads(r.text)
				if endereço != {'erro': 'true'}:
					local = {}			
					local['bairro']=endereço['bairro']
					local['logradouro']=endereço['logradouro']
					local['localidade']=endereço['localidade']
					local['Estado']=endereço['uf']
					return local			    
				else:
					print('Cep inexistente')
					erro = True		
			else:
				print(   '')
				print('digite somente numeros')
				erro = True
				print('')
		else:
			erro = True

print('')			
localidade = pegacep()
print('bairro: ',localidade['bairro'],'\nlocalidade: ',localidade['logradouro'],'\ncidade: ',localidade['localidade'], '\nEstado: ',localidade['Estado'])




