## Description

From orignal code developed by Jonathan Yantis:
Dead simple TCP Ping tool written in Python3. Establishes one connection per
second, times out after one second, and defaults to 10000 connections unless
interrupted with Ctrl-C.

George Uhl added the following features:
May run over IPv4 or IPv6, user can specify a source IP on the client host
and included ping-like statistical summary including RTT minimum, mean(avg),
median, maximum and standard deviation.

## Usage

```
$ ./tcpping.py
Usage: ./tcpping.py --d host [--s source] [--v IP version] [--p port] [--c count]
```

## Example
```
$ ./tcpping.py --d www.google.com --v 4 --p 443 --c 5
Connected to www.google.com (142.250.73.228) [443]: tcp_seq=0 time=26.12 ms
Connected to www.google.com (142.250.73.228) [443]: tcp_seq=1 time=21.40 ms
Connected to www.google.com (142.250.73.228) [443]: tcp_seq=2 time=27.60 ms
Connected to www.google.com (142.250.73.228) [443]: tcp_seq=3 time=44.68 ms
Connected to www.google.com (142.250.73.228) [443]: tcp_seq=4 time=20.33 ms

TCP Ping Results: Connections (Total/Pass/Fail): [5/5/0] (Failed: 0%)
rtt min/avg/med/max/mdev = 20.330/28.026/26.120/44.680/9.802 ms


## Contributors
* Jonathan Yantis ([yantisj](https://github.com/yantisj))
* Modified by George Uhl [guhl1956] (https://github.com/guhl1956))

## License
tcpping is licensed under the GNU AGPLv3 License.
