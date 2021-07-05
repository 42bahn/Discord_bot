import discord
import requests
from bs4 import BeautifulSoup

def remove_tag(tags):   # bs4를 통해 추출한 태그를 인자로 넘겨주어 해당 태그를 지워주는 함수
    for tag in tags:
        tag.decompose()

##################### Naver 날씨 정보 조회 ##########################
async def naver_weather(ctx):
    url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%98%A4%EB%8A%98%EB%82%A0%EC%94%A8"
    
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
    soup = BeautifulSoup(res.text, "lxml")
    # end

    remove_tag(soup.find_all("span", attrs={"class":"blind"}))
    
    today = soup.find("div", attrs={"class":"main_info"})
    print(today.text)
    if today is not None:
        current = today.find("span", attrs={"class":"todaytemp"}).get_text() + today.find("span", attrs={"class":"tempmark"}).get_text()
        cast = today.find("p", attrs={"class":"cast_txt"}).get_text()
    else :
        current = "알수없음"
        cast = "알수없음"

    # weekly = soup.find("div", attrs={"class":"_weeklyWeather"})
    # am_rain_rate = weekly.find("span", attrs={"class":"point_time morning"}).get_text().strip()
    # pm_rain_rate = weekly.find("span", attrs={"class":"point_time afternoon"}).get_text().strip()

    # atmosphere = ""
    # dust_info = soup.find("div", attrs={"class":"sub_info"})
    # for dust in dust_info.find_all("dt"):
    #     atmosphere += dust.get_text() + " : " + dust.find_next_sibling("dd").get_text() + "\n"
    
    embed = discord.Embed(title = "[오늘의 날씨]",
    description = "", color = 0x62c1cc)
    embed.add_field(name = f"현재 온도 {current}", value = f"{cast}", inline = False)
    # embed.add_field(name = "강수 확률", value = f"오전 : {am_rain_rate}, 오후 : {pm_rain_rate}", inline = False)
    # embed.add_field(name = "대기오염정보", value = f"{atmosphere}", inline = False)
    
    await ctx.send(embed = embed)
####################################################################