<h1>Task_manager Менеджер задач</h1>

<p>Это API менеджера задач, построенный с использованием django rest framework.</p>

<h2>Особенности</h2>

<ul>
<li>Аутентификация пользователей (регистрация и вход)</li>
<li>Создание, обновление и удаление задач (операции CRUD)</li>
<li>Создание, обновление, удаление проекта и привязка задач к проеку (операции CRUD)</li>
</ul>

<h2>Установка</h2>

<ol>
<li>Клонируйте репозиторий:</li>
</ol>

<ol start="2">
<li>Перейдите в каталог проекта:</li>
</ol>

<pre><code>cd &lt;/task_manager2_0&gt;
</code></pre>

<ol start="3">
<li>Установите зависимости:</li>
</ol>

<pre><code>pip install -r requirements.txt
</code></pre>

<ol start="5">
<li>Запустите сервер :</li>
</ol>

<pre><code>python manage.py runserver
</code></pre>

<h2>Конечные точки API</h2>

<h3>Пользователи</h3>

<ul>
<li><code>POST create_user/</code>: Зарегистрировать нового пользователя.</li>
<li><code>POST api-token-auth/</code>: Войти и получить токен доступа.</li>
</ul>

<h3>Задачи</h3>

<ul>
<li><code>POST api/v1/task/ </code>: Создать новую задачу.</li>
<li><code>GET api/v1/task/ <code>: Получить все задачи аутентифицированного пользователя.</li>
<li><code>PUT api/v1/task/{task_id} </code>: Обновить задачу.</li>
<li><code>DELETE api/v1/task/{task_id} </code>: Удалить задачу.</li>
</ul>

<h3>Проект</h3>

<ul>
<li><code>POST api/v1/project/ </code>: Создать новуый проект.</li>
<li><code>GET api/v1/project/ <code>: Получить все проекты аутентифицированного пользователя.</li>
<li><code>PUT api/v1/project/{project_id} </code>: Обновить проект.</li>
<li><code>DELETE api/v1/task/{project_id} </code>: Удалить проект.</li>
</ul>

  
