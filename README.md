
Description
WireHawk is a powerful and lightweight network traffic analysis tool designed to automate the use of Bettercap and Wireshark (or similar tools) for real-time packet sniffing and monitoring. 
Unlike traditional network analysis tools, WireHawk does not require setting the network interface into promiscuous mode, allowing for more stealthy and efficient network monitoring.

The tool is designed with penetration testers, network administrators, and security enthusiasts in mind. It facilitates seamless packet capture and analysis by automating the process of network interception using Bettercap, 
while simultaneously using Wireshark (or tshark) for in-depth traffic analysis.

With a simple and customizable terminal interface, WireHawk empowers users to monitor network traffic effortlessly, uncovering potential security vulnerabilities, unauthorized access, or network inefficiencies.

Features
Automated Bettercap & Wireshark Integration: Seamlessly integrates Bettercap's MITM (Man-in-the-Middle) attacks and traffic interception with Wireshark's packet capture and analysis.
No Promiscuous Mode Required: Capture and analyze network traffic without needing to set your network interface into promiscuous mode, providing stealthier monitoring.
Real-Time Monitoring: Monitor and capture live network traffic with the ability to filter and analyze packets in real-time.
Customizable Terminal Interface: Easy-to-use command-line interface with configurable options for network interface, target IP, and gateway IP.
Cross-Platform Support: Designed to work on most Linux distributions commonly used in penetration testing and security analysis.
Installation
To install WireHawk, simply clone the repository and install the required dependencies:

bash
Copy code
git clone https://github.com/username/[repository-name].git
cd [repository-name]
pip install -r requirements.txt
You will also need to have Bettercap and Wireshark (or tshark) installed on your system.

Usage
Run the script with the following command:

bash
Copy code
python3 [script-name].py -i <interface> -t <target-ip> -g <gateway-ip>
-i: Network interface (e.g., eth0, wlan0)
-t: Target IP address
-g: Gateway IP address (usually the router)
