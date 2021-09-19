#!/usr/bin/env python3

NAMES = ['bart', 'homer', 'marge', 'lisa', 'guta', 'salam', 'tzanca', 'mihaita', 'vali', 'adrian']
# Generate docker-compose.yml.
#
with open("docker-compose.yml", "w") as f:
    f.write("version: '3'\n\nservices:\n")

    for index, name in enumerate(NAMES):
        f.write(f"  tor-{name}:\n")
        f.write(f"    container_name: 'tor-{name}'\n")
        f.write("    image: 'pickapp/tor-proxy:latest'\n")
        f.write("    ports:\n")
        f.write(f"      - '{9990+index}:8888'\n")
        f.write("    environment:\n")
        f.write("      - IP_CHANGE_SECONDS=60\n")
        f.write("    restart: always\n")

# Generate proxy-list.txt.
#
with open("proxy-list.txt", "w") as f:
    for index, name in enumerate(NAMES):
        f.write(f'http://127.0.0.1:{9990+index}\n')
