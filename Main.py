import mechanize
import pyperclip
import requests
import random
import string
import msvcrt
import time
import json
import sys
import csv
import io
import os

BR = mechanize.Browser()
BR.set_handle_robots(False)
BR.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

Path = os.getenv('APPDATA')

BASE_LIBRARY = []

def Checker(VARIABLE):
    try:
        while True:
            try:
                BR.open(VARIABLE, timeout=5)
                return True
                break
            except Exception as e:
                break
                            
    except:
        return False


def Add_Record_Bitly(response):

    URL_LIBRARY = {}
    while True:
        try:
            with open(f"{Path}/Library_B.json", 'r') as f:
                DATA = json.load(f)
                break
        except Exception:
            with open(f"{Path}/Library_B.json", "w") as outfile:
                json.dump(BASE_LIBRARY, outfile, indent=4)
                continue

    URL_LIBRARY['DATE'] = response['created_at']
    URL_LIBRARY['URL'] = response['link']
    URL_LIBRARY['LONG_URL'] = response['long_url']
    if Checker(response['long_url']) == True:
        try:
            BR.open(response['long_url']) 
            URL_LIBRARY['Title'] = BR.title()
        except Exception:
            URL_LIBRARY['Title'] = ("$ Download Link?")
    else:
        URL_LIBRARY['Title'] = ("$ Download Link or Invalid Link")

    DATA.append(URL_LIBRARY)
    with open(f"{Path}/Library_B.json", 'w') as f:
        json.dump(DATA, f, indent=4)


def Add_Record_Cuttly(data):

    URL_LIBRARY_2 = {}
    while True:
        try:
            with open(f"{Path}/Library_C.json", 'r') as f:
                DATA = json.load(f)
                break
        except Exception:
            with open(f"{Path}/Library_C.json", "w") as outfile:
                json.dump(BASE_LIBRARY, outfile, indent=4)
                continue

    URL_LIBRARY_2['DATE'] = data["date"]
    URL_LIBRARY_2['URL'] = data["shortLink"]
    URL_LIBRARY_2['LONG_URL'] = data["fullLink"]
    URL_LIBRARY_2['Title'] = data["title"]

    DATA.append(URL_LIBRARY_2)
    with open(f"{Path}/Library_C.json", 'w') as f:
        json.dump(DATA, f, indent=4)


def View_Records_Bitly():
    while True:
        Content = ""
        try:
            with open(f"{Path}/Library_B.json") as json_file:
                for line in json_file.read():
                    Content += line
        except Exception:
            print("$ There is no Data to View....")
            break

        Content = json.loads(Content)

        with io.open("Shorted-Data-Bitly.csv", "w", encoding="utf-8") as f:
            writer = csv.DictWriter(f, Content[0].keys())
            writer.writeheader()

            for x in Content:
                writer.writerow(x)
        print("$ All Records Saved to CSV Document..")
        break


def View_Records_Cuttly():
    while True:
        Content = ""
        try:
            with open(f"{Path}/Library_C.json") as json_file:
                for line in json_file.read():
                    Content += line
        except Exception:
            print("$ There is no Data to View....")
            break

        Content = json.loads(Content)

        with io.open("Shorted-Data-Cuttly.csv", "w", encoding="utf-8") as f:
            writer = csv.DictWriter(f, Content[0].keys())
            writer.writeheader()

            for x in Content:
                writer.writerow(x)
        print("$ All Records Saved to CSV Document..")
        break


def Add_data_Bitly():

    URL_LIBRARY = {}
    while True:
        try:
            with open(f"{Path}/Library_B.json", 'r') as f:
                DATA = json.load(f)
                break
        except Exception:
            with open(f"{Path}/Library_B.json", "w") as outfile:
                json.dump(BASE_LIBRARY, outfile, indent=4)
                continue

    URL_LIBRARY['DATE'] = response['created_at']
    URL_LIBRARY['URL'] = response['link']
    URL_LIBRARY['LONG_URL'] = response['long_url']
    if Checker(response['long_url']) == True:
        try:
            BR.open(response['long_url'])
            URL_LIBRARY['Title'] = BR.title()
        except Exception:
            URL_LIBRARY['Title'] = ("$ Download Link?")
    else:
        URL_LIBRARY['Title'] = ("$ Download Link or Invalid Link")

    DATA.append(URL_LIBRARY)
    with open(f"{Path}/Library_B.json", 'w') as f:
        json.dump(DATA, f, indent=4)


