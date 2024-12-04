import discord
from discord.ext import commands

class HelpCogs(commands.Cog):
    def __init__(self, bot) :
        self.bot = bot

    @commands.command()
    async def info(self, ctx) :
        embed = discord.Embed(
            title="Voici la liste des commandes :",
            description="Vous verrai ci dessous la listes des commandes du serveur",
            color=discord.Color.purple()
        )
        
        embed.add_field(
            name=" :game_die: Lancer un dée :",
            value="!dee ",
            inline=False
        )

        embed.add_field(
            name="Choisir un chiffre au hasard grâce a 2 nombre: ",
            value="!choisir <premier nombre> <deuxième nombre> ",
            inline=False
        )

        embed.add_field(
            name="Expulser un membre: ",
            value="!kickoff <membre> <raison de l'expulsion> ",
            inline=False
        )

        embed.add_field(
            name="Bannir un membre : ",
            value="!ban <membre> <raison>",
            inline=False
        )

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(HelpCogs(bot))