# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['cleveland.craigslist.org']
    start_urls = ['https://cleveland.craigslist.org/search/jjj']

    def parse(self, response):
        jobs = response.xpath('//p[@class="result-info"]')
        for job in jobs:
            relative_url = job.xpath('a/@href').extract_first()
            absolute_url = response.urljoin(relative_url)
            title = job.xpath('a/text()').extract_first()
            address = job.xpath('span[@class="result-meta"]/span[@class="result-hood"]/text()').extract_first("")[2:-1]

            yield Request(absolute_url, callback=self.parse_page, meta={'URL': absolute_url, 'Title': title, 'Address': address})

        relative_next_url = response.xpath('//a[@class="button next"]/@href').extract_first()
        absolute_next_url = response.urljoin(relative_next_url)

        yield Request(absolute_next_url, callback=self.parse)

    def parse_page(self, response):
        url = response.meta.get('URL')
        title = response.meta.get('Title')
        address = response.meta.get('Address')
        description = "".join(line for line in response.xpath('//*[@id="postingbody"]/text()').extract()).strip()
        compensation = response.xpath('//p[@class="attrgroup"]/span/b/text()')[0].extract()
        employment_type = response.xpath('//p[@class="attrgroup"]/span/b/text()')[1].extract()
        yield{'URL': url,
              'Title': title,
              'Address': address,
              'Description': description,
              'Compensation': compensation,
              'Employement Type': employment_type
              }
