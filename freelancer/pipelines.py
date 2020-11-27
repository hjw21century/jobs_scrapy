# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

count = 0
class FreelancerPipeline:
    def process_item(self, item, spider):
        global count
        count = count + 1
        print('------------------------[{}]----------------------'.format(count))
        print('|                                                 |')
        print('head: ' + item['head'])
        print('detailurl: ' + item['detailurl'])
        print('deadline: ' + item['deadline'].strftime('%Y%m%d'))
        print('description: ' + item['description'])
        print('tags: ' + item['tags'])
        print('price: ' + item['price'])


        
        file = open('alljobs.txt','a') 
        file.writelines('------------------------[{}]----------------------'.format(count)) 
        file.writelines('\n') 
        file.writelines('head: ' + item['head']) 
        file.writelines('\n') 
        file.writelines('detailurl: ' + item['detailurl']) 
        file.writelines('\n') 
        file.writelines('deadline: ' + item['deadline'].strftime('%Y%m%d')) 
        file.writelines('\n') 
        file.writelines('description: ' + item['description']) 
        file.writelines('\n') 
        file.writelines('tags: ' + item['tags']) 
        file.writelines('\n')
        file.writelines('price: ' + item['price']) 
        file.writelines('\n')
        file.writelines('price: ' + item['price']) 
        file.writelines('\n')
        file.close() 
        return item
