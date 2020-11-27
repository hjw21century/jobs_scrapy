import scrapy
from freelancer  import FreelancerItem
from datetime import timedelta, date
import sys

class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['www.freelancer.com/jobs/']
    start_urls = ['https://www.freelancer.com/jobs//']
    base_urls = 'https://www.freelancer.com/'

    def __init__(self):
        for index in range(3):
            if index == 0 or index == 1:
                pass
            else:
                self.start_urls.append('https://www.freelancer.com/jobs/{}/'.format(index))
    
    def parse(self, response):
    	sel=scrapy.Selector(response)
    	projects=sel.css('.JobSearchCard-item')
    	for project in projects:
            try:
                freelancerItem = FreelancerItem()
                freelancerItem['head'] = self.base_urls + project.css('.JobSearchCard-primary-heading').css('a::text').extract()[0].lstrip('\n ').rstrip('\n ')
                freelancerItem['detailurl'] = project.css('.JobSearchCard-primary-heading').css('a::attr(href)').extract()[0]
                deadline = project.css('.JobSearchCard-primary-heading').css('.JobSearchCard-primary-heading-days').css('::text').extract()[0]
                freelancerItem['deadline'] = date.today() +  timedelta(days = int(deadline.split('days')[0].replace(' ', '')))
                freelancerItem['description'] = project.css('.JobSearchCard-primary-description').css('::text').extract()[0].lstrip('\n ').rstrip('\n ')
                freelancerItem['tags'] =  '|'.join(filter(lambda item:not item.startswith('\n '), project.css('.JobSearchCard-primary-tags').css('::text').extract()))
                freelancerItem['price'] = project.css('.JobSearchCard-primary-price').css('::text').extract()[0].lstrip('\n ').rstrip('\n ')
                yield freelancerItem
            except Exception as excep:
                print('freelancerItem except:{} lineno:{}'.format(excep, sys.exc_info()[-1].tb_lineno))
                continue

    # def start_requests(self):
    #     for index in range(2):
    #         if index == 0:
    #             url = 'https://www.freelancer.com/jobs/'
    #         else:
    #             url = 'https://www.freelancer.com/jobs/{}/'.format(index)
    #         yield scrapy.Request(url, meta = {
    #                             'dont_redirect': True,
    #                             'handle_httpstatus_list': [302]
    #                         },
    #                         callback=self.parse, dont_filter=True)
    	

