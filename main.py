import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from random import randrange as random


def check(t, d):  # t - text, d - dictionary
    return any([word in t.lower() for word in d])


def getword(t, d):
    for word in d:
        if word in t.lower():
            return word.title()


mayhem = ['пиздец', 'беспредел']
integrali = ['папей интегралов']
agression = ['агрессия']
giving = ['Лови!', 'Держи!', 'Рад помочь!', 'А вот и ваш ответ!']
froggy = ['жаб']
language = ['лангуаже', 'лангуаге']
session = ['сессия', 'экзамен', 'добор', 'пересдача']
ugay = ['сука я кто', 'сука, я кто', 'хто я?']
proizv = ['папей производных']
spor = ['о чем спор?', 'о чём спор?', 'если через 10 лет...', 'спор фиита', 'спор на фиите']
stream = ['каво?', 'вообще не понятно...', 'надо бы запустить стрим...']
delaetsya = ['делается']
exam = '''_________Матрицы___________
1. Матрица, понятие матрицы.
2. Виды матриц: квадратные, прямоугольные, скалярные, диагональные.
3. Операции над матрицами: умножение матрицы на число, сложение матриц, 
умножение матриц и их свойства.
4. Транспонированная матрица. Взаимодействие транспонирования с
операциями.
5. Понятие об обратной матрице. Теорема о единственности обратной матрицы.
6. Матрицы-делители нуля. Примеры.
7. Существование необратимых матриц (Теорема о том, что матрица-делитель
нуля не может быть обратима).
8. Степени квадратной матрицы и отрицательные степени (только для обратимых
матриц).
9. Многочлен от матриц.\n
_________Определители___________
10. Подстановки и перестановки.
11. Характеристики σ(P) (delta), ε(P) (epsilon) и их свойства.
12. Композиция перестановок. Формы записи перестановок.
13. Группа перестановок и её некоммутативность.
14. Три определения определителя и их эквивалентности.
15. Свойства определителей.
16. Миноры и алгебраические дополнения.
17. Малая и средняя теоремы Лапласа.
18. «Теорема об ошибке».
19. Теорема об определителе произведения квадратных матриц.
20. Критерий равенства нулю определителя (только достаточность).
21. Приложение теории определителей: критерий обратимости матрицы,
теорема Крамера, критерий наличия ненулевых решений у квадратной ОСЛУ.\n
_________КЧ___________
22. Комплексные числа – понятие.
23. Алгебраические операции над комплексными числами и их свойства.
24. Комплексное сопряжение.
25. Модуль и аргумент комплексного числа.
26. Умножение комплексных чисел в тригонометрической форме.
27. Возведение в степень комплексного числа (формула Муавра).
28. Деление во множестве комплексных чисел. Деление в алгебраической и
тригонометрической формах.
29. Модуль и аргумент комплексного числа (сводка свойств).
30. Корни из комплексных чисел. Основная теорема о корнях. Геометрия корней.
31. Корни n-ой степени из единицы. Группа корней n-ой степени из единицы.
32. Первообразные корни и их существование.\n
_____________ Многочлены___________________
33. Определение многочлена.
34. Алгебраические операции над многочленами и их свойства.
35. Деление с остатком во множестве многочленов.
36. Определитель Вандермонда и его свойства. Вычисление определителя
Вандермонда.
37. Теорема единственности для многочленов.
38. Корни многочленов.
39. Основная теорема алгебры (без доказательства) и следствие из неё (с
доказательством).
40. Теорема Безу и следствие из неё.
41. Кратность корня (определение).
42. Теорема о разложении многочлена по корням над полем комплексных чисел.
43. Многочлены с вещественными коэффициентами. Теорема о комплексных
корнях такого многочлена.
44. Разложение многочлена с вещественными коэффициентами на множители
над полем вещественных чисел.
45. Общие делители (ОД) многочленов. Понятие о наибольшем общем делителе
(НОД).
46. Теорема: Если P(x) = h(x)∙g(x) + r(x), то НОД(P, g) = НОД(g, r).
47. Теорема: Если P(x) = h(x)∙g(x), то НОД(P, g) = g.
48. Теорема: алгоритм Евклида.
49. Многочлен и его производная.
50. Теорема о том, что при переходе к производной, кратность корня падает на
единицу.
51. Задача о нахождении многочлена, который имеет те же корни, что и
исходный многочлен, но его корни – простые.'''
blacklist = [355746597, -170393012]  # Kspich, Kai
vk_session = vk_api.VkApi(token="05128f85ead375f22797a6becd5c6dcf089a0fe8b66def904b9ed8166c471f1c51fbb95582ba30d89501f")
vk = vk_session.get_api()
dangerous_point = False
longpoll = VkBotLongPoll(vk_session, "190285544")


def give_answer(number, u_i=None, c_i=None):
    num_of_pic = 457239429
    if u_i:
        try:
            vk.messages.send(
                user_id=u_i,
                random_id=get_random_id(),
                message=giving[random(0, 3, 1)],
                attachment='photo-190285544_' + str(num_of_pic + number))
        except:
            vk.messages.send(
                user_id=118167164,
                random_id=get_random_id(),
                message='Бля, почти упал! А всё из-за этого:\n'+str(event.object))

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
            attachment=['photo-190285544_457239428', 'photo-190285544_457239429'])
    elif u_i:
        vk.messages.send(
            user_id=u_i,
            random_id=get_random_id(),
            attachment=['photo-190285544_457239428', 'photo-190285544_457239429'])


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
                    elif check(text, integrali):
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
                            message='Кто-то сказал "' + getword(text, session) + '"?',
                            attachment='photo-190285544_457239024')
                    elif check(text, ugay):
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            attachment='photo-190285544_457239025')
                    elif check(text, proizv):
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            attachment='photo-190285544_457239023')
                    elif 'помидор' in text.lower() and event.object.get('from_id') == 273576556:
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            attachment='photo-190285544_457239029')
                    elif check(text, delaetsya):
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            attachment='photo-190285544_457239028')
                    elif check(text, spor):
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
# TODO Reply Таво
# TODO В муте клоун дединсайд
