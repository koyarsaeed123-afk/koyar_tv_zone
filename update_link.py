import requests
import re
import os

# لێرەدا لێنکی ئەو لاپەڕەیە دابنێ کە ئەم لێنکەی تێدایە (نەک لێنکی m3u8 خۆی)
# چونکە دەمانەوێت سکریپتەکە بچێت لێنکە تازەکە بدۆزێتەوە
SOURCE_PAGE = "لێرە ناونیشانی سێرڤەر یان لاپەڕەی سەرچاوە دابنێ"

def get_live_link():
    try:
        response = requests.get(SOURCE_PAGE, timeout=10)
        # گەڕان بەدوای لێنکی نوێ لە ناو کۆدەکاندا
        match = re.search(r'http://104\.160\.15\.134/[^"\']+\.m3u8', response.text)
        if match:
            new_link = match.group(0)
            # دروستکردنی فایلی M3U بۆ ئەوەی سایتەکەت بیخوێنێتەوە
            with open("playlist.m3u", "w", encoding="utf-8") as f:
                f.write("#EXTM3U\n")
                f.write("#EXTINF:-1, AVA Sport HD\n")
                f.write(new_link)
            print("لێنکەکە بە سەرکەوتوویی نوێ کرایەوە!")
        else:
            print("لێنکەکە نەدۆزرایەوە.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_live_link()
