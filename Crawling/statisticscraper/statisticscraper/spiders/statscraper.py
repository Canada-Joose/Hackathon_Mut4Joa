import scrapy
import csv

file = open('stat.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["title","link","date","source"])
class StatisticSpider(scrapy.Spider):
    name = 'StatisticSpider'
    allowed_domains = ['stat.korea.ac.kr']
    start_urls = ['https://stat.korea.ac.kr/stat/community/notice_under.do']

    def parse(self, response):
        
            titles = response.xpath('//*[@id="jwxe_main_content"]/div/div/div/div[2]/ul/li/a/text()').extract()
            links = response.xpath('//*[@id="jwxe_main_content"]/div/div/div/div[2]/ul/li/a/@href').extract()
            dates = response.xpath('//*[@id="jwxe_main_content"]/div/div/div/div[2]/ul/li/span/text()').extract()
            sources = response.xpath('//*[@id="jwxe_main_content"]/div/div/div/div[2]/ul/li/span/i/text()').extract()


            for item in zip(titles, links, dates,sources):
                info = {
                    'title' : item[0].strip(),
                    'link' : item[1].strip(),
                    'date' : item[2].strip(),
                    'source':item[3].strip()
                }

                row = []
                row.append(info['title'])
                row.append(info['link'])
                row.append(info['date'])
                row.append(info['source'])
                writer.writerow(row)
                print("**************************")

                yield info

        