#!/usr/bin/python3

import sys
import argparse
from pathlib import Path

pathOfPackages = '/usr/lib/python3/dist-packages'

if Path(pathOfPackages).exists():
    sys.path.append(pathOfPackages)
else:
    print("It can be an issue with import package miio.airhumidifier")
    print("Find where is located package miio.airhumidifier and correct variable: pathOfPackages")
    print("pathOfPackages:", pathOfPackages)

pathOfPackages = '/usr/local/lib/python3.5/dist-packages'

if Path(pathOfPackages).exists():
    sys.path.append(pathOfPackages)
    import miio.airhumidifier
else:
    print("It can be an issue with import package miio.airhumidifier")
    print("Find where is located package miio.airhumidifier and correct variable: pathOfPackages")
    print("pathOfPackages:", pathOfPackages)
    import miio.airhumidifier

parser = argparse.ArgumentParser(description='Script which comunicate with AirHumidifier.')
parser.add_argument('IPaddress', help='IP address of AirHumidifier' )
parser.add_argument('token', help='token to login to device')
parser.add_argument('--mode', choices=['Auto', 'Silent', 'Medium', 'High'], help='choose mode operation')
parser.add_argument('--targetLevel', type=int, choices=range(30, 90, 10), help='choose mode operation')
parser.add_argument('--power', choices=['ON', 'OFF'], help='power ON/OFF')
parser.add_argument('--debug', action='store_true', help='if define more output is printed')

args = parser.parse_args()
if args.debug:
    print(args)
MyHumidifier = miio.airhumidifier.AirHumidifier(args.IPaddress, args.token)

if args.mode:
    if args.mode == "Auto":
            MyHumidifier.set_mode(miio.airhumidifier.OperationMode.Auto)
    elif args.mode == "Silent":
            MyHumidifier.set_mode(miio.airhumidifier.OperationMode.Silent)
    elif args.mode == "Medium":
            MyHumidifier.set_mode(miio.airhumidifier.OperationMode.Medium)
    elif args.mode == "High":
            MyHumidifier.set_mode(miio.airhumidifier.OperationMode.High)

if args.targetLevel:
    MyHumidifier.set_target_humidity(args.targetLevel)

if args.power:
    if args.power == "ON":
        MyHumidifier.on()
    elif args.power == "OFF":
        MyHumidifier.off()

print(MyHumidifier.status())