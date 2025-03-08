import argparse
import os


def set_env_variable(env_var, value, env_path):
    os.environ[env_var] = value
    with open(env_path, "a") as file:
        file.write(f"{env_var}={value}\n")
    print(f"{env_var} saved to environment variable and .env file at {env_path}.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Set environment variables for Discord Webhook URL, Port Number, and Notification Message."
    )
    parser.add_argument(
        "--webhook",
        required=True,
        help="The Discord Webhook URL to set as an environment variable. (Required)",
    )
    parser.add_argument(
        "--port", help="The port number to set as an environment variable. (Optional)"
    )
    parser.add_argument(
        "--message",
        help="The custom notification message to set as an environment variable. (Optional)",
    )
    args = parser.parse_args()

    # Ensure .env is created in the project root (~/notify_ip_change/.env)
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env_path = os.path.join(project_root, ".env")

    set_env_variable("DISCORD_WEBHOOK_URL", args.webhook, env_path)

    if args.port:
        set_env_variable("SERVER_PORT", args.port, env_path)

    if args.message:
        set_env_variable("NOTIFICATION_MESSAGE", args.message, env_path)
