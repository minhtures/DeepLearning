import scrapy 
from scrapy.selector import Selector
from project1.items import LehoiItem
class QuotesSpider(scrapy.Spider):
	name = "phapluat"
	# start_urls=[
	# 	'https://vnexpress.net/the-gioi','https://vnexpress.net/the-gioi-p2'
	# ]
	start_urls=['https://vnexpress.net/phap-luat-p{}'.format(i) for i in range(1,45)]
	def parse(self, response):
		links= response.xpath('//article[@class="item-news item-news-common "]/h3[@class="title-news"]/a/@href').getall()
		for link in links:
#			print(link)
			yield scrapy.Request(link, callback=self.saveFile)

	def saveFile(self,response):
#		pass
		title = response.xpath('//h1[@class="title-detail"]/text()').extract()
		description = response.xpath('//div[@class="container"]/div/p[@class="description"]/text()').extract()
		question = Selector(response).xpath('//article[@class="fck_detail "]')
		content = question.css('p ::text').getall()
#		content = response.xpath('//article[@class="item-news item-news-common "]/p[@class="description"]/a/text()').extract()
		# content = list(set(content))
		# content.remove('\n')
		# print(content)
#		print(len(content))
#		print(content)
#		content = response.xpath('//*[@id="chapter"]/div/p/text()').extract()
		# name1 = response.xpath('//article[@class="item-news item-news-common"]/h3[@class="title-news"]/a/text()').extract()
		# # question = Selector(response).xpath('//article[@class="item-news item-news-common "]/p[@class="description"]')
		# # content = question.css('a ::text').getall()
		# content1 = response.xpath('//article[@class="item-news item-news-common"]/p[@class="description"]/a/text()').extract()
#		print(len(content1))
		# for i in range(len(title)):
		if content is not None:
			strName = hash(title[0])
			listContent=''.join(content)
			strContent=title[0]+". "+description[0]+listContent
			# print(strContent)
			nameFile = str(strName)+'.txt'
			text = strContent.replace("\xa0",'').replace("\xad",'').replace('         ','').encode("utf-8")
			f = open('F:/Desktop/Hoctap/DeepLearning/Xe/'+nameFile,'wb')
			f.write(text)
			f.close()

		# for i in range(len(name1)):
		# 	if content1[i] is not None:
		# 		strName = hash(name1[i]);
		# 		strContent=name1[i].strip()+'\n'+content1[i]
		# 		nameFile = str(strName)+'.txt'
		# 		text = strContent.replace("\xa0",'').replace("\xad",'').replace('         ','').encode("utf-8")
		# 		f = open('F:/Desktop/Hoctap/DeepLearning/Data/'+nameFile,'wb')
		# 		f.write(text)
		# 		f.close()

