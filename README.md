# Network Scanner

A simple Python script to scan a local network for active devices using socket connections. Built for educational purposes to learn about networking and cybersecurity.

⚠️ **Legal Notice**: Only scan networks you own or have explicit permission to scan. Unauthorized scanning is illegal.

## Features
- Scans a specified network range (e.g., 192.168.1.0/24).
- Detects active devices by attempting to connect to port 80.
- Saves results to `scan_results.txt`.

## Requirements
- Python 3.x
- No external libraries needed

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Bipin583/network-scanner.git
   cd network-scanner

   running for tool -->
python3 scanner.py
Example input: 192.168.1.0/24

Example Output-->
Scanning network: 192.168.1.0/24
[+] 192.168.1.1 is active
[+] 192.168.1.100 is active
Scan completed in 5.32 seconds
Results saved to scan_results.txt
