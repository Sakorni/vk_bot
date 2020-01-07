import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
def check(t,d):#t - text, d - dictionary
    return any([word in t.lower() for word in d])
mayhem = ['пиздец', 'беспредел']
integrali = ['папей интегралов']
agression = ['агрессия']
froggy = ['жаб']
language = ['лангуаже','лангуаге']
session = ['сессия', 'экзамен', 'добор', 'пересдача']
ugay = ['сука я кто','сука, я кто']
proizv = ['папей производных']
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
42. Теорема о разложении многочлена по корням над полем комплексных чисел.\n
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

vk_session = vk_api.VkApi(token="b8de20df2f74e9f6e8ebddbc800f88b9290ffeac55a93482bedb63ed5eda79ffd41e8d7677b57b1bda967")
vk = vk_session.get_api()
dangerous_point = False
longpoll = VkBotLongPoll(vk_session, "190612884")#190612884 - test ; 190285544 - working
for event in longpoll.listen():
    #print(event)
    if event.type == VkBotEventType.MESSAGE_NEW:
        text = event.obj.text
        print(event)
        firstone = True
        if event.from_chat:
            print(dangerous_point, text)
            if text.lower() == 'программа':
                vk.messages.send(
                    chat_id=event.chat_id,
                    random_id=get_random_id(),
                    message=exam)
            if len(text)>1:
                dangerous_point = text[-1] == '.' and text[-2] != '.'
            if dangerous_point:
                vk.messages.send(
                    chat_id=event.chat_id,
                    random_id=get_random_id(),
                    attachment='photo-190285544_457239019')
                dangerous_point = False
            else:
                if check(text, mayhem):
                    vk.messages.send(
                        chat_id=event.chat_id,
                        random_id=get_random_id(),
                        attachment='photo-190285544_457239018')
                elif check(text,integrali):
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
                elif check (text, session):
                    vk.messages.send(
                        chat_id=event.chat_id,
                        random_id=get_random_id(),
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
                elif check (text, delaetsya):
                    vk.messages.send(
                        chat_id=event.chat_id,
                        random_id=get_random_id(),
                        attachment='photo-190285544_457239028')
                elif 'кошмар?' in text.lower(): #TODO
                    vk.messages.send(
                        chat_id=event.chat_id,
                        random_id=get_random_id(),
                        message='Кошмар!')