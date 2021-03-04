# -*- coding=utf-8
# appid 已在配置中移除,请在参数 Bucket 中带上 appid。Bucket 由 BucketName-APPID 组成
# 1. 设置用户配置, 包括 secretId，secretKey 以及 Region
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging
import json


class My_txy:

    def __init__(self, 地区='ap-chengdu'):
        with open('mydata.json', 'r', encoding='utf-8') as f:
            js1 = json.load(f)
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        secret_id = js1.get('user_data').get('SecretId')  # 替换为用户的 secretId
        secret_key = js1.get('user_data').get('SecretKey')  # 替换为用户的 secretKey
        region = 地区  # 替换为用户的 Region
        token = None  # 使用临时密钥需要传入 Token，默认为空，可不填
        scheme = 'https'  # 指定使用 http/https 协议来访问 COS，默认为 https，可不填
        config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
        # 2. 获取客户端对象
        self.client = CosS3Client(config)
        self.config = config
        self.scheme = scheme
        self.region = region
        self.bucket = js1.get('tong')
        # 参照下文的描述。或者参照 Demo 程序，详见 https://github.com/tencentyun/cos-python-sdk-v5/blob/master/qcloud_cos/demo.py

# d1 = {'Owner': {'ID': 'qcs::cam::uin/550191537:uin/550191537',
#                 'DisplayName': '550191537'},
#       'Buckets': {'Bucket': [
#                                 {'Name': 'pscly001-1253082658',
#                                     'Location': 'ap-chengdu',
#                                   'CreationDate': '2018-08-26T18:37:07Z'},
#                                  {'Name': 'test1-1253082658',
#                                   'Location': 'ap-chengdu',
#                                   'CreationDate': '2020-12-01T06:43:56Z'},
#                                  {'Name': 'utools-tc-1253082658',
#                                   'Location': 'ap-chengdu',
#                               'CreationDate': '2020-12-01T05:17:16Z'}
#                             ]
#                   }
#       }
# print(d1['Buckets']['Bucket'])



    # 新建桶:
    # Bucket='examplebucket-1250000000'
    # response = client.create_bucket(
    #    Bucket='py-test1'
    # )

    # def 创建桶(self):
    #     # 新的桶名字 = input("请输入新的桶名字:")
    #     response = self.client.create_bucket(
    #         Bucket='pyt1-1250000000'
    #     )
    #     return response

    def 查询桶(self):
        桶 = self.client.list_buckets()
        # print(桶)
        return 桶
    def 查询桶2(self):
        桶数据 = self.查询桶()
        # 桶数据 = {'Owner': {'ID': 'qcs::cam::uin/550191537:uin/550191537', 'DisplayName': '550191537'},
        #     'Buckets': {
        #         'Bucket': [
        #             {'Name': 'pscly001-1253082658', 'Location': 'ap-chengdu', 'CreationDate': '2018-08-26T18:37:07Z'},
        #             {'Name': 'py1-1253082658', 'Location': 'ap-chengdu', 'CreationDate': '2021-03-03T03:23:27Z'},
        #             {'Name': 'utools-tc-1253082658', 'Location': 'ap-chengdu','CreationDate': '2020-12-01T05:17:16Z'}]
        #                 }
        #      }
        for i in 桶数据.get('Buckets').get('Bucket'):
            # i = {'Name': 'pscly001-1253082658', 'Location': 'ap-chengdu', 'CreationDate': '2018-08-26T18:37:07Z'}
            print(f'''桶名称:{i.get('Name')},  地区:{i.get('Location')},  创建日期{i.get('CreationDate')}''')

    # py1-1253082658
    def 查询桶内(self):
        # TODO 我要删除数据，验证一下有没有这个东西
        response = self.client.list_objects(
            Bucket = self.bucket
            # Prefix='folder1'
        )

        桶内_data = {'Name': 'py1-1253082658', 'EncodingType': 'url', 'Prefix': None, 'Marker': None, 'MaxKeys': '1000',
                   'IsTruncated': 'false', 'Contents': [{'Key': '111..png', 'LastModified': '2021-03-03T04:00:11.000Z',
                                                         'ETag': '"2ad5352ef6164072498ad917a1c89671"',
                                                         'Size': '2367444',
                                                         'Owner': {'ID': '1253082658', 'DisplayName': '1253082658'},
                                                         'StorageClass': 'STANDARD'}, {'Key': 'picture.jpg',
                                                                                       'LastModified': '2021-03-03T03:28:59.000Z',
                                                                                       'ETag': '"d8d0c443352a2cbf2655017257b78901"',
                                                                                       'Size': '49736',
                                                                                       'Owner': {'ID': '1253082658',
                                                                                                 'DisplayName': '1253082658'},
                                                                                       'StorageClass': 'STANDARD'},
                                                        {'Key': '壁纸1.png', 'LastModified': '2021-03-03T07:16:35.000Z',
                                                         'ETag': '"731c0843387bc2bd23bee78aa652133e"',
                                                         'Size': '3048186',
                                                         'Owner': {'ID': '1253082658', 'DisplayName': '1253082658'},
                                                         'StorageClass': 'STANDARD'}]}

        return response

    def 查询桶内2(self, type=1):
        '''
        type : 这个东西是查看运行模式，
            如果是1，那就是单纯的查询桶内对象
            如果是2，那就是吧桶内的对象变成列表返回['对象1','对象2']
        '''
        桶数据 = self.查询桶内()
        if type == 1:
            if 桶数据.get('Contents'):
                for i in 桶数据.get('Contents'):
                    # print(i)
                    # print(i.get('Key'))
                    print(f'''文件名称 {i.get('Key')}, 创建日期 {i.get('LastModified')}, 大小约 {int(i.get('Size')) // 1024}kb''')
                return [i.get('Key') for i in 桶数据.get('Contents')]
            print('桶中没有数据')

        if type == 2:
            return [i.get('Key') for i in 桶数据.get('Contents')]
    # 上传：
    # 根据文件大小自动选择简单上传或分块上传，分块上传具备断点续传功能。

    def 上传(self):
        import win32ui
        dlg = win32ui.CreateFileDialog(1)
        dlg.SetOFNInitialDir('C:/1cly')
        是否选择 = dlg.DoModal()   # 选择开始  选了就是1  没选就是2
        if 是否选择 == 2:
            print('未选中文件')
            return None
        文件路径 = dlg.GetPathName()    # 获取路径

        文件名字  = 文件路径.rsplit('\\')[-1]
        response = self.client.upload_file(
           Bucket=self.bucket,
           LocalFilePath=文件路径,   # 本地路径
           Key=文件名字,   # 上传后的名字
           PartSize=1,
           MAXThread=10,
           EnableMD5=False
        )
        print(response['ETag'])

    def 下载(self):
        print('文件默认下载到当前的目录')
        self.查询桶内2()
        要下载的文件名 = input('请输入你要下载的文件名字:')
        response = self.client.download_file(
            Bucket = self.bucket,
            Key = 要下载的文件名,
            DestFilePath = 要下载的文件名  # 这个是下载的位置
        )


        print(response)
        print(response.get('Body'))



    def 删除桶内数据(self):

        # 用户输入文件名，然后我去验证桶中是否有这个文件
        while 1:
            桶内数据 = self.查询桶内2(2)
            删除文件是否对的上 = 1
            print(f'桶内数据{桶内数据}')
            输入_待删除的文件 = input('请输入你要删除的文件，可以使用中文逗号隔开\n:').strip('').rsplit('，')
            for i in 输入_待删除的文件:
                if i not in 桶内数据:
                    print(f'{i} 文件不存在, 请重新输入')
                    删除文件是否对的上 = 0
            if 删除文件是否对的上:
                break


        需要删除的文件 = {'Object': []}
        for i in 输入_待删除的文件:
            需要删除的文件.get('Object').append({'Key': i})
        print('将会删除', 需要删除的文件)
        response = self.client.delete_objects(
            Bucket = self.bucket,
            Delete = 需要删除的文件
            # Delete={
            #     'Object': [
            #         {
            #             'Key': 要删除的文件1
            #         },
            #         {
            #             'Key': 'exampleobject2'
            #         }
            #     ]
            # }
        )
        return response

if __name__ == '__main__':
    a1 = My_txy()
    # a1.删除桶内数据()
    # a1.上传()
    x1 = a1.查询桶内2()
    # print(x1)
    # a1.下载()
    # a1.查询桶2()



