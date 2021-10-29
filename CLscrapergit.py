# -*- coding: utf-8 -*-
import scrapy

#cleans the text from the body of a listing. Returns a list of words.
def text_clean(text):
    clean_text = []
    for t in text:
        t = (''.join(char for char in t if (char.isalnum() or char == ' '))).lower()
        t = t.split(' ')
        clean_text += t
    return(clean_text)

#Searches for certain keywords and returns listings containing those words.
#Function needs to be modified to find keywords you're interested in.
def keyword_search(text):
    if '' in text
        return(True)
    else:
        return(False)

class HousingSpider(scrapy.Spider):
    name = '' #Name of file
    allowed_domains = ['#region.craigslist.org'] #Page for Craigslist region you're interested in.
    start_urls = [''] #Page containing the listings you want to scrape.

    def parse(self, response):
        listings = response.xpath("//ul[@class='rows']/li")
        for listing in listings:
            link = listing.xpath(".//a/@href").get()

            yield scrapy.Request(url=link, callback=self.parse_listing, meta={'link_url': link})

        next_page_rel = response.xpath(".//a[@class='button next']/@href").getall()
        next_page = f'https://ALLOWED_DOMAINS{next_page_rel[0]}' #navigates to next page of listings. ALLOWED_DOMAINS
        #should be replaced with the domain from allowed_domains variable.
        if next_page:
            yield scrapy.Request(url = next_page, callback=self.parse)

    def parse_listing(self, response):
        link = response.request.meta['link_url']
        time = response.xpath(".//p[@id='display-date']/time/@title").getall()
        text = text_clean(response.xpath(".//section[@id='postingbody']/text()").getall())

        if keyword_search(text) == True:
            yield {
                'time': time,
                'link': link,
            }



    

    
    