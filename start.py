import os
from dotenv import load_dotenv
import discord 
from discord.ext import commands
from keep_alive import keep_alive

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

class StBot(commands.Bot) :
    async def setup_hook(self) :#cherche les extension
        for extention in ['games','help', 'moderation'] : #boucle sur les extension présent dans modération
            await self.load_extension(f"cogs.{extention}") # cherche les extension cogs présent dans modération  #installer flask load_dotenv()

intents = discord.Intents.all()
bot = StBot(command_prefix='!', intents=intents)

keep_alive()
def main() :
    bot.run(token)

if __name__ == '__main__' :
    main()
