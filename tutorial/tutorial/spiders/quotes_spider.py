import scrapy
from datetime import date, timedelta

today = date.today()
d = date.today() - timedelta(days=1)
d1 = today.strftime("%Y-%m-%d")
d2 = d.strftime("%Y-%m-%d")
year = 2021
month = 3
day = 9

date = d1
date_1 = d2
the_url = 'https://www.epexspot.com/en/market-data?market_area=DE-LU&trading_date='+date_1+'&delivery_date='+date+'&underlying_year=&modality=Auction&sub_modality=DayAhead&product=60&data_mode=table&period='


class ScrapeTableSpider(scrapy.Spider):
    name = 'scrape-table'
    print(date)
    print(date_1)

    allowed_domains = ['https://www.epexspot.com/en/market-data?market_area=DE-LU&trading_date='+date_1+'&delivery_date='+date+'&underlying_year=&modality=Auction&sub_modality=DayAhead&product=60&data_mode=table&period=']
    start_urls = ['http://https://www.epexspot.com/en/market-data?market_area=DE-LU&trading_date='+date_1+'&delivery_date='+date+'&underlying_year=&modality=Auction&sub_modality=DayAhead&product=60&data_mode=table&period=']
    
 
    def start_requests(self):
        #the_url = 'https://www.epexspot.com/en/market-data?market_area=DE-LU&trading_date='+date_1+'&delivery_date='+date+'&underlying_year=&modality=Auction&sub_modality=DayAhead&product=60&data_mode=table&period='
        urls = [
            the_url,
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
 
    def parse(self, response):
        #for row in response.xpath('//*[@class="table-01 table-length-1"]//tbody/tr'):
        i=0
        for row in response.xpath('//*[@class="table-01 table-length-1"]//tbody/tr'):
            
            
            yield {
                'date' : str(date),
                'hours' : str(i)+' - '+str(i+1),
                'buy_volume' : row.xpath('td[1]//text()').extract_first(),
                'sell_volume': row.xpath('td[2]//text()').extract_first(),
                'volume' : row.xpath('td[3]//text()').extract_first(),
                'price' : row.xpath('td[4]//text()').extract_first(),

            }
            i=i+1
