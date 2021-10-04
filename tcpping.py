#!/usr/bin/env python3
"""
TCP Ping Test (defaults to port 80, 10000 packets)
- Ctrl-C Exits with Results
"""

import sys
import socket
import time
import signal
import argparse
from statistics import mean,median,stdev
from timeit import default_timer as timer

host = None
source = None
port = 80
version = 4
min_time = 99999.9
max_time = 0.0
avg_time = 0.0
sum_time = 0.0
rtt_set = set()

# Default to 10000 connections max
maxCount = 10000
myCount = 10
count = 0

## Inputs
# --d destination --s source --v version --p port --c count
#
# Mandatory dest can be hostname or explicit IPv4 or IPv6 address
# Optional source can be hostname or explicit IPv4 or IPv6 address assigned to any interface on this client.
# Optional version specified as [4|6] depending on the protocol to use, IPv4 or IPv6. Defaults to IPv4.
# Optional server port to try to connect on.  Defaults to port 80.
# Optional ping count.  Currently defaults to 10. Maximum of 10000 allowed.

parser = argparse.ArgumentParser()
parser.add_argument('--d', type=str, required=True)
parser.add_argument('--s', type=str)
parser.add_argument('--v', type=int)
parser.add_argument('--p', type=int)
parser.add_argument('--c', type=int)
args = parser.parse_args()

host = args.d
if args.s:
	source = args.s
if args.v:
	version = args.v
if args.p:
	port = args.p
if args.c:
        if args.c > maxCount :
            print("ping count must be 10000 or less")
            exit()
        else:
            myCount = args.c

# Pass/Fail counters
passed = 0
failed = 0


def getResults(rset):
    """ Summarize Results """

    # Print the number of total/pass/fail pings
    lRate = 0
    if failed != 0:
        lRate = failed / (count) * 100
        lRate = "%.3f" % lRate

    print("\nTCP Ping Results: Connections (Total/Pass/Fail): [{:}/{:}/{:}] (Failed: {:}%)".format((count), passed, failed, str(lRate)))

    # Print summary statistics if at least one ping was successful.
    if failed != count:

        # Print RTT Minimun/Mean/Median/StdDev across all the RTTs collected during the run
        print("rtt min/avg/med/max/mdev = {:.3f}".format(min(rset)),"/{:.3f}".format(mean(rset)),"/{:.3f}".format(median(rset)),"/{:.3f}".format(max(rset)),"/{:.3f}".format(stdev(rset))," ms", sep='')


def signal_handler(signal, frame):
    """ Catch Ctrl-C and Exit """
    avg_time = sum_time / count
    getResults(rtt_set)
    sys.exit(0)


# Register SIGINT Handler
signal.signal(signal.SIGINT, signal_handler)

# Loop while less than max count or until Ctrl-C caught
while count < myCount:

    # Increment Counter
    count += 1

    success = False

    # New  IPv4 or IPv5 Socket
    if version == 4:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        family = socket.AF_INET
    elif version == 6:
        s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        family = socket.AF_INET6
    else:
        print("IP protocol id must be 4 or 6")
        failed += 1
        exit()

    # 1sec Timeout
    s.settimeout(1)

    # Start a timer
    s_start = timer()

    # Try to Connect
    try:
        # Bind socket to local source IP is specified
        if source :
            s.bind((source, 0)) 

        # Connect to remote host on specified port
        s.connect((host, int(port)))
        s.shutdown(socket.SHUT_RD)
        addr = socket.getaddrinfo(host, None, family)[0][4][0]
        success = True
    
    # Connection Timed Out
    except socket.timeout:
        print("Connection timed out!")
        failed += 1
    # Other error
    except OSError as e:
        print("OS Error:", e)
        failed += 1

    # Stop Timer
    s_stop = timer()
    s_runtime = "%.2f" % (1000 * (s_stop - s_start))

    # Put the ping RTT result into the result set
    rtt_set.add(float(s_runtime))

    if success:
        print("Connected to %s (%s) [%s]: tcp_seq=%s time=%s ms" % (host, addr, port, (count-1), s_runtime))
        passed += 1

    # Sleep for 1sec
    if count < maxCount:
        time.sleep(1)

# Output Results if maxCount reached
getResults(rtt_set)
