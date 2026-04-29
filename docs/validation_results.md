# Validation Results

## VPCS to VyOS Ping Test

VPCS was configured with:

```text
ip 10.10.10.2/24 10.10.10.1
```
### Ping to VyOS succeeded:
84 bytes from 10.10.10.1 icmp_seq=1 ttl=64
84 bytes from 10.10.10.1 icmp_seq=2 ttl=64
84 bytes from 10.10.10.1 icmp_seq=3 ttl=64

## Automation Host to VyOS Ping Test
### The automation host was configured with:
```
ip addr add 10.10.10.10/24 dev eth0
ip link set eth0 up
```
### Ping to VyOS succeeded:
```
64 bytes from 10.10.10.1: seq=0 ttl=64
64 bytes from 10.10.10.1: seq=1 ttl=64
64 bytes from 10.10.10.1: seq=2 ttl=64
```
## SSH Test
### SSH from the automation host to VyOS succeeded:
```ssh automation@10.10.10.1
Welcome to VyOS!
```

## Python Automation Test
The Python Netmiko script successfully connected to VyOS, collected interface and routing information, and saved a configuration backup.
```
Connected to: vyos
Saved config backup to: backups/vyos_2026-04-29_02-21-43_config.txt
```

