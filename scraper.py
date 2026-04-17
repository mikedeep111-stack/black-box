import cloudscraper
import json

def run():
    scraper = cloudscraper.create_scraper()
    # مصدر بيانات بديل وأكثر استقراراً للأفلام الحديثة
    url = "https://vidsrc.xyz/movies/latest/page-1.json"
    
    try:
        print("[*] Bypassing security layers...")
        r = scraper.get(url, timeout=20)
        
        if r.status_code == 200:
            data = r.json()
            movies = []
            # جلب البيانات من مصفوفة 'result'
            items = data.get('result', [])
            for item in items:
                movies.append({
                    "title": item.get('title'),
                    "imdb": item.get('imdb_id'),
                    "url": f"https://vidsrc.me/embed/{item.get('imdb_id')}"
                })
            
            with open('database.json', 'w') as f:
                json.dump(movies, f, indent=4)
            print(f"[+] System Online: {len(movies)} movies captured.")
        else:
            print(f"[-] Access Denied. Status: {r.status_code}")

    except Exception as e:
        print(f"[-] Exploit Failed. Reason: {e}")

if __name__ == "__main__":
    run()
