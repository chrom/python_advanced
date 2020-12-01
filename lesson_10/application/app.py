# 1) Написать REST для блога (использовать валидацию).
# Реализовать модель Пост (название, содержание, дата публикации, автор, кол-во просмотров, тег).
# Реализовать модель тег.
# Реализовать модель автор (имя, фамилия, кол-во публикаций автора).
# Добавить валидацию ко всем полям.
# Реализовать модуль заполнения всех полей БД валидными (адеквадными данными :) ).
# Добавить вывод всех постов по тегу, при каждом обращении к  конкретному посту увеличовать кол-во просмотров на 1.
# При обращении к автору, выводить все его публикации.

from flask import Flask, request, jsonify, Response
from .models import Author, Post, Tag

app = Flask(__name__)


@app.route('/author', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/author/<string:user_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def author(author_id=None):
    if request.method == 'GET':
        users = Author.objects()
        users_json = users.to_json()
        return Response(users_json, content_type='application/json')

    elif request.method == 'POST':
        user = Author(**request.json).save()
        user_json = user.to_json()
        return Response(user_json, content_type='application/json')

    elif request.method == 'PUT' and author_id:
        user = Author.objects().get(id=author_id)
        user.update(**request.json)
        user.reload()
        return Response(user.to_json(), content_type='application/json')

    elif request.method == 'DELETE' and author_id:
        Author.objects(id=author_id).delete()
        return jsonify({'status': 'Deleted'})
    else:
        return jsonify({'status': 'Error'})


app.run(debug=True)
