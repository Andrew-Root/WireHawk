# WireHawk

#### WireHawk is a powerful and lightweight network traffic analysis tool designed to automate the use of Bettercap and Wireshark (or similar tools) for real-time packet sniffing and monitoring. Unlike traditional network analysis tools, WireHawk does not require setting the network interface into promiscuous mode, allowing for more stealthy and efficient network monitoring. The tool is designed with penetration testers, network administrators, and security enthusiasts in mind. It facilitates seamless packet capture and analysis by automating the process of network interception using Bettercap, while simultaneously using Wireshark (or tshark) for in-depth traffic analysis. With a simple and customizable terminal interface, WireHawk empowers users to monitor network traffic effortlessly, uncovering potential security vulnerabilities, unauthorized access, or network inefficiencies.

## Features
##### * Automated Bettercap & Wireshark Integration: Seamlessly integrates Bettercap's MITM (Man-in-the-Middle) attacks and traffic interception with Wireshark's packet capture and analysis.
##### * No Promiscuous Mode Required: Capture and analyze network traffic without needing to set your network interface into promiscuous mode, providing stealthier monitoring.
##### * Real-Time Monitoring: Monitor and capture live network traffic with the ability to filter and analyze packets in real-time.
##### * Customizable Terminal Interface: Easy-to-use command-line interface with configurable options for network interface, target IP, and gateway IP.
##### * Cross-Platform Support: Designed to work on most Linux distributions commonly used in penetration testing and security analysis.

## Python Dependencies
* argparse (part of the standard library, no installation required)
* subprocess (part of the standard library, no installation required)
* time (part of the standard library, no installation required)
* colorama (installable via pip install colorama)

## External Tools
* Bettercap (can be installed via `apt-get install bettercap` on Debian-based distributions)
* Tshark (part of Wireshark, installable via `apt-get install tshark`)

### Run the script with the following command:
* `python3 WireHawk.py -i <interface> -t <target-ip> -g <gateway-ip>`
* `-i`: Network interface (e.g., eth0, wlan0)
* `-t`: Target IP address
* `-g`: Gateway IP address (usually the router)
