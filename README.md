## Description

From orignal code developed by Jonathan Yantis:
Dead simple TCP Ping tool written in Python3. Establishes one connection per
second, times out after one second, and defaults to 10000 connections unless
interrupted with Ctrl-C.

George Uhl added the following features:
May run over IPv4 or IPv6, user can specify a source IP on the client host
and included ping-like statistical summary including RTT minimum, mean(avg),
maximum and standard deviation.

## Usage

```
$ ./tcpping.py
Usage: ./tcpping.py --d host [--s source] [--v IP version] [--p port] [--c count]

# Mandatory dest can be hostname or explicit IPv4 or IPv6 address
# Optional source can be hostname or explicit IPv4 or IPv6 address assigned to any interface on this client.
# Optional version specified as [4|6] depending on the protocol to use, IPv4 or IPv6. Defaults to IPv4.
# Optional server port to try to connect on.  Defaults to port 80.
# Optional ping count.  Currently defaults to 10. Maximum of 10000 allowed.
```

## Example
```
$ ./tcpping.py --d www.google.com
Connected to www.google.com (142.250.73.196) [80]: tcp_seq=0 time=17.59 ms
Connected to www.google.com (142.250.73.196) [80]: tcp_seq=1 time=17.30 ms
Connected to www.google.com (142.250.73.196) [80]: tcp_seq=2 time=17.36 ms
Connected to www.google.com (142.250.73.196) [80]: tcp_seq=3 time=17.32 ms
Connected to www.google.com (142.250.73.196) [80]: tcp_seq=4 time=17.32 ms
Connected to www.google.com (142.250.73.196) [80]: tcp_seq=5 time=17.41 ms
Connected to www.google.com (142.250.73.196) [80]: tcp_seq=6 time=17.38 ms
Connected to www.google.com (142.250.73.196) [80]: tcp_seq=7 time=17.70 ms
Connected to www.google.com (142.250.73.196) [80]: tcp_seq=8 time=17.31 ms
Connected to www.google.com (142.250.73.196) [80]: tcp_seq=9 time=17.33 ms

TCP Ping Results: Connections (Total/Pass/Fail): [10/10/0] (Failed: 0%)
rtt min/avg/max/mdev = 17.300/17.411/17.700/0.140 ms

## Contributors
* Jonathan Yantis ([yantisj](https://github.com/yantisj))
* Modified by George Uhl [guhl1956] (https://github.com/guhl1956))

## License
tcpping is licensed under the GNU AGPLv3 License.
