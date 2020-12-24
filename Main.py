import requests
import msvcrt
import json
import random
import string
import os
import sys
import time


def Pause():
    msvcrt.getch()


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

Banner = r'''
(01) Bit.ly URL Shortener
        $ Best for Download Links
        $ Links Managment Avilable in the Bit.ly Dashbourd

(02) Cutt.ly URL Shortener
        $ Best for URL Sharing
        $ Links Management Avilable in the Cutt.ly Dashbourd

(03) API Management Section
        $ Add/Manage API-TOKEN

(04) How to USE\?
        $ How to Get My API-TOKEN
        $ How to USE This Programe

(05) Exit

>> Enter Your Choice : '''

Banner2 = r'''
(01) Cutt.ly API-TOKEN 

(02) Bit.ly API-TOKEN

(03) Make [ Database.json ] Document

(04) Main Menu

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
                        print("$ Got to API Management Section...")
                        Pause()
                        Clear()
                        break

                    if TOKEN == "":
                        print("$ Your API Token is Invalid...!")
                        print("$ Got to API Management Section...")
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

                    data = '{ "long_url": "'+URL+'", "domain": "bit.ly"}'

                    response = requests.post(
                        'https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data).json()
                    try:
                        print("\n\n$ Shorted Url  : ", response['link'])
                        print("$ Created Date : ",
                              response['created_at'], "\n\n")
                        Pause()
                        Clear()
                        break
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
                        print("$ Got to API Management Section...")
                        Pause()
                        Clear()
                        break

                    if TOKEN == "":
                        print("$ Your API Token is Invalid...!")
                        print("$ Got to API Management Section...")
                        Pause()
                        Clear()
                        break
                    else:
                        pass

                    URL = input("\n$ Enter Long URL : ")
                    api_url = f"https://cutt.ly/api/api.php?key={TOKEN}&short={URL}"
                    data = requests.get(api_url).json()["url"]
                    try:
                        if data["status"] == 7:
                            shortened_url = data["shortLink"]
                            print("\n\n$ Shorted Url  :", shortened_url)
                            print("$ Created Date :",
                                  data["date"], "\n\n")
                            Pause()
                            Clear()
                            break
                        if data["status"] == 6:
                            print("$ The link provided is from a blocked domain")
                            Pause()
                            Clear()
                            break
                        if data["status"] == 5:
                            print(
                                "$ The link has not passed the validation. Includes invalid characters")
                            Pause()
                            Clear()
                            break
                        if data["status"] == 4:
                            print("$ Invalid API key")
                            Pause()
                            Clear()
                            break
                        if data["status"] == 3:
                            print("$ The preferred link name is already taken")
                            Pause()
                            Clear()
                            break
                        if data["status"] == 2:
                            print("$ The entered link is not a link")
                            Pause()
                            Clear()
                            break
                        if data["status"] == 1:
                            print("$ The link has already been shortened")
                            Pause()
                            Clear()
                            break
                    except Exception:
                        print("\n\n$ Error Shortening the Given URL..!")
                        print(
                            '$ Possible Ressons : $ The URL You Provided is not an URL')
                        print('                     $ Internet Connection Error')
                        Pause()
                        Clear()
                        continue

        except KeyboardInterrupt:
            print("$ You Terminated the Programm..")
            sys.exit()
    if User_Choice == 3:
        Clear()
        print("$ API-TOKEN Management Section....")
        while True:
            try:
                X = int(input(Banner2))
                break
            except ValueError:
                Clear()
                continue
        if X == 1:
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

                CUTTLY_TOKEN = input("$ Enter API TOKEN : ")
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
        if X == 2:
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
                BITLY_TOKEN = input("$ Enter API TOKEN : ")
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
        if X == 3:
            while True:
                BASE = {
                    "BITLY_TOKEN": "",
                    "CUTTLY_TOKEN": ""
                }
                with open("Database.json", "w") as outfile:
                    json.dump(BASE, outfile, indent=2)
                print("$ Document Created..")
                Pause()
                Clear()
                break
        if X == 4:
            Clear()
            continue
    if User_Choice == 4:
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
    if User_Choice == 5:
        print("$ Press Anything for Exit...!")
        Pause()
        sys.exit()
    else:
        Clear()
        continue
