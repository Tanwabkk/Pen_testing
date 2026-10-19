import socket 

website = input("Enter website (e.g google.com): ").strip()

try:
    ip = socket.gethostname(website)
    print(f"IP address of {website}: {ip}")
except socket.gaierror:
    print("Could not resove hostname.")
