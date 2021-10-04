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
./tcpping.py --d 172.28.9.44 --s 172.28.9.40 --c 5 --v 4 --p 443
Connected to 172.28.9.44 (172.28.9.44) [443]: tcp_seq=0 time=4.48 ms
Connected to 172.28.9.44 (172.28.9.44) [443]: tcp_seq=1 time=0.38 ms
Connected to 172.28.9.44 (172.28.9.44) [443]: tcp_seq=2 time=0.40 ms
Connected to 172.28.9.44 (172.28.9.44) [443]: tcp_seq=3 time=0.39 ms
Connected to 172.28.9.44 (172.28.9.44) [443]: tcp_seq=4 time=0.43 ms

TCP Ping Results: Connections (Total/Pass/Fail): [5/5/0] (Failed: 0%)
rtt min/avg/med/max/mdev = 0.380/1.216/0.400/4.480/1.825 ms```

## Contributors
* Jonathan Yantis ([yantisj](https://github.com/yantisj))
* Modified by George Uhl [guhl1956] (https://github.com/guhl1956))

## License
tcpping is licensed under the GNU AGPLv3 License.
