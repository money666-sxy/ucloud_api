from ucloud.core import auth
from ucloud.core import exc
from ucloud.client import Client

import time

client = Client({
    "region": "",  # 相关REGION信息。https://docs.ucloud.cn/api/summary/regionlist
    "project_id": "",  # https://console.ucloud.cn/dashboard 页面左上角获取
    "public_key": "",
    "private_key": "",
    # 公私钥 https://console.ucloud.cn/uapi/apikey
    "base_url": "https://api.ucloud.cn",
})

data = {
    "Zone": "",  # 相关Zone信息。可用区ABCD在region后添加01、02、03、04
    # "ResourceId": '', #控制台获取资源id

    # "BeginTime": int(time.time()-60),
    # "EndTime": int(time.time()),
    # 开始结束时间控制在一分钟

    # "MetricName.0": "NetworkOutUsage",
    # "MetricName.1": "NetworkIn",
    # "MetricName.2": "NetworkOut",
    # "MetricName.3": "NetworkInUsage",
    # 查询监控的指标项。目前仅允许以下四项：NetworkOut:出向带宽，NetworkIn:入向带宽，NetworkOutUsage:出向带宽使用率，NetworkInUsage:入向带宽使用率

    "ResourceType": 'uhost'  # 资源类型
}  # 具体产品参数在https://docs.ucloud.cn/api/

try:
    resp = client.invoke("GetPathXMetric", data)  # 此处填写action
except exc.RetCodeException as e:
    resp = e.json()
