#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from random import randint as random
from keys import Real as Key

mayhem = ['пиздец', 'беспредел']
integrals = ['папей интегралов']
agression = ['агрессия']
yes_or_not = [['К о н е ч н о !', 'Абсолютно верно!', 'В точку!', 'Есессна!', 'Очевидно!',
               'Ну... Получается так, да.'],
              ['Не-а!', 'Н и х у я', 'А вот тут ты ошибаешься...', 'Нет.',
               'Что за херню я только что лицезрел? Чистейший бред от и до!',
               'Нет. Прошу, забудь как писать, чтобы никто больше не видел подобное.']]
cute_word = ['Милашка моя', 'Зайка моя', 'Великоуважаемый мешок костей и плоти',  'Лапочка ты наша',
             'Котя']
froggy = ['жаба', 'жабу']
language = ['лангуаже', 'лангуаге']
session = ['добор', 'пересдача']
ugay = ['сука я кто', 'сука, я кто', 'хто я']
derivatives = ['папей производных']
dispute = ['о чем спор?', 'о чём спор?', 'если через 10 лет...', 'спор фиита',
           'спор на фиите']
stream = ['каво?', 'вообще не понятно...', 'надо бы запустить стрим...']
delaetsya = ['это делается', 'это и делается']
exam_program = ['photo-190285544_457239428', 'photo-190285544_457239429']
am_i_right = ['так ведь?', 'правильно говорю?', 'верно понял?', 'правильно понял?', 'получается?', 'двачер?']
blacklist = [355746597]  # Kspich
vk_session = vk_api.VkApi(token=Key)
vk = vk_session.get_api()
exclamation = False
dangerous_point = False
longpoll = VkBotLongPoll(vk_session, '190285544')


def report(message: str) -> None:
    """Процедура репорта об ошибке"""
    vk.messages.send(
        user_id=118167164,
        random_id=get_random_id(),
        message='Бля, чуть не упал, а всё из-за этого!\n' + message)


def vk_send(is_user=True, id=None, message: str = None, attachment=None) -> None:
    """Процедура отправки сообщений"""
    if is_user:
        vk.messages.send(
            user_id=id,
            random_id=get_random_id(),
            message=message,
            attachment=attachment)
    else:
        vk.messages.send(
            chat_id=id,
            random_id=get_random_id(),
            message=message,
            attachment=attachment)


def check(t: str, d: 'list[str]') -> bool:
    return any([word in t.lower() for word in d])


def get_word(t: str, d: 'list[str]') -> str:
    for word in d:
        if word in t.lower():
            return word.title()

"""
def give_answer(number, u_i=None, c_i=None):
    num_of_pic = 457239429
    if u_i:
        vk_send(
            id=u_i,
            message=giving[random(0, 3, 1)],
            attachment='photo-190285544_' + str(num_of_pic + number))
    elif c_i:
        vk_send(
            is_user=False,
            id=c_i,
            attachment='photo-190285544_' + str(num_of_pic + number))

def exam(msg, u_i=None, c_i=None):
    if msg[0] == 'ответ':
        condition = msg[1].isdigit() and (0 < int(msg[1]) < 52)
        if condition:
            if u_i:
                give_answer(int(msg[1]), u_i=u_i)
            elif c_i:
                give_answer(int(msg[1]), c_i=c_i)
        else:
            if u_i:
                vk_send(
                    id=u_i,
                    message='Бля, ты обосрался')
            elif c_i:
                vk_send(
                    is_user=False,
                    id=c_i,
                    message='Бля, ты обосрался')
"""

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW and \
            len(event.obj.text) > 1 and \
            event.object.get('from_id') > 0:
        text = event.obj.text
        if event.from_user:
            is_user = True
            id = event.object.from_id
        else:
            is_user = False
            id = event.chat_id
        if not (event.object.get('from_id') in blacklist):
            dangerous_point = text[-1] == '.' and text[-2] != '.'
            exclamation = event.object.get('from_id') == 27053186 and \
                text[-1] == '!'
            if dangerous_point:
                if event.object.get('from_id') == 27053186:
                    vk_send(
                        is_user=is_user,
                        id=id,
                        message='Gotcha, bitch!',
                        attachment='photo-190285544_457239019')
                else:
                    vk_send(
                        is_user=is_user,
                        id=id,
                        attachment='photo-190285544_457239019')
                    dangerous_point = False
            elif exclamation:
                vk_send(
                    is_user=is_user,
                    id=id,
                    message='И ведь не соврал...',
                    attachment='photo-190285544_457239427')
            elif check(text, mayhem):
                vk_send(
                    is_user=is_user,
                    id=id,
                    attachment='photo-190285544_457239018')
            elif check(text, integrals):
                vk_send(
                    is_user=is_user,
                    id=id,
                    attachment='photo-190285544_457239017')
            elif check(text, agression):
                vk_send(
                    is_user=is_user,
                    id=id,
                    attachment='photo-190285544_457239020')
            elif check(text, language):
                vk_send(
                    is_user=is_user,
                    id=id,
                    attachment='photo-190285544_457239022')
            elif check(text, froggy):
                vk_send(
                    is_user=is_user,
                    id=id,
                    attachment='photo-190285544_457239021')
            elif check(text, session):
                vk_send(
                    is_user=is_user,
                    id=id,
                    message=f'Кто-то сказал \
                             "{get_word(text, session)}"?',
                    attachment='photo-190285544_457239024')
            elif check(text, ugay):
                vk_send(
                    is_user=is_user,
                    id=id,
                    attachment='photo-190285544_457239025')
            elif check(text, derivatives):
                vk_send(
                    is_user=is_user,
                    id=id,
                    attachment='photo-190285544_457239023')
            elif 'помидор' in text.lower() and \
                    event.object.get('from_id') == 273576556:
                vk_send(
                    is_user=is_user,
                    id=id,
                    attachment='photo-190285544_457239029')
            elif check(text, delaetsya):
                vk_send(
                    is_user=is_user,
                    id=id,
                    attachment='photo-190285544_457239028')
            elif check(text, dispute):
                vk_send(
                    is_user=is_user,
                    id=id,
                    message='Ну, как говорится...',
                    attachment='photo-190285544_457239425')
            elif check(text, stream):
                vk_send(
                    is_user=is_user,
                    id=id,
                    message='Как говорит некая Растя:',
                    attachment='photo-190285544_457239426')
            elif 'кошмар?' in text.lower():
                vk_send(
                    is_user=is_user,
                    id=id,
                    message='Кошмар!')
            elif check(text, am_i_right):
                yes_no = random(0, 1)
                answer = random(0, len(yes_or_not[yes_no])-1)
                if event.object.from_id == 118167164:  #  Protocol "Of course, master"
                    vk_send(
                        is_user=is_user,
                        id=id,
                        message=f'*id118167164(Ох, Создатель)...\n {yes_or_not[0][random(0, len(yes_or_not[0])-1)]}'
                    )
                else:
                    vk_send(
                        is_user=is_user,
                        id=id,
                        message=f'*id{event.object.from_id}({cute_word[random(0, len(cute_word)-1)]})...\n{yes_or_not[yes_no][answer]}'
                )
# TODO: Подумать о переносе кейвордов в отдельный файл...
# TODO: В муте клоун дединсайд
# TODO: Попробовать кейворды и их фотографии запихнуть в словарь, это сократит код
# TODO: Придумать реализацию с БД и добавлением туда персональных кейвордов пользователей
