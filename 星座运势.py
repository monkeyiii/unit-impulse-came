import requests
from bs4 import BeautifulSoup

def xingzuoyunshi(xing):
    (xingzuo, zuo) = xing
    yunshia= "https://www.d1xz.net/yunshi/today/Aries/"
    yunshiw= yunshia[:34] + xingzuo
    req = requests.get(url=yunshiw)
    req.encoding = "utf-8"
    html = req.text
    soup = BeautifulSoup(req.text, features="html.parser")
    company_items = soup.find_all("div", class_="txt")
    for company_item in company_items:
        dd = company_item.text.strip()
    return dd



