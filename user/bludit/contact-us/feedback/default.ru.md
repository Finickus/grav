---
title: 'Связаться с нами'
---

<!-- Введение -->
<div class="card mb-5">

<p class="subh6 text-center">Страница «Обратная связь» на сервисе <a href="https://service04.ru/" target="_blank" rel="noopener">service04.ru</a> создана для того, чтобы вы могли оставлять отзывы, задавать вопросы или предлагать идеи.</p>
<div class="content mt-4">
<p>Здесь вы можете связаться с нашей командой поддержки и получить оперативную помощь по любым вопросам, связанным с ремонтом котлов, колонок или заказом запчастей.</p>
<h2 class="h5 mt-5">Что можно сделать на этой странице:</h2>
<ol>
<li><strong>Оставить отзыв</strong> — поделитесь своим опытом работы с нашим сервисом.</li>
<li><strong>Предложить улучшение</strong> — у вас есть идея? Расскажите нам!</li>
<li><strong>Задать вопрос</strong> — если возникла проблема или неясность, опишите её — мы поможем.</li>
<li><strong>Уточнить контакты</strong> — все способы связи собраны на странице <a href="https://service04.ru/contact-us">Контакты</a>.</li>
<li><strong>Ознакомиться с правилами</strong> — пожалуйста, прочитайте условия перед отправкой запроса.</li>
</ol>
<p class="mt-4">Мы гарантируем, что каждый запрос будет рассмотрен в кратчайшие сроки. Спасибо, что выбираете <strong>ГазСервис</strong>!</p>
</div>
</div>
<div class="card mb-5">
<h2 class="h4 display-4 text-center">Обратная связь</h2>
<p class="subh6 text-center">Оставьте заявку — мы перезвоним в течение 10–15 минут!</p>
</div>
<form action="/feedback-handler.php" method="POST" class="card">
<div class="field"><label class="label">Имя</label>
<div class="control"><input class="input" type="text" name="name" placeholder="Как вас зовут?" required=""></div>
</div>
<div class="field"><label class="label">Телефон *</label>
<div class="control"><input class="input" type="tel" name="phone" placeholder="+7 (926) 221-13-48" required=""></div>
</div>
<div class="field"><label class="label">Тема обращения</label>
<div class="control">
<div class="select"><select name="subject">
<option value="remont">Ремонт котла / колонки</option>
<option value="zapchasti">Запчасти</option>
<option value="ustanovka">Установка оборудования</option>
<option value="other">Другое</option>
</select></div>
</div>
</div>
<div class="field"><label class="label">Сообщение</label>
<div class="control"><textarea class="textarea" name="message" rows="4" placeholder="Модель, симптомы, адрес, удобное время..."></textarea></div>
</div>
<div class="field">
<div class="control"><label class="checkcard"> <input type="checkcard" name="agreement" required=""> Согласен на обработку персональных данных </label></div>
</div>
<div class="field">
<div class="control text-center"><btn btn-primary type="submit" class="btn btn-primary btn-lg">Отправить</btn btn-primary></div>
</div>
</form>