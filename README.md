Simple Python TCP Port Scanner

A lightweight, multi-purpose Python script designed to perform TCP port scans on a target host or IP address. It scans a specified range of ports, identifies open connections, and resolves well-known standard services (such as HTTP, SSH, FTP).

Features

Standard TCP Connect Scanning: Uses Python's native socket library to establish TCP handshake attempts.

Service Resolution: Attempts to translate open port numbers into standard network service names (e.g., Port 80 -> http).

Configurable Port Ranges: Easily adjustable start and end port ranges.

Zero Dependencies: Built entirely with Python standard libraries—no external packages required.

Prerequisites

Python 3.6+ installed on your system.

Usage

Clone the repository:

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name


Run the script:

python port_scanner.py


Provide a target:
When prompted, enter a valid IP address or domain name:

Target IP or hostname: scanme.nmap.org


Example Output

Target IP or hostname: scanme.nmap.org

Scanning scanme.nmap.org
Started at 14:22:05
----------------------------------------
  Port 22: OPEN (ssh)
  Port 80: OPEN (http)

Scan complete. 2 open port(s) found.


How It Works

Socket Creation: For each port in the requested range, the script initializes an IPv4 TCP socket (AF_INET, SOCK_STREAM).

Timeout Control: Sets a 1-second non-blocking timeout to avoid hanging on filtered ports.

Connection Check: Uses socket.connect_ex() to check for open states (returning 0 on success).

Service Mapping: Utilizes socket.getservbyport() to fetch the default service name associated with open ports.

To test use IP addresses that you are allow to use or your own 
