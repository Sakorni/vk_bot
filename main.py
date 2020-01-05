import vk_api
from token_holder import token as t
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
mayhem = ['пиздец', 'беспредел']
integrali = ['папей интегралов']
agression = ['агрессия']
froggy = ['жаб']
language = ['лангуаже','лангуаге']
sesssion = ['сессия', 'экзамен', 'добор', 'пересдача']
ugay = ['сука я кто','сука, я кто']
proizv = ['папей производных']
vk_session = vk_api.VkApi(token=t())
vk = vk_session.get_api()
dangerous_point = False
longpoll = VkBotLongPoll(vk_session, "190285544")
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        text = event.obj.text
        firstone = True
        if event.from_chat:
            if len(text)>1:
                dangerous_point = text[-1] == '.' and text[-2] != '.'
            bespredel = mayhem[0] in text.lower() or mayhem[1] in text.lower()
            if dangerous_point:
                vk.messages.send(
                    chat_id=event.chat_id,
                    random_id=get_random_id(),
                    attachment='photo-190285544_457239019')
            else:
                if firstone:
                    for word in mayhem:
                        if word in text.lower():
                            vk.messages.send(
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                attachment='photo-190285544_457239018')
                            firstone = False
                            break
                if firstone:
                    for word in integrali:
                        if word in text.lower():
                            vk.messages.send(
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                attachment='photo-190285544_457239017')
                            firstone = False
                            break
                if firstone:
                    for word in agression:
                        if word in text.lower():
                            vk.messages.send(
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                attachment='photo-190285544_457239020')
                            firstone = False
                            break
                if firstone:
                    for word in language:
                        if word in text.lower():
                            vk.messages.send(
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                attachment='photo-190285544_457239022')
                            firstone = False
                            break
                if firstone:
                    for word in froggy:
                        if word in text.lower():
                            vk.messages.send(
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                attachment='photo-190285544_457239021')
                            firstone = False
                            break
                if firstone:
                    for word in sesssion:
                        if word in text.lower():
                            vk.messages.send(
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                attachment='photo-190285544_457239024')
                            firstone = False
                            break
                if firstone:
                    for word in ugay:
                        if word in text.lower():
                            vk.messages.send(
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                attachment='photo-190285544_457239025')
                            firstone = False
                            break
                if firstone:
                    for word in proizv:
                        if word in text.lower():
                            vk.messages.send(
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                attachment='photo-190285544_457239023')
                            firstone = False
                            break
