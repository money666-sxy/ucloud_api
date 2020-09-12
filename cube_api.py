import urllib.request
import requests
from ucloud.core import auth
import time
import yaml
import base64

public_key = ""
private_key = ""


def author(d):
    cred = auth.Credential(
        public_key,
        private_key,
    )
    signation = cred.verify_ac(d)
    return signation


# 此为pod的yaml文件
podBase_yaml = '''
apiVersion: v1beta1
kind: Pod
spec:
  containers:
  - name: cubename
    image: 'uhub.service.ucloud.cn/money666_hub/nginx:1.0'
    resources:
      limits:
        memory: 1024Mi
        cpu: 1000m
    volumeMounts: []
  volumes: []
  restartPolicy: Always
'''

pod_Base = base64.b64encode(podBase_yaml.encode())
pod_Base_str = eval(str(pod_Base).strip('b'))

URL = 'https://api.ucloud.cn'
data = {
    "Action": 'CreateCubePod',
    "Region": "cn-bj2",
    "Zone": "cn-bj2-02",  # 相关Zone信息。可用区ABCD在region后添加01、02、03、04
    "ProjectId": 'org-',  # 项目ID https://console.ucloud.cn/
    "VPCId":     "uvnet-",  # 所属vpc  https://console.ucloud.cn/vpc/vpc
    "SubnetId":  "subnet-",  # 详情在创建cube 所属子网查看
    "Pod": pod_Base_str
}  # 具体产品参数在https://docs.ucloud.cn/api/

signation = author(data)
data.update({"Signature": signation})

resp = requests.post(url=URL, data=data)
print(resp.text)
print(resp.status_code)
