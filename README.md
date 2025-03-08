# notify-ip-change

A Python script to monitor global IP changes and send notifications to Discord via Webhook.

## Setup Environment

Follow these steps to set up the environment:

### 1. Clone the Repository
```sh
git clone https://github.com/yd501media/notify-ip-change.git
cd notify-ip_change
```

### 2. Install Required Python Libraries
```sh
pip install -r requirements.txt
```

## Usage

### 1. Set Environment Variables
Use `set_env.py` to configure the required environment variables:
```sh
python3 src/set_env.py --webhook https://discord.com/api/webhooks/YOUR_WEBHOOK_URL --port 25565 --message "New Server IP Detected"
```

This will create a `.env` file in the project root (`~/notify_ip_change/.env`) with the following values:
```
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/YOUR_WEBHOOK_URL
SERVER_PORT=25565
NOTIFICATION_MESSAGE=New Server IP Detected
```

- `DISCORD_WEBHOOK_URL` (**Required**): The Discord Webhook URL to send notifications.
- `SERVER_PORT` (*Optional*): The port number associated with the service running on the server.
- `NOTIFICATION_MESSAGE` (*Optional*): A custom message to include in notifications.

### 2. Run the Script
Navigate to the project root and execute `notify_ip_change.py`:
```sh
python3 src/notify_ip_change.py
```

The script will:
- Fetch the current global IP address.
- Compare it with the last recorded IP stored in `server_ip.txt`.
- If changed, send a message to Discord including the new IP and port.
- Store the latest IP in `server_ip.txt` in the project root (`~/notify_ip_change/server_ip.txt`).

### **Message Format in Discord**
If `SERVER_PORT` is set:
```
New Server IP Detected: 203.0.113.45:25565
```
If `SERVER_PORT` is **not** set:
```
New Server IP Detected: 203.0.113.45
```

## Automate with Cron
To run the script periodically using `cron`, follow these steps:

### 1. Open Crontab
```sh
crontab -e
```

### 2. Add the Following Entry
```sh
0 * * * * cd /path/to/notify-ip-change && /usr/bin/python3 src/notify_ip_change.py
```

This will check for IP changes every 60 minutes and notify Discord if the IP has changed.
