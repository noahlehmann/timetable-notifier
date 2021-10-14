import http.client


class HttpCaller:
    def __init__(self, url, path):
        self.url = url
        # should start with /
        self.path = path

    def get_content(self):
        connection = http.client.HTTPSConnection(self.url)
        connection.request("GET", self.path)
        response = connection.getresponse()
        content = response.read().decode()
        connection.close()
        return content
