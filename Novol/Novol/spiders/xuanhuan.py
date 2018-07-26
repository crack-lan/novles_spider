# -*- coding: utf-8 -*-
import scrapy
from ..items import Books

class XuanhuanSpider(scrapy.Spider):
    name = 'xuanhuan'
    allowed_domains = ['qishu.cc']
    start_urls = ['http://www.qishu.cc/xuanhuan/list1_1.html']
    def parse(self, response):
        ddurls = response.xpath('//span[@class="mainSoftName"]/a/@href').extract()
        for ddurl in ddurls:
            urle='http://www.qishu.cc'+ddurl
            yield scrapy.Request(
                url=urle,
                callback=self.parse_cos
            )
        # next_page=response.xpath('//dfn/a[1]/@href').extract_first('')
        # if next_page:
        #     next_url='http://www.qishu.cc'+next_page
        #     yield scrapy.Request(next_url)
    def parse_cos(self,response):
        title=response.xpath('//dt[@id="downInfoTitle"]/text()').extract_first('')
        info=response.xpath('//dd[@class="downInfoRowL"]/text()').extract()
        result=[]
        for msg in info:
            if '\r'not in msg:
                result.append(msg)
        #如果拿到的数据是6个，取数据，否则全部设置未知
        if len(result)==6:
            yxhj=result[0]
            xsyy=result[1]
            xslx=result[2]
            xszz=result[3]
            xsdx=result[4]
            gxsj=result[5]
        else:
            yxhj=xslx=xsdx=xsyy=xszz=gxsj='未知'
        download_url=response.xpath('//div[@id="downAddress"]/a[2]/@href').extract_first('')
        book=Books()
        book['title']=title
        book['xsyy']=xsyy
        book['yxhj']=yxhj
        book['xslx']=xslx
        book['xszz']=xszz
        book['xsdx']=xsdx
        book['gxsj']=gxsj
        book['download_url']=[download_url]

        yield book