# Build your own Discord bot

This repository contains source code for building a Discord bot using Python.

## How to configure and run this bot

1. Clone the repository.
2. Rename is the `.env.example` file to `.env` in the Source directory.
3. Replace the `DISCORD_BOT_TOKEN` in the `.env` file with your Discord Bot Token.
4. Run the `bot.py` file using `python bot.py` command.
5. Install the Bot in your Discord server

## Running the Bot using Docker

1. Pull the docker image using the command `docker pull anuraj/discord-bot:latest`.
2. Next run the docker container `docker run -d --name discordbot --env DISCORD_BOT_TOKEN="<ADD-YOUR-DISCORD-BOT-TOKEN-HERE>" anuraj/discord-bot:latest`
3. Install the Bot in your Discord server

## Building the docker image

1. Build the docker image using the command `docker build -t <YOUR-DOCKER-HUB-NAME>/discord-bot .`

Happy Coding 😊