from download import Downloader
from parse import *

def process(url, web_page_path=None, data_path=None):
    for i in range(0,80):
        try:
            params = {'page': f'{i}'}

            downloader = Downloader(url, params, "POST")
            downloader.get_html()
            downloader.save(web_page_path)
            parser = Parser(web_page_path)
            parser.parse()
            parser.save(f"{i}.json")
            print(str(i)+" скачалась")
        except:
            print(str(i)+" не скачалась")


process("https://calorizator.ru/product/all", "PARSED_FILE.html", "PARSED_FILE.json")


