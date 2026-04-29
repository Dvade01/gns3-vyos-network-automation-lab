# GNS3 VyOS Network Automation Lab

## Overview

This project is a hands-on network automation lab built with GNS3, VyOS, Alpine Linux, SSH, and Python Netmiko.

The goal of the lab is to simulate a small network environment, enable SSH access to a virtual router, and use Python automation to collect network information and back up the router configuration.

## Lab Topology

```text
PC1 / VPCS
10.10.10.2/24
     |
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
## Tools Used

- GNS3
- VMware Workstation Pro
- GNS3 VM
- VyOS rolling release
- Alpine Linux Docker container
- Python 3
- Netmiko
- SSH
- VPCS

## What This Lab Demonstrates

- Building a virtual network in GNS3
- Installing and configuring a VyOS router
- Configuring an internal lab subnet
- Enabling SSH access on VyOS
- Creating an automation host with Python and Netmiko
- Connecting to a router over SSH
- Collecting interface and routing information
- Backing up the router configuration with Python

## IP Addressing
| Device            | Interface |     IP Address | Purpose                  |
| ----------------- | --------- | -------------: | ------------------------ |
| VyOS              | eth0      |  10.10.10.1/24 | Router / SSH target      |
| PC1 / VPCS        | eth0      |  10.10.10.2/24 | Connectivity test client |
| automation-python | eth0      | 10.10.10.10/24 | Automation host          |
| automation-python | eth1      |   DHCP via NAT | Internet/package access  |

## VyOS Configuration Summary

```text
set interfaces ethernet eth0 address '10.10.10.1/24'
set service ssh port '22'
set system login user automation authentication plaintext-password '<LAB_PASSWORD>'
```
##Automation Script
The Python script connects to the VyOS router using SSH and Netmiko, runs operational commands, prints results, and saves a configuration backup.

### Commands collected:

show interfaces
show ip route
show configuration

## Example Output
Connected to: vyos

=== Interfaces ===
eth0  10.10.10.1/24  u/u

=== Routes ===
C>* 10.10.10.0/24 is directly connected, eth0

Saved config backup to: backups/vyos_2026-04-29_02-21-43_config.txt

## Lessons Learned
### This lab helped reinforce:

Basic GNS3 setup and troubleshooting
Virtual router installation
Internal lab networking
SSH-based device management
Python network automation fundamentals
The difference between connectivity issues at Layer 2, IP configuration issues, and automation tooling issues
## Future Improvements
### Planned improvements:
Add a second VyOS router
Configure OSPF between routers
Create an inventory file for multiple devices
Add Ansible playbooks
Add automated compliance checks
Add configuration drift detection

## Step 4: Add your Python script

Create a folder called:

```text
scripts
```
Inside it, create:
```
backup_vyos_config.py
```

Put this in it:

```
from datetime import datetime
from pathlib import Path
from netmiko import ConnectHandler


device = {
    "device_type": "vyos",
    "host": "10.10.10.1",
    "username": "automation",
    "password": "{PASSWORD}", # will make this a into an enviroment variable later
}


backup_dir = Path("backups")
backup_dir.mkdir(exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


with ConnectHandler(**device) as connection:
    hostname = connection.send_command("show host name").strip() or "vyos"
    interfaces = connection.send_command("show interfaces")
    routes = connection.send_command("show ip route")
    config = connection.send_command("show configuration")

    print(f"Connected to: {hostname}")

    print("\n=== Interfaces ===")
    print(interfaces)

    print("\n=== Routes ===")
    print(routes)

    backup_file = backup_dir / f"{hostname}_{timestamp}_config.txt"
    backup_file.write_text(config, encoding="utf-8")

    print(f"\nSaved config backup to: {backup_file}")
```
For a more professional version later, we will move the password out of the script and into an environment variable or separate ignored file.
