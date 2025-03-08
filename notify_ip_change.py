import requests
import json
import os
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
    load_dotenv()
    
    DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
    SERVER_PORT = os.getenv("SERVER_PORT")
    IP_FILE_PATH = "server_ip.txt"
    
    if not DISCORD_WEBHOOK_URL or not SERVER_PORT:
        print("Error: Environment variables DISCORD_WEBHOOK_URL and SERVER_PORT must be set in .env file.")
        exit(1)
    
    ip_address = get_global_ip()
    ip_address_old = read_old_ip(IP_FILE_PATH)
    
    if ip_address and ip_address != ip_address_old:
        message = f"Minecraft Server Global IP has changed: {ip_address}:{SERVER_PORT}"
        send_to_discord(DISCORD_WEBHOOK_URL, message)
        write_new_ip(IP_FILE_PATH, ip_address)
