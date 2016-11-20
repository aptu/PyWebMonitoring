#!/usr/bin/python

# The script generates traffic on my instance of the time server.
# Takes command-line arguments:
# --url : url to hit
# --rps : requests per seconds
# --jitter : float to represent the shakiness of rate. 
# Rate of hitting the website = rps * (1.0 +- jitter).

# Assumption: the user inputs url as "http://<name>"


import argparse
import sys
import urllib2
import datetime
import time
import random



def trafficgen(url, rps, jit):
    actual_rps = random.randint(rps * (1.0 - jit), rps * (1.0 + jit))
    print "[%s] Generating %d requests" % (datetime.datetime.now(), actual_rps)
    for i in xrange(actual_rps):
        urllib2.urlopen(url)
    
    
if __name__ == "__main__":   
    
   
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default = "http://localhost:8080", help = "Url to hit")
    parser.add_argument("--rps", default = 10, type = int, help = "Average requests per second")
    parser.add_argument("--jitter", default = 0, type = float, help = "Shakiness of the rate")
    args = parser.parse_args()
    
    
    #info = urllib2.urlopen(args.url)
    #print info.read()
    
    while True:
        start = datetime.datetime.now()
        trafficgen(args.url, args.rps, args.jitter)
        diff = datetime.datetime.now() - start
        #print "time elapsed: %s" % diff
        time_to_sleep = (datetime.timedelta(seconds = 1) - diff).total_seconds()
        time.sleep(time_to_sleep)
        
    
    
        
    