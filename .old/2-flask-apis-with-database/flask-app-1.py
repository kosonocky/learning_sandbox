import requests as req

if __name__ == '__main__':
    response = req.post('http://127.0.0.1:8080/api?key1=value1')
    print(response)
