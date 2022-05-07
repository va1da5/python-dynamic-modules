import requests


def get_public_ip():
    ip = requests.get("https://ifconfig.info/ip", verify=False).text.strip()
    return {"ip": ip}
