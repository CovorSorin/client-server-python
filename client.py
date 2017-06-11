import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://localhost:8000")

a = 10
b = 5
print "a + b = %s" % str(proxy.add(a,b))
print "a - b = %s" % str(proxy.subtract(a,b))