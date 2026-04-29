# GNS3 VyOS Network Automation Lab

## Overview
This project is a hands-on network automation lab built with GNS3, VyOS, Alpine Linux, SSH, and Python Netmiko.

The lab simulates a small internal network, enables SSH access to a VyOS router, and uses Python automation to collect network information and back up the router configuration.

## Lab Topology

```text
PC1 / VPCS
10.10.10.2/24
     |
Ethernet Switch
     |
     |------------------ VyOS Router
     |                   eth0: 10.10.10.1/24
     |
automation-python
eth0: 10.10.10.10/24
eth1: NAT / Internet access
```

Tools Used
GNS3
VMware Workstation Pro
GNS3 VM
VyOS
Alpine Linux Docker container
Python 3
Netmiko
SSH
VPCS

What This Lab Demonstrates
Building a virtual network in GNS3
Installing and configuring a VyOS router
Configuring an internal lab subnet
Enabling SSH access on VyOS
Creating an automation host with Python and Netmiko
Connecting to a router over SSH
Collecting interface and routing information
Backing up the router configuration with Python

| Device            | Interface |     IP Address | Purpose                  |
| ----------------- | --------- | -------------: | ------------------------ |
| VyOS              | eth0      |  10.10.10.1/24 | Router / SSH target      |
| PC1 / VPCS        | eth0      |  10.10.10.2/24 | Connectivity test client |
| automation-python | eth0      | 10.10.10.10/24 | Automation host          |
| automation-python | eth1      |   DHCP via NAT | Internet/package access  |

Automation Script

The Python script connects to the VyOS router using SSH and Netmiko, runs operational commands, prints results, and saves a configuration backup.

Commands collected:

show interfaces
show ip route
show configuration


Example Output
```
Connected to: vyos

=== Interfaces ===
eth0  10.10.10.1/24  u/u

=== Routes ===
C>* 10.10.10.0/24 is directly connected, eth0

Saved config backup to: backups/vyos_2026-04-29_02-21-43_config.txt
```

Future Improvements
Add a second VyOS router
Configure OSPF between routers
Create an inventory file for multiple devices
Add Ansible playbooks
Add automated compliance checks

