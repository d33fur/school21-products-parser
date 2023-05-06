import requests
import html

class Downloader:
    # это конструктор он принимает путь к файлу, параметры и метод
    def __init__(self, url, params, method):
        self.url = url
        self.params = params
        self.method = method

    # этот метод возвращает строку с контентом, которую получил по запросу на URL
    def get_html(self):
        if(self.method == "GET"):
            self.response = requests.get(self.url)
        elif(self.method == "POST"):
            self.response = requests.post(self.url, params=self.params)
        else:
            print("uncorrect method name")

    # метод сохраняет полученную строку в файл, путь к которому подается в аргументе
    def save(self, nameOfFile):
        with open(nameOfFile, 'w', encoding='utf-8') as f:
            f.write(html.unescape(self.response.text))