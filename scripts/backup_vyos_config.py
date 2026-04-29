import os
from datetime import datetime
from pathlib import Path

from netmiko import ConnectHandler


device = {
    "device_type": "vyos",
    "host": "10.10.10.1",
    "username": "automation",
    "password": os.getenv("VYOS_PASSWORD"),
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
