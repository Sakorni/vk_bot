#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from random import randrange as random
from keys import Testkey

mayhem = ['пиздец', 'беспредел']
integrals = ['папей интегралов']
agression = ['агрессия']
giving = ['Лови!', 'Держи!', 'Рад помочь!', 'А вот и ваш ответ!']
froggy = ['жаб']
language = ['лангуаже', 'лангуаге']
session = ['сессия', 'экзамен', 'добор', 'пересдача']
ugay = ['сука я кто', 'сука, я кто', 'хто я?']
derivatives = ['папей производных']
dispute = ['о чем спор?', 'о чём спор?', 'если через 10 лет...', 'спор фиита',
           'спор на фиите']
stream = ['каво?', 'вообще не понятно...', 'надо бы запустить стрим...']
delaetsya = ['делается']


blacklist = [355746597]  # Kspich, Kai
vk_session = vk_api.VkApi(token=Workingkey)
vk = vk_session.get_api()
dangerous_point = False
longpoll = VkBotLongPoll(vk_session, '190285544')



def check(t: str, d: dict) -> bool:
    return any([word in t.lower() for word in d])


def getword(t: str, d: dict) -> str:
    for word in d:
        if word in t.lower():
            return word.title()


def give_answer(number, u_i=None, c_i=None):
    num_of_pic = 457239429
    if u_i:
        vk.messages.send(
            user_id=u_i,
            random_id=get_random_id(),
            message=giving[random(0, 3, 1)],
            attachment='photo-190285544_' + str(num_of_pic + number))
    elif c_i:
        vk.messages.send(
            chat_id=c_i,
            random_id=get_random_id(),
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
                vk.messages.send(
                    user_id=u_i,
                    random_id=get_random_id(),
                    message='Бля, ты обосрался')
            elif c_i:
                vk.messages.send(
                    chat_id=c_i,
                    random_id=get_random_id(),
                    message='Бля, ты обосрался')


def program(c_i=None, u_i=None):
    if c_i:
        vk.messages.send(
            chat_id=c_i,
            random_id=get_random_id(),
            attachment=['photo-190285544_457239428',
                        'photo-190285544_457239429'])
    elif u_i:
        vk.messages.send(
            user_id=u_i,
            random_id=get_random_id(),
            attachment=['photo-190285544_457239428',
                        'photo-190285544_457239429'])


def vk_send(chat_id=None, mes: str = None, att: str = None) -> None:
    """Процедура отправки сообщений"""
    vk.messages.send(
            chat_id=chat_id,
            random_id=get_random_id(),
            message=mes,
            attachment=att)


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW and \
            event.obj.text != '':
        text = event.obj.text
        for_exam = text.lower().split()
        if event.from_user:
            if text.lower() == 'программа':
                program(u_i=event.object.from_id)
            elif len(for_exam) > 2:
                exam(for_exam, event.object.from_id)
        elif event.from_chat and \
                event.object.get('from_id') > 0:
            if text.lower() == 'программа':  # Начало блока экзамена
                program(c_i=event.chat_id)
            if len(for_exam) > 1 and for_exam[0] == 'ответ':
                if len(for_exam) == 3 and for_exam[2] == 'лс':
                    exam(for_exam, u_i=event.object.from_id)
                else:
                    exam(for_exam, c_i=event.chat_id)  # Конец блока экзамена
            if not (event.object.get('from_id') in blacklist):
                if len(text) > 1:
                    dangerous_point = text[-1] == '.' and text[-2] != '.'
                    exclamation = event.object.get('from_id') == 27053186 and \
                        text[-1] == '!'
                    if dangerous_point:
                        if event.object.get('from_id') == 27053186:
                            vk.messages.send(
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                message='Gotcha, bitch!',
                                attachment='photo-190285544_457239019')
                        else:
                            vk.messages.send(
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                attachment='photo-190285544_457239019')
                            dangerous_point = False
                    elif exclamation:
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='И ведь не соврал...',
                            attachment='photo-190285544_457239427')
                    elif check(text, mayhem):
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            attachment='photo-190285544_457239018')
                    elif check(text, integrals):
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            attachment='photo-190285544_457239017')
                    elif check(text, agression):
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            attachment='photo-190285544_457239020')
                    elif check(text, language):
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            attachment='photo-190285544_457239022')
                    elif check(text, froggy):
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            attachment='photo-190285544_457239021')
                    elif check(text, session):

                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message=f'Кто-то сказал \
                                     "{getword(text, session)}"?',
                            attachment='photo-190285544_457239024')
                    elif check(text, ugay):
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            attachment='photo-190285544_457239025')
                    elif check(text, derivatives):
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            attachment='photo-190285544_457239023')
                    elif 'помидор' in text.lower() and \
                         event.object.get('from_id') == 273576556:
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            attachment='photo-190285544_457239029')
                    elif check(text, delaetsya):
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            attachment='photo-190285544_457239028')
                    elif check(text, dispute):
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Ну, как говорится...',
                            attachment='photo-190285544_457239425')
                    elif check(text, stream):
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Как говорит некая Растя:',
                            attachment='photo-190285544_457239426')
                    elif 'кошмар?' in text.lower():
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Кошмар!')
# TODO: Reply Таво
# TODO: В муте клоун дединсайд
