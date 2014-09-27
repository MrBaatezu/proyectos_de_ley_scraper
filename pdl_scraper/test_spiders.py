import os
import unittest

from scrapy.http import TextResponse, Request

from pdl_scraper.spiders.proyecto_spider import ProyectoSpider


class TestProyectoSpider(unittest.TestCase):
    def setUp(self):
        self.spider = ProyectoSpider()

    def test_parse(self):
        filename = os.path.join('spiders', 'frontpage.html')
        results = self.spider.parse(fake_response_from_file(filename))
        item = results[0]
        self.assertEqual(u'03838/2014-CR', item['numero_proyecto'])
        self.assertEqual(u'http://www2.congreso.gob.pe/Sicr/TraDocEstProc/CLProLey2011.nsf/Sicr/TraDocEstProc/CLProLey2011.nsf/PAporNumeroInverso/9860D82E1806539D05257D5F007A74B5?opendocument',
                         item['seguimiento_page'],
                         )



def fake_response_from_file(filename, url=None):
    """
    Create a Scrapy fake HTTP response from a HTML file
    @param file_name: The relative filename from the responses directory,
                      but absolute paths are also accepted.
    @param url: The URL of the response.
    returns: A scrapy HTTP response which can be used for unittesting.

    taken from http://stackoverflow.com/a/12741030/3605870
    """
    if not url:
        url = 'http://www.example.com'

    request = Request(url=url)
    if not filename[0] == '/':
        responses_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(responses_dir, filename)
    else:
        file_path = filename

    file_content = open(file_path, 'r').read()

    response = TextResponse(url=url,
        request=request,
        body=file_content)
    return response