from google.appengine.ext import webapp
import urllib2
import logging

class WeatherProxy(webapp.RequestHandler):
    
    def get(self):
        logging.info("get")
        self.response.headers['Content-Type'] = 'text/javascript'
        param = self.request.get
        write = self.response.out.write
        callBackKey = param('weatherCallBack')
        cityId = param('cityId')
        originContent = self.fetchContentFromUrl('http://m.weather.com.cn/data/' + cityId + '.html')
        write(callBackKey + '(' + originContent + ');')
        pass
    
    def post(self):
        logging.info("post")
        return self.get(self)
    
    


    def fetchContentFromUrl(self,url):
        print(url)
        header ={'User-Agent':'mozilla/5.0 (windows; U; windows NT 5.1; zh-cn)'}
        req=urllib2.Request(url,None,header)
        response = urllib2.urlopen(req)
        page = response.read()
        return page
    
    
app = webapp.WSGIApplication([('/weather', WeatherProxy)])










