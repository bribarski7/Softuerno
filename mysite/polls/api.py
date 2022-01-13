import requests

data = requests.post("https://tues2022.proxy.beeceptor.com/my/api/test").json()

list = []
for i in range(0, 5):
    list.append(data["data"][i]["temperature"])


class TemperatureApi:
    @staticmethod
    def maxT():
        return max(list)

    @staticmethod
    def minT():
        return min(list)

    @staticmethod
    def averageT():
        return sum(list) / len(list)