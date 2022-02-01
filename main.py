# Importing libraries.
import os
import disnake
from disnake import Option, OptionType
from disnake.ext import commands
from decouple import config, UndefinedValueError


# Fetching environment variables.
try:
    tokens = {
        'discord': config('DISCORD_API_TOKEN', cast=str)
    }
except UndefinedValueError:
    exit()


# The primary Bot class.
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='//', 
            intents=disnake.Intents.all(), 
            help_command=None, 
            strip_after_prefix=True, 
            case_insensitive=True
        )
        
    async def on_connect(self):
        os.system('clear')
        
    async def on_ready(self):
        print('Bot is ready for testing / use!')
        
    async def on_message(self, message: disnake.Message):
        if message.author == self.user:
            return
        
bot = Bot()
  
    
# The cog for declaring main commands.
class CoreCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.slash_command(
        name='hello',
        description='Greets a server member with a simple greeting message.',
        options=[
            Option("member", "Mention the server member.", OptionType.user, required=True)
        ]
    )
    async def _hello(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member):
        await inter.send(f'Hey! {member}, nice to meet you!')
        
        
# Load cogs into the bot.
bot.add_cog(CoreCommands(bot))


# Run the bot.
bot.run(tokens['discord'])