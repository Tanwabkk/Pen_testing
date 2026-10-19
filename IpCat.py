import socket 

website = input("Enter website (e.g google.com): ").strip()

try:
    ip = socket.gethostbyname(website)
    print(f"IP address of {website}: {ip}")
except socket.gaierror:
    print("Could not resolve hostname.")
