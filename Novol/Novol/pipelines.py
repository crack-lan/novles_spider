# -*- coding: utf-8 -*-
import xlwt
from scrapy.pipelines.files import FilesPipeline
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy

class NovolPipeline(object):
    def __init__(self):
        self.workbook=xlwt.Workbook(encoding='utf-8')
        self.sheet=self.workbook.add_sheet(u'小说信息表')
        self.sheet.write(0,0,'小说标题')
        self.sheet.write(0,1,'运行环境')
        self.sheet.write(0,2,'小说语言')
        self.sheet.write(0,3,'小说类型')
        self.sheet.write(0,4,'小说作者')
        self.sheet.write(0,5,'小说大小')
        self.sheet.write(0,6,'更新时间')
        self.sheet.write(0,7,'下载地址')
        self.count=1
    def close_spider(self,spider):
        self.workbook.save(u'奇书小说信息.xls')
    def process_item(self, item, spider):
        self.sheet.write(self.count,0,item['title'])
        self.sheet.write(self.count,1,item['yxhj'])
        self.sheet.write(self.count,2,item['xsyy'])
        self.sheet.write(self.count,3,item['xslx'])
        self.sheet.write(self.count,4,item['xszz'])
        self.sheet.write(self.count,5,item['xsdx'])
        self.sheet.write(self.count,6,item['gxsj'])
        self.sheet.write(self.count,7,item['download_url'][0])
        self.count+=1
        return item
class Mypipline(FilesPipeline):
    def get_media_requests(self,item,info):
        url=item['download_url'][0]
        request = scrapy.Request(
            url=url,
            meta={'item':item}
        )
        return [request]
    def file_path(self, request, response=None, info=None):
        item=request.meta['item']
        title=item['title']
        return '%s.txt'%title