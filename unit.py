import urllib2, unittest

BASE_URL='http://localhost:5001'
JSON_HEADER={'accept':'application/json'}

def get_resp(header=''):
    if header != '': request = urllib2.Request(BASE_URL, headers=header)
    else: request = urllib2.Request(BASE_URL)
    return urllib2.urlopen(request).read()
 
class TestUM(unittest.TestCase):
    def setUp(self):
        pass
    def testjson_accept_header(self):
        test = get_resp(JSON_HEADER)
        self.assertEqual(test, '{"message": "Good morning"}')
    def testno_accept_header(self):
        test = get_resp()
        self.assertEqual(test, "<p>Hello, World</p>")
 
if __name__ == '__main__':
    unittest.main()


