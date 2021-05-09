import scrapy


class GetTranscriptionsSpider(scrapy.Spider):
    name = 'get_transcriptions'

    start_urls = [
        'https://presidente.gob.mx/sala-de-prensa/'
    ]

    custom_settings = {
        'FEEDS':
        {
            '../data_extracted/data_%(time)s.json': {
                'format': 'json',
                'encoding': 'utf-8',
                'stor_empty': False,
                'fields': None,
                'ident': 4,
                'overwrite': True,
            },
            '../data_extracted/data_%(time)s.csv': {
                'format': 'csv',
                'encoding': 'utf-8',
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

    """ Short title =
            //div[contains(@class, "category-version-estenografica")]
            //h3[@class="entry-title"]/a/text()
        url =
            //div[contains(@class, "category-version-estenografica")]
            //h3[@class="entry-title"]/a/@href
        Next page link =
            //div[@class="pagenavbar"][2]/div
            /span[@class="page-numbers current"]
            /following-sibling::*[1]/@href """

    def parse(self, response):

        posts = response.xpath('//div[contains\
            (@class, "category-version-estenografica")]\
            //h3[@class="entry-title"]')

        for post in posts:
            # Scrape the short_title and link from first posts(4)
            short_title = post.xpath('a/text()').get()
            url = post.xpath('a/@href').get()

            # Go to scrape post details
            yield response.follow(url,
                                  callback=self.parse_post_details,
                                  cb_kwargs={
                                    'short_title': short_title,
                                    'url': url
                                  })

            # Go to next page
            next_page_button_link = response.xpath(
                    '//div[@class="pagenavbar"]\
                    [last()]/div/span[@class="page-numbers current"]\
                    /following-sibling::*[1]/@href').get()
            if next_page_button_link:
                yield response.follow(
                    next_page_button_link,
                    callback=self.parse)

    """ Title: //header[@class="entry-header"]
           /h2[@class="entry-title"]/text()
        Body: //div[@class="entry-content"]/p
              With tags p and strong for the speakers """

    def parse_post_details(self, response, **kwargs):
        short_title = url = None
        if kwargs:
            short_title = kwargs['short_title']
            url = kwargs['url']
        title = response.xpath('//header[@class="entry-header"]/h2[@class="entry-title"]/text()').get()
        body = response.xpath('//div[@class="entry-content"]/p[text()]').getall()

        yield {
            'short_title': short_title,
            'title': title,
            'url': url,
            'body': body
        }
