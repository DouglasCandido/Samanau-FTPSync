import json

file = open('filetest.txt','r')

for line in file:
	a = line
	
	
	class Object:
		def to_JSON(self):
			line = a.replace('\n', ',')
			words = line.split(',')
			for	word in words:
				initializer.data_e_hora = words[0]
				initializer.bateria = words[1]
				initializer.checksum = words[2]
				initializer.latg = words[3]
				initializer.latm = words[4]
				initializer.latp = words[5]
				initializer.lats = words[6]
				initializer.long = words[7]
				initializer.lonm = words[8]
				initializer.lonp = words[9]
				initializer.lons = words[10]
				initializer.temp_int = words[11]
			return json.dumps(self,default=lambda o:o.__dict__,sort_keys=True,indent=4)
	initializer = Object()
	dados = initializer.to_JSON()
	arquivo=open('dados.txt', 'a+')
	arquivo.write(dados+"\n")
	arquivo.close()
	print("\n"+"Os valores formatados para JSON à seguir serão gravados no arquivo dados.txt:"+"\n")
	print(initializer.to_JSON())
file.close()
print('\n'+'\n'+"Tarefas de odificação concluídas. Arquivo dados.txt salvo!"+'\n'+'\n')