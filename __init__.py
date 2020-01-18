import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from keys import Real as tiktoken
vk_session = vk_api.VkApi(token=tiktoken)
vk = vk_session.get_api()
dangerous_point = False
longpoll = VkBotLongPoll(vk_session, '190285544')
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        print(event)
