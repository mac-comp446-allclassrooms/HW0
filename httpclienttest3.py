import unittest
import json
from json import loads


import httpclient
import httpclienttest2

class TestHttpClient(httpclienttest2.TestHttpClient):

    def testPostWithParams(self):
        client = httpclient.HttpClient('httpbin.org')
        response = client.doPostWithParams('/post', {'Foo' : 'Bar'})
        data = json.loads(response.body)
        self.assertEqual(data['form']['Foo'], 'Bar')

    # EXTRA CREDIT - DO NOT UNCOMMENT THIS, IT WILL FAIL
    # ONLY UMCOMMENT AND WORK UNLESS YOU WANT TO COMPLETE THE TEST SO IT PASSES
    
    #### The second test below fails, if you can debug it then you will receive extra credit.
    
    # def testGetWithParams(self):
    #     client = httpclient.HttpClient('httpbin.org')
    #     response = client.doGetWithParams('/get', {'Foo' : 'Bar', 'foo' : 'bar'})
    #     data = json.loads(response.body)
    #     self.assertEquals(data['args'], {'Foo' : 'Bar', 'foo' : 'bar'})
    
if __name__ == '__main__':
    unittest.main()
