from nextcord.ext import commands
from nextcord import Intents, Interaction, SlashOption, File, Embed, Color, ButtonStyle
import random
from PIL import Image, ImageDraw
from nextcord.ui import Button, View


intents = Intents.default()
intents.message_content = True

def gen_imgs_with_circles(width, height):
    image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    for i in range(1000):
        x = random.randint(0, width)
        y = random.randint(0, height)
        radius = random.randint(10, 200)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color, outline=None)
    return image

def gen_imgs_with_shapes(width, height):
    image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    for i in range(100):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        shape = random.choice(['rectangle', 'ellipse', 'line'])
        if shape == 'rectangle':
            draw.rectangle((x1, y1, x2, y2), fill=color, outline=None)
        elif shape == 'ellipse':
            draw.ellipse((x1, y1, x2, y2), fill=color, outline=None)
        elif shape == 'line':
            draw.line((x1, y1, x2, y2), fill=color, width=random.randint(1, 10))
    return image

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

@bot.slash_command(name='about', description='What is VariantArt🎨?')
async def about(interaction: Interaction):
    await interaction.response.send_message('VariantArt🎨 is a bot that generates algorithmic art which can be further minted as NFT by users or users can download generated arts.')

@bot.slash_command(name="algorithmic-art", description="What is algorithmic art?")
async def define_algorithmic_art(interaction: Interaction):
    website = Button(label="Wikipedia", url=f"https://en.wikipedia.org/wiki/Algorithmic_art")
    myview = View(timeout=180)
    myview.add_item(website)
    await interaction.response.send_message("**What is Algorithmic art?**\n\n**Algorithmic art** is a type of art that is created using computer algorithms. The artist sets up a set of rules or procedures, often using mathematical functions or algorithms, that define the parameters of the artwork. These rules can be programmed into a computer program or written out by hand, and the resulting artwork is generated automatically by the computer based on the rules set by the artist.\nWanna Learn more about Algorithmic art? Navigate here:", view=myview)

@bot.slash_command(name='generate-circles-art', description='Generates a art using randomly placed circles of Random sizes')
async def generate_img_with_circles(interaction: Interaction, width:int=1280, height:int=720):
    image = gen_imgs_with_circles(width, height)
    image.save('image.png')
    with open('image.png', 'rb') as f:
        img = File(f)
    download = Button(label='Download', url="https://www.google.com", emoji="💾")
    mint = Button(label="Mint", url="https://www.google.com")
    myview = View(timeout=180)
    myview.add_item(download)
    myview.add_item(mint)
    await interaction.response.send_message(file=img, view=myview)

@bot.slash_command(name='generate-shapes-art', description='Generates a art using randomly placed shapes of Random sizes')
async def generate_img_with_shapes(interaction: Interaction, width:int=1280, height:int=720):
    image = gen_imgs_with_shapes(width, height)
    image.save('image.png')
    with open('image.png', 'rb') as f:
        img = File(f)
    download = Button(label='Download', url="", emoji="💾")
    mint = Button(label="Mint", url="https://www.google.com")
    myview = View(timeout=180)
    myview.add_item(download)
    myview.add_item(mint)
    await interaction.response.send_message(file=img, view=myview)


token = "your_discord_bot_token"
bot.run(token)
