import flask
import flask_wtf
import wtforms
from itertools import permutations
start_set = list(sorted(set([i for i in "Корєнев Олександр Олександрович".replace(' ', '').upper()])))
start_set.insert(5, "Є")
start_set = start_set[1::]
print(start_set)


def get_result(m: int):
    global start_set
    with open('result.txt', mode='w') as f:
        for i in permutations(start_set, m):
            f.write('<br>')
            f.write(''.join(i))
            f.write('</br>')
    with open('result.txt') as f:
        return f.read()


class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = 'e9fc4fca2c9fb29090742ad630e417bb5db210c9951f2420478ababd'


class Form(flask_wtf.FlaskForm):
    size = wtforms.IntegerField()


app = flask.Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET', 'POST'])
def hello():
    form = Form()
    if flask.request.method == 'POST':
        if not form.data.get('size'):
            return flask.redirect(flask.request.url)
        else:
            return get_result(form.data.get('size'))
    return flask.render_template_string("""
    <h3>Лабораторна робота</h3>
    <h3>студента групи ІВ-72</h3>
    <h3>Корєнева Олександра</h3>
    <br>Початкова множина - {А, В, Д, Е, Є, И, К, Л, Н, О, Р, С, Ч}</br> 
    <br>Вивчити алгоритм генерації підмножин заданої множини, який
        використовує принципи роботи алгоритму генерації двійкових векторів.
        Написати програму генерації підмножин у лексикографічному порядку,
        використовуючи алгоритм генерації двійкових векторів.
        Вхідні параметри мають такі значення: 
        № Опис варіанта
        1. Множину  сформувати з букв свого прізвища, імені та
        по батькові, виключивши повторення букв.
        2. Максимальне значення n дорівнює кількості одержаних різних букв з
        прізвища, імені та по батькові.
        3. Значення m може змінюватися довільно від 1 до n . </br>
    <form action="" method="post" name="login">
    {{form.hidden_tag()}}
    <p>
        {{form.size}}<br>
    </p>
    <p><input type="submit" value="get result"></p>
    </form>""", form=form)


if __name__ == '__main__':
    app.run()
