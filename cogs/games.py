import random
from discord.ext import commands

class GamesCog(commands.Cog) :
    def __init__(self, bot) :
        self.bot = bot
    
    @commands.command()
    async def dee(self, ctx) :
        try :
            await ctx.send(f"le nombre choisie et {random.randint(1,6)}")
        except Exception as e :
            print(e)
    
    @commands.command()
    async def choisir(self, ctx, nb1 : int, nb2 : int) :
        try : 
            if (nb1 < nb2) :
                await ctx.send("Erreur,Le premier nombre dois être impérativemnt inférieur au deuxième...")
                return
            await ctx.send(f"le nombre choisie entre {nb1} et {nb2} est {random.randint(nb1,nb2)}")
        except Exception as e :
            print(e)

async def setup(bot) :
    await bot.add_cog(GamesCog(bot))