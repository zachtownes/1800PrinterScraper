with open("c:/windows/temp/extip.log", "w") as outfile:	
    import requests
    outfile.write("Imported Requests\n")
    from bs4 import BeautifulSoup
    outfile.write("Imported BeautifulSoup\n")
    from string import whitespace
    outfile.write("Imported Whitespace\n")
    import math
    url = "http://10.10.207.24"
    print(url)
    page = requests.get(url)
    print(page.content)
    print("Set Page Variable\n")
    soup = BeautifulSoup(page.content, 'html.parser')
    print("Set Soup Variable\n")
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
        '''url = "http://ctacinv/api/PrinterLevels?PythonScript=true"
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
    
'''
