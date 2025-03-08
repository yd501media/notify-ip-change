import json
import os

import requests
from dotenv import load_dotenv


def get_global_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        response.raise_for_status()
        return response.json().get("ip")
    except requests.RequestException as e:
        print(f"Error retrieving IP address: {e}")
        return None


def read_old_ip(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return file.read().strip()
    return None


def write_new_ip(file_path, ip):
    with open(file_path, "w") as file:
        file.write(ip)


def send_to_discord(webhook_url, message):
    data = {"content": message}
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
        response.raise_for_status()
        print("Message sent to Discord successfully.")
    except requests.RequestException as e:
        print(f"Error sending message to Discord: {e}")


if __name__ == "__main__":
    dotenv_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env"
    )
    load_dotenv(dotenv_path)

    DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
    SERVER_PORT = os.getenv("SERVER_PORT")
    NOTIFICATION_MESSAGE = os.getenv("NOTIFICATION_MESSAGE", "New Server IP Detected")

    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    IP_FILE_PATH = os.path.join(project_root, "server_ip.txt")

    if not DISCORD_WEBHOOK_URL:
        print(
            "Error: Environment variable DISCORD_WEBHOOK_URL must be set in .env file."
        )
        exit(1)

    ip_address = get_global_ip()
    ip_address_old = read_old_ip(IP_FILE_PATH)

    if ip_address and ip_address != ip_address_old:
        if SERVER_PORT:
            message = f"{NOTIFICATION_MESSAGE}: {ip_address}:{SERVER_PORT}"
        else:
            message = f"{NOTIFICATION_MESSAGE}: {ip_address}"

        send_to_discord(DISCORD_WEBHOOK_URL, message)
        write_new_ip(IP_FILE_PATH, ip_address)
