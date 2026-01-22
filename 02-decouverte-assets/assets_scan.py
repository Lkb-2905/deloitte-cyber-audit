def main() -> None:
    try:
        from scapy.all import ARP, Ether, srp  # type: ignore
    except Exception:
        print("Scapy requis. Installez: pip install scapy")
        return

    target = "192.168.1.0/24"
    packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=target)
    result = srp(packet, timeout=2, verbose=0)[0]

    for _, received in result:
        print(f"{received.psrc} {received.hwsrc}")


if __name__ == "__main__":
    main()
