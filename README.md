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

| Device | Interface | IP Address | Purpose |
|---|---|---:|---|
| VyOS | eth0 | 10.10.10.1/24 | Router / SSH target |
| PC1 / VPCS | eth0 | 10.10.10.2/24 | Connectivity test client |
| automation-python | eth0 | 10.10.10.10/24 | Automation host |
| automation-python | eth1 | DHCP via NAT | Internet/package access |

## VyOS Configuration Summary

```text
set interfaces ethernet eth0 address '10.10.10.1/24'
set service ssh port '22'
set system login user automation authentication plaintext-password '<LAB_PASSWORD>'
```

## Automation Script

The Python script connects to the VyOS router using SSH and Netmiko, runs operational commands, prints results, and saves a configuration backup.

Script location:

```text
scripts/backup_vyos_config.py
```

Commands collected:

```text
show interfaces
show ip route
show configuration
```

## Example Output

```text
Connected to: vyos

=== Interfaces ===
eth0  10.10.10.1/24  u/u

=== Routes ===
C>* 10.10.10.0/24 is directly connected, eth0

Saved config backup to: backups/vyos_2026-04-29_02-21-43_config.txt
```

## Running the Script

Set the lab password as an environment variable:

```bash
export VYOS_PASSWORD='<LAB_PASSWORD>'
python scripts/backup_vyos_config.py
```

## Lessons Learned

This lab helped reinforce:

- Basic GNS3 setup and troubleshooting
- Virtual router installation
- Internal lab networking
- SSH-based device management
- Python network automation fundamentals
- The difference between Layer 2 connectivity issues, IP configuration issues, and automation tooling issues

## Future Improvements

Planned improvements:

- Add a second VyOS router
- Configure OSPF between routers
- Create an inventory file for multiple devices
- Add Ansible playbooks
- Add automated compliance checks
- Add configuration drift detection
