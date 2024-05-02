# IP Address Checker with Discord Integration

This Dockerized script checks the public IP address twice a day and posts it in a Discord channel. Additionally, it listens to the same Discord channel for requests to post the IP address again.

## Setup Instructions

### 1. Create a Discord Bot

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click on "New Application" and give your bot a name.
3. Navigate to the "Bot" tab on the left sidebar and click "Add Bot".
4. Note down the bot token. You will need this token for authentication.

### 2. Obtain the Discord Channel ID

1. Open Discord and navigate to the server and channel where you want to post the IP address.
2. Right-click on the channel name and select "Copy ID". Note down the copied ID. 

### 3. Create a Discord Webhook

1. In your Discord server, navigate to the channel where you want to post the IP address.
2. Click on the settings gear icon next to the channel name.
3. Go to "Integrations" > "Webhooks" and click "Create Webhook".
4. Give your webhook a name and note down the webhook URL.

### 4. Set Environment Variables

Create a `.env` file in the root directory of this project with the following variables:

DISCORD_WEBHOOK_URL=<your_discord_webhook_url>
DISCORD_API_URL=https://discord.com/api/v9
DISCORD_CHANNEL_ID=<your_discord_channel_id>
DISCORD_BOT_TOKEN=<your_discord_bot_token>

Replace `<your_discord_webhook_url>`, `<your_discord_channel_id>`, and `<your_discord_bot_token>` with the respective values obtained in the previous steps.

### 5. Build and Run Docker Container

```bash
# Build Docker image
docker build -t ip-checker .

# Run Docker container
docker run -d --restart=always --env-file .env ip-checker
