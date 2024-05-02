import requests
import time
import os

# Function to get public IP address
def get_public_ip():
    response = requests.get('https://api.ipify.org')
    return response.text.strip()

# Function to send message to Discord channel
def send_discord_message(ip_address):
    discord_webhook_url = os.getenv('DISCORD_WEBHOOK_URL')
    message = f"New IP address: {ip_address}"
    payload = {"content": message}
    response = requests.post(discord_webhook_url, json=payload)
    if response.status_code == 200:
        print("Message sent successfully to Discord.")
    else:
        print(f"Failed to send message to Discord. Status code: {response.status_code}")

# Main function
def main():
    previous_ip = None
    while True:
        current_ip = get_public_ip()
        if current_ip != previous_ip:
            print("IP address has changed.")
            send_discord_message(current_ip)
            previous_ip = current_ip
        else:
            print("IP address hasn't changed.")
        time.sleep(300)  # Check every 5 minutes

if __name__ == "__main__":
    main()
