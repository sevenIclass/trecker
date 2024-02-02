from getmac import get_mac_address as gma
from requests import *
from common.save import save
import subprocess
import socket
import datetime

def getdata():
    hostname = socket.gethostname()
    time = timer()
    date = getdate()
    local_ip = socket.gethostbyname(hostname)
    public_ip = get('http://api.ipify.org').text
    ether_mac = gma(interface="Ethernet 3")
    mac = gma()
    winID = winchester()
    data = {
        'date': date,
        'time': time,
        'desc name': hostname,
        'local ip': local_ip,
        'public ip': public_ip,
        'mac1': mac,
        'mac2': ether_mac,
        'winchester ID': winID,
        'geo': None
    }
    save(data)

def timer():
    a = datetime.datetime.now()
    h = a.hour
    m = a.minute
    if len(str(h)) != 2:
        h = (f'0{a.hour}')
    if len(str(m)) != 2:
        m = (f'0{a.minute}')
    time = (f'{h}:{m}')
    return time


def getdate():
    a = datetime.datetime.now()
    m = a.month
    d = a.day
    if len(str(m)) != 2:
        m = (f'0{a.month}')
    if len(str(d)) != 2:
        d = (f'0{a.day}')
    date = (f'{d}.{m}.{a.year}')
    return date


def winchester():
    a = subprocess.check_output('wmic diskdrive get serialnumber', universal_newlines=True)
    a = str(a).replace('\n','').replace('SerialNumber','')
    return a
