from urllib.request import urlopen, quote
import json
import pandas as pd

city = pd.read_csv("city.csv")
ak = ""  # 百度地图API密钥


def getlatlng(name):
    url = "http://api.map.baidu.com/geocoding/v3/"
    address = quote(name)
    url_com = url + '?' + 'address=' + address + '&output=json' + '&ak=' + ak
    req = urlopen(url_com)
    data = req.read().decode()
    temp = json.loads(data)
    lat = temp['result']['location']['lat']
    lng = temp['result']['location']['lng']
    print(indexes,lat,lng)
    return lat, lng


for indexes in city.index:
    get_location = getlatlng(city.loc[indexes, 'name'])
    city.loc[indexes,'lat'] = get_location[0]
    city.loc[indexes,'lng'] = get_location[1]

city.to_csv(r'city_latlng.csv',index = False)

WH_lat = 30.598466736400987
WH_lng = 114.31158155473231
origin = format(WH_lat,'.16') + ',' + format(WH_lng,'.16')
print(origin)

# 11：常规路线，即多数用户常走的一条经验路线，满足大多数场景需求，是较推荐的一个策略
def getdistdura(dest_lat, dest_lng):
    url = "http://api.map.baidu.com/routematrix/v2/driving"
    destination = format(dest_lat,'.16') + ',' + format(dest_lng,'.16')
    url_com = url + '?' + '&output=json' + "&origins=" + origin + "&destinations=" + destination + "&ak=" + ak + "&tactics=11"
    req = urlopen(url_com)
    data = req.read().decode()
    temp = json.loads(data)
    dist_text = temp['result'][0]['distance']['text']
    dura_text = temp['result'][0]['duration']['text']
    dist_value = temp['result'][0]['distance']['value']
    dura_value = temp['result'][0]['duration']['value']
    print(dest_lat,dist_text)
    return dist_text, dura_text, dist_value, dura_value


for indexes in city.index:
    dest_lat = city.loc[indexes,'lat']
    dest_lng = city.loc[indexes,'lng']
    get_result = getdistdura(dest_lat,dest_lng)
    city.loc[indexes,'dist_text'] = get_result[0]
    city.loc[indexes,'dura_text'] = get_result[1]
    city.loc[indexes,'dist_value'] = get_result[2]
    city.loc[indexes,'dura_value'] = get_result[3]

print(city.head(5))
city.to_csv(r'city_distdura.csv',index = False)
