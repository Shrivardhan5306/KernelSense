import socket

import psutil


def get_network_interfaces():
    """Return information about available network interfaces."""
    interfaces = []

    addresses = psutil.net_if_addrs()
    statistics = psutil.net_if_stats()

    for name, address_list in addresses.items():
        interface = {
            "name": name,
            "status": "down",
            "addresses": []
        }

        if name in statistics:
            interface["status"] = (
                "up" if statistics[name].isup else "down"
            )

        for address in address_list:
            address_info = {
                "family": str(address.family),
                "address": address.address
            }

            if address.netmask:
                address_info["netmask"] = address.netmask

            if address.broadcast:
                address_info["broadcast"] = address.broadcast

            interfaces.append({
                **interface,
                "addresses": [
                    address_info
                ]
            })

    return interfaces


def get_network_statistics():
    """Return network traffic statistics."""
    statistics = psutil.net_io_counters()

    return {
        "bytes_sent": statistics.bytes_sent,
        "bytes_received": statistics.bytes_recv,
        "packets_sent": statistics.packets_sent,
        "packets_received": statistics.packets_recv,
        "errors_in": statistics.errin,
        "errors_out": statistics.errout,
        "packets_dropped_in": statistics.dropin,
        "packets_dropped_out": statistics.dropout
    }


def check_internet_connection(host="8.8.8.8", port=53, timeout=3):
    """Check whether an external network connection can be established."""
    try:
        socket.setdefaulttimeout(timeout)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
            connection.connect((host, port))

        return True

    except (OSError, socket.timeout):
        return False


def get_network_status():
    """Return complete network information."""
    return {
        "interfaces": get_network_interfaces(),
        "statistics": get_network_statistics(),
        "internet_connected": check_internet_connection()
    }
