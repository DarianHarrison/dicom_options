
# starter code for consuming dicom files with requests library and orthanc_rest_client

##########################
# CONSTANTS
##########################

USER="orthanc"
PASS="orthanc"
HOST="10.163.168.140"
PORT="8042"

HARD_CODED_FILENAME="f689ddd2-662f8fe1-8b18180d-ec2a2cee-937917af"

##########################
# SMOKE TEST
##########################

import requests
BASE_URL="http://{}:{}@{}:{}".format(USER,PASS,HOST,PORT) # optional replace http for https
x = requests.get(BASE_URL+"/instances", verify=False)
print("files: ",eval(x.text))

##########################
# SAVE TO FILE
##########################
import requests
session = requests.sessions.Session() # New session
session.verify = False   # Disable certificate checking

from beren import Orthanc
from requests.auth import HTTPBasicAuth


REST_BASE_URL='http://{}:{}'.format(HOST,PORT) # optional replace http for https

auth = HTTPBasicAuth(USER, PASS)
orthanc = Orthanc(REST_BASE_URL, auth=auth, warn_insecure=False)

def save_dcm_file(instance_id):
    fileName = '.'.join([instance_id, "dcm"])
    with open(fileName, 'wb') as dcm:
        for chunk in orthanc.get_instance_file(instance_id,session=session):
            dcm.write(chunk)

save_dcm_file(HARD_CODED_FILENAME)


##########################
# PLOT
##########################
import matplotlib.pyplot as plt
import pydicom
ds = pydicom.dcmread(HARD_CODED_FILENAME+".dcm")
plt.imshow(ds.pixel_array, cmap=plt.cm.bone) 
plt.show()