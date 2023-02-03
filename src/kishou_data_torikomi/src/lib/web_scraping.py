import urllib.request
from bs4 import BeautifulSoup
import re

def str2float(weather_data):
    try:
        return float(weather_data)
    except:
        return -999

def str2float_wind(weather_data):
    if(weather_data=='東'):
        return float(1)
    elif(weather_data=='東北東'):
        return float(2)
    elif(weather_data=='北東'):
        return float(3)
    elif(weather_data=='北北東'):
        return float(4)
    elif(weather_data=='北'):
        return float(5)
    elif(weather_data=='北北西'):
        return float(6)
    elif(weather_data=='北西'):
        return float(7)
    elif(weather_data=='西北西'):
        return float(8)
    elif(weather_data=='西'):
        return float(9)
    elif(weather_data=='西南西'):
        return float(10)
    elif(weather_data=='南西'):
        return float(11)
    elif(weather_data=='南南西'):
        return float(12)
    elif(weather_data=='南'):
        return float(13)
    elif(weather_data=='南南東'):
        return float(14)
    elif(weather_data=='南東'):
        return float(15)
    elif(weather_data=='東南東'):
        return float(16)
    else:
        return -999

def time_format(time):
    pattern = re.compile('\d{2}\:\d{2}')
    
    if(not pattern.match(time)):
        if(re.compile('[1][0-9]').match(time) or re.compile('[2][0-4]').match(time)):
            return '%s:00'%(time)
        elif(re.compile('[1-9]').match(time)):
            return '0%s:00'%(time)
        
    return(time)

"""
    ##############################################

    JMA Webpage Scraping 10min a1

    ##############################################
"""
def jma_scraping_10min_a1(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,features="html.parser")
    trs = soup.find("table", { "class" : "data2_s" })

    table_data = []

    for tr in trs.findAll('tr')[3:]:
        tds = tr.findAll('td')
        if tds[1].string == None:
            break
        row = []
        row.append(time_format(tds[0].string))            # data[0] : 時分
        row.append(str2float(tds[1].string)) # data[1] : 降水量
        row.append(str2float(tds[2].string)) # data[2] : 気温
        row.append(str2float(tds[3].string)) # data[3] : 湿度
        row.append(str2float(tds[4].string)) # data[4] : 平均 風速	
        row.append(str2float_wind(tds[5].string)) # data[5] : 平均 風向
        row.append(str2float(tds[6].string)) # data[6] : 最大瞬間 風速
        row.append(str2float_wind(tds[7].string)) # data[7] : 最大瞬間 風向
        row.append(str2float(tds[8].string)) # data[8] : 日照時間

        table_data.append(row)

    return table_data

"""
    ##############################################

    JMA Webpage Scraping hourly a1

    ##############################################
"""
def jma_scraping_hourly_a1(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,features="html.parser")
    trs = soup.find("table", { "class" : "data2_s" })

    table_data = []

    for tr in trs.findAll('tr')[3:]:
        tds = tr.findAll('td')
        if tds[1].string == None:
            break
        row = []
        row.append(time_format(tds[0].string)) # data[0] : 時分
        row.append(str2float(tds[1].string)) # data[1] : 降水量
        row.append(str2float(tds[2].string)) # data[2] : 気温
        row.append(str2float(tds[3].string)) # data[3] : 露点温度
        row.append(str2float(tds[4].string)) # data[4] : 蒸気圧	
        row.append(str2float(tds[5].string)) # data[5] : 湿度
        row.append(str2float(tds[6].string)) # data[6] : 平均風速
        row.append(str2float_wind(tds[7].string)) # data[7] : 風向
        row.append(str2float(tds[8].string)) # data[8] : 日照時間

        table_data.append(row)

    return table_data

"""
    ##############################################

    JMA Webpage Scraping 10min s1

    ##############################################
"""
def jma_scraping_10min_s1(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,features="html.parser")
    trs = soup.find("table", { "class" : "data2_s" })

    table_data = []

    for tr in trs.findAll('tr')[2:]:
        tds = tr.findAll('td')
        if tds[1].string == None:
            break
        
        row = []
        row.append(time_format(tds[0].string))            # data[0] : 時分
        row.append(str2float(tds[1].string)) # data[1] : 気圧現地
        row.append(str2float(tds[2].string)) # data[2] : 気圧水面
        row.append(str2float(tds[3].string)) # data[3] : 降水量
        row.append(str2float(tds[4].string)) # data[4] : 気温
        row.append(str2float(tds[5].string)) # data[5] : 湿度
        row.append(str2float(tds[6].string)) # data[6] : 平均 風速
        row.append(str2float_wind(tds[7].string)) # data[7] : 平均 風向
        row.append(str2float(tds[8].string)) # data[8] : 最大瞬間 風速
        row.append(str2float_wind(tds[9].string)) # data[9] : 最大瞬間 風向
        row.append(str2float(tds[10].string)) # data[10] : 日照時間(分)

        table_data.append(row)

    return table_data

"""
    ##############################################

    JMA Webpage Scraping hourly s1

    ##############################################
"""
def jma_scraping_hourly_s1(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,features="html.parser")
    trs = soup.find("table", { "class" : "data2_s" })

    table_data = []

    for tr in trs.findAll('tr')[2:]:
        tds = tr.findAll('td')
        if tds[1].string == None:
            break
        
        row = []
        row.append(time_format(tds[0].string))  # data[0] : 時分
        row.append(str2float(tds[1].string)) # data[1] : 気圧現地
        row.append(str2float(tds[2].string)) # data[2] : 気圧水面
        row.append(str2float(tds[3].string)) # data[3] : 降水量
        row.append(str2float(tds[4].string)) # data[4] : 気温
        row.append(str2float(tds[5].string)) # data[5] : 露点温度
        row.append(str2float(tds[6].string)) # data[6] : 蒸気圧
        row.append(str2float(tds[7].string)) # data[7] : 湿度
        row.append(str2float(tds[8].string)) # data[8] : 風速
        row.append(str2float_wind(tds[9].string)) # data[9] : 風向 
        row.append(str2float(tds[10].string)) # data[10] : 日照時間 
        row.append(str2float(tds[11].string)) # data[11] : 全天日射量
        
        

        table_data.append(row)

    return table_data