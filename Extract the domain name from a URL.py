"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. 
"""

def domain_name(url):
	if ":" in url:
		url = url[url.index("/") + 2:]
		url = url[:url.index(".")]
	
	elif "www." in url:
		url = url.replace("www.", "")
		url = url[:url.index(".")]

	return url

print(domain_name("www.rwr47sepqrcmchoqp.com"))