with open("c:/windows/temp/extip.log", "w") as outfile:	
    import requests
    outfile.write("Imported Requests\n")
    from bs4 import BeautifulSoup
    outfile.write("Imported BeautifulSoup\n")
    from string import whitespace
    outfile.write("Imported Whitespace\n")
    import math
    url = "https://10.10.207.138/web/guest/en/websys/webArch/getStatus.cgi"
    print(url)
    try:
        page = requests.get(url, verify=False)
        print(page)
        outfile.write("Set Page Variable\n")
        soup = BeautifulSoup(page.content, 'html.parser')
        print(soup)
        outfile.write("Set Soup Variable\n")
        tonerArea6 = soup.findAll(class_="tonerArea")
        print(tonerArea6)
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
            '''         
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
            '''
    except requests.exceptions.ConnectionError:
        print("Toner levels not available")
        '''
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
        '''