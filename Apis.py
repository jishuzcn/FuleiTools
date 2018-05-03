#!/usr/bin/python
# -*- coding: utf-8 -*-
import LoginFulei
from bs4 import BeautifulSoup
import requests
import re
import furl
from Tools import FuleiTool


class Spider(object):

    def __init__(self):
        super().__init__()
        self.login = LoginFulei.LoginFulei()
        self.tools = FuleiTool()

    def isLogin(self):
        return self.login.isLogin()

    def getAllHolderOrDealer(self, HolderFlag=True):
        """
        得到所有商户或者经销商,默认为商户
        :param HolderFlag: 是否是商户,默认为商户
        :return: 返回dict集合

        """
        # 这里只获取彩票机首页的html信息
        htm = self.getHtml()
        soup = BeautifulSoup(htm, "lxml")
        if HolderFlag:
            select = soup.find(id='holderId')
        else:
            select = soup.find(id='dealerId')
        option = select.findAll("option")
        data = {}
        for o in option:
            if HolderFlag:
                if not o.text == '商户选择':
                    data.setdefault(o.attrs['value'], o.text)
            else:
                if not o.text == '经销商选择':
                    data.setdefault(o.attrs['value'], o.text)
        return data

    def get_lottery_name(self, id):
        """
        得到彩票机里存放的彩票种类名
        :return: str字符串
        """
        html = self.getHtml(self.tools.generate_url(True, type='eType1', id=id))
        soup = BeautifulSoup(html, "lxml")
        return soup.tbody.tr.findAll('td')[5].text

    def getHtml(self, url=None):
        """
        得到某一页的Html信息
        :param url: url链接
        :return: html文本信息
        """
        header = self.login.flheader.getshjList()
        header.setdefault('Cookie', 'PHPSESSID=%s' % self.login.getCookie())
        htm = ""
        if url is None:
            while True:
                try:
                    htm = self.login.session.get(r"http://www.kadawo.com/fulei/index.php/equipment/shjList",
                                                 headers=header,
                                                 allow_redirects=False)
                    break
                except (requests.exceptions.ChunkedEncodingError, requests.ConnectionError) as e:
                    # logging.error("There is a error: %s" % e)
                    print("error")
                    continue
        else:
            while True:
                try:
                    htm = self.login.session.get(url, headers=header, allow_redirects=False)
                    break
                except (requests.exceptions.ChunkedEncodingError, requests.ConnectionError) as e:
                    # logging.error("There is a error: %s" % e)
                    continue
        return htm.text

    # 形成富文本，参数是文本内容和字体颜色
    def getmsg(self, themsg, thecolor):
        msg = '<html><head/><body><p><span style=" font-family:Microsoft YaHei;font-size:9pt; color:{};">{}</span></p></body></html>'.format(
            thecolor, themsg)
        return msg
