import socket
import threading
import time
import ipaddress

def scan_ip(ip):
    try:
        # Create a socket with a 1-second timeout
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        # Attempt to connect to port 80 (common for devices)
        result = sock.connect_ex((str(ip), 80))
        sock.close()
        if result == 0:
            print(f"[+] {ip} is active")
            with open("scan_results.txt", "a") as f:
                f.write(f"{ip}\n")
    except:
        pass

def scan_network(network):
    print(f"Scanning network: {network}")
    start_time = time.time()
    threads = []
    
    # Iterate through all IPs in the network
    for ip in ipaddress.ip_network(network):
        thread = threading.Thread(target=scan_ip, args=(ip,))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    
    print(f"Scan completed in {time.time() - start_time:.2f} seconds")
    print("Results saved to scan_results.txt")

if __name__ == "__main__":
    network = input("Enter network to scan (e.g., 192.168.1.0/24): ")
    scan_network(network)