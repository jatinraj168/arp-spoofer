# ARP Spoofer

A Python script to demonstrate ARP spoofing using the **Scapy** library. This script allows you to perform a man-in-the-middle (MITM) attack by manipulating ARP tables in a local network.

> **Disclaimer:** This project is intended for educational purposes only. Unauthorized use of this script on networks without explicit permission is illegal and unethical.

---

## Features
- Spoofs ARP tables of a target device and a router.
- Restores ARP tables on termination to minimize disruption.
- Uses Scapy for raw packet manipulation.

---

## Requirements
- Python 3.x
- **Scapy** library

### Installation
Install Scapy using pip:
```bash
pip install scapy
```

Run the script with root privileges:

```bash
sudo python3 arp_spoof.py <victim_ip> <router_ip>
Replace <victim_ip> with the IP address of the target device.
Replace <router_ip> with the IP address of the router.
```
