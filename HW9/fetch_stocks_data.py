import asyncio
import json
import bs4
import aiohttp
import requests
from datetime import datetime
from lxml import html
from xml.etree.ElementTree import fromstring
from HW9.StockCompany import StockCompany
from HW9.resouces.URLs import *
from HW9.resouces.XPATHs import *
from HW9.resouces.CSSs import *


LATEST_USD_RATE = 0
result = []


async def fetch_response(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def get_company_p_e(url):
    tasks = [asyncio.create_task(fetch_response(BASE_URL + url))]
    for responses in await asyncio.gather(*tasks):
        tree = html.fromstring(responses)
        p_e = tree.xpath(P_E_RATIO_XPATH)
        return str(p_e[0].strip()) if len(p_e) > 0 else 0


async def get_possible_profit(url):
    tasks = [asyncio.create_task(fetch_response(BASE_URL + url))]
    for responses in await asyncio.gather(*tasks):
        tree = html.fromstring(responses)
        container_with_52_low = tree.xpath(WEEK_LOW_52_XPATH)
        container_with_52_high = tree.xpath(WEEK_HIGH_52_XPATH)
        _52_low = float(str(tree.xpath(WEEK_LOW_52_XPATH)[0].text).replace(",", "").strip()) \
            if len(container_with_52_low) > 0 else 0
        _52_high = float(str(tree.xpath(WEEK_HIGH_52_XPATH)[0].text).replace(",", "").strip()) \
            if len(container_with_52_high) > 0 else 0
        profit = 0 if _52_high == 0 else _52_low / _52_high * 100
        return round(profit, 3)


async def get_stock_company(tag: bs4.element.Tag):
    name = tag.select(COMPANY_NAME_CSS).pop().text
    price = round(float(str(tag.select("td")[1].text).replace(",", "").strip().split("\n")[0]) * LATEST_USD_RATE, 3)
    url = tag.select(COMPANY_NAME_CSS).pop().attrs['href']
    pe = round(float(await get_company_p_e(url)), 3)
    possible_profit = await get_possible_profit(url)
    code = tag.select(COMPANY_NAME_CSS).pop().attrs['href'].split("/stocks/")[1].split("-")[0]
    yearly_rate = float(str(tag.select(YEARLY_RATE_CSS).pop().text)[:-1])
    result.append(StockCompany(name, price, url, pe, possible_profit, code, yearly_rate))


def get_latest_usd_rate() -> float:
    r = requests.get(f"{RATE_URL}{datetime.today().strftime('%d/%m/%Y')}")
    element = fromstring(r.content)
    return float(str(next(x for x in element.findall("Valute") if x.attrib['ID'] == 'R01235')[4].text).replace(",", "."))


def write_data_to_json(name_of_file: str, data: list) -> None:
    with open(f'{name_of_file}.json', 'w', encoding='utf-8') as f:
        json.dump(json.dumps([ob.__dict__ for ob in data]), f, ensure_ascii=False,  indent=4)


async def main():
    tasks = [asyncio.create_task(fetch_response(SP500_URL + f"?p={page_no}")) for page_no in range(1, 11)]
    for responses in await asyncio.gather(*tasks):
        companies = bs4.BeautifulSoup(responses)  # response with 50 companies on the single page
        inner_tasks = [asyncio.create_task(get_stock_company(company)) for company in
                       companies.select(COMPANY_ROW_IN_TABLE)]
        await asyncio.gather(*inner_tasks)


if __name__ == "__main__":
    LATEST_USD_RATE = get_latest_usd_rate()
    asyncio.run(main())
    write_data_to_json("top_10_price", sorted(result, key=lambda x: x.price, reverse=True)[:10])
    write_data_to_json("top_10_p_e", sorted(result, key=lambda x: x.pe, reverse=True)[:10])
    write_data_to_json("top_10_yearly_rate", sorted(result, key=lambda x: x.yearly_rate, reverse=True)[:10])
    write_data_to_json("top_10_possible_profit", sorted(result, key=lambda x: x.possible_profit, reverse=True)[:10])
