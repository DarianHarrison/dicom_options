### option1: standalone docker with local volume as backing store

```
mkdir /tmp/orthanc-db
docker run -p 4242:4242 -p 8042:8042 --rm -v /tmp/orthanc-db/:/var/lib/orthanc/db/ jodogne/orthanc:1.9.2
```
```
md5sum 3c8dd8fc-8aaa-4435-b5c5-6b1694ac7db2
```
d7ed604ecbc575ab45820f91ba576581


### option 2: create a statefulset


option 3: ingest

