import json

# функция открывает файл
def openFile(fileName):
    try:
        with open(fileName, "r", encoding='utf-8') as f:
            return json.load(f)
    except:
        print("unknown file name")

# функция выполняет поиск по имени и возвращает все указанные аргументы продукта, если такие существуют
def getInfoByName(fileName, name, *args):
    if(len(args) == 0):
        args = "proteins", "fat", "carbohydrates", "calories"
    data = openFile(fileName)

    if data != None:
        answer = []

        for i in data:
            if(i["name"] == name):
                for j in args:
                    try:
                        answer.append({j : [i["foodEnergy"][j]]})
                    except:
                        print(name+" does not have '"+j+"' attribute")
                break

        return answer

# функция возвращает весь список продуктов
def getProductList(fileName):
    data = openFile(fileName)

    if data != None:
        answer = []
        for i in data:
            answer.append(i["name"])
        return answer

# функция принимает аргумент продукта, метод и число, например "calories", ">=", 2 и возвращает все продукты у которые calories >= 2
def getProductsWithOption(fileName, attribute, method, number):
    data = openFile(fileName)

    if data != None:
        answer = []

        if(method == "=="):
            for i in data:
                if(i["foodEnergy"][attribute] == number):
                    answer.append(i)
        elif(method == ">"):
            for i in data:
                if(i["foodEnergy"][attribute] > number):
                    answer.append(i)
        elif(method == "<"):
            for i in data:
                if(i["foodEnergy"][attribute] < number):
                    answer.append(i)
        elif(method == "<="):
            for i in data:
                if(i["foodEnergy"][attribute] <= number):
                    answer.append(i)
        elif(method == ">="):
            for i in data:
                if(i["foodEnergy"][attribute] >= number):
                    answer.append(i)
        elif(method == "!="):
            for i in data:
                if(i["foodEnergy"][attribute] != number):
                    answer.append(i)
        return answer