from download import Downloader
from parse import *
from data import *

def process(url, web_page_path=None, data_path=None):
    params = {'page': '1'}
    downloader = Downloader(url, params, "GET")
    downloader.get_html()
    downloader.save(web_page_path)
    parser = Parser(web_page_path)
    parser.parse()
    parser.save(data_path)
    data1 = getProductList(data_path) # посмотрим список продуктов
    data2 = getInfoByName(data_path, "7up", "proteins", "calories", "calories", "fat") # выведем параметры 7up
    data3 = getProductsWithOption(data_path, "proteins", ">", 1) # найдем все продукты с proteins > 1

    downloader = Downloader(url, params, "POST")
    downloader.get_html()
    downloader.save(web_page_path)
    parser = Parser(web_page_path)
    parser.parse()
    parser.save(data_path)
    data4 = getProductList(data_path) # посмотрим список продуктов
    data5 = getInfoByName(data_path, 'Яйцо куриное (вареное вкрутую)', 'proteins', 'fat') # выведем параметры куриного яйца
    data6 = getProductsWithOption(data_path, "fat", "<=", 10) # найдем все продукты с fat <= 10
    return data1, data2, data3, data4, data5, data6

temp = process("https://calorizator.ru/product/all", "PARSED_FILE.html", "PARSED_FILE.json")
for i in temp:
    print(i)
    print("")
