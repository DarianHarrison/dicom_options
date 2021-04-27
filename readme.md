### option1: standalone docker with local volume as backing store

1)
```
mkdir /tmp/orthanc-db
docker run -p 4242:4242 -p 8042:8042 --rm -v /tmp/orthanc-db/:/var/lib/orthanc/db/ jodogne/orthanc:1.9.2
```

2) manually upload a sample dicom file

3) proove same file do an mdsum on 
```
md5sum /tmp/orthanc-db/3c/8d/3c8dd8fc-8aaa-4435-b5c5-6b1694ac7db2
```
d7ed604ecbc575ab45820f91ba576581

now do an mdusm on uploaded file "CT_small.dcm"
```
md5sum
```
d7ed604ecbc575ab45820f91ba576581

notice it is the same file that is stored in a persistent volume. 

### option 2: create a statefulset

on a k8s master
```
kubectl apply -f 
```




option 3: ingest

