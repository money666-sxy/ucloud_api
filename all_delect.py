from ufile import filemanager
from ufile import bucketmanager
from ufile import config
import json


def all_delect(public_bucket, public_key, private_key):
    hello_file = filemanager.FileManager(public_key, private_key)
    ret, resp = hello_file.getfilelist(public_bucket)
    while dict(ret)["DataSet"]:
        for i in dict(ret)["DataSet"]:
            cloudfile_name = dict(i)["FileName"]
            hello_file.deletefile(public_bucket, cloudfile_name)
            # print(cloudfile_name)
            ret, resp = hello_file.getfilelist(public_bucket)
    print('删除完成,请移步控制台手动删除bucket')


if __name__ == "__main__":
    public_bucket = input('输入bucket名（不带后缀）：')
    public_key = input('输入公钥：')
    private_key = input('输入私钥：')
    print('地区列表：https://docs.ucloud.cn/api/summary/regionlist')
    region = input('输入区域(cn-bj)：')
    # 设置上传host后缀,外网可用后缀形如 .cn-bj.ufileos.com（cn-bj为北京地区，其他地区具体后缀可见控制台：对象存储-单地域空间管理-存储空间域名）
    config.set_default(uploadsuffix='.{0}.ufileos.com'.format(region))
    # 设置下载host后缀，普通下载后缀即上传后缀，CDN下载后缀为 .ufile.ucloud.com.cn
    config.set_default(downloadsuffix='.ufile.ucloud.com.cn')

    all_delect(public_bucket, public_key, private_key)
