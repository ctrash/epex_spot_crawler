import scrapy
 
 
class ScrapeTableSpider(scrapy.Spider):
    name = 'scrape-table'
    allowed_domains = ['https://getbootstrap.com/docs/4.0/content/tables']
    start_urls = ['http://https://getbootstrap.com/docs/4.0/content/tables/']
 
 
    def start_requests(self):
        urls = [
            'https://getbootstrap.com/docs/4.0/content/tables',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
 
    def parse(self, response):
        #for row in response.xpath('//*[@class="table-01 table-length-1"]//tbody/tr'):
        for row in response.xpath('//*[@class="table table-striped"]//tbody/tr'):
            i = 0
            yield {
                'time': i+"-"(i+1);
                'buy_volume' : row.xpath('td[1]//text()').extract_first(),
                'sell_volume': row.xpath('td[2]//text()').extract_first(),
                'volume' : row.xpath('td[3]//text()').extract_first(),
                'price' : row.xpath('td[3]//text()').extract_first(),

            }
            i = i+1
