import scrapy 
from scrapy.selector import Selector
from project1.items import LehoiItem
class QuotesSpider(scrapy.Spider):
	name = "giaoduc1"
	# start_urls=[
	# 	'https://vnexpress.net/the-gioi','https://vnexpress.net/the-gioi-p2'
	# ]
	start_urls=['https://dantri.com.vn/giao-duc-huong-nghiep/trang-{}.htm'.format(i) for i in range(2,31)]
	start_urls.append('https://dantri.com.vn/giao-duc-huong-nghiep.htm')
	def parse(self, response):
		links= response.xpath('//div[@class="news-item news-item--timeline news-item--left2right"]/div[@class="news-item__content"]/h3[@class="news-item__title"]/a/@href').getall()
		for link in links:
#			print(link)
			yield scrapy.Request('https://dantri.com.vn'+link, callback=self.saveFile)

	def saveFile(self,response):
#		pass
		title = response.xpath('//h1[@class="dt-news__title"]/text()').get()
		description = response.xpath('//div[@class="dt-news__body"]/div/h2/text()').get()
		question = Selector(response).xpath('//div[@class="dt-news__body"]/div[@class="dt-news__content"]')
		content = question.css('p ::text').getall()
		title = str(title).strip()
		description = str(description).strip()
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
			strName = hash(title)
			listContent=''.join(content)
			strContent=title+". "+description+listContent
			# print(strContent)
			nameFile = str(strName)+'.txt'
			text = strContent.replace("\xa0",'').replace("\xad",'').replace('         ','').encode("utf-8")
			f = open('F:/Desktop/Hoctap/DeepLearning/Giaoduc/'+nameFile,'wb')
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

