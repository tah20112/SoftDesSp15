""" This script is used to scrape data from Twitter. It specifically searches for tweets that refer to Linux and four specific distributions of GNU/Linux """

# Import relevant packages
from pattern.web import *
import pickle

# Set search engine preferences for use with pattern
engine = Twitter(license = None, throttle = 0.5, language = 'en')

# Spend roughly 12 minutes pulling tweets that have #ubuntu in them
ubuntu = engine.search('#ubuntu', type = SEARCH, start = 1, count = 10, size = None, cached = True)
for i in range(2,12):
	# 'adder' is the next post to be tacked to the end of the ubuntu list
	adder = engine.search('#ubuntu', type = SEARCH, start = i, count = 10, size = None, cached = True)
	ubuntu.extend(adder)
	time.sleep(60)

# The above ^^^ block of code is repeated four more times, but each time it searches for a different Linux #hashtag 

# Create a list containing only the text for each tweet (rather than the user and URL info)
ubuntu_text = []
for i in range(len(ubuntu)-1):
	ubuntu_text.append(ubuntu[i]['text'])

# Use pickle to store scraped data for later
u = open('ubuntu_data.pickle','w')
pickle.dump(ubuntu_text,u)
u.close()

# These ^^^ two blocks are also repeated for each distro

arch = engine.search('#archlinux', type = SEARCH, start = 1, count = 10, size = None, cached = True)
for i in range(2,12):
	adder = engine.search('#archlinux', type = SEARCH, start = i, count = 10, size = None, cached = True)
	arch.extend(adder)
	time.sleep(60)

arch_text = []
for i in range(len(arch)-1):
	arch_text.append(arch[i]['text'])

a = open('arch_data.pickle','w')
pickle.dump(arch_text,a)
a.close()

redhat = engine.search('#redhat', type = SEARCH, start = 1, count = 10, size = None, cached = True)
for i in range(2,12):
	adder = engine.search('#redhat', type = SEARCH, start = i, count = 10, size = None, cached = True)
	redhat.extend(adder)
	time.sleep(60)

redhat_text = []
for i in range(len(redhat)-1):
	redhat_text.append(redhat[i]['text'])

r = open('redhat_data.pickle','w')
pickle.dump(redhat_text,r)
r.close()

debian = engine.search('#debian', type = SEARCH, start = 1, count = 10, size = None, cached = True)
for i in range(2,12):
	adder = engine.search('#debian', type = SEARCH, start = i, count = 10, size = None, cached = True)
	debian.extend(adder)
	time.sleep(60)

debian_text = []
for i in range(len(debian)-1):
	debian_text.append(debian[i]['text'])

d = open('debian_data.pickle','w')
pickle.dump(debian_text,d)
d.close()

linux = engine.search('#linux', type = SEARCH, start = 1, count = 10, size = None, cached = True)
for i in range(2,12):
	adder = engine.search('#linux', type = SEARCH, start = i, count = 10, size = None, cached = True)
	linux.extend(adder)
	time.sleep(60)

linux_text = []
for i in range(len(linux)-1):
	linux_text.append(linux[i]['text'])

l = open('linux_data.pickle','w')
pickle.dump(linux_text,l)
l.close()

# At this point, there should be 5 pickle files containing 109 tweets each