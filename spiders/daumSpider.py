import scrapy, re

from daum.items import DaumItem
import time

from datetime import datetime


class CommunitySpider(scrapy.Spider):
    name = "daumCrawler"



    def start_requests(self):

        for i in range(1, 31, 1):
            yield scrapy.Request("http://movie.daum.net/moviedb/grade?movieId=1172&type=netizen&page=%d" % i,self.parse_daum1)

        for i in range(1, 62, 1):
            yield scrapy.Request("http://movie.daum.net/moviedb/grade?movieId=2657&type=netizen&page=%d" % i,self.parse_daum2)

        for i in range(1, 335, 1):
            yield scrapy.Request("http://movie.daum.net/moviedb/grade?movieId=50364&type=netizen&page=%d" % i,
                                 self.parse_daum3)

        for i in range(1, 232, 1):
            yield scrapy.Request("http://movie.daum.net/moviedb/grade?movieId=43569&type=netizen&page=%d" % i,self.parse_daum4)



    def parse_daum1(self, response):
        #output = 'movie.txt'
        index = 0
        #f = open(output, 'a', encoding='utf-8')

        for sel in response.xpath('//html/body/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/ul[2]/li'):
            item = DaumItem()

            item['rates'] = int(sel.xpath('div/div[1]/em[@class="emph_grade"]/text()').extract()[0])

            index = index + 1

            print('savingprivateryan\t%d'% item['rates'])
            #print item['rates']
            #f.write('thedarkknight\t%d'% item['rates'])

            time.sleep(1)

            yield item

    def parse_daum2(self, response):
        # output = 'movie.txt'
        index = 0
        # f = open(output, 'a', encoding='utf-8')

        for sel in response.xpath('//html/body/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/ul[2]/li'):
            item = DaumItem()

            item['rates'] = int(sel.xpath('div/div[1]/em[@class="emph_grade"]/text()').extract()[0])

            index = index + 1

            print('forestgump\t%d' % item['rates'])
            # print item['rates']
            # f.write('thedarkknight\t%d'% item['rates'])

            time.sleep(1)

            yield item

    def parse_daum3(self, response):
        # output = 'movie.txt'
        index = 0
        # f = open(output, 'a', encoding='utf-8')

        for sel in response.xpath('//html/body/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/ul[2]/li'):
            item = DaumItem()

            item['rates'] = int(sel.xpath('div/div[1]/em[@class="emph_grade"]/text()').extract()[0])

            index = index + 1

            print('inception\t%d' % item['rates'])
            # print item['rates']
            # f.write('thedarkknight\t%d'% item['rates'])

            time.sleep(1)

            yield item

    def parse_daum4(self, response):
        # output = 'movie.txt'
        index = 0
        # f = open(output, 'a', encoding='utf-8')

        for sel in response.xpath('//html/body/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/ul[2]/li'):
            item = DaumItem()

            item['rates'] = int(sel.xpath('div/div[1]/em[@class="emph_grade"]/text()').extract()[0])

            index = index + 1

            print('thedarkknight\t%d' % item['rates'])
            # print item['rates']
            # f.write('thedarkknight\t%d'% item['rates'])

            time.sleep(1)

            yield item