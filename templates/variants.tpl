{% extends "base.html" %}

{% block content %}
    <h1>"Вы искали "{{ message }}"</h1>
    
    <form action="/result" method="POST">
        <div class="mb-3">
            <label class="form-label">Выберите вариант:</label>
            
            {% for item in search_list %}
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" value="{{ item }}" name="search" id="ch_{{ loop.index }}">
                    
                    <label class="form-check-label" for="ch_{{ loop.index }}">{{ item }}</label>
                </div>
            {% endfor %}
        </div>
        
        <button type="submit" class="btn btn-primary">Искать</button>
    </form>
{% endblock %}