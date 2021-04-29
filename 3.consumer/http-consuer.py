import requests

USER="orthanc"
PASS="orthanc"
HOST="10.163.168.140"
PORT="8042"
BASE_URL="http://{}:{}@{}:{}".format(USER,PASS,HOST,PORT)

x = requests.get(BASE_URL+"/studies")

y = requests.get(BASE_URL+"/studies/8a8cf898-ca27c490-d0c7058c-929d0581-2bbf104d")
print(y.content)
# curl "http://orthanc:orthanc@10.163.168.140:8042/instances/8a8cf898-ca27c490-d0c7058c-929d0581-2bbf104d/file"

# import matplotlib.pyplot as plt
# import pydicom
# ds = pydicom.dcmread("sample.dcm")
# plt.imshow(ds.pixel_array, cmap=plt.cm.bone) 
# plt.show()
