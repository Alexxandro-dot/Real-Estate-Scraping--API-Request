from http.cookies import SimpleCookie
from urllib.parse import urlparse, parse_qs, urlencode
import json

URL='https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.536739%2C%22east%22%3A-122.329919%2C%22south%22%3A37.707608%2C%22north%22%3A37.842913%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22filterState%22%3A%7B%22isForSaleByAgent%22%3A%7B%22value%22%3Afalse%7D%2C%22isForSaleByOwner%22%3A%7B%22value%22%3Afalse%7D%2C%22isNewConstruction%22%3A%7B%22value%22%3Afalse%7D%2C%22isForSaleForeclosure%22%3A%7B%22value%22%3Afalse%7D%2C%22isComingSoon%22%3A%7B%22value%22%3Afalse%7D%2C%22isAuction%22%3A%7B%22value%22%3Afalse%7D%2C%22isPreMarketForeclosure%22%3A%7B%22value%22%3Afalse%7D%2C%22isPreMarketPreForeclosure%22%3A%7B%22value%22%3Afalse%7D%2C%22isForRent%22%3A%7B%22value%22%3Atrue%7D%2C%22isAllHomes%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22isMapVisible%22%3Afalse%7D&includeMap=false&includeList=true'

def cookie_parser():
    cookie_string= 'zguid=23|%246357d797-c41c-4518-99bf-418c1b61ef8c; zgsession=1|d0ecdab5-74da-4911-9e6e-60517e759d28; _ga=GA1.2.1019427332.1584684752; _gid=GA1.2.337213944.1584684752; _pxvid=c826cbe3-6a71-11ea-aa45-0242ac12000b; zjs_user_id=null; zjs_anonymous_id=%226357d797-c41c-4518-99bf-418c1b61ef8c%22; _gcl_au=1.1.75950928.1584684754; KruxPixel=true; DoubleClickSession=true; _fbp=fb.1.1584684754632.698330712; KruxAddition=true; __gads=ID=bd1953a279722338:T=1584685340:S=ALNI_MYC1jYeTR-y5nWH2L2sH-0G1X8QHQ; ki_r=; ki_s=199442%3A0.0.0.0.0; FSsampler=1344456025; GASession=true; JSESSIONID=491498A0403EF2A34DF9978E6750A834; AWSALB=bFIYxMJiOXLZvIFpCEqKBrZ0e5lHfWTvGRN0nn0Cg8is3Vf1k2CdRtovh6p8YGzchZj+IJkhYgY6mEOhpLXcZktEKYu/heWypIGUF/b3J9HYjkp67V3C/fl8th+M; AWSALBCORS=bFIYxMJiOXLZvIFpCEqKBrZ0e5lHfWTvGRN0nn0Cg8is3Vf1k2CdRtovh6p8YGzchZj+IJkhYgY6mEOhpLXcZktEKYu/heWypIGUF/b3J9HYjkp67V3C/fl8th+M; search=6|1587283584551%7Crect%3D37.842913%252C-122.329919%252C37.707608%252C-122.536739%26rid%3D20330%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26sort%3Ddays%26z%3D1%26fs%3D0%26fr%3D1%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%09%01%0920330%09%09%09%090%09US_%09; _px3=cedd9fa9f24bb1588d2f1b456d6afe2521ae66beceb2c90c28d988e2f04b76e3:74VNUxO7MtyRgTkvhz+OLYquFvs9vOKa+S6DEHMOvscP+hJTcxDuIyD/nyACz/SILqOPpmJEqGOnzn4kov82TA==:1000:OEOxD4ZwCYzbxGv/KNSZcv3s6C1hdC20Bhi7rskQrZl8ifvswtrJ+5fmD80Akc8v7ZJoLTndEUiDmLZ5iH13Ey3Eh5vHl1p3EINmv/huPiv+9BJYZ2m600aZg0F0A1ei9NFPF6sulrOleI0Vx91F2J/qzYWBzHtdqkv1lwROvW0=; _gat=1; ki_t=1584685344640%3B1584685344640%3B1584691741227%3B1%3B305'
    cookie=SimpleCookie()
    cookie.load(cookie_string)

    cookies= {}

    for key, morsel in cookie.items():
        cookies[key]= morsel.value

    return cookies
    #print(cookies)
def parse_new_url(url, page_number):
    #in order to access the url string
    url_parsed=urlparse(url)
    query_string=parse_qs(url_parsed.query)
    # print(query_string)
    search_query_state= json.loads(query_string.get('searchQueryState')[0])
    #print(type(search_query_state))

    search_query_state ['pagination']= {"currentPage":page_number}
    #print(search_query_state)
    query_string.get('searchQueryState')[0]= search_query_state
    #print (query_string)
    encoded_qs=urlencode(query_string, doseq=1)
    new_url=f"https://www.zillow.com/search/GetSearchPageState.htm?{encoded_qs}"
    #print(new_url)
    return new_url

    #url pagenumber 3:
parse_new_url(URL,6)