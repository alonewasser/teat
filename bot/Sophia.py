
from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api, random



vk_session = vk_api.VkApi(login='+79182229469', password='45ovizor', app_id=2685278)
vk_session.auth(token_only=True)

session_api = vk_session.get_api()

longpoll = VkLongPoll(vk_session)


def send_message(peer_id, message=None, attachment=None, keyboard=None, payload=None):
      session_api.messages.send(peer_id=peer_id, message=message,
                                          random_id=random.randint(- 2147483648, + 2147483648),
                                          attachment=attachment, keyboard=keyboard, payload=payload)


for event in longpoll.listen():

    if event.type ==VkEventType.MESSAGE_NEW:
     print('Текст сообщения: ' + str(event.text))
     response = event.text.lower()
     if event.from_user and not (event.from_me):
        if response == 'привет':
            send_message(peer_id=event.peer_id, message='Здравствуй')
        elif response == 'люблю тебя':
            send_message(peer_id=event.peer_id, message='И я тебя люблю, зайка <3')
        elif response == 'как дела?':
            send_message(peer_id=event.peer_id, message='Пойдет, как у тебя?')
        elif response == 'что делаешь?':
            send_message(peer_id=event.peer_id, message='Сижу, занимаюсь версткой, а ты?')
        elif response == 'чем занимаешься?':
            send_message(peer_id=event.peer_id, message='Сижу, занимаюсь версткой, а ты?')
        elif response == 'чем занимаешься':
            send_message(peer_id=event.peer_id, message='Сижу, занимаюсь версткой, а ты?')
        elif response == 'тупая пизда':
            send_message(peer_id=event.peer_id, message='Иди на хуй')
        elif response == 'как дела':
            send_message(peer_id=event.peer_id, message='Пойдет, как у тебя?')
        elif response == 'что делаешь':
            send_message(peer_id=event.peer_id, message='Сижу, занимаюсь версткой, а ты?')
        elif response == 'хочу тебя':
            send_message(peer_id=event.peer_id, message='Я тоже <3 :)')
        elif response == 'эй':
            send_message(peer_id=event.peer_id, message='шо?')
        elif response == 'как ты':
            send_message(peer_id=event.peer_id, message='Норм, а ты?')
        elif response == 'как ты?':
            send_message(peer_id=event.peer_id, message='Норм, а ты?')
        elif response == 'ты как':
            send_message(peer_id=event.peer_id, message='Норм, а ты?')
        elif response == 'ты как?':
            send_message(peer_id=event.peer_id, message='Норм, а ты?')
        elif response == 'пс':
            send_message(peer_id=event.peer_id, message='шо?')
        elif response == 'ну эй':
            send_message(peer_id=event.peer_id, message='шо?')
        elif response == 'ну эййй':
            send_message(peer_id=event.peer_id, message='шо?')
        elif response == 'пс пс':
            send_message(peer_id=event.peer_id, message='шо?')
        elif response == 'пс пс пс':
            send_message(peer_id=event.peer_id, message='шо?')
        elif response == 'эййй':
            send_message(peer_id=event.peer_id, message='шооо')
        elif response == 'хочу к тебе':
            send_message(peer_id=event.peer_id, message='И я <3')
        elif response == 'обнимаю':
            send_message(peer_id=event.peer_id, message='Обнимаю <3')
        elif response == '*обнимаю*':
            send_message(peer_id=event.peer_id, message='*Обнимаю взаимно*')
        elif response == 'ахах':
            send_message(peer_id=event.peer_id, message='ахахах')
        elif response == 'ахахахаха':
            send_message(peer_id=event.peer_id, message='ААХААХАХАХХАХХАА')
        elif response == 'пойдем гулять':
            send_message(peer_id=event.peer_id, message='Не хочу, у меня дела')
        elif response == 'пойдем гулять?':
            send_message(peer_id=event.peer_id, message='Не хочу, у меня дела')
        elif response == 'пососи':
            send_message(peer_id=event.peer_id, message='Пососи сам, ублюдок')
        elif response == 'отсоси':
            send_message(peer_id=event.peer_id, message='Пососи сам, ублюдок')
        elif response == 'сама пососи':
            send_message(peer_id=event.peer_id, message='Пососи сам, ублюдок')
        elif response == 'пойдём гулять':
            send_message(peer_id=event.peer_id, message='Не хочу, у меня дела')
        elif response == 'пойдём гулять?':
            send_message(peer_id=event.peer_id, message='Не хочу, у меня дела')
        elif response == 'соня':
            send_message(peer_id=event.peer_id, message='Что?')
        elif response == 'соня, привет':
            send_message(peer_id=event.peer_id, message='Привет')
        elif response == 'че делаешь?':
            send_message(peer_id=event.peer_id, message='Сижу, занимаюсь версткой, а ты?')
        elif response == 'ы':
            send_message(peer_id=event.peer_id, message='Ыыы')
        elif response == 'помоги':
            send_message(peer_id=event.peer_id, message='Не помогу')
        elif response == 'есть в долг?':
            send_message(peer_id=event.peer_id, message='Нету, я бомж')
        elif response == 'ответь нормально':
            send_message(peer_id=event.peer_id, message='пиши сюда ---> https://vk.com/jannyandmarjo')
        elif response == 'хуй соси':
            send_message(peer_id=event.peer_id, message='Сам соси, СаСаЛкА)0)00)')
        elif response == 'че делаешь':
            send_message(peer_id=event.peer_id, message='Сижу, занимаюсь версткой, а ты?')
        elif response == 'воняеш':
            send_message(peer_id=event.peer_id, message=':(')
        elif response == 'воняешь':
            send_message(peer_id=event.peer_id, message=':(')
        elif response == 'лох':
            send_message(peer_id=event.peer_id, message='ты спермобак ебаный')
        elif response == 'сам ты лох':
            send_message(peer_id=event.peer_id, message='ты спермобак ебаный')
        elif response == 'знаешь, что я дебилка?':
            send_message(peer_id=event.peer_id, message='Да, знаю')
        elif response == 'знаешь что я дебилка?':
            send_message(peer_id=event.peer_id, message='Да, знаю')
        elif response == 'я дебилка?':
            send_message(peer_id=event.peer_id, message='Да')
        elif response == '😚':
            send_message(peer_id=event.peer_id, message=':***')
        elif response == ':*':
            send_message(peer_id=event.peer_id, message=':*****')
        elif response == 'скинь бота':
            send_message(peer_id=event.peer_id, message='Нет, я его не для этого самостоятельно прописывала, чтобы какой-то щегол поросил его.')
        elif response == 'кинь бота':
            send_message(peer_id=event.peer_id, message='Нет, я его не для этого самостоятельно прописывала, чтобы какой-то щегол поросил его.')
        elif response == 'го курить':
            send_message(peer_id=event.peer_id, message='Не курю')
        elif response == 'пошли курить':
            send_message(peer_id=event.peer_id, message='Не курю')
        elif response == 'пойдем покурим':
            send_message(peer_id=event.peer_id, message='Не курю')
        elif response == 'покурим':
            send_message(peer_id=event.peer_id, message='Не курю')
        elif response == 'го по пиву':
            send_message(peer_id=event.peer_id, message='Не пью')
        elif response == 'го выпьем':
            send_message(peer_id=event.peer_id, message='Не пью')
        elif response == 'го курить?':
            send_message(peer_id=event.peer_id, message='Не курю')
        elif response == 'пошли курить?':
            send_message(peer_id=event.peer_id, message='Не курю')
        elif response == 'пойдем покурим?':
            send_message(peer_id=event.peer_id, message='Не курю')
        elif response == 'покурим?':
            send_message(peer_id=event.peer_id, message='Не курю')
        elif response == 'го по пиву?':
            send_message(peer_id=event.peer_id, message='Не пью')
        elif response == 'го выпьем?':
            send_message(peer_id=event.peer_id, message='Не пью')
        elif response == 'сонь':
            send_message(peer_id=event.peer_id, message='Что?')
        elif response == 'хелп':
            send_message(peer_id=event.peer_id, message='Я занята, напиши на другую страницу, если у тебя действительно что-то ВАЖНОЕ! https://vk.com/jannyandmarjo')
        elif response == 'отдай бота':
            send_message(peer_id=event.peer_id, message='Нет, я его не для этого самостоятельно прописывала, чтобы какой-то щегол поросил его.')
        elif response == 'продай бота':
            send_message(peer_id=event.peer_id,
                         message='Нет, я его не для этого самостоятельно прописывала, чтобы какой-то щегол поросил его.')







