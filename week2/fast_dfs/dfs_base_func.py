import os

from fdfs_client.client import Fdfs_client

# from config.config import BasePathConfig, FastDfsConfig
from utilss.base_func import get_short_uuid


class FastDfsBase(object):
    """fastDFS 基类
    :param ip: fast ip地址
    :param port: 端口
    :attr tracker_conf: tracker配置
    :attr client: 客户端连接
    """

    def __init__(self, ip, port):
        # self.tracker_conf = get_tracker_conf(BasePathConfig.fast_dfs_conf_path)
        # self.tracker_conf = get_tracker_conf('client.conf')
        self.tracker_conf = {'host_tuple': (ip,), 'port': port, 'timeout': 601, 'name': 'Tracker Pool'}
        self.client = Fdfs_client(self.tracker_conf)

    def upload_filename(self, filename):
        """通过文件路径上传文件
        :param filename: 文件路径
        :return: fast地址
        """
        # 本地上传
        res = self.client.upload_by_filename(filename)
        remote_file_id = res['Remote file_id'].decode()
        return remote_file_id

    def upload_buffer(self, buffer, ext_name):
        """上传缓存
        :param buffer: 缓存
        :param ext_name: 格式
        :return:fast地址
        """
        res = self.client.upload_by_buffer(buffer, file_ext_name=ext_name)
        remote_file_id = res['Remote file_id'].decode()
        return remote_file_id

    def download_file(self, file_id, filename):
        """下载fast文件
        :param file_id: fast地址
        :param filename: 文件名
        :return: none
        """
        # res = self.client.download_to_file(filename, file_id)
        # return res
        buffer_content = self.download_buffer(file_id)
        with open(filename, 'wb') as f:
            f.write(buffer_content)

    def download_buffer(self, file_id):
        """下载fast文件为缓存
        :param file_id: fast地址
        :return: 文件内容
        """
        file_buffer = self.client.download_to_buffer(file_id.encode())
        buffer_content = file_buffer['Content']
        return buffer_content

    def delete_file(self, file_id):
        """删除fast文件
        :param file_id: fast地址
        :return: 删除结果
        """
        res = self.client.delete_file(file_id.encode())
        return res

    def dataframe_to_fast(self, data):
        """dataframe 保存csv到fast
        :param data: dataframe
        :return: none
        """
        file_uuid = get_short_uuid()
        file_path = BasePathConfig.upload_path + file_uuid + '.csv'
        try:
            data.to_csv(file_path, index=False, encoding='utf_8_sig')
            remote_file_id = self.upload_filename(file_path)
        except IOError as e:
            raise e
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
        return remote_file_id


if __name__ == '__main__':
    # python -m cube.database.fast_dfs.dfs_base_func
    fast_dfs = FastDfsBase(FastDfsConfig.host, FastDfsConfig.port)
    # for i in [
    #     'group1/M00/00/2F/CgAugmDAdqqAZdoZAACTKDy9Tnw5073292',
    # ]:
    #     delete_res = fast_dfs.delete_file(i)
    #     print(delete_res)
    # 'group1/M00/00/F1/CgAt52GcMIuAD3tOAAAADvR7W1A689.csv'
    # 'group1/M00/00/F1/CgAt52GjdNKACsrRADTpCCMH5D006.docx'
    # res1 = fast_dfs.upload_filename('/Users/hayley/bmsmart/模型工具相关/孤东8-27-斜14_数据标注.docx')
    res1 = fast_dfs.upload_filename("/Users/hayley/bmsmart/模型工具相关/表格标题预处理-测试文件.docx")
    print(res1)
    # group1/M00/01/BE/CgAugmPaA5yAWGoqABmH3jCYYA868.docx
    # file_id = 'group1/M00/00/F1/CgAt52GjdNKACsrRADTpCCMH5D006.docx'
    # file_id = 'group1/M00/00/47/CgAuN2PaBkqAUHJMABjaN5NJL6o33.docx'
    # fast_dfs.download_file(file_id, '/Users/hayley/Desktop/fast-demo.docx')








