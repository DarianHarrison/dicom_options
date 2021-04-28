on all worker where we wil schedule the pv
1)
```
kubectl get nodes
kubectl create ns l10ns
kubectl config set-context --current --namespace=l10ns
mkdir -p /tmp/orthanc-db
```
2) edit pv,pvc and statefulset

3) apply
```
kubectl apply -f pv
kubectl apply -f pvc
kubectl apply -f statefulset
```

2) go to ui <ip>:8082, authenticate with user:orthanc pass: orthanc

3) manually upload a sample dicom file

4) proove same file do an mdsum on 
```
md5sum /tmp/orthanc-db/3c/8d/3c8dd8fc-8aaa-4435-b5c5-6b1694ac7db2
```
d7ed604ecbc575ab45820f91ba576581

now do an mdusm on uploaded file "CT_small.dcm"
```
md5sum
```
d7ed604ecbc575ab45820f91ba576581

notice it is the same file that is stored in a directory. 

on a k8s master
```

```