def Add_data_Cuttly():

    URL_LIBRARY = {}
    while True:
        try:
            with open(f"{Path}/Library_C.json", 'r') as f:
                DATA = json.load(f)
                break
        except Exception:
            with open(f"{Path}/Library_C.json", "w") as outfile:
                json.dump(BASE_LIBRARY, outfile, indent=4)
                continue

    URL_LIBRARY['DATE'] = data["date"]
    URL_LIBRARY['URL'] = data["shortLink"]
    URL_LIBRARY['LONG_URL'] = data["fullLink"]
    URL_LIBRARY['Title'] = data['title']

    DATA.append(URL_LIBRARY)
    with open(f"{Path}/Library_C.json", 'w') as f:
        json.dump(DATA, f, indent=4)


def Pause():
    msvcrt.getch()


def Clip(clipdata):
    pyperclip.copy(clipdata)


def Clear():
    os.system('cls')


def Net_Status(host="https://www.google.com"):
    try:
        requests.get(host)
        return True
    except:
        return False


if Net_Status() == True:
    pass
else:
    print("$ No Internet Conncetion...")
    Pause()
    sys.exit()

os.system("COLOR A")

Banner = r'''
(01) Bit.ly URL Shortener
        $ Best for Download Links
        $ Links Managment Avilable in the Bit.ly Dashbourd

(02) Cutt.ly URL Shortener
        $ Best for URL Sharing
        $ Links Management Avilable in the Cutt.ly Dashbourd

(03) Short Several links at once
        $ For Shorting Multiple Links at Same Time 

(04) API Management Section
        $ Add/Manage API-TOKEN

(05) History
        $ Save History as SpreadSheet

(06) How to USE?
        $ How to Get My API-TOKEN

(07) Exit

>> Enter Your Choice : '''

Banner2 = r'''
$ API-TOKEN Management Section....

(01) Bit.ly API-TOKEN 

(02) Cutt.ly API-TOKEN

(03) Make [ Database.json ] Document

(04) Main Menu

>> Enter Your Choice : '''

Banner3 = r'''
(01) Save Previous Bitly Shortening History
        $ File Type : CSV [SPREADSHEET]

(02) Save Previous Cuttly Shortening History
        $ File Type : CSV [SPREADSHEET]

(03) Main Menu

>> Enter Your Choice : '''

Banner4 = r'''
(01) Short Multiple Links at Once | Bit.ly

(02) Short Multiple Links at Once | Cutt.ly

(03) Main Menu

>> Enter Your Choice : '''


