import requests

x = requests.get("http://orthanc:orthanc@10.163.168.140:8042/studies")
print(x.text)

