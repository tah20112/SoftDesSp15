""" This script retrieves the data from TwitterMining.py and analyzes it using pattern.en sentiment analysis. It outputs a plot of the polarity and subjectivity of various linux distributions. The goal is to determine Twitter's opinion of Linux distros. """

# import useful packages
import pickle
from pattern.en import *
import numpy as np
import matplotlib.pyplot as plt

# Grab the files pickled by TwitterMining.py
u_file = open('ubuntu_data.pickle','r')
a_file = open('arch_data.pickle','r')
r_file = open('redhat_data.pickle','r')
d_file = open('debian_data.pickle','r')
l_file = open('linux_data.pickle','r')

# Retrieve data from the pickled files
u_data = pickle.load(u_file)
a_data = pickle.load(a_file)
r_data = pickle.load(r_file)
d_data = pickle.load(d_file)
l_data = pickle.load(l_file)

# Make some lists for later use
u_polar = []
u_subj = []
a_polar = []
a_subj = []
r_polar = []
r_subj = []
d_polar = []
d_subj = []
l_polar = []
l_subj = []

# Each for loop takes the tweets for the respective distro and creates two lists: one containing all the polarity values and one containing all the subjectivity values
for post in u_data:
	sent = sentiment(post)
	# So this if statement without each for loop removes all the (0,0) tuples. Thus, if your tweet was just "<url> #archlinux" you don't skew the data!
	if sent != (0.0,0.0):
		u_polar.append(sent[0])
		u_subj.append(sent[1])

for post in a_data:
	sent = sentiment(post)
	if sent != (0.0,0.0):
		a_polar.append(sent[0])
		a_subj.append(sent[1])

for post in r_data:
	sent = sentiment(post)
	if sent != (0.0,0.0):
		r_polar.append(sent[0])
		r_subj.append(sent[1])

for post in d_data:
	sent = sentiment(post)
	if sent != (0.0,0.0):
		d_polar.append(sent[0])
		d_subj.append(sent[1])

for post in l_data:
	sent = sentiment(post)
	if sent != (0.0,0.0):
		l_polar.append(sent[0])
		l_subj.append(sent[1])

# Averages all the lists of sentiment data and makes datapoints stored as lists
u_point = [np.mean(u_polar),np.mean(u_subj)]
a_point = [np.mean(a_polar),np.mean(a_subj)]
r_point = [np.mean(r_polar),np.mean(r_subj)]
d_point = [np.mean(d_polar),np.mean(d_subj)]
l_point = [np.mean(l_polar),np.mean(l_subj)]

# Makes plot
plt.figure()

plt.plot(u_point[1], u_point[0], label = "Ubuntu", marker = 'o')
plt.plot(a_point[1], a_point[0], label = "Arch Linux", marker = 'o')
plt.plot(r_point[1], r_point[0], label = "Redhat", marker = 'o')
plt.plot(d_point[1], d_point[0], label = "Debian", marker = 'o')
plt.plot(l_point[1], l_point[0], label = "Linux", marker = 'o')
# This line is just a reference point. It's the zero polarity line
plt.plot([0,.2,.4,.6,.8,1],[0,0,0,0,0,0], color = 'k')

plt.xlabel("Subjectivity")
plt.ylabel("Polarity")
plt.title("Twitter's Opinion of Linux Distros")
plt.legend(loc = "upper right")

plt.xlim(0,1)
plt.ylim(-0.3,0.3)

plt.savefig("LinuxOpinion.png")

# All these print commands are for my benefit as a data analyst
print len(u_polar)
print len(a_polar)
print len(r_polar)
print len(d_polar)
print len(l_polar)

print u_point
print a_point
print r_point
print d_point
print l_point