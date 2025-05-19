# Network Scanner

A Python-based tool to scan a local network for active devices using socket connections. Designed for educational purposes to explore networking and cybersecurity concepts, inspired by tools like Nmap.

⚠️ **Legal Notice**: Only scan networks you own or have explicit permission to scan. Unauthorized scanning is illegal and unethical.

## Features
- Scans a specified network range (e.g., `192.168.1.0/24`).
- Detects active devices on a user-specified port (e.g., 80, 443, 22).
- Resolves hostnames for active devices.
- Saves results to `scan_results.csv` with IP, hostname, port, and status.
- Lightweight, requiring no external libraries.

## Requirements
- Python 3.6 or higher (`python3 --version`)
- Root privileges may be required on Linux (use `sudo`)
- Compatible with Kali Linux, Ubuntu, and Windows

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Bipin583/network-scanner.git
   cd network-scanner
   ```
2. Verify Python 3 is installed:
   ```bash
   python3 --version
   ```

## Usage
1. Run the script, preferably with root privileges on Linux:
   ```bash
   sudo python3 scanner.py
   ```
2. Enter the network range (e.g., `192.168.1.0/24`) and port (e.g., `80`).

**Example**:
```bash
$ sudo python3 scanner.py
Enter network to scan (e.g., 192.168.1.0/24): 192.168.1.0/24
Enter port to scan (e.g., 80, 443, 22): 80
Scanning network: 192.168.1.0/24 on port 80
[+] 192.168.1.1 (router.local) is active on port 80
[+] 192.168.1.100 (desktop.local) is active on port 80
Scan completed in 4.12 seconds
Results saved to scan_results.csv
```

⚠️ **Ethical Use**: Always obtain explicit permission before scanning any network.

## Example Output
`scan_results.csv`:
```csv
IP,Hostname,Port,Status
192.168.1.1,router.local,80,Active
192.168.1.100,desktop.local,80,Active
```

## Screenshots
![Scan Output](screenshots/scan_output.png)

## Troubleshooting
- **No devices found**: Verify the network range (`ip addr` to check) or try other ports (e.g., 443, 22).
- **Permission errors**: Run with `sudo` on Linux (`sudo python3 scanner.py`).
- **Slow scanning**: Use a smaller range (e.g., `192.168.1.0/28`) or adjust timeout in `scanner.py` (line: `sock.settimeout(0.5)`).
- **CSV empty**: Ensure the script ran successfully and devices were found.

## Notes
- **Performance**: Large networks (e.g., `/16`) may be slow; prefer `/24` or smaller ranges.
- **Future Improvements**:
  - Support for scanning multiple ports simultaneously.
  - Add a GUI using Tkinter.
  - Integrate with Nmap for advanced scanning.
- **Compatibility**: Tested on Kali Linux, Ubuntu, and Windows (no `sudo` needed on Windows).

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/new-feature`).
3. Commit changes (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a pull request.

## License
MIT License

## Contact
- GitHub: [Bipin583](https://github.com/Bipin583)
- Email: your.email@example.com

## Acknowledgments
- Inspired by Nmap and networking tutorials.
- Built as part of my cybersecurity learning journey.
