import os
import argparse

def set_env_variable(env_var, value):
    os.environ[env_var] = value
    with open(".env", "a") as file:
        file.write(f"{env_var}={value}\n")
    print(f"{env_var} saved to environment variable and .env file.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Set environment variables for Discord Webhook URL and Port Number.")
    parser.add_argument("--webhook", help="The Discord Webhook URL to set as an environment variable.")
    parser.add_argument("--port", help="The port number to set as an environment variable.")
    args = parser.parse_args()
    
    if args.webhook:
        set_env_variable("DISCORD_WEBHOOK_URL", args.webhook)
    
    if args.port:
        set_env_variable("SERVER_PORT", args.port)
