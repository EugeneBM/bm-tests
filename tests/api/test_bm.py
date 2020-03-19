import requests
import json

class TestBm:

    __url = "https://httpbin.org/anything"
    __test_json = "{\"name\":\"ironman\"}"

    def test_get_request_response_status_code_200(self):
        response = requests.get(self.__url)
        assert response.status_code == 200

    def test_get_request_response_body_is_correct(self):
        response = requests.get(self.__url)
        body = response.text
        assert body == ""

    def test_post_request_response_status_code_200(self):
        response = requests.post(self.__url, self.__test_json)
        assert response.status_code == 200

    def test_post_request_response_body_is_correct(self):
        response = requests.post(self.__url, self.__test_json)
        body = response.text
        json_data = json.loads(body)

        assert json_data["args"] == {}
        assert json_data["files"] == {}
        assert json_data["form"] == {}
        assert json_data["data"] == self.__test_json
        assert json_data["json"] == self.__test_json
        assert json_data["method"] == "POST"
        assert json_data["url"] == self.__url
