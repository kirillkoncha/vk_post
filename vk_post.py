from vk_api import VkUpload, VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from conf import TOKEN, GROUP_ID
import markovify
vk_session = VkApi(token='f96c1c20592c07afe8c9ac7e76673768d014db929c245686a92ccae1f5bbe7244f7e821fd7b4c930827a4')
vk = vk_session.get_api()
model_json = open('mark_model.json').read()
model = markovify.Text.from_json(model_json)
import sched, time
s = sched.scheduler(time.time, time.sleep)
def post(sc): 
    vk.wall.post(message=model.make_short_sentence(280), owner_id='-194924812')
    s.enter(120, 1, post, (sc,))

s.enter(120, 1, post, (s,))
s.run()
