#!/usr/bin/python3
import urllib.request
import os
import threading
import multiprocessing


web =["https://api.github.com","http://bilgisayar.mu.edu.tr/","https://www.python.org/",
"http://www.google.com","https:/sadsdas.com"]
def check (url):
    print("checking these urls\n" , url )
    print_pid()
    getload_avg()
    print("your cpu core is  =>", multiprocessing.cpu_count())
    for i in range(5):
        if(urllib.request.urlopen(url[i]).getcode()==200):
            print("this url is valid =>",url[i])
        else:
            print("there are 404 errors or something are getting bad",url[i])
def print_pid():
    print("checking PID of the process is =>",os.getpid())

def get_multiprocess():
    multiprocess = multiprocessing.cpu_count()
    print("your cpu core is =>",multiprocess)

def getload_avg():
	"""get the load average over
the lasr 1,5 and 15 minutes we using os.getloadavg() method"""
	last1min, lastmin5 = os.getloadavg()
    print("last 1 minute loadavg is => \n",last1min)
    print("last 5 minute loadavg is => \n",last5min)
    get_multiprocess()
    if(multiprocess-lastmin5 <1):
        break;

check(web)
