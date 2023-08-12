import requests
import json


Vcncy = []

def GetVacancy(Params):
	Url = 'https://api.hh.ru/vacancies'
	Headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0', 'accept': '*/*'}



	Resp = requests.get(Url, headers = Headers, params = Params)
	Data = Resp.content.decode('utf-8')
	Resp.close()

	jsObj = json.loads(Data)['items']
	for v in jsObj:
		Vcncy.append('Вакансия: '+ v['name'])
		#Vcncy.append('Работодатель: '+ v['employer']['name'])
		Vcncy.append('Требования: '+ v['snippet']['requirement'])
		#Vcncy.append('Зп от: '+ str(v['salary']['from']))
		Vcncy.append('Url: '+ v['alternate_url'])


	#with open('js1.json', 'w') as js:
	#	json.dump(Vcncy, js, ensure_ascii=False, indent=1)

	return Vcncy
