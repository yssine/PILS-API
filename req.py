import requests


url="http://greengardian-api.onrender.com/"


data={
  "soil": 38,
  "temp": 25.4,
  "hum": 69.6,
  "light": 1862.0
}
x = requests.post(url+"esp/d5251247-50bc-4881-90a3-2c737308be17", json = data)

print(x.text)


x = requests.get(url+"get-val/?uuid=d5251247-50bc-4881-90a3-2c737308be17",)

print(x.text)

# myobj = {'uuid': 'd5251247-50bc-4881-90a3-2c737308be17'}

