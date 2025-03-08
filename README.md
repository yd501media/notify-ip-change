# notify-ip-change

A Python script to monitor global IP changes and send notifications to Discord via Webhook.

## Setup Environment

Follow these steps to set up the environment:

### 1. Clone the Repository
```sh
git clone https://github.com/yd501media/notify-ip-change.git
cd notify-ip-change
```

### 2. Install Required Python Libraries
```sh
pip install -r requirements.txt
```

## Usage

### 1. Set Environment Variables
Use `set_env.py` to configure the required environment variables:
```sh
python set_env.py --webhook https://discord.com/api/webhooks/YOUR_WEBHOOK_URL --port 25565
```

This will create a `.env` file in the project root with the following values:
```
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/YOUR_WEBHOOK_URL
SERVER_PORT=25565
```

### 2. Run the Script
Navigate to the `src/` directory and execute `notify_ip_change.py`:
```sh
python src/notify_ip_change.py
```

The script will:
- Fetch the current global IP address
- Compare it with the last recorded IP
- If changed, send a message to Discord including the new IP and port

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
