import threading
import queue
import requests

q = queue.Queue()
valid_proxies = []
lock = threading.Lock()

# Open the file at the beginning of the script to create or clear it
with open("Scrapper/scrapy_app/valid_proxy.txt", "w") as valid_file:
    pass

with open("Scrapper/scrapy_app/proxy_list.txt", "r") as f:
    proxies = f.read().split("\n")
    for p in proxies:
        q.put(p)

def check_proxies():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            # res = requests.get("http://ipinfo.io/json", proxies={"http": proxy, "https": proxy}, timeout=3)
            res = requests.get("https://google.com", proxies={"https": proxy}, timeout=3)
            if res.status_code == 200:
                print(proxy)
                with lock:  # Utiliser un verrou pour la sécurité des threads
                    valid_proxies.append(proxy)
                    # Écrire directement dans le fichier à chaque proxy valide trouvé
                    with open("Scrapper/scrapy_app/valid_proxy.txt", "a") as valid_file:
                        valid_file.write(proxy + "\n")
        except:
            continue

for _ in range(10):
    threading.Thread(target=check_proxies).start()
