#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from random import randint as random
from keys import Real as Key

mayhem = ['это пиздец ', ' беспредел ', 'полный пиздец ', ' пиздец ']
mayhem_answers = ['Согласен, это полный', 'И не говори! Сплошной',
                  'Что бы сказал на это Насека?',
                  'Не, ну границы-то знать надо... Это уже какой-то']
integrals = ['папей интегралов']
agression = ['агрессия']
yes_or_not = [['К о н е ч н о !', 'Абсолютно верно!', 'В точку!', 'Есессна!',
               'Очевидно!',
               'Ну... Получается так, да.'],
              ['Не-а!', 'Н и х у я', 'А вот тут ты ошибаешься...', 'Нет.',
               'Что за херню я только что лицезрел? Чистейший бред от и до!',
               'Нет. Прошу, забудь как писать, чтобы никто больше не видел'
               ' подобное.']]
cute_word = ['Милашка моя', 'Золотце', 'Великоуважаемый мешок костей и плоти',
             'Лапочка ты наша', 'Котя']
froggy = ['жаба', 'жабу']
language = ['лангуаже', 'лангуаге']
u_gay = ['сука я кто', 'сука, я кто', 'хто я']
u_gay_answers = ['Ты еще спрашиваешь?', 'Ну, тут долго думать даже не надо, '
                                        'если честно', 'Ответ, так сказать, на поверхности',
                 'Я готов подсказать!', 'Хах! Легчайший вопрос в моей жизни!']
derivatives = ['папей производных']
dispute = ['о чем спор?', 'о чём спор?', 'если через 10 лет...', 'спор фиита',
           'спор на фиите']
stream = ['каво?', 'вообще не понятно...', 'надо бы запустить стрим...']
delaetsya = ['это делается', 'это и делается']
exam_program = ['photo-190285544_457239428', 'photo-190285544_457239429']
am_i_right = ['так ведь?', 'правильно говорю?', 'верно понял?',
              'правильно понял?', 'получается?', 'двачер?']
funny = ['воу, как смешно', 'ха-ха-ха', 'нихуя ты пошутил',
         ' фить ', ' фьють ']
drama = ['дешевые драмы', 'мдам, что за драма...']
sudo_users = [118167164, 255536801, 202071395]
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


def vk_send(is_user=True, id=None, message: str = None,
            attachment=None) -> None:
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
    """Проверяет, есть ли слово в списке"""
    # TODO: Можно убрать check и использовать get_word вместо неё
    return any([word in t.lower() for word in d])


def get_word(t: str, d: 'list[str]') -> str:
    """Возвращает слово из списка"""
    for word in d:
        if word in t.lower():
            return word.title()
    return ''


vagina = False
dangerous_point: bool
is_user: bool
id: int  # TODO: Поменять название переменной для избежания коллизии имён
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW and \
            len(event.obj.text) > 1 and \
            event.object.get('from_id') > 0:
        text = event.obj.text
        rnd = random(0, 20)
        if event.from_user:
            is_user = True
            id = event.object.from_id
        else:
            is_user = False
            id = event.chat_id
        if not (event.object.get('from_id') in blacklist):
            dangerous_point = bool(text[-1] == '.' and text[-2] != '.'
                                   and event.object.from_id == 27053186)
            exclamation = event.object.get('from_id') == 27053186 and \
                          text[-1] == '!'
            if event.object.from_id in sudo_users and \
                'sudo' in text.lower():
                if text.lower() == "sudo пизда":
                    vagina = True
                elif text.lower() == "sudo не пизда":
                    vagina = False
            if dangerous_point:
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
            elif vagina and ("да" == text.lower()):
                vk_send(
                    is_user=is_user,
                    id=id,
                    attachment='photo-190285544_457239482')
            elif check(text, mayhem):
                vk_send(
                    is_user=is_user,
                    id=id,
                    message=mayhem_answers[rnd % len(mayhem_answers)],
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
            elif check(text, u_gay):
                vk_send(
                    is_user=is_user,
                    id=id,
                    message=u_gay_answers[rnd % len(u_gay_answers)],
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
                answer = random(0, len(yes_or_not[yes_no]) - 1)
                if event.object.from_id in sudo_users and \
                        'sudo' in text.lower():
                    vk_send(
                        is_user=is_user,
                        id=id,
                        message=f'*id{event.object.from_id}(Ох, Создатель)...'
                                f'\n {yes_or_not[0][rnd % len(yes_or_not[0])]}'
                    )
                else:
                    vk_send(
                        is_user=is_user,
                        id=id,
                        message=f'*id{event.object.from_id}'
                                f'({cute_word[random(0, len(cute_word) - 1)]})...\n'
                                f'{yes_or_not[yes_no][answer]}'
                    )
            elif check(text, funny):
                print(1)
                vk_send(
                    is_user=is_user,
                    id=id,
                    attachment='audio164693486_456239512'
                )
            elif check(text, drama):
                vk_send(
                    is_user=is_user,
                    id=id,
                    message='На эту тему даже песня есть!',
                    attachment='audio371745432_456428678'
                )
# TODO: Подумать о переносе кейвордов в отдельный файл...
# TODO: В муте клоун дединсайд
# TODO: Попробовать кейворды и их фотографии запихнуть в словарь,
#  это сократит код
# TODO: Придумать реализацию с БД и добавлением туда персональных
#  кейвордов пользователей
