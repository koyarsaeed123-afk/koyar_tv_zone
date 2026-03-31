import requests

# ئەمە ئەو لینکە درێژەیە کە لە وایەرشارک دۆزیومانەتەوە
url = "http://104.160.15.134/R3V1jnchKGB2Dkfg__hi__eli2DFfBgx9CXNZhwy3__ih__vl1wsSN3l68YiEGOgi9MhRf9giOCd__hi__y47iHbYnwodZmedCbdZM0zqdN5sd__hi__pHw59wON5qgvFhy9UL__hi__b9bamq4kd2hEnFQQ8ZTguB076a89cSzAca__ih__4a8Q1XEx2iGtRHKh0snlF56bVp4sX5G2KeatpbLGOi4__hi__oRTok0yne27mDC65whUoleu37TMeVfSgM1P__hi__LTWZW5NcWNbOzT6cNH4D54a4f52KP00cgRWLjbOvxa1u1HEbAgKzRDDftaqcvrGDPS5__hi__Ys==---/cache/AVA-Sport-HD-LB/m3u8/AVA-Sport-HD_tracks-v1a1_mono.m3u8"

# ئەم زانیارییانە زۆر گرنگن بۆ ئەوەی سێرڤەرەکە ڕێگەمان بدات لینکەکە وەربگرین
headers = {
    'User-Agent': 'And$MyTV', 
    'Host': '104.160.15.134',
    'Connection': 'Keep-Alive'
}

def get_new_link():
    try:
        # لێرەدا وەک ئەوەی مۆبایلەکە بین، داواکاری دەنێرین بۆ سێرڤەر
        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            with open("playlist.m3u", "w", encoding="utf-8") as f:
                f.write("#EXTM3U\n")
                f.write("#EXTINF:-1, AVA Sport HD\n")
                f.write(url)
            print("سەرکەوتوو بوو: فایلی M3U دروست کرا.")
        else:
            print(f"سێرڤەر وەڵامی نەدایەوە. کۆد: {response.status_code}")
    except Exception as e:
        print(f"کێشەیەک لە سکریپتەکە هەیە: {e}")

if __name__ == "__main__":
    get_new_link()