while True:
    while True:
        try:
            Clear()
            User_Choice = int(input(Banner))
            break
        except ValueError:
            Clear()
            continue
    if User_Choice == 1:
        try:
            if Net_Status() == True:
                while True:
                    Clear()
                    print("$ Connection OK...")
                    print("$ Waiting for User Data...\n\n")
                    while True:
                        try:
                            with open("Database.json", "r") as TOKENFILE:
                                TOKEN_DATA = json.load(TOKENFILE)
                                break
                        except Exception:
                            BASE = {
                                "BITLY_TOKEN": "",
                                "CUTTLY_TOKEN": ""
                            }
                            with open("Database.json", "w") as outfile:
                                json.dump(BASE, outfile, indent=2)
                            continue
                    try:
                        TOKEN = TOKEN_DATA["BITLY_TOKEN"]
                        pass

                    except Exception:
                        print("$ Your API-TOKEN is Empty..!")
                        print("$ Manage it Via API Management Section...")
                        Pause()
                        Clear()
                        break

                    if TOKEN == "":
                        print("$ Your API Token is Invalid...!")
                        print("$ Manage it Via API Management Section...")
                        Pause()
                        Clear()
                        break
                    else:
                        pass

                    headers = {
                        'Authorization': f'Bearer {TOKEN}',
                        'Content-Type': 'application/json',
                    }
                    URL = input("$ Enter Long URL : ")
                    if URL == "":
                        break

                    data = '{ "long_url": "'+URL+'", "domain": "bit.ly"}'

                    response = requests.post(
                        'https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data).json()
                    try:
                        Clip(response['link'])
                        print("\n\n$ Shorted Url  : ", response['link'])
                        print("$ Created Date : ",
                              response['created_at'], "\n\n")
                        print("      > URL COPIED TO CLIPBOARD < ")
                        Add_data_Bitly()
                        print("      >    RECORD UPDATED :)    < ")
                        Pause()
                        Clear()
                        continue
                    except Exception as x:
                        print(x)
                        print("\n\n$ Error Shortening the Given URL..!")
                        print(
                            '$ Possible Ressons : $ The URL You Provided is not an URL')
                        print('                     $ Internet Connection Error')
                        Pause()
                        Clear()
                        continue
            else:
                print("$ Connection Faild...")
                Pause()
                Clear()
        except KeyboardInterrupt:
            print("$ You Terminated the Programm..")
            sys.exit()
    if User_Choice == 2:
        try:
            if Net_Status() == True:
                while True:
                    Clear()
                    print("$ Connection OK...")
                    print("$ Waiting for User Data...\n\n")
                    while True:
                        try:
                            with open("Database.json", "r") as TOKENFILE:
                                TOKEN_DATA = json.load(TOKENFILE)
                                break
                        except Exception:
                            BASE = {
                                "BITLY_TOKEN": "",
                                "CUTTLY_TOKEN": ""
                            }
                            with open("Database.json", "w") as outfile:
                                json.dump(BASE, outfile, indent=2)
                            continue
                    try:
                        TOKEN = TOKEN_DATA["CUTTLY_TOKEN"]
                        pass

                    except Exception:
                        print("$ Your API-TOKEN is Empty..!")
                        print("$ Manage it Via API Management Section...")
                        Pause()
                        Clear()
                        break

                    if TOKEN == "":
                        print("$ Your API Token is Invalid...!")
                        print("$ Manage it Via API Management Section...")
                        Pause()
                        Clear()
                        break
                    else:
                        pass

                    URL = input("\n$ Enter Long URL : ")
                    if URL == "":
                        break

                    api_url = f"https://cutt.ly/api/api.php?key={TOKEN}&short={URL}"
                    data = requests.get(api_url).json()["url"]
                    try:
                        if data["status"] == 7:
                            shortened_url = data["shortLink"]
                            Clip(shortened_url)
                            print("\n\n$ Shorted Url  :", shortened_url)
                            print("$ Created Date :",
                                  data["date"], "\n\n")
                            print("      > URL COPIED TO CLIPBOARD < ")
                            Add_data_Cuttly()
                            print("      >    RECORD UPDATED :)    < ")
                            Pause()
                            Clear()
                            continue
                        if data["status"] == 6:
                            print("$ The link provided is from a blocked domain")
                            Pause()
                            Clear()
                            continue
                        if data["status"] == 5:
                            print(
                                "$ The link has not passed the validation. Includes invalid characters")
                            Pause()
                            Clear()
                            continue
                        if data["status"] == 4:
                            print("$ Invalid API key")
                            Pause()
                            Clear()
                            continue
                        if data["status"] == 3:
                            print("$ The preferred link name is already taken")
                            Pause()
                            Clear()
                            continue
                        if data["status"] == 2:
                            print("$ The entered link is not a link")
                            Pause()
                            Clear()
                            continue
                        if data["status"] == 1:
                            print("$ The link has already been shortened")
                            Pause()
                            Clear()
                            continue
                    except Exception:
                        print("\n\n$ Error Shortening the Given URL..!")
                        print(
                            '$ Possible Ressons : $ The URL You Provided is not an URL')
                        print('                     $ Internet Connection Error')
                        Pause()
                        Clear()
                        continue
            else:
                print("$ Connection Faild...")
                Pause()
                Clear()
        except KeyboardInterrupt:
            print("$ You Terminated the Programm..")
            sys.exit()
    if User_Choice == 3:
        try:
            if Net_Status() == True:
                while True:
                    Clear()
                    while True:
                        try:
                            VAR_X = input(Banner4)
                            if VAR_X == "":
                                clear()
                                continue
                            else:
                                break
                        except Exception:
                            Clear()
                            continue
                    if VAR_X == str(1):
                        Clear()
                        try:
                            if Net_Status() == True:
                                while True:
                                    while True:
                                        try:
                                            with open("Database.json", "r") as TOKENFILE:
                                                TOKEN_DATA = json.load(TOKENFILE)
                                                break
                                        except Exception:
                                            BASE = {
                                                "BITLY_TOKEN": "",
                                                "CUTTLY_TOKEN": ""
                                            }
                                            with open("Database.json", "w") as outfile:
                                                json.dump(BASE, outfile, indent=2)
                                                continue
                                    try:
                                        TOKEN = TOKEN_DATA["BITLY_TOKEN"]
                                        pass

                                    except Exception:
                                        print("$ Your API-TOKEN is Empty..!")
                                        print("$ Manage it Via API Management Section...")
                                        Pause()
                                        Clear()
                                        break

                                    if TOKEN == "":
                                        print("$ Your API Token is Invalid...!")
                                        print("$ Manage it Via API Management Section...")
                                        Pause()
                                        Clear()
                                        break
                                    else:
                                        pass
                                    
                                    headers = {
                                        'Authorization': f'Bearer {TOKEN}',
                                        'Content-Type': 'application/json',
                                    }
                                    LST = []
                                    J = 1
                                    N = 1
                                    print("$ Leave Blank for Proceed... \n")
                                    while True:
                                        Data = input(f"$ Provide URL #{J}  : ")
                                        if Data == "":
                                            print("\n")
                                            break
                                        LST.append(Data)
                                        J = J+1
                                        continue
                                    for x in LST:
                                        URL = x
                                        data = '{ "long_url": "'+URL+'", "domain": "bit.ly"}'
                                        response = requests.post(
                                            'https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data).json()
                                        try:
                                            print(f"$ Link Number  : #{N}")
                                            print("$ Shorted URL  :", response['link'])
                                            print("$ Shorted Date :", response['created_at'])
                                            print("\n")
                                            Add_Record_Bitly(response)
                                        except Exception:
                                            print(f"$ Link Number  : Cannot be Generated..")
                                            print("\n")
                                        N = N+1
                                    print("      >    RECORDS UPDATED :)    < ")
                                    print("      >    ..PRESS ANY KEY..     < ")
                                    Pause()
                                    Clear()
                                    break

                            else:
                                print("$ Connection Faild...")
                                Pause()
                                Clear()
                        except Exception:
                            print("$ Please Check Your internet Connection")
                            Pause()
                    if VAR_X == str(2):
                        Clear()
                        try:
                            if Net_Status() == True:
                                while True:
                                    while True:
                                        try:
                                            with open("Database.json", "r") as TOKENFILE:
                                                TOKEN_DATA = json.load(TOKENFILE)
                                                break
                                        except Exception:
                                            BASE = {
                                                "BITLY_TOKEN": "",
                                                "CUTTLY_TOKEN": ""
                                            }
                                            with open("Database.json", "w") as outfile:
                                                json.dump(BASE, outfile, indent=2)
                                                continue
                                    try:
                                        TOKEN = TOKEN_DATA["CUTTLY_TOKEN"]
                                        pass

                                    except Exception:
                                        print("$ Your API-TOKEN is Empty..!")
                                        print("$ Manage it Via API Management Section...")
                                        Pause()
                                        Clear()
                                        break

                                    if TOKEN == "":
                                        print("$ Your API Token is Invalid...!")
                                        print("$ Manage it Via API Management Section...")
                                        Pause()
                                        Clear()
                                        break
                                    else:
                                        pass
                                    
                                    KEY = TOKEN_DATA["CUTTLY_TOKEN"]

                                    LST_2 = []
                                    O = 1
                                    F = 1
                                    print("$ Leave Blank for Proceed... \n")
                                    while True:
                                        Data = input(f"$ Provide URL #{O}  : ")
                                        if Data == "":
                                            print("\n")
                                            break
                                        LST_2.append(Data)
                                        O = O+1
                                        continue
                                    for x in LST_2:
                                        URL_2 = x
                                        payload = {'key': ''+KEY+'', 'short': ''+URL_2+''}
                                        data = requests.get('https://cutt.ly/api/api.php', payload).json()["url"]
                                        if data['status'] == 7:
                                            print(f"$ Link Number  : #{F}")
                                            print("$ Shorted URL  :", data["shortLink"])
                                            print("$ Shorted Date :", data["date"])
                                            print("\n")
                                            Add_Record_Cuttly(data)
                                        else:
                                            print(f"$ Link Number  : Cannot be Generated..")
                                            print("\n")
                                        F = F+1
                                    print("      >    RECORDS UPDATED :)    < ")
                                    print("      >    ..PRESS ANY KEY..     < ")
                                    Pause()
                                    Clear()
                                    break

                            else:
                                print("$ Connection Faild...")
                                Pause()
                                Clear()
                        except Exception:
                            print("$ Please Check Your internet Connection")
                            Pause()
                    if VAR_X == str(3):
                        break

            else:
                print("$ Connection Faild...")
                Pause()
                Clear()
        except KeyboardInterrupt:
            print("$ You Terminated the Programm..")
            sys.exit()
    if User_Choice == 4:
        Clear()
        while True:
            try:
                X = int(input(Banner2))
                break
            except ValueError:
                Clear()
                continue
        if X == 2:
            if Net_Status() == True:
                while True:
                    print("\n\n$ Cutt.ly API TOKEN\n")
                    while True:
                        try:
                            DATA = open("Database.json", "r")
                            json_object = json.load(DATA)
                            break
                        except Exception:
                            BASE = {
                                "BITLY_TOKEN": "",
                                "CUTTLY_TOKEN": ""
                            }
                            with open("Database.json", "w") as outfile:
                                json.dump(BASE, outfile, indent=2)
                            continue

                    if json_object["CUTTLY_TOKEN"] == "":
                        print("$ Your Currunt API-TOKEN : Empty")
                    else:
                        print("$ Your Currunt API-TOKEN : " + json_object["CUTTLY_TOKEN"])
                    print("\n")
                    CUTTLY_TOKEN = input("$ Enter API TOKEN : ")
                    if CUTTLY_TOKEN == "":
                        print("\n$ No TOKEN Provided...")
                        time.sleep(1.5)
                        break
                    letters = string.ascii_lowercase
                    result_str = ''.join(random.choice(letters)
                                         for i in range(5))
                    URL = ("https://www.google.com/search?q=" + result_str)
                    api_url = f"https://cutt.ly/api/api.php?key={CUTTLY_TOKEN}&short={URL}"
                    data = requests.get(api_url).json()["url"]
                    if data["status"] == 7:
                        json_object["CUTTLY_TOKEN"] = CUTTLY_TOKEN
                        a_file = open("Database.json", "w")
                        json.dump(json_object, a_file, indent=2)
                        a_file.close()
                        print("\n$ TOKEN Updated..")
                        Pause()
                        Clear()
                        break
                    else:
                        print("\n$ Invalid API TOKEN..!")
                        Pause()
                        Clear()
                        continue
                    Pause()
                    Clear()
            else:
                print("$ Connection Faild...")
                Pause()
                Clear()
        if X == 1:
            if Net_Status() == True:
                while True:
                    print("\n\n$ Bit.ly API TOKEN\n")
                    while True:
                        try:
                            DATA = open("Database.json", "r")
                            json_object = json.load(DATA)
                            break
                        except Exception:
                            BASE = {
                                "BITLY_TOKEN": "",
                                "CUTTLY_TOKEN": ""
                            }
                            with open("Database.json", "w") as outfile:
                                json.dump(BASE, outfile, indent=2)
                            continue
                    if json_object["CUTTLY_TOKEN"] == "":
                        print("$ Your Currunt API-TOKEN : Empty")
                    else:
                        print("$ Your Currunt API-TOKEN : " + json_object["BITLY_TOKEN"])
                    print("\n")
                    BITLY_TOKEN = input("$ Enter API TOKEN : ")
                    if BITLY_TOKEN == "":
                        print("\n$ No TOKEN Provided...")
                        time.sleep(1.5)
                        break
                    letters = string.ascii_lowercase
                    result_str = ''.join(random.choice(letters)
                                         for i in range(5))
                    headers = {
                        'Authorization': f'Bearer {BITLY_TOKEN}',
                        'Content-Type': 'application/json',
                    }
                    URL = ("https://www.google.com/search?q=" + result_str)
                    data = '{ "long_url": "'+URL+'", "domain": "bit.ly"}'
                    response = requests.post(
                        'https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data).json()
                    try:
                        response['link'] == True
                        json_object["BITLY_TOKEN"] = BITLY_TOKEN
                        a_file = open("Database.json", "w")
                        json.dump(json_object, a_file, indent=2)
                        a_file.close()
                        print("\n$ TOKEN Updated..")
                        Pause()
                        Clear()
                        break
                    except Exception:
                        print("\n$ Invalid API TOKEN..!")
                        Pause()
                        Clear()
                        continue
                    Pause()
                    Clear()
            else:
                print("$ Connection Faild...")
                Pause()
                Clear()
        if X == 3:
            while True:
                try:
                    DATA = open("Database.json", "r")
                    json_object = json.load(DATA)
                    print("\n$ Document Already Created..")
                    Pause()
                    break
                except Exception:
                    BASE = {
                        "BITLY_TOKEN": "",
                        "CUTTLY_TOKEN": ""
                    }
                    with open("Database.json", "w") as outfile:
                        json.dump(BASE, outfile, indent=2)
                    print("\n$ Document Created..")
                    Pause()
                    Clear()
                    break
        if X == 4:
            Clear()
            continue
    if User_Choice == 5:
        Clear()
        while True:
            try:
                X = int(input(Banner3))
                break
            except ValueError:
                Clear()
                continue

        if X == 1:
            print("$ Working....")
            View_Records_Bitly()
            Pause()
        if X == 2:
            print("$ Working....")
            View_Records_Cuttly()
            Pause()
        if X == 3:
            Clear()
    if User_Choice == 6:
        Clear()
        print('''
        $ How to Get Your Unique API-TOKEN..?
        
        $ Bit.ly Users
            >> Sign Up to Bitly via > https://bitly.com/a/sign_up 
            >> Once You Created Your Account Go to Profile Settings
            >> In There You Have Option > Generic Access Token < Click on it
            >> It Will Request Your Password
            >> Once You Gave it You Have Your API-TOKEN
            >> Enter it via API Management Section\n\n''')
        print('''
        $ Cutt.ly Users
            >> Sgin Up to Cutly via > https://cutt.ly/register
            >> Once You Created Your Account Go Edit Account
            >> in Your Left You Wil See Your API-TOKEN
            >> if You Can't See it Click on Manage API
            >> Enter TOKEN Via API Management Section''')
        Pause()
        Clear()
    if User_Choice == 7:
        print("$ Press Anything for Exit...!")
        Pause()
        Clear()
        sys.exit()
    else:
        Clear()
        continue
