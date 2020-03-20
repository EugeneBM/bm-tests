import requests
import json


class TestBm:

    __key = "name"
    __value = "ironman"
    __url = "https://httpbin.org/anything"
    __test_json = "{{\"{0}\": \"{1}\"}}".format(__key, __value)

    def test_get_request_response_status_code_200(self):
        response = requests.get(self.__url)
        assert response.status_code == 200

    def test_get_request_response_body_is_correct(self):
        response = requests.get(self.__url)
        json_data = json.loads(response.text)
        headers = json_data["headers"]

        assert json_data["args"] == {}
        assert json_data["data"] == ""
        assert json_data["files"] == {}
        assert json_data["form"] == {}
        assert headers["Accept"] == '*/*'
        assert headers["Accept-Encoding"] == 'gzip, deflate'
        assert headers["Host"] == 'httpbin.org'
        assert json_data["json"] is None
        assert json_data["method"] == "GET"
        assert json_data["url"] == self.__url

    def test_post_request_response_status_code_200(self):
        response = requests.post(self.__url, self.__test_json)
        assert response.status_code == 200

    def test_post_request_response_body_is_correct(self):
        response = requests.post(self.__url, self.__test_json)
        json_data = json.loads(response.text)
        headers = json_data["headers"]

        assert json_data["args"] == {}
        assert json_data["data"] == self.__test_json
        assert json_data["files"] == {}
        assert json_data["form"] == {}
        assert headers["Accept"] == '*/*'
        assert headers["Accept-Encoding"] == 'gzip, deflate'
        assert headers["Content-Length"] == '{0}'.format(len(self.__test_json))
        assert headers["Host"] == 'httpbin.org'
        assert json_data["json"] == {'{0}'.format(self.__key): '{0}'.format(self.__value)}
        assert json_data["method"] == "POST"
        assert json_data["url"] == self.__url
