#!/usr/bin/env python3
import json
import sys

def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--host':
        hostname = sys.argv[2] if len(sys.argv) > 2 else ''
        print(json.dumps({}))
        return

    inventory = {
        "staging": {
            "hosts": [
                "staging-01.local",
                "staging-02.local"
            ]
        },
        "production": {
            "hosts": [
                "prod-web01.local",
                "prod-db01.local"
            ]
        },
        "webservers": {
            "hosts": ["staging-01.local", "prod-web01.local"],
            "vars": {"role": "web"}
        },
        "databases": {
            "hosts": ["staging-02.local", "prod-db01.local"],
            "vars": {"role": "db"}
        },
        "_meta": {
            "hostvars": {
                "staging-01.local": {
                    "ansible_host": "192.168.0.100",
                    "ansible_user": "evgenii",
                    "env": "staging"
                },
                "staging-02.local": {
                    "ansible_host": "192.168.0.100",
                    "ansible_user": "evgenii",
                    "env": "staging"
                },
                "prod-web01.local": {
                    "ansible_host": "192.168.0.100",
                    "ansible_user": "evgenii",
                    "env": "production",
                    "http_port": 80
                },
                "prod-db01.local": {
                    "ansible_host": "10.0.0.11",
                    "ansible_user": "evgenii",
                    "env": "production",
                    "postgres_port": 5432
                }
            }
        }
    }

    print(json.dumps(inventory, indent=2))

if __name__ == "__main__":
    main()
