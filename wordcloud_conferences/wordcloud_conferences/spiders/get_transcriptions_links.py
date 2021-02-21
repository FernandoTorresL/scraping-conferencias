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
        print(response.status, response.headers)
        print('\n\n')

        titles = response.xpath('//div[contains(@class, "category-boletines")]//h4[@class="entry-title"]/a/text()').getall()
        links = response.xpath('//div[contains(@class, "category-boletines")]//h4[@class="entry-title"]/a/@href').getall()
        image_links = response.xpath('//div[contains(@class, "category-boletines")]//a/img/@src').getall()

        print('Títulos: ')
        for title in titles:
            print(f'- {title}')
        print('\n\n')

        print('Links: ')
        for link in links:
            print(f'- {link}')
        print('\n\n')

        print('Images_links: ')
        for image_link in image_links:
            print(f'- {image_link}')
        print('\n\n')

        print('*' * 10)
        print('\n\n')
