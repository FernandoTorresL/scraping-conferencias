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

    # Título = //div[contains(@class, "category-version-estenografica")]//h3[@class="entry-title"]/a/text()
    # link = //div[contains(@class, "category-version-estenografica")]//h3[@class="entry-title"]/a/@href

    # next page link = //div[@class="pagenavbar"][2]/div/span[@class="page-numbers current"]/following-sibling::*[1]/@href

    def parse(self, response):

        posts = response.xpath('//div[contains(@class, "category-version-estenografica")]//h3[@class="entry-title"]')

        for post in posts:

            short_title = post.xpath('a/text()').get()
            link = post.xpath('a/@href').get()

            yield {
                'short_title': short_title,
                'link': link
            }

            next_page_button_link = response.xpath('//div[@class="pagenavbar"][last()]/div/span[@class="page-numbers current"]/following-sibling::*[1]/@href').get()

            if next_page_button_link:
                yield response.follow(next_page_button_link, callback=self.parse)


