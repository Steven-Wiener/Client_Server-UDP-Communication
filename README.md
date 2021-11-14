# Client/Server UDP Communication
Simulating a client requesting a "movie" from a server.\
For this program, there are two files: a client (`UDPClient.py`) and server (`UDPServer.py`), running on two different hosts.
1. A client requests a "movie" from a server, stored in `client_log`. The request packet contains:
   - `name` : Client Nname _example: Steven_
   - `movie` : Movie Name _example: Troll 2_
   - `time` : Movie Start Time _example: 18:00_
2. Upon receiving the request, a server returns a response to the client, stored in `server_log`:
   - `name`: Hostname of the server _example: 'tux-59.cae.wisc.edu'_
   - `movie`: Name of the movie _example: Troll 2_
   - `time` : Movie Start Time _example: 18:00_
   - `cost`: Cost for watching the movie _example: '$5.00'_
   - `password`: 8-bit integer which will serve as password for decoding the movie (simulated by RNG)

![UDP Client Server](udp-client-server-overview.png)

## Getting Started
Run `UDPServer.py` on a host, then run `UDPClient.py` on a separate host, after replacing the `serverName` and `serverPort` variables in both files with your chosen hosts.

### Prerequisites
* [Python](https://www.python.org/downloads/)

### Info
- Authors: Steven Wiener
- Purpose: ECE537
- Created: 05.17.19
- Image source: https://pythontic.com/modules/socket/udp-client-server-example