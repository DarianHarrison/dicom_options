
# starter code for consuming dicom files with requests library and orthanc_rest_client

import requests

##########################
# CONSTANTS
##########################

USER="orthanc"
PASS="orthanc"
HOST="10.163.168.140"
PORT="8042"
BASE_URL="http://{}:{}@{}:{}".format(USER,PASS,HOST,PORT)


##########################
# SMOKE TEST
##########################

x = requests.get(BASE_URL+"/instances")
print(x.text)

##########################
# SAVE TO FILE
##########################
from orthanc_rest_client import Orthanc
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth(USER, PASS)
orthanc = Orthanc('http://{}:{}'.format(HOST,PORT), auth=auth, warn_insecure=False)

def save_dcm_file(instance_id):
    fileName = '.'.join([instance_id, "dcm"])
    with open(fileName, 'wb') as dcm:
        for chunk in orthanc.get_instance_file(instance_id):
            dcm.write(chunk)

save_dcm_file("f689ddd2-662f8fe1-8b18180d-ec2a2cee-937917af")


##########################
# PLOT
##########################
import matplotlib.pyplot as plt
import pydicom
ds = pydicom.dcmread("f689ddd2-662f8fe1-8b18180d-ec2a2cee-937917af.dcm")
plt.imshow(ds.pixel_array, cmap=plt.cm.bone) 
plt.show()
