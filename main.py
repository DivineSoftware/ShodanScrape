from shodan import Shodan
import os
from sys import exit

banner2 = """
  ██████  ██░ ██  ▒█████  ▓█████▄  ▄▄▄       ███▄    █      ██████  ▄████▄   ██▀███   ▄▄▄       ██▓███  ▓█████  ██▀███  
▒██    ▒ ▓██░ ██▒▒██▒  ██▒▒██▀ ██▌▒████▄     ██ ▀█   █    ▒██    ▒ ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▒██▀▀██░▒██░  ██▒░██   █▌▒██  ▀█▄  ▓██  ▀█ ██▒   ░ ▓██▄   ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
  ▒   ██▒░▓█ ░██ ▒██   ██░░▓█▄   ▌░██▄▄▄▄██ ▓██▒  ▐▌██▒     ▒   ██▒▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒░▓█▒░██▓░ ████▓▒░░▒████▓  ▓█   ▓██▒▒██░   ▓██░   ▒██████▒▒▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒██▒ ░  ░░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░ ▒░▒░▒░  ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒    ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░ ▒ ░▒░ ░  ░ ▒ ▒░  ░ ▒  ▒   ▒   ▒▒ ░░ ░░   ░ ▒░   ░ ░▒  ░ ░  ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░
░  ░  ░   ░  ░░ ░░ ░ ░ ▒   ░ ░  ░   ░   ▒      ░   ░ ░    ░  ░  ░  ░          ░░   ░   ░   ▒   ░░          ░     ░░   ░ 
      ░   ░  ░  ░    ░ ░     ░          ░  ░         ░          ░  ░ ░         ░           ░  ░            ░  ░   ░     
                           ░                                       ░                                                    
"""                        
def init():
    os.system("cls || clear")
    print(banner2)

#config
count = True

key = ""
api = ""
queried = []
init()
try:
    keys = []
    i = 1
    with open("key.txt","r") as keyfile:
        keys = keyfile.read().splitlines()
    for k in keys:
        print(str(i)+". "+k)
        i+=1
    num = input("Choose an API key>>> ").strip()
    try:
        key = keys[int(num)-1]
    except: print("[-] Error: invalid choice"); exit(1)
except:
    print("[-] Error: key.txt not found")
    key = input("Enter your Shodan API key>>> ").strip()

try:
    api = Shodan(key)
except: print("[-] Error: invalid Shodan API key")

def searchloop():
 while True:
  try:
    init()
    query = input("Enter your query>>> ")
    if count:
        print(f"[+] Found {api.count(query)['total']} matches")
    try:
      for banner in api.search_cursor(query):
        queried.append(banner)
        with open("results.txt","a") as results:
            results.write(banner["ip_str"]+"\n")
        print(banner["ip_str"])
    except: pass
    print("[+] Saved IPs to results.txt")
    if input("Show IP details? y/n>>> ").strip().lower() == "y":
        for host in queried:
            print(f'IP:{host["ip_str"]} ISP:{host["isp"]} GEO:{host["location"]["country_name"]} {host["location"]["longitude"]}:{host["location"]["latitude"]}')
    input('Press any key to continue...')
  except KeyboardInterrupt:
        break
  except Exception as e: pass
  
if __name__ == "__main__":
    searchloop()