import threading
import requests


def get_response(response):
    res = response.get("results")
    print(res)


def get_response2(response):
    res = response.get("results")[0].get("Location")
    print(res)

def get_error():
    print("Error")

def servicio_1(url, success_callback, error_callback):
    res = requests.get(url)
    if res.status_code == 200:
        success_callback(res.json())
    else:
        error_callback()



def servicio_2(url, success_callback, error_callback):
    res = requests.get(url)
    if res.status_code == 200:
        success_callback(res.json())
    else:
        error_callback()


if __name__ == "__main__":
    threading.Thread(target=servicio_1, kwargs={"url":"https://randomuser.me/api", "success_callback":get_response, "error_callback": get_error}).start()
    threading.Thread(target=servicio_2, kwargs={"url":"https://randomuser.me/api/?gender=female", "success_callback":get_response2, "error_callback":get_error}).start()