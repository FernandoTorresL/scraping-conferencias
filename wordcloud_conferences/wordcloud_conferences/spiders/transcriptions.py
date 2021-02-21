import scrapy

class GetTranscriptionsLinksSpider(scrapy.Spider):
    name = 'get_transcriptions_links'

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

    # Título = //div[contains(@class, "category-boletines")]//h4[@class="entry-title"]/a/text()
    # link = //div[contains(@class, "category-boletines")]//h4[@class="entry-title"]/a/@href
    # Image_link = //div[contains(@class, "category-boletines")]//a/img/@src'

    def parse(self, response):
        print('*' * 10)
        print('\n\n')

        for transcription in response.xpath('//div[contains(@class, "category-boletines")]//h4[@class="entry-title"]'):
            title = transcription.xpath('a/text()').get()
            link = transcription.xpath('a/@href').get()
            print(dict(title=title, link=link))
            yield {
                'title': title,
                'link': link
            }

