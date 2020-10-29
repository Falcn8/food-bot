import random
import discord
from discord.ext import commands
import asyncio
import os
from colorama import Fore, Back, Style, init

clear = lambda: os.system('cls')
clear()

client = commands.Bot(command_prefix = '!')

foods = ["🍇 Grapes",
"🍈 Melon",
"🍉 Watermelon",
"🍊 Tangerine",
"🍋 Lemon",
"🍌 Banana",
"🍍 Pineapple",
"🥭 Mango",
"🍎 Red Apple",
"🍏 Green Apple",
"🍐 Pear",
"🍑 Peach",
"🍒 Cherries",
"🍓 Strawberry",
"🥝 Kiwi Fruit",
"🍅 Tomato",
"🥥 Coconut",
"🥑 Avocado",
"🍆 Eggplant",
"🥔 Potato",
"🥕 Carrot",
"🌽 Ear of Corn",
"🌶️ Hot Pepper",
"🥒 Cucumber",
"🥬 Leafy Green",
"🥦 Broccoli",
"🧄 Garlic",
"🧅 Onion",
"🍄 Mushroom",
"🥜 Peanuts",
"🌰 Chestnut",
"🍞 Bread",
"🥐 Croissant",
"🥖 Baguette Bread",
"🥨 Pretzel",
"🥯 Bagel",
"🥞 Pancakes",
"🧇 Waffle",
"🧀 Cheese Wedge",
"🍖 Meat on Bone",
"🍗 Poultry Leg",
"🥩 Cut of Meat",
"🥓 Bacon",
"🍔 Hamburger",
"🍟 French Fries",
"🍕 Pizza",
"🌭 Hot Dog",
"🥪 Sandwich",
"🌮 Taco",
"🌯 Burrito",
"🥙 Stuffed Flatbread",
"🧆 Falafel",
"🥚 Egg",
"🍳 Cooking",
"🥘 Shallow Pan of Food",
"🍲 Pot of Food",
"🥣 Bowl with Spoon",
"🥗 Green Salad",
"🍿 Popcorn",
"🧈 Butter",
"🧂 Salt",
"🥫 Canned Food",
"🍱 Bento Box",
"🍘 Rice Cracker",
"🍙 Rice Ball",
"🍚 Cooked Rice",
"🍛 Curry Rice",
"🍜 Steaming Bowl",
"🍝 Spaghetti"
"🍠 Roasted Sweet Potato",
"🍢 Oden",
"🍣 Sushi",
"🍤 Fried Shrimp",
"🍥 Fish Cake with Swirl",
"🥮 Moon Cake",
"🍡 Dango",
"🥟 Dumpling",
"🥠 Fortune Cookie",
"🥡 Takeout Box",
"🦪 Oyster",
"🍦 Soft Ice Cream",
"🍧 Shaved Ice",
"🍨 Ice Cream",
"🍩 Doughnut",
"🍪 Cookie",
"🎂 Birthday Cake",
"🍰 Shortcake",
"🧁 Cupcake",
"🥧 Pie",
"🍫 Chocolate Bar",
"🍬 Candy",
"🍭 Lollipop",
"🍮 Custard",
"🍯 Honey Pot",
"🍼 Baby Bottle",
"🥛 Glass of Milk",
"☕ Hot Beverage",
"🍵 Teacup Without Handle",
"🍶 Sake",
"🍾 Bottle with Popping Cork",
"🍷 Wine Glass",
"🍸 Cocktail Glass",
"🍹 Tropical Drink",
"🍺 Beer Mug",
"🍻 Clinking Beer Mugs",
"🥂 Clinking Glasses",
"🥃 Tumbler Glass",
"🥤 Cup with Straw",
"🧃 Beverage Box",
"🧉 Mate",
"🧊 Ice",
"🥢 Chopsticks",
"🍽️ Fork and Knife with Plate",
"🍴 Fork and Knife",
"🥄 Spoon"]

@client.event
async def on_ready():
    print(Fore.LIGHTBLUE_EX + """
___________________   ________  ________    ______________________   _____    ____________________
\_   _____/\_____  \  \_____  \ \______ \   \_   _____/\_   _____/  /  _  \  /   _____/\__    ___/
 |    __)   /   |   \  /   |   \ |    |  \   |    __)   |    __)_  /  /_\  \ \_____  \   |    |   
 |     \   /    |    \/    |    \|    `   \  |     \    |        \/    |    \/        \  |    |   
 \___  /   \_______  /\_______  /_______  /  \___  /   /_______  /\____|__  /_______  /  |____|   
     \/            \/         \/        \/       \/            \/         \/        \/            
     
""" + Fore.WHITE)

@client.event
async def on_message(message):
    if message.content.startswith("food") or message.content.startswith("Food"):
        await message.channel.send(random.choice(foods))
        print("Sent\n")

client.run("YOUR TOKEN HERE")
