with open("c:/windows/temp/extip.log", "w") as outfile:
	from email.mime.text import MIMEText
	outfile.write("Imported MIMEText\n")
	from email.mime.multipart import MIMEMultipart
	outfile.write("Imported MIMEMultipart\n")
	from email.mime.base import MIMEBase
	outfile.write("Imported MIMEBase\n")
	from email import encoders
	outfile.write("Importated Encoders\n")
	import time
	outfile.write("Imported Time\n")	
	import requests
	outfile.write("Imported Requests\n")
	from bs4 import BeautifulSoup
	outfile.write("Imported BeautifulSoup\n")
	from string import whitespace
	outfile.write("Imported Whitespace\n")
	import smtplib
	outfile.write("Imported Whitespace\n")
	import math
	outfile.write("Imported Math\n")
	import json
	outfile.write("Imported JSON\n")
	url = "http://ctacinv/api/PrinterLevels?GetShortPrinters=true"
	page = requests.get(url, verify=False)
	print(page.content)
	Printers = json.loads(page.content)
	for printer in Printers:
		printerName = printer['PrinterName']
		printerIp = printer['PrinterIp']
		printerName = printerName.replace("{", "").replace("}", "").replace("'", "")
		printerIp = printerIp.replace("{", "").replace("}", "").replace("'", "")
		print(printerName + "|" + printerIp)
		url = "http://"+printerIp+"/"

		print(url)
		try:
			page = requests.get(url, verify=False)
			outfile.write("Set Page Variable\n")
			soup = BeautifulSoup(page.content, 'html.parser')
			outfile.write("Set Soup Variable\n")
			tonerArea1 = soup.find(class_="mainContentArea")
			if(tonerArea1):
				tonerTables = tonerArea1.findAll(class_="tableDataCellStand width15")
				tonerValues = tonerArea1.findAll(class_="tableDataCellStand width25 valignBottom")
				try:
					Black = tonerTables[0]
					Black = Black.getText().strip()
					Black = Black.replace('\r', '').replace('\n', '').replace("Order","").replace("?", "").replace("†","")
					Black = Black.replace('Black Cartridge', ' ').replace(' ', '')
					BlackValue = tonerValues[0].getText()
					BlackValue = BlackValue.replace('\r', '').replace('\n', '').replace(' ', '').replace("†","").replace("*","").replace("%","").replace('<', '').replace('‡','')
					if ('-' in BlackValue):
						BlackValue = '0'
					BlackToner = Black + " " + BlackValue
					print(BlackToner)
				except IndexError:
					Black= ""
					BlackValue = "" 
				try:
					Cyan = tonerTables[1]
					Cyan = Cyan.getText().strip()
					Cyan = Cyan.replace('\r', '').replace('\n', '').replace("Order","").replace("?", "").replace("†","")
					Cyan = Cyan.replace('Cyan Cartridge', ' ').replace(' ', '')
					CyanValue = tonerValues[1].getText()
					CyanValue = CyanValue.replace('\r', '').replace('\n', '').replace(' ', '').replace("†","").replace("*","").replace("%","").replace('<', '').replace('‡','')
					if('-' in CyanValue):
						CyanValue = '0'
					CyanToner = Cyan + " " + CyanValue
					print(CyanToner)
				except IndexError:
					Cyan = ""
					CyanValue = ""
				try:
					Magenta = tonerTables[2]
					Magenta = Magenta.getText().strip()
					Magenta = Magenta.replace('\r', '').replace('\n', '').replace("Order","").replace("?", "").replace("†","")
					Magenta = Magenta.replace('Magenta Cartridge', ' ').replace(' ', '')
					MagentaValue = tonerValues[2].getText()
					MagentaValue = MagentaValue.replace('\r', '').replace('\n', '').replace(' ', '').replace("†","").replace("*","").replace("%","").replace('<', '').replace('‡','')
					if('-' in MagentaValue):
						MagentaValue = '0'
					MagentaToner = Magenta + " " + MagentaValue
					print(MagentaToner)
				except IndexError:
					Magenta = ""
					MagentaValue = ""
				try:
					Yellow = tonerTables[3]
					Yellow = Yellow.getText().strip()
					Yellow = Yellow.replace('\r', '').replace('\n', '').replace("Order","").replace("?", "").replace("†","")
					Yellow = Yellow.replace('Yellow Cartridge', ' ').replace(' ', '')
					YellowValue = tonerValues[3].getText()
					YellowValue = YellowValue.replace('\r', '').replace('\n', '').replace(' ', '').replace("†","").replace("*","").replace("%","").replace('<', '').replace('‡','')
					if( '-' in YellowValue):
						YellowValue = '0'
					YellowToner = Yellow + " " + YellowValue
					print(YellowToner)
				except IndexError:
					Yellow = ""
					YellowValue = ""
				url = "http://ctacinv/api/PrinterLevels?PythonScript=true"
				data = {
					"PrinterName": printerName,
					"PrinterIP": printerIp,
					"BlackModel": Black,
					"BlackLevel": BlackValue,
					"CyanModel": Cyan,
					"CyanLevel": CyanValue,
					"MagentaModel": Magenta,
					"MagentaLevel": MagentaValue,
					"YellowModel": Yellow,
					"YellowLevel": YellowValue,
					}
				upload = requests.post(url, verify=False, json=data)
				print(upload.status_code)
				del Black
				del BlackValue
				del Cyan
				del CyanValue
				del Magenta
				del MagentaValue
				del Yellow
				del YellowValue
			tonerArea2 = soup.find(id="DeviceStatusSuppliesSectionId")
			if(tonerArea2):
				for i in range(5):
					position = str(i)
					TonerName = tonerArea2.find(id="SupplyName"+position)
					TonerLevel = tonerArea2.find(id="SupplyPLR"+position)
					TonerModel = tonerArea2.find(id="SupplyPartNumber"+position)
					if(TonerLevel):
						TonerLevel = TonerLevel.getText().strip()
						TonerName = TonerName.getText().strip()
						TonerModel = TonerModel.getText().strip()
						print(TonerLevel + " " + TonerName + " " + TonerModel)
					else:
						break
					if("Black" in TonerName):
						print("BLACK!")
						BlackModel = TonerModel.replace("Order","").replace("?", "").replace("†","").replace("*","").replace("%","")
						BlackLevel = TonerLevel.replace("†","").replace("*","").replace("%","").replace('<', '').replace('‡','')
						if('-' in BlackLevel):
							BlackLevel = '0'
					if("cyan" in TonerName):
						print("CYAN!")
						CyanModel = TonerModel.replace("Order","").replace("?", "").replace("†","")
						CyanLevel = TonerLevel.replace("†","").replace("*","").replace("%","").replace('<', '').replace('‡','')
						if('-' in CyanLevel):
							CyanLevel = '0'
					if("Magenta" in TonerName):
						print("MAGENTA!")
						MagentaModel = TonerModel.replace("Order","").replace("?", "").replace("†","")
						MagentaLevel = TonerLevel.replace("†","").replace("*","").replace("%","").replace('<', '').replace('‡','')
						if('-' in MagentaLevel):
							MagentaLevel = '0'
					if("Yellow" in TonerName):
						print("YELLOW!")
						YellowModel = TonerModel.replace("Order","").replace("?", "").replace("†","")
						YellowLevel = TonerLevel.replace("†","").replace("*","").replace("%","").replace('<', '').replace('‡','')
						if('-' in YellowLevel):
							YellowLevel = '0'
					if("Maint" in TonerName):
						print("MAINTINENCE!")
						MaintinenceModel = TonerModel.replace("Order","").replace("?", "").replace("†","")
						MaintinenceLevel = TonerLevel.replace("†","").replace("*","").replace("%","").replace('<', '').replace('‡','')
						if('-' in MaintinenceLevel):
							MaintinenceLevel = '0'
				try: 
					BlackModel
				except NameError:
					BlackModel = ""
					BlackLevel = ""
				try:
					CyanModel
				except NameError:
					CyanModel = ""
					CyanLevel = ""
				try:
					MagentaModel
				except NameError:
					MagentaModel = ""
					MagentaLevel = ""
				try:
					YellowModel
				except NameError:
					YellowModel = ""
					YellowLevel = ""
				try:
					MaintinenceModel
				except NameError:
					MaintinenceModel = ""
					MaintinenceLevel = ""
				url = "http://ctacinv/api/PrinterLevels?PythonScript=true"
				data = {
					"PrinterName": printerName,
					"PrinterIP": printerIp,
					"BlackModel": BlackModel,
					"BlackLevel": BlackLevel,
					"CyanModel": CyanModel,
					"CyanLevel": CyanLevel,
					"MagentaModel": MagentaModel,
					"MagentaLevel": MagentaLevel,
					"YellowModel": YellowModel,
					"YellowLevel": YellowLevel,
					"MaintinenceModel": MaintinenceModel,
					"MaintinenceLevel": MaintinenceLevel
					}
				upload = requests.post(url, verify=False, json=data)
				print(upload.status_code)
				del BlackModel
				del BlackLevel
				del CyanModel
				del CyanLevel
				del MagentaModel
				del MagentaLevel
				del YellowModel
				del YellowLevel
				del MaintinenceModel
				del MaintinenceLevel
			tonerArea5 = soup.find(id="deviceStatusPage")
			if(tonerArea5):
				try:
					for i in range(5):
						position = str(i)
						TonerSections = tonerArea5.findAll(class_="hpConsumableBlockHeaderText")
						if(TonerSections):
							TonerSections = TonerSections[i].getText().split("<br>")
							TonerSections = TonerSections[0].strip()
							TonerName = TonerSections.split("%")
							TonerModel = TonerName[1]
							TonerName = TonerName[0]
							print(TonerModel+"|"+TonerName)
						else:
							break
						if("Black" in TonerName):
							print("BLACK!")
							BlackModel = TonerModel.replace('\r', '').replace('\n', '').replace("Order","").replace("?", "").replace("†","")
							TonerLevel = TonerName.replace("Black Cartridge", "").replace('\r', '').replace('\n', '').replace("Order","").replace("?", "").replace("†","").strip()
							BlackLevel = TonerLevel.replace("†","").replace("*","").replace("%","").replace('<', '').replace('‡','')
							if('-' in BlackLevel):
								BlackLevel = '0'
						if("cyan" in TonerName):
							print("CYAN!")
							CyanModel = TonerModel.replace('\r', '').replace('\n', '').replace("Order","").replace("?", "").replace("†","")
							TonerLevel = TonerName.replace("Cyan Cartridge", "").replace('\r', '').replace('\n', '').replace("Order","").replace("?", "").replace("†","").strip()
							CyanLevel = TonerLevel.replace("†","").replace("*","").replace("%","").replace('<', '').replace('‡','')
							if('-' in CyanLevel):
								CyanLevel = '0'
						if("Magenta" in TonerName):
							print("MAGENTA!")
							MagentaModel = TonerModel.replace('\r', '').replace('\n', '').replace("Order","").replace("?", "").replace("†","")
							TonerLevel = TonerName.replace("Magenta Cartridge", "").replace('\r', '').replace('\n', '').replace("Order","").replace("?", "").replace("†","").strip()
							MagentaLevel = TonerLevel.replace("†","").replace("*","").replace("%","").replace('<', '').replace('‡','')
							if('-' in MagentaLevel):
								MagentaLevel = '0'
						if("Yellow" in TonerName):
							print("YELLOW!")
							YellowModel = TonerModel.replace('\r', '').replace('\n', '').replace("Order","").replace("?", "").replace("†","")
							TonerLevel = TonerName.replace("Yellow Cartridge", "").replace('\r', '').replace('\n', '').replace("Order","").replace("?", "").replace("†","").strip()
							YellowLevel = TonerLevel.replace("†","").replace("*","").replace("%","").replace('<', '').replace('‡','')
							if('-' in YellowLevel):
								YellowLevel = '0'
						if("Maint" in TonerName):
							print("MAINTINENCE!")
							MaintinenceModel = TonerModel.replace('\r', '').replace('\n', '').replace("Order","").replace("?", "").replace("†","")
							TonerLevel = TonerName.replace("Maintenance Kit", "").replace('\r', '').replace('\n', '').replace("Order","").replace("?", "").replace("†","").strip()
							MaintinenceLevel = TonerLevel.replace("†","").replace("*","").replace("%","").replace('<', '').replace('‡','')
							if('-' in MaintinenceLevel):
								MaintinenceLevel = '0'
				except IndexError:
					print("IndexComplete")
				try: 
					BlackModel
					print(BlackModel)
					print(BlackLevel)
				except NameError:
					BlackModel = ""
					BlackLevel = ""
					print(BlackModel)
					print(BlackLevel)
				try:
					CyanModel
					print(CyanModel)
					print(CyanLevel)
				except NameError:
					CyanModel = ""
					CyanLevel = ""
					print(CyanModel)
					print(CyanLevel)
				try:
					MagentaModel
					print(MagentaModel)
					print(MagentaLevel)
				except NameError:
					MagentaModel = ""
					MagentaLevel = ""
					print(MagentaModel)
					print(MagentaLevel)
				try:
					YellowModel
					print(YellowModel)
					print(YellowLevel)
				except NameError:
					YellowModel = ""
					YellowLevel = ""
					print(YellowModel)
					print(YellowLevel)
				try:
					MaintinenceModel
					print(MaintinenceModel)
					print(MaintinenceLevel)
				except NameError:
					MaintinenceModel = ""
					MaintinenceLevel = ""
					print(MaintinenceModel)
					print(MaintinenceLevel)
				url = "http://ctacinv/api/PrinterLevels?PythonScript=true"
				data = {
					"PrinterName": printerName,
					"PrinterIP": printerIp,
					"BlackModel": BlackModel,
					"BlackLevel": BlackLevel,
					"CyanModel": CyanModel,
					"CyanLevel": CyanLevel,
					"MagentaModel": MagentaModel,
					"MagentaLevel": MagentaLevel,
					"YellowModel": YellowModel,
					"YellowLevel": YellowLevel,
					"MaintinenceModel": MaintinenceModel,
					"MaintinenceLevel": MaintinenceLevel
					}
				upload = requests.post(url, verify=False, json=data)
				print(upload.status_code)
				del BlackModel
				del BlackLevel
				del CyanModel
				del CyanLevel
				del MagentaModel
				del MagentaLevel
				del YellowModel
				del YellowLevel
				del MaintinenceModel
				del MaintinenceLevel
			tonerArea3 = soup.find(class_="mainContentArea width100")
			if(tonerArea3):
				tonerTables = tonerArea3.findAll(class_="width100")
				tonerValues = tonerArea3.findAll(class_="alignRight valignTop")
				try:
					Black = tonerTables[2].find('td')
					Black = Black.getText().strip()
					Black = Black.replace('\r', '').replace('\n', '').replace("Order","").replace("?", "").replace("†","")
					Black = Black.replace('Black Cartridge', ' ').replace(' ', '')
					BlackValue = tonerValues[0].getText()
					BlackValue = BlackValue.replace('\r', '').replace('\n', '').replace(' ', '').replace("†","").replace("*","").replace("%","").replace('<', '').replace('‡','')
					if('-' in BlackValue):
						BlackValue = '0'
					BlackToner = Black + " " + BlackValue
					print(BlackToner)
				except IndexError:
					Black= ""
					BlackValue = ""
				try:
					Cyan = tonerTables[6].find('td')
					Cyan = Cyan.getText().strip()
					Cyan = Cyan.replace('\r', '').replace('\n', '').replace("Order","").replace("?", "").replace("†","")
					Cyan = Cyan.replace('Cyan Cartridge', ' ').replace(' ', '')
					CyanValue = tonerValues[1].getText()
					CyanValue = CyanValue.replace('\r', '').replace('\n', '').replace(' ', '').replace("†","").replace("*","").replace("%","").replace('<', '').replace('‡','')
					if('-' in CyanValue):
						CyanValue = '0'
					CyanToner = Cyan + " " + CyanValue
					print(CyanToner)
				except IndexError:
					Cyan = ""
					CyanValue = ""
				try:
					Magenta = tonerTables[11].find('td')
					Magenta = Magenta.getText().strip()
					Magenta = Magenta.replace('\r', '').replace('\n', '').replace("Order","").replace("?", "").replace("†","")
					Magenta = Magenta.replace('Magenta Cartridge', ' ').replace(' ', '')
					MagentaValue = tonerValues[2].getText()
					MagentaValue = MagentaValue.replace('\r', '').replace('\n', '').replace(' ', '').replace("†","").replace("*","").replace("%","").replace('<', '').replace('‡','')
					if('-' in MagentaValue):
						MagentaValue = '0'
					MagentaToner = Magenta + " " + MagentaValue
					print(MagentaToner)
				except IndexError:
					Magenta = ""
					MagentaValue = ""
				try:
					Yellow = tonerTables[15].find('td')
					Yellow = Yellow.getText().strip()
					Yellow = Yellow.replace('\r', '').replace('\n', '').replace("Order","").replace("?", "").replace("†","")
					Yellow = Yellow.replace('Yellow Cartridge', ' ').replace(' ', '')
					YellowValue = tonerValues[3].getText()
					YellowValue = YellowValue.replace('\r', '').replace('\n', '').replace(' ', '').replace("†","").replace("*","").replace("%","").replace('<', '').replace('‡','')
					if('-' in YellowValue):
						YellowValue = '0'
					YellowToner = Yellow + " " + YellowValue
					print(YellowToner)
				except IndexError:
					Yellow = ""
					YellowValue = ""
				url = "http://ctacinv/api/PrinterLevels?PythonScript=true"
				data = {
					"PrinterName": printerName,
					"PrinterIP": printerIp,
					"BlackModel": Black,
					"BlackLevel": BlackValue,
					"CyanModel": Cyan,
					"CyanLevel": CyanValue,
					"MagentaModel": Magenta,
					"MagentaLevel": MagentaValue,
					"YellowModel": Yellow,
					"YellowLevel": YellowValue,
					}
				upload = requests.post(url, verify=False, json=data)
				print(upload.status_code)
				del Black
				del BlackValue
				del Cyan
				del CyanValue
				del Magenta
				del MagentaValue
				del Yellow
				del YellowValue
			tonerArea4 = soup.find(class_="mainContentArea width100 pad10")
			if(tonerArea4):
				tonerTables = tonerArea4.findAll(class_="width100")
				tonerValues = tonerArea4.findAll(class_="alignRight valignTop")
				try:
					Black = tonerTables[0].find('td')
					Black = Black.getText().strip()
					Black = Black.replace('\r', '').replace('\n', '').replace("Order","").replace("?", "").replace("†","")
					Black = Black.replace('Black Cartridge', ' ').replace(' ', '')
					BlackValue = tonerValues[0].getText()
					BlackValue = BlackValue.replace('\r', '').replace('\n', '').replace(' ', '').replace("†","").replace("*","").replace("%","").replace('<', '').replace('‡','')
					if('-' in BlackValue):
						BlackValue = '0'
					BlackToner = Black + " " + BlackValue
					print(BlackToner)
				except IndexError:
					Black= ""
					BlackValue = "" 
				try:
					Cyan = tonerTables[2].find('td')
					Cyan = Cyan.getText().strip()
					Cyan = Cyan.replace('\r', '').replace('\n', '').replace("Order","").replace("?", "").replace("†","")
					Cyan = Cyan.replace('Cyan Cartridge', ' ').replace(' ', '')
					CyanValue = tonerValues[1].getText()
					CyanValue = CyanValue.replace('\r', '').replace('\n', '').replace(' ', '').replace("†","").replace("*","").replace("%","").replace('<', '').replace('‡','')
					if('-' in CyanValue):
						CyanValue = '0'
					CyanToner = Cyan + " " + CyanValue
					print(CyanToner)
				except IndexError:
					Cyan = ""
					CyanValue = ""
				try:
					Magenta = tonerTables[4].find('td')
					Magenta = Magenta.getText().strip()
					Magenta = Magenta.replace('\r', '').replace('\n', '').replace("Order","").replace("?", "").replace("†","")
					Magenta = Magenta.replace('Magenta Cartridge', ' ').replace(' ', '')
					MagentaValue = tonerValues[2].getText()
					MagentaValue = MagentaValue.replace('\r', '').replace('\n', '').replace(' ', '').replace("†","").replace("*","").replace("%","").replace('<', '').replace('‡','')
					if('-' in MagentaValue):
						MagentaValue = '0'
					MagentaToner = Magenta + " " + MagentaValue
					print(MagentaToner)
				except IndexError:
					Magenta = ""
					MagentaValue = ""
				try:
					Yellow = tonerTables[6].find('td')
					Yellow = Yellow.getText().strip()
					Yellow = Yellow.replace('\r', '').replace('\n', '').replace("Order","").replace("?", "").replace("†","")
					Yellow = Yellow.replace('Yellow Cartridge', ' ').replace(' ', '')
					YellowValue = tonerValues[3].getText()
					YellowValue = YellowValue.replace('\r', '').replace('\n', '').replace(' ', '').replace("†","").replace("*","").replace("%","").replace('<', '').replace('‡','')
					if('-' in YellowValue):
						YellowValue = '0'
					YellowToner = Yellow + " " + YellowValue
					print(YellowToner)
				except IndexError:
					Yellow = ""
					YellowValue = ""
				url = "http://ctacinv/api/PrinterLevels?PythonScript=true"
				data = {
					"PrinterName": printerName,
					"PrinterIP": printerIp,
					"BlackModel": Black,
					"BlackLevel": BlackValue,
					"CyanModel": Cyan,
					"CyanLevel": CyanValue,
					"MagentaModel": Magenta,
					"MagentaLevel": MagentaValue,
					"YellowModel": Yellow,
					"YellowLevel": YellowValue,
					}
				upload = requests.post(url, verify=False, json=data)
				print(upload.status_code)
				del Black
				del BlackValue
				del Cyan
				del CyanValue
				del Magenta
				del MagentaValue
				del Yellow
				del YellowValue	
			if not tonerArea1 and not tonerArea2 and not tonerArea3 and not tonerArea4 and not tonerArea5:
				url = "http://" + printerIp + "/web/guest/en/websys/webArch/getStatus.cgi"
				print(url)
				try:
					page = requests.get(url, verify=False)
					outfile.write("Set Page Variable\n")
					soup = BeautifulSoup(page.content, 'html.parser')
					outfile.write("Set Soup Variable\n")
					tonerArea6 = soup.findAll(class_="tonerArea")
					if(tonerArea6):
						Black = tonerArea6[0]
						Blackimg = Black.find('img')
						BlackLevel = int(Blackimg.get('width'))
						BlackLevel = (BlackLevel/162)*100
						BlackLevel = math.floor(BlackLevel)
						

						Cyan = tonerArea6[1]
						Cyanimg = Cyan.find('img')
						CyanLevel = int(Cyanimg.get('width'))
						CyanLevel = (CyanLevel/162)*100
						CyanLevel = math.floor(CyanLevel)

						Magenta = tonerArea6[2]
						Magentaimg = Magenta.find('img')
						MagentaLevel = int(Magentaimg.get('width'))
						MagentaLevel = (MagentaLevel/162)*100
						MagentaLevel = math.floor(MagentaLevel)

						Yellow = tonerArea6[3]
						Yellowimg = Yellow.find('img')
						YellowLevel = int(Yellowimg.get('width'))
						YellowLevel = (YellowLevel/162)*100
						YellowLevel = math.floor(YellowLevel)
						print(BlackLevel)
						print(CyanLevel)
						print(MagentaLevel)
						print(YellowLevel)

						url = "http://ctacinv/api/PrinterLevels?PythonScript=true"
						data = {
							"PrinterName": printerName,
							"PrinterIP": printerIp,
							"BlackModel": "Ricoh Model",
							"BlackLevel": BlackLevel,
							"CyanModel": "Ricoh Model",
							"CyanLevel": CyanLevel,
							"MagentaModel": "Ricoh Model",
							"MagentaLevel": MagentaLevel,
							"YellowModel": "Ricoh Model",
							"YellowLevel": YellowLevel,
							"MaintinenceModel": "",
							"MaintinenceLevel": ""
							}
						upload = requests.post(url, verify=False, json=data)
						print(upload.status_code)
						del BlackLevel
						del CyanLevel
						del MagentaLevel
						del YellowLevel
					if not tonerArea6:
						url = "https://" + printerIp + "/web/guest/en/websys/webArch/getStatus.cgi"
						print(url)
						try:
							page = requests.get(url, verify=False)
							outfile.write("Set Page Variable\n")
							soup = BeautifulSoup(page.content, 'html.parser')
							outfile.write("Set Soup Variable\n")
							tonerArea6 = soup.findAll(class_="tonerArea")
							if(tonerArea6):
								Black = tonerArea6[0]
								Blackimg = Black.find('img')
								BlackLevel = int(Blackimg.get('width'))
								BlackLevel = (BlackLevel/162)*100
								BlackLevel = math.floor(BlackLevel)
								

								Cyan = tonerArea6[1]
								Cyanimg = Cyan.find('img')
								CyanLevel = int(Cyanimg.get('width'))
								CyanLevel = (CyanLevel/162)*100
								CyanLevel = math.floor(CyanLevel)

								Magenta = tonerArea6[2]
								Magentaimg = Magenta.find('img')
								MagentaLevel = int(Magentaimg.get('width'))
								MagentaLevel = (MagentaLevel/162)*100
								MagentaLevel = math.floor(MagentaLevel)

								Yellow = tonerArea6[3]
								Yellowimg = Yellow.find('img')
								YellowLevel = int(Yellowimg.get('width'))
								YellowLevel = (YellowLevel/162)*100
								YellowLevel = math.floor(YellowLevel)
								print(BlackLevel)
								print(CyanLevel)
								print(MagentaLevel)
								print(YellowLevel)
								url = "http://ctacinv/api/PrinterLevels?PythonScript=true"
								data = {
									"PrinterName": printerName,
									"PrinterIP": printerIp,
									"BlackModel": "Ricoh Model",
									"BlackLevel": BlackLevel,
									"CyanModel": "Ricoh Model",
									"CyanLevel": CyanLevel,
									"MagentaModel": "Ricoh Model",
									"MagentaLevel": MagentaLevel,
									"YellowModel": "Ricoh Model",
									"YellowLevel": YellowLevel,
									"MaintinenceModel": "",
									"MaintinenceLevel": ""
									}
								upload = requests.post(url, verify=False, json=data)
								print(upload.status_code)
								del BlackLevel
								del CyanLevel
								del MagentaLevel
								del YellowLevel
							if not tonerArea1 and not tonerArea2 and not tonerArea3 and not tonerArea4 and not tonerArea5 and not tonerArea6:
								print("Toner levels not available")
								url = "http://ctacinv/api/PrinterLevels?PythonScript=true"
								data = {
									"PrinterName": printerName,
									"PrinterIP": printerIp,
									"BlackModel": "Toner Model Undefined",
									"BlackLevel": "Toner Level Undefined",
									"CyanModel": "Toner Model Undefined",
									"CyanLevel": "Toner Level Undefined",
									"MagentaModel": "Toner Model Undefined",
									"MagentaLevel": "Toner Level Undefined",
									"YellowModel": "Toner Model Undefined",
									"YellowLevel": "Toner Level Undefined",
									}
								upload = requests.post(url, verify=False, json=data)
								print(upload.status_code)
						except requests.exceptions.ConnectionError:
							print("Web interface unreachable")
							url = "http://ctacinv/api/PrinterLevels?PythonScript=true"
							data = {
								"PrinterName": printerName,
								"PrinterIP": printerIp,
								"BlackModel": "Printer Web Interface Failed",
								"BlackLevel": "Printer Web Interface Failed",
								"CyanModel": "Printer Web Interface Failed",
								"CyanLevel": "Printer Web Interface Failed",
								"MagentaModel": "Printer Web Interface Failed",
								"MagentaLevel": "Printer Web Interface Failed",
								"YellowModel": "Printer Web Interface Failed",
								"YellowLevel": "Printer Web Interface Failed",
								}
							upload = requests.post(url, verify=False, json=data)
							print(upload.status_code)
						except requests.exceptions.ConnectionError:
							print("Web interface unreachable")
							url = "http://ctacinv/api/PrinterLevels?PythonScript=true"
							data = {
								"PrinterName": printerName,
								"PrinterIP": printerIp,
								"BlackModel": "Printer Web Interface Failed",
								"BlackLevel": "Printer Web Interface Failed",
								"CyanModel": "Printer Web Interface Failed",
								"CyanLevel": "Printer Web Interface Failed",
								"MagentaModel": "Printer Web Interface Failed",
								"MagentaLevel": "Printer Web Interface Failed",
								"YellowModel": "Printer Web Interface Failed",
								"YellowLevel": "Printer Web Interface Failed",
								}
							upload = requests.post(url, verify=False, json=data)
							print(upload.status_code)
				except requests.exceptions.ConnectionError:
					print("Web interface unreachable")
					url = "http://ctacinv/api/PrinterLevels?PythonScript=true"
					data = {
						"PrinterName": printerName,
						"PrinterIP": printerIp,
						"BlackModel": "Printer Web Interface Failed",
						"BlackLevel": "Printer Web Interface Failed",
						"CyanModel": "Printer Web Interface Failed",
						"CyanLevel": "Printer Web Interface Failed",
						"MagentaModel": "Printer Web Interface Failed",
						"MagentaLevel": "Printer Web Interface Failed",
						"YellowModel": "Printer Web Interface Failed",
						"YellowLevel": "Printer Web Interface Failed",
						}
					upload = requests.post(url, verify=False, json=data)
					print(upload.status_code)
		except requests.exceptions.ConnectionError:
			print("Web interface unreachable")
			url = "http://ctacinv/api/PrinterLevels?PythonScript=true"
			data = {
				"PrinterName": printerName,
				"PrinterIP": printerIp,
				"BlackModel": "Printer Web Interface Failed",
				"BlackLevel": "Printer Web Interface Failed",
				"CyanModel": "Printer Web Interface Failed",
				"CyanLevel": "Printer Web Interface Failed",
				"MagentaModel": "Printer Web Interface Failed",
				"MagentaLevel": "Printer Web Interface Failed",
				"YellowModel": "Printer Web Interface Failed",
				"YellowLevel": "Printer Web Interface Failed",
				}
			upload = requests.post(url, verify=False, json=data)
			print(upload.status_code)

