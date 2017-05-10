#Lora Gateway Status: time last seen on TTN

import datetime
import urllib.request, json 

def convertTime(EpochTime):
    time = EpochTime/(1e9)
    humanTime = datetime.datetime.fromtimestamp(time).strftime('%c')
    return humanTime

def getEUI():
    gateway_eui = input("Enter TTN gateway EUI: ")
    if gateway_eui == "" or gateway_eui == "00800000a00004d2":
        print("Notman TTN Gateway last seen on:")
        gateway_eui = "00800000a00004d2" # Notman House Lora Gateway
    else:
        print(gateway_eui, "last seen on:")
    return gateway_eui


def getTime(gateway_eui):
    address = "http://noc.thethingsnetwork.org:8085/api/v2/gateways/eui-" + gateway_eui

    with urllib.request.urlopen(address) as url:
        data = json.loads(url.read().decode())

    gatewayTime = int(data["time"])
    return gatewayTime

print(convertTime(getTime(getEUI())))
