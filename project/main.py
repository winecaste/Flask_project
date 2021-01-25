
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from flask import current_app


main = Blueprint('main', __name__)



Данные = [{
    'Вопрос': 'Какого газа в атмосфере Земли больше всего?',  
    'Варианты': ['Кислород', 'Углекислый газ', 'Водорот', 'Азот'],  
    'Ответ': 'Азот'},  
    {
    'Вопрос': 'Какой римской цифры не существует?',
    'Варианты': ['1000', '0', '10000', '100000'],
    'Ответ': '0'},
    {
    'Вопрос': 'Чего боятся люди, которые страдают алекторофобией?',
    'Варианты': ['Собак', 'Кур', 'Бород', 'Чеснока'],
    'Ответ': 'Кур'},
     {
    'Вопрос': 'В какой стране более одной столицы?',
    'Варианты': ['ЮАР', 'Алжир', 'Тунис'],
    'Ответ': 'ЮАР'},
     {
    'Вопрос': 'Мозг используется только на 10%. Правда или ложь?',
    'Варианты': ['Правда', 'Ложь'],
    'Ответ': 'Ложь'},
]



@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        punkty = 0
        Варианты = request.form

        for pnr, odp in Варианты.items():
            if odp == Данные[int(pnr)]['Ответ']:
                punkty += 1

        flash('Правильных ответов: {0}'.format(punkty))
        return redirect(url_for('main.profile'))

    return render_template('profile.html', Вопрос=Данные)
    

    