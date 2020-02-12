#HTTP -----------------------------------------------
# Can use HTTP requests isntead of raw sockets  
import urllib2
response = urllib2.urlopen("http://127.0.0.1:8080")
html = response.read()
print(html)


#Create a request object before sending and add headers
import urllib2
req = urllib2.Request("http://127.0.0.1:8080")
req.add_header('Referer', 'http://www.python.org/')
#Add an api key to gain access
req.add_header('api-key', '1010')
#Add cookie details to gain access
req.add_header('cookie', "alien_id={}".format(i))
resp = urllib2.urlopen(req)
content = resp.read()

#Post data
#urllib 1 needed to encode the url
import urllib
url = 'http://myserver/post_service'
data = urllib.urlencode({'name' : 'joe', 'age'  : '10'})
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
print response.read()


#Perform directory transversal on unsecure urls
import urllib2
for i in range(5):
    extraPath = "../"*i
    url = "http://127.0.0.1:8082/humantechconfig?file={}human.conf".format(extraPath)
    response = urllib2.urlopen(url)
    html = response.read()

