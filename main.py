import telebot 
from config import token
from logic import Pokemon

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['feed'])
def feed(message):
    username = message.from_user.username
    if username in Pokemon.pokemons.keys():
        pokemon = Pokemon.pokemons[username]
        result = pokemon.feed()
        bot.reply_to(message, result)
    else:
        bot.reply_to(message, "Сначала создай покемона командой /go")

@bot.message_handler(commands=['info'])
def info(message):
    username = message.from_user.username
    if username in Pokemon.pokemons.keys():
        pokemon = Pokemon.pokemons[username]
        info_text = f"{pokemon.info()}\n\nУровень: {pokemon.level}\nОпыт: {pokemon.exp}/{pokemon.exp_to_next_level}\nСытость: {pokemon.hunger}%\nСчастье: {pokemon.happiness}%\nВес: {pokemon.weight:.1f}кг\nЕда: {pokemon.inventory.get('food', 0)}"
        bot.send_message(message.chat.id, info_text)
    else:
        bot.reply_to(message, "Сначала создай покемона командой /go")

@bot.message_handler(commands=['achievements'])
def achievements(message):
    username = message.from_user.username
    if username in Pokemon.pokemons.keys():
        pokemon = Pokemon.pokemons[username]
        achievements_text = pokemon.get_achievements()
        bot.send_message(message.chat.id, achievements_text)
    else:
        bot.reply_to(message, "Сначала создай покемона командой /go")

bot.infinity_polling(none_stop=True)
