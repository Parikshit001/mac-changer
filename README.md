# Mac-Changer
This Python script, named mac_changer.py, offers a user-friendly interface for changing the Media Access Control (MAC) address of your network interface on a Linux system. It provides two methods for customization:

🥇 Specifying an Interface: Use the -i or --interface option to define the network interface you want to modify the MAC address for.

🥈 Providing a New MAC Address: Utilize the -m or --mac option to explicitly set the desired MAC address for the interface. If not provided, the script will attempt to generate a random one.

## Installation
```
git clone https://github.com/Parikshit001/mac-changer
pip3 install -r requirements.txt
sudo +x macchanger.py
python3 macchanger.py
```

## Usage
```
python3 macchanger.py -h -> pulls down a help menu
python3 macchanger.py -i -> specify a netwrok interface
python3 macchanger.py -m -> specify a manual mac address
> NOTE: The tool is still under development and doesn't have a random mac addr list
```

#### Example:
```
python3 macchanger.py -i wlan0 -m xx:xx:xx:xx:xx:xx:
```
