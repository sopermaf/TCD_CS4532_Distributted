import urllib2


print urllib2.urlopen("http://localhost:8000/echo-server.php?message=test").read()


