#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from random import randrange as random
from keys import Real as Key

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
exam_program = ['photo-190285544_457239428', 'photo-190285544_457239429']  # Программа экзамена
blacklist = [355746597]  # Kspich
vk_session = vk_api.VkApi(token=Key)
vk = vk_session.get_api()
exclamation = False
dangerous_point = False
longpoll = VkBotLongPoll(vk_session, '190285544')


def report(message: str):
    """Процедура репорта об ошибке"""
    vk.messages.send(
        user_id=118167164,
        random_id=get_random_id(),
        message=message)


def vk_send(is_user: bool = True, id: int = None, message: str = None, attachment = None):
    """Процедура отправки сообщений"""
    try:
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
    except:
        report(message='Чуть не умер!\n' + str(event.object))

def check(t: str, d: 'list[str]') -> bool:
    return any([word in t.lower() for word in d])


def getword(t: str, d: 'list[str]'):
    for word in d:
        if word in t.lower():
            return word.title()


def give_answer(number: int, u_i: int = None, c_i: int = None):
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


def exam(msg: 'list[str]', u_i: int = None, c_i: int = None):
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


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW and \
            len(event.obj.text) > 1 and \
            event.object.get('from_id') > 0:
        text = event.obj.text
        for_exam = text.lower().split()
        if event.from_user:
            is_user = True
            id = event.object.from_id
        else:
            is_user = False
            id = event.chat_id
        if text.lower() == 'программа':
            vk_send(is_user=is_user, id=id, attachment=exam_program)
        elif len(for_exam) > 1 and is_user:  #  TODO доделать нормальную реализацию, поиграться с функцией exam
            exam(for_exam, event.object.from_id)
        if len(for_exam) > 1 and for_exam[0] == 'ответ':
            if len(for_exam) == 3 and for_exam[2] == 'лс':
                exam(for_exam, u_i=event.object.from_id)
            else:
                exam(for_exam, c_i=event.chat_id)  # Конец блока экзамена
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
                             "{getword(text, session)}"?',
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
# TODO: Reply Таво
# TODO: В муте клоун дединсайд
