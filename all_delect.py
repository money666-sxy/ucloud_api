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
        #     # while cloudfile_name:
            hello_file.deletefile(public_bucket, cloudfile_name)
            # print(cloudfile_name)
            ret, resp = hello_file.getfilelist(public_bucket)
    print('删除完成,请移步控制台手动删除bucket')


if __name__ == "__main__":
    public_bucket = input('输入bucket名（不带后缀）：')
    public_key = input('输入公钥：')
    private_key = input('输入私钥：')
    region = input('输入区域：')

    all_delect(public_bucket, public_key, private_key)
