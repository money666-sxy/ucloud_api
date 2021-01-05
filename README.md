# 一、调用 api 接口

**1、安装依赖**

```
yum install python3 -y
yum install git -y
pip3 install ucloud-sdk-python3
git clone https://github.com/ucloud/ucloud-sdk-python3.git
cd ucloud-sdk-python3
python3 setup.py install
```

**2、填写必填**

> 对照 api 文档填写参数（yes 为必填参数）
> 文档 ：https://docs.ucloud.cn/api/

```
git clone https://github.com/money666-sxy/ucloud_api.git
cd ucloud_api/
vim generalization_call.py
```

**3、执行脚本**

```
python3 generalization_call.py
```

# 二、删除 bucket 下的所有文件

> 可以使用此脚本傻瓜式删除 bucket 下的所有文件进而删除 bucket，使用方法如下

**1、安装依赖**

```
git clone https://github.com/ucloud/ufile-sdk-python.git
cd ufile-sdk-python/
python3 setup.py install
pip3 install ufile
cd ..
```

**2、执行脚本**

```
git clone https://github.com/money666-sxy/ucloud_api.git
cd ucloud_api/
python3 all_delect.py
```

执行之后按照提示输入 bucket 名称、公私钥、地区等即可

**3、操作完成回到控制台手动删除 bucket**

> 操作链接：https://console.ucloud.cn/ufile/ufile
