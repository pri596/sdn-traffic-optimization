# users/utils/network_collector.py
import psutil
import socket
import time

def ip_to_int(ip):
    parts = ip.split(".")
    return (int(parts[0]) * 256**3) + (int(parts[1]) * 256**2) + (int(parts[2]) * 256) + int(parts[3])

def get_latest_network_data():
    # Source IP
    src_ip = socket.gethostbyname(socket.gethostname())

    # Destination IP and protocol
    connections = psutil.net_connections(kind="inet")
    if connections and connections[0].raddr:
        dst_ip = connections[0].raddr.ip
        protocol = 1 if connections[0].type == socket.SOCK_STREAM else 2
    else:
        dst_ip = "0.0.0.0"
        protocol = 0

    # Packet count & bytes
    net1 = psutil.net_io_counters()
    p1 = net1.packets_recv
    time.sleep(1)
    net2 = psutil.net_io_counters()
    p2 = net2.packets_recv
    packet_count = p2 - p1
    bytes_value = net2.bytes_sent + net2.bytes_recv
    duration_ms = 1000  # 1-second interval

    return {
        "src_ip": src_ip,
        "dst_ip": dst_ip,
        "protocol": protocol,
        "duration_ms": duration_ms,
        "packet_count": packet_count,
        "bytes": bytes_value
    }
