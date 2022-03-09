import discord
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def remove_tag(tags):   # bs4를 통해 추출한 태그를 인자로 넘겨주어 해당 태그를 지워주는 함수
    for tag in tags:
        tag.decompose()

##################### Naver 날씨 정보 조회 ##########################
async def ballot_counting(ctx):
    url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjFY&x_csa=%7B%22isMapTab%22%3Afalse%7D&pkid=7001&qvt=0&query=%EC%A0%9C20%EB%8C%80%20%EB%8C%80%ED%86%B5%EB%A0%B9%EC%84%A0%EA%B1%B0%20%EA%B0%9C%ED%91%9C%ED%98%84%ED%99%A9"
    
    ## Based on Selenium 
    # driver = init_webdriver()
    # driver.get(url)
    # try:
    #     WebDriverWait(driver=driver, timeout=10).until(EC.presence_of_element_located((By.CLASS_NAME, "cs_weather")))
    # finally:
    #     soup = BeautifulSoup(driver.page_source, "lxml")
    ## end
    
    # Based on requests, bs4
    res = requests.get(url)
    res.raise_for_status()
    print(res);

    # soup = BeautifulSoup(res.text, "html.parser")
    soup = BeautifulSoup(res.text, "lxml")
    print(res);

    # end

    remove_tag(soup.find_all("span", attrs={"class":"blind"}))
    
    rate = soup.find("span", attrs={"class":"number_area"})

    # if rate is not None:
    #     current = rate.find("span", attrs={"class":"todaytemp"}).get_text() + rate.find("span", attrs={"class":"tempmark"}).get_text()
    #     cast = rate.find("p", attrs={"class":"cast_txt"}).get_text()
    # else :
    #     current = "알수없음"
    #     cast = "알수없음"

    # weekly = soup.find("div", attrs={"class":"_weeklyWeather"})
    # am_rain_rate = weekly.find("span", attrs={"class":"point_time morning"}).get_text().strip()
    # pm_rain_rate = weekly.find("span", attrs={"class":"point_time afternoon"}).get_text().strip()

    # atmosphere = ""
    # dust_info = soup.find("div", attrs={"class":"sub_info"})
    # for dust in dust_info.find_all("dt"):
    #     atmosphere += dust.get_text() + " : " + dust.find_next_sibling("dd").get_text() + "\n"
    
    embed = discord.Embed(title = "[제20대 개표 현황]", description = "", color = 0x62c1cc)
    embed.add_field(name = f"개표율", value = f"{rate}", inline = False)
    # embed.add_field(name = "강수 확률", value = f"오전 : {am_rain_rate}, 오후 : {pm_rain_rate}", inline = False)
    # embed.add_field(name = "대기오염정보", value = f"{atmosphere}", inline = False)
    
    await ctx.send(embed = embed)
####################################################################