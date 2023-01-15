from keyboard import sender
from main import *

for event in bot.longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        request = event.text.lower()
        user_id = str(event.user_id)
        msg = event.text.lower()
        if request == 'go':
            sender(user_id, f'Супер, приятно познакомиться, {bot.name(user_id)}!')
        elif request == 'начать поиск':
            bot.write_msg(user_id, 'Пару мгновений...')
            creating_database()
            bot.find_user(user_id)
            bot.write_msg(user_id, f'Нашёл для тебя пару, жми на кнопку "Вперёд"')
        elif request == 'вперёд':
            for i in line:
                offset += 1
                bot.find_persons(user_id, offset)

                
                break

        else:
            bot.write_msg(user_id, f'Такая команда мне не знакома, напиши "Go", чтобы появились кнопки!')
