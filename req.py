import requests


url="http://localhost:6969/"
# myobj = {'uuid': 'd5251247-50bc-4881-90a3-2c737308be17'}

x = requests.get(url+"get-val/?uuid=d5251247-50bc-4881-90a3-2c737308be17",)

print(x.text)


data={
  "soil": 58,
  "temp": 28.4,
  "hum": 69.6,
  "light": 862.0
}
x = requests.post(url+"esp/d5251247-50bc-4881-90a3-2c737308be17", json = data)

print(x.text)