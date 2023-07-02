{% extends "base.html" %}

{% block content %}
    <h1>{{ message }}</h1>

    <form action="/variants" method="GET">
        <div class="mb-3">
            <label for="searchField" class="form-label">Введите название лекарства или действующего вещества:</label>

            <input type="text" name="search" class="form-control" id="searchField" placeholder="лоперамид">
        </div>

        <button type="submit" class="btn btn-primary">Искать</button>
    </form>
{% endblock %}