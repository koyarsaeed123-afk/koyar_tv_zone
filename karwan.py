import requests
import re

# لیستی ئەو کەناڵانەی دەتەوێت لەناو فایلەکەدا بن
# دەتوانیت ناوی تری بۆ زیاد بکەیت بەپێی ئەوەی لە سایتی کاروان تیڤیدا هەیە
channels = {
    "Ava Sport": "https://karwan.tv/ava-sport.html",
    "Amozhgary": "https://karwan.tv/amozhgary-tv.html",
    "KurdSat": "https://karwan.tv/kurdsat.html",
    "Rudaw": "https://karwan.tv/rudaw-tv.html"
}

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1",
    "Referer": "https://karwan.tv/"
}

def get_tokenized_link(url):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        # گەڕان بەدوای لینکی m3u8 کە تۆکنی پێوەیە
        match = re.search(r'(https?://[^\s"\'?]+\.m3u8\?[^"\']*)', response.text)
        if match:
            return match.group(1).replace("&amp;", "&")
    except:
        return None
    return None

def create_m3u():
    with open("karwan_tv.m3u", "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        print("دەستکرا بە کۆکردنەوەی لینکەکان...")
        
        for name, url in channels.items():
            link = get_tokenized_link(url)
            if link:
                f.write(f'#EXTINF:-1, {name}\n')
                f.write(f'{link}\n')
                print(f"✅ لینک بۆ {name} زیادکرا.")
            else:
                print(f"❌ نەتوانرا لینک بۆ {name} بدۆزرێتەوە.")

if __name__ == "__main__":
    create_m3u()
    print("\nفایلی 'karwan_tv.m3u' بە سەرکەوتوویی دروستکرا!")
