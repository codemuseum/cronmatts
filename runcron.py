from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import urlfetch

class MainPage(webapp.RequestHandler):
  def get(self):
    result = urlfetch.fetch(url='http://recentdelicious.heroku.com/aggregates', method=urlfetch.POST, follow_redirects=False)
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write(str(result.status_code) + ' :: ' + result.content)

class RecentDeliciousClearer(webapp.RequestHandler):
  def get(self):
    result = urlfetch.fetch(url='http://recentdelicious.heroku.com/aggregates/1?_method=delete', method=urlfetch.POST, follow_redirects=False)
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write(str(result.status_code) + ' :: ' + result.content)

class TwitterAutoSharer(webapp.RequestHandler):
  def get(self):
    result = urlfetch.fetch(url='http://riveti-twitter-auto-sharer.heroku.com/aggregates', method=urlfetch.POST, follow_redirects=False)
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write(str(result.status_code) + ' :: ' + result.content)

class TwitterAutoSharerClearer(webapp.RequestHandler):
  def get(self):
    result = urlfetch.fetch(url='http://riveti-twitter-auto-sharer.heroku.com/aggregates/1?_method=delete', method=urlfetch.POST, follow_redirects=False)
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write(str(result.status_code) + ' :: ' + result.content)

class AmazonTopVideoGames(webapp.RequestHandler):
  def get(self):
    result = urlfetch.fetch(url='http://amazon-top-video-games.heroku.com/crawls', method=urlfetch.POST, follow_redirects=False)
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write(str(result.status_code) + ' :: ' + result.content)

class AmazonTopVideoGamesClearer(webapp.RequestHandler):
  def get(self):
    result = urlfetch.fetch(url='http://amazon-top-video-games.heroku.com/crawls/1?_method=delete', method=urlfetch.POST, follow_redirects=False)
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write(str(result.status_code) + ' :: ' + result.content)

class DealcatcherPopularImport(webapp.RequestHandler):
  def get(self):
    result = urlfetch.fetch(url='http://dealcatcher-popular-import.heroku.com/crawls', method=urlfetch.POST, follow_redirects=False)
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write(str(result.status_code) + ' :: ' + result.content)

class DealcatcherPopularImportClearer(webapp.RequestHandler):
  def get(self):
    result = urlfetch.fetch(url='http://dealcatcher-popular-import.heroku.com/crawls/1?_method=delete', method=urlfetch.POST, follow_redirects=False)
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write(str(result.status_code) + ' :: ' + result.content)

class HuluPopularRivetiImport(webapp.RequestHandler):
  def get(self):
    result = urlfetch.fetch(url='http://hulu-popular-riveti-import.heroku.com/crawls', method=urlfetch.POST, follow_redirects=False)
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write(str(result.status_code) + ' :: ' + result.content)

class HuluPopularRivetiImportClearer(webapp.RequestHandler):
  def get(self):
    result = urlfetch.fetch(url='http://hulu-popular-riveti-import.heroku.com/crawls/1?_method=delete', method=urlfetch.POST, follow_redirects=False)
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write(str(result.status_code) + ' :: ' + result.content)

class ItunesMusicImport(webapp.RequestHandler):
  def get(self):
    result = urlfetch.fetch(url='http://itunes-music-import.heroku.com/crawls', method=urlfetch.POST, follow_redirects=False)
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write(str(result.status_code) + ' :: ' + result.content)

class ItunesMusicImportClearer(webapp.RequestHandler):
  def get(self):
    result = urlfetch.fetch(url='http://itunes-music-import.heroku.com/crawls/1?_method=delete', method=urlfetch.POST, follow_redirects=False)
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write(str(result.status_code) + ' :: ' + result.content)

class RottenTomatoesSearchImport(webapp.RequestHandler):
  def get(self):
    result = urlfetch.fetch(url='http://rotten-tomatoes-search-import.heroku.com/crawls', method=urlfetch.POST, follow_redirects=False)
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write(str(result.status_code) + ' :: ' + result.content)

class RottenTomatoesSearchImportClearer(webapp.RequestHandler):
  def get(self):
    result = urlfetch.fetch(url='http://rotten-tomatoes-search-import.heroku.com/crawls/1?_method=delete', method=urlfetch.POST, follow_redirects=False)
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write(str(result.status_code) + ' :: ' + result.content)

class YelpEventsRivetiImport(webapp.RequestHandler):
  def get(self):
    result = urlfetch.fetch(url='http://yelp-events-riveti-import.heroku.com/crawls', method=urlfetch.POST, follow_redirects=False)
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write(str(result.status_code) + ' :: ' + result.content)

class YelpEventsRivetiImportClearer(webapp.RequestHandler):
  def get(self):
    result = urlfetch.fetch(url='http://yelp-events-riveti-import.heroku.com/crawls/1?_method=delete', method=urlfetch.POST, follow_redirects=False)
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write(str(result.status_code) + ' :: ' + result.content)

class YoutubePopularRivetiImport(webapp.RequestHandler):
  def get(self):
    result = urlfetch.fetch(url='http://youtube-popular-riveti-import.heroku.com/crawls', method=urlfetch.POST, follow_redirects=False)
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write(str(result.status_code) + ' :: ' + result.content)

class YoutubePopularRivetiImportClearer(webapp.RequestHandler):
  def get(self):
    result = urlfetch.fetch(url='http://youtube-popular-riveti-import.heroku.com/crawls/1?_method=delete', method=urlfetch.POST, follow_redirects=False)
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write(str(result.status_code) + ' :: ' + result.content)



application = webapp.WSGIApplication(
                                     [('/', MainPage), ('/clearrecentdelicious', RecentDeliciousClearer), 
                                       ('/twitter-auto-sharer', TwitterAutoSharer), ('/twitter-auto-sharer-clear', TwitterAutoSharerClearer),
                                      ('/amazon-top-video-games', AmazonTopVideoGames), ('/amazon-top-video-games-clear', AmazonTopVideoGamesClearer), 
                                      ('/dealcatcher-popular-import', DealcatcherPopularImport), ('/dealcatcher-popular-import-clear', DealcatcherPopularImportClearer), 
                                      ('/hulu-popular-riveti-import', HuluPopularRivetiImport), ('/hulu-popular-riveti-import-clear', HuluPopularRivetiImportClearer), 
                                      ('/itunes-music-import', ItunesMusicImport), ('/itunes-music-import-clear', ItunesMusicImportClearer), 
                                      ('/rotten-tomatoes-search-import', RottenTomatoesSearchImport), ('/rotten-tomatoes-search-import-clear', RottenTomatoesSearchImportClearer), 
                                      ('/yelp-events-riveti-import', YelpEventsRivetiImport), ('/yelp-events-riveti-import-clear', YelpEventsRivetiImportClearer), 
                                      ('/youtube-popular-riveti-import', YoutubePopularRivetiImport), ('/youtube-popular-riveti-import-clear', YoutubePopularRivetiImportClearer)],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()