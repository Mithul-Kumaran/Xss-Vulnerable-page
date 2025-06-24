import socket
import sys
import pyfiglet

def scan_ports(target, start_port, end_port):
    print(f"Scanning {target} from port {start_port} to {end_port}...\n")
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        s.close()

if __name__ == "__main__":
    banner = pyfiglet.figlet_format("Port Scanner")
    print(banner)

    if len(sys.argv) != 4:
        print("Usage: python port_scanner.py <target> <start_port> <end_port>")
        sys.exit(1)

    target_host = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])

    scan_ports(target_host, start_port, end_port)
