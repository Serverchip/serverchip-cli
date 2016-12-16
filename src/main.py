import argparse
import ipaddress


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("ip", type=is_valid_ip, help="IPv4 address of the ESP32")

    return parser.parse_args()


def is_valid_ip(ip):
    try:
        ip = ipaddress.ip_address(ip)
        return ip
    except ValueError:
        raise argparse.ArgumentTypeError("Not a valid IPv4 or IPv6 address")


if __name__ == '__main__':
    args = get_args()
    print(args.ip)
    print(args.ip.version)
    print(args.ip.is_private)
