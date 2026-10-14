import socket
import sys
from datetime import datetime

def scan_port(target, port):
    """Attempt a TCP connection to a single port."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()
        return result == 0
    except socket.error:
        return False

def scan_target(target, start_port, end_port):
    """Scan a range of ports on the target host."""
    print(f"\nScanning {target}")
    print(f"Started at {datetime.now().strftime('%H:%M:%S')}")
    print("-" * 40)

    open_ports = []

    for port in range(start_port, end_port + 1):
        if scan_port(target, port):
            open_ports.append(port)
            try:
                service = socket.getservbyport(port)
            except OSError:
                service = "unknown"
            print(f"  Port {port}: OPEN ({service})")

    print(f"\nScan complete. {len(open_ports)} open port(s) found.")
    return open_ports

if __name__ == "__main__":
    target = input("Target IP or hostname: ")
    scan_target(target, 1, 1024)
