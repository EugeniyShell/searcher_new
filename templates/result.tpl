{% extends "base.html" %}

{% block content %}
    <h1>
        Вы искали {% for item in search_list %}
            "{{ item }}"{% if not loop.last %}, {% endif %}
        {% endfor %}.
    </h1>

    <div class="list-group list-group-flush">
        {% if result_list|length %}
            <h2 class="list-group-item">
                Нам удалось найти:
            </h2>

            {% for item in result_list %}
                <a class="list-group-item flex" href="{{ item.link }}" target="_blank">
                    <span>
                        {{ item.name }}
                    </span>

                    <span class="badge bg-primary rounded-pill">
                        {{ item.price }}
                    </span>
                </a>
            {% endfor %}
        {% else %}
            <h2 class="list-group-item">
                Нам ничего не удалось найти.
            </h2>
        {% endif %}
    </div>
{% endblock %}