#!usr/bin/python
# -*- coding: utf-8 -*-
'''
工具类  ---  那些需要重复使用的代码块
'''
import re
import time
import FuleiHeader
import LoginFulei

class FuleiTool(object):
    def __init__(self):
        self.header = FuleiHeader.FuleiHeader()
        pass

    @staticmethod
    def getHash(htm):
        """
        :param: html文本信息
        :return: str字符串
        """
        hash_pattern = re.compile(r'<input type="hidden" name="__hash__" value="(.*?)"')
        _hash = re.findall(hash_pattern,htm)[0]
        return _hash

    # tim = '2018-04-25'
    @staticmethod
    def timeToTimestamp(tim):
        # 转换成时间数组
        timeArray = time.strptime(tim,"%Y-%m-%d")
        # 转换成时间戳
        return int(time.mktime(timeArray))

    @staticmethod
    def get_startTime(timestamp):
        t = time.localtime(float(timestamp))
        return int(time.mktime(time.strptime(time.strftime('%Y-%m-%d 00:00:00', t), '%Y-%m-%d %H:%M:%S')))

    @staticmethod
    def get_endTime(timestamp):
        t = time.localtime(float(timestamp))
        return int(time.mktime(time.strptime(time.strftime('%Y-%m-%d 23:59:59', t), '%Y-%m-%d %H:%M:%S')))

    @staticmethod
    def timestampToTime(timestamp):
        x = time.localtime(float(timestamp))
        return time.strftime("%Y-%m-%d",x)

    #得到当天0点的时间戳
    @staticmethod
    def getStartTimeOfToday():
        t = time.localtime(time.time())
        return int(time.mktime(time.strptime(time.strftime('%Y-%m-%d 00:00:00', t),'%Y-%m-%d %H:%M:%S')))

    #得到当天23点59的时间戳
    @staticmethod
    def getEndTimeOfToday():
        t = time.localtime(time.time())
        return int(time.mktime(time.strptime(time.strftime('%Y-%m-%d 23:59:59', t),'%Y-%m-%d %H:%M:%S')))

    '''
    因为后台要用'/'作为传输的分隔符，所以要转换一下url链接
    把所有'?'、'='、'&'符转换为'/'
    '''
    @staticmethod
    def urlReplace(url):
        if not url.find('?&') == -1:
            url = url.replace('?&','/')
        if not url.find('?') == -1:
            url = url.replace('?','/')
        if not url.find('=') == -1:
            url = url.replace('=','/')
        if not url.find('&') == -1:
            url = url.replace('&','/')
        return url


    def getMoney(self,eid, startTime, endTime):
        """
        :param eid: 设备id
        :param startTime: 开始时间，时间戳格式
        :param endTime: 结束时间，时间戳格式
        :return: 服务器会返回[次数，金额]
        """
        url = "http://www.kadawo.com/fulei/index.php/equipment/hjslAjax"
        login = LoginFulei.LoginFulei()
        header = self.header.postHjsl()
        header.setdefault('Cookie', 'PHPSESSID=%s' % login.getCookie())
        post_data = "did=" + eid + "&startTime=" + str(startTime) + "&endTime=" + str(endTime)
        result = login.session.post(url, data=post_data, headers=header)
        return result.text.strip('[]').split(',')

    def getTotalPage(self, htm):
        """
        :param htm:
        :return: 返回总页数
        """
        total_page_pattern = re.compile(r"1/(.*?) 页")
        total = re.findall(total_page_pattern, htm)[0]
        return total

    def generate_url(self, single=False, **kwargs):
        """
        warning!!! 如果不是访问首页必须要传startTime与endTime
        :param kwargs: type,szType,startTime,endTime,__hash__,
              type = signIn、eType1、refund、eType1information
        :return: str
        首页
        eType1/id/571/__hash__/hash/
        首页条件查询
        eType1/id/571/startTime/2018-03-01/endTime/2018-04-01/__hash__/hash/
        出货详情
        refund/id/571/startTime/2018-03-01/endTime/2018-04-01/__hash__/hash/
        现金收支
        eType1information/id/571/szType/xj/startTime/2018-03-01/endTime/2018-04-01/__hash__/hash/
        在线收支
        eType1information/id/571/szType/zx/startTime/2018-03-01/endTime/2018-04-01/__hash__/hash/
        导出单个设备的excel文件数据
        equipment/outPut/page/eType1information/szType/zx/did/867793034475113/startTime/2018-03-01/endTime/2018-04-01
        """
        url = "http://www.kadawo.com/fulei/index.php/equipment/"
        if single is True:
            url = url + kwargs['type'] + "/id/" + kwargs['id'] + "/"
        elif 'szType' in kwargs.keys():
            url = url + kwargs['type'] + "/id/" + kwargs['id'] + "/szType/" + kwargs['szType'] + \
                  "/startTime/" + kwargs['startTime'] + "/endTime/" + kwargs['endTime'] + "/__hash__/" + kwargs[
                      'hash'] + "/"
        else:
            url = url + kwargs['type'] + "/id/" + kwargs['id'] + "/startTime/" + kwargs['startTime'] + \
                  "/endTime/" + kwargs['endTime'] + "/__hash__/" + kwargs['hash'] + "/"

        return url