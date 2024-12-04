import discord
from discord.ext import commands

class ModCogs(commands.Cog) :
    def __init__(self, bot) :
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kickoff(self, ctx, member : discord.Member,*, reason : str) :
        try :
            await member.kick(reason=reason)
            await ctx.send(f"le membre {member} a étais expulsé du serveur pour : {reason}")
        except Exception as e :
            print(e)
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason : str) :
        try :
            await member.ban(reason=reason)
            await ctx.send(f"le membre {member} a etais bannie du serveur pour avoir : {reason}")
        except Exception as e :
            print(e)

