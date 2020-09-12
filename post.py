import urllib.request
import requests
from ucloud.core import auth
import time


def author(d):
    # 签名算法，输出签名
    public_key = ""  # 公私钥 https://console.ucloud.cn/uapi/apikey
    private_key = ""
    cred = auth.Credential(
        public_key,
        private_key,
    )
    signation = cred.verify_ac(d)
    return signation


def main():
    URL = 'https://api.ucloud.cn'
    data = {
        "Action": '',  # action参数在https://docs.ucloud.cn/api/二级页面
        "ProjectId": '',  # https://console.ucloud.cn/dashboard 页面左上角获取
        "Region": "",  # 相关REGION信息。https://docs.ucloud.cn/api/summary/regionlist
        "Zone": "",  # 相关Zone信息。可用区ABCD在region后添加01、02、03、04
        "ResourceId": '',  # 控制台获取资源id

        # "BeginTime": int(time.time()-60),
        # "EndTime": int(time.time()),
        # 开始结束时间控制在一分钟

        # "MetricName.0": "NetworkOutUsage",
        # "MetricName.1": "NetworkIn",
        # "MetricName.2": "NetworkOut",
        # "MetricName.3": "NetworkInUsage",
        # 查询监控的指标项。目前仅允许以下四项：NetworkOut:出向带宽，NetworkIn:入向带宽，NetworkOutUsage:出向带宽使用率，NetworkInUsage:入向带宽使用率

        "ResourceType": '',  # 资源类型
    }  # 具体产品参数在https://docs.ucloud.cn/api/

    signation = author(data)
    data.update({"Signature": signation})

    resp = requests.post(url=URL, data=data)
    print(resp.text)
    print(resp.status_code)


if __name__ == "__main__":
    main()
