import requests
import re
import urllib3

# بۆ ئەوەی ئاگادارکردنەوەی SSL بێزارمان نەکات
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

channels = {
    "Ava Sport": "https://karwan.tv/ava-sport.html",
    "Amozhgary": "https://karwan.tv/amozhgary-tv.html"
}

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1",
}

def get_tokenized_link(url):
    try:
        # لێرە verify=False مان بۆ زیاد کردووە
        response = requests.get(url, headers=headers, timeout=15, verify=False)
        match = re.search(r'(https?://[^\s"\'?]+\.m3u8\?[^"\']*)', response.text)
        if match:
            return match.group(1).replace("&amp;", "&")
    except Exception as e:
        print(f"هەڵە لە کاتی پەیوەندی: {e}")
    return None

def create_m3u():
    try:
        # بەکارهێنانی رێڕەوی تەواو (Full Path) بۆ دڵنیایی
        import os
        file_path = os.path.join(os.getcwd(), "karwan_tv.m3u")
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            for name, url in channels.items():
                link = get_tokenized_link(url)
                if link:
                    f.write(f'#EXTINF:-1, {name}\n{link}\n')
                    print(f"✅ {name} سەرکەوتوو بوو")
        
        print(f"\nفایلەکە لێرە دروست بوو: {file_path}")
    except Exception as e:
        print(f"هەڵە لە دروستکردنی فایل: {e}")

if __name__ == "__main__":
    create_m3u()
