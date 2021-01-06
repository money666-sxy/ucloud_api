import hashlib
import base64

# 使用之前请熟读签名原理
# https://docs.ucloud.cn/api/summary/signature
data = {
    # 按照文档上的‘顺序'填写好必填参数
    # https://docs.ucloud.cn/api/二级页面
    "Action": "CreateUHostInstance",
    "PublicKey": "",
    "Region": "",
    "Zone": "",
    # 关于镜像ID https://console.ucloud.cn/uapi/detail?id=DescribeImage
    # 可以在此接口查看对应地区镜像
    "ImageId": "",
    # 关于password
    # 1、在format后 引号中 输入密码
    # 2、也可以在 第三方网站 https://tool.oschina.net/encrypt?type=3 生成base64 加密之后的密码
    "Password": str(base64.b64encode("{0}".format("").encode('utf-8')))[2:-1],
    "Disks.0.IsBoot": "True",
    "Disks.0.Type": "LOCAL_SSD",
    "Disks.0.Size": "20",
    "LoginMode": "Password"
}
PrivateKey = ""


def create_url(d: dict, PrivateKey):
    url = ''
    for i, j in data.items():
        url = url + i + j
    url = url + PrivateKey
    sha = hashlib.sha1(url.encode('utf-8'))
    Signature = sha.hexdigest()
    print('签名为:', Signature)
    base_url = 'http://api.ucloud.cn/?'
    for k, v in data.items():
        base_url = base_url+k+'='+v+'&'

    finnal_url = base_url+'Signature'+'='+Signature
    print('请求URL为:', finnal_url)
    return finnal_url


if __name__ == "__main__":
    url = create_url(data, PrivateKey)
