import scrapy

class GetTranscriptionsSpider(scrapy.Spider):
    name = 'get_transcriptions'

    start_urls = [
        'https://presidente.gob.mx/sala-de-prensa/'
    ]

    custom_settings = {
        'FEEDS': {
            'transcriptions_links.json': {
                'format': 'json',
                'encoding': 'utf8',
                'stor_empty': False,
                'fields': None,
                'ident': 4,
                'overwrite': True,
            },
        },
        'CONCURRENT_REQUESTS': 24,
        'MEMUSAGE_LIMIT_MB': 2048,
        'MEMUSAGE_NOTIFY_MAIL': ['fertorresmx@gmail.com'],
        'ROBOTSTXT_OBEY': True,
        'USER_AGENT': 'FerTorres'
    }

    def parse(self, response):
        # Short title = //div[contains(@class, "category-version-estenografica")]//h3[@class="entry-title"]/a/text()
        # url = //div[contains(@class, "category-version-estenografica")]//h3[@class="entry-title"]/a/@href
        # Next page link = //div[@class="pagenavbar"][2]/div/span[@class="page-numbers current"]/following-sibling::*[1]/@href

        posts = response.xpath('//div[contains(@class, "category-version-estenografica")]//h3[@class="entry-title"]')

        for post in posts:
            short_title = post.xpath('a/text()').get()
            url = post.xpath('a/@href').get()

            yield response.follow( url, callback=self.parse_url, cb_kwargs={'short_title': short_title, 'url': url} )

            next_page_button_link = response.xpath('//div[@class="pagenavbar"][last()]/div/span[@class="page-numbers current"]/following-sibling::*[1]/@href').get()
            if next_page_button_link:
                yield response.follow(next_page_button_link, callback=self.parse)

    def parse_url(self, response, **kwargs):
        # Title: //header[@class="entry-header"]/h2[@class="entry-title"]/text()
        #Body: //div[@class="entry-content"]/p #With tags p and strong for the speakers

        short_title = kwargs['short_title']
        title = response.xpath('//header[@class="entry-header"]/h2[@class="entry-title"]/text()').get()
        url = kwargs['url']
        body = response.xpath('//div[@class="entry-content"]/p').getall()

        yield {
            'short_title': short_title,
            'title': title,
            'url': url,
            'body': body
        }
