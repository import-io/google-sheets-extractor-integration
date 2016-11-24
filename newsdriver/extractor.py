#
# Copyright 2016 Import.io
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import requests
import os
import logging

logger = logging.getLogger(__name__)


class Extractor(object):

    def __init__(self, extractor_id):
        self._extractor_id = extractor_id
        self._api_key = os.environ['IMPORT_IO_API_KEY']


class ExtractorGet(Extractor):

    def __init__(self, extractor_id):
        super(ExtractorGet, self).__init__(extractor_id)

    def get(self):

        url = "https://store.import.io/store/extractor/{0}".format(self._extractor_id)

        querystring = {
            "_apikey": self._api_key
        }

        headers = {
            'cache-control': "no-cache",
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        logger.debug(response.text)
        return response.json()


class ExtractorGetUrlList(Extractor):

    def __init__(self, extractor_id):
        super(ExtractorGetUrlList, self).__init__(extractor_id)

    def get(self):
        """
        Call the Extractor API to return the URLs associated with an extractor
        :return:  array of str
        """
        api = ExtractorGet(extractor_id=self._extractor_id)

        extractor = api.get()

        url = "https://store.import.io/store/extractor/{0}/_attachment/urlList/{1}".format(
            self._extractor_id, extractor['urlList'])
        querystring = {
            "_apikey": self._api_key
        }

        headers = {
            'accept-encoding': "gzip",
            'cache-control': "no-cache",
        }
        logger.debug("url: ".format(url))
        response = requests.request("GET", url, headers=headers, params=querystring)

        logger.debug(response.text)
        return response.text.split('\n')


class ExtractorPutUrlList(Extractor):

    def __init__(self, extractor_id):
        super(ExtractorPutUrlList, self).__init__(extractor_id)

    def put(self, urls):
        """
        Calls the Extractor API with a list of URLs to associate with an extractor
        :param urls: array of str containing the URLs
        :return: None
        """
        url = "https://store.import.io/store/extractor/{0}/_attachment/urlList".format(self._extractor_id)

        querystring = {
            "_apikey": self._api_key
        }

        headers = {
            'content-type': "text/plain"
        }

        data = "\n".join(urls)

        response = requests.request("PUT", url, data=data, headers=headers, params=querystring)


class ExtractorStart(Extractor):

    def __init__(self, extractor_id):
        super(ExtractorStart, self).__init__(extractor_id)

    def start(self):
        pass


class ExtractorStatus(Extractor):
    """
    Returns the status of extractor which is one of the following states:

    1. CANCELED
    2. FINISHED
    3. STARTED

    """

    def __init__(self, extractor_id):
        super(ExtractorStatus, self).__init__(extractor_id)

    def get(self):
        url = "https://store.import.io/store/extractor/_search"

        querystring = {"_sort": "_meta.creationTimestamp",
                       "_mine": "true",
                       "q": "_missing_%3Aarchived%20OR%20archived%3Afalse",
                       "_page": "1",
                       "_apikey": self._api_key
                       }

        headers = {
            'cache-control': "no-cache",
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)



