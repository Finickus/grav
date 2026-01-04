---
title: Связаться с нами
metadata:
  description: Связаться с нами Страница «Обратная связь» на сервисе service04.ru
    создана для того, чтобы вы могли оставлять отзывы, задавать вопросы или предлагать
    идеи.
  og:type: website
  og:title: Связаться с нами - Service04
  og:description: Связаться с нами Страница «Обратная связь» на сервисе service04.ru
    создана для того, чтобы вы могли оставлять отзывы, задавать вопросы или предлагать
    идеи.
  og:url: https://service04.ru/contact-us/feedback
  og:site_name: Service04
  og:locale: ru_RU
  og:image: https://service04.ru/images/og-default.jpg
  og:image:width: '1200'
  og:image:height: '630'
  canonical: https://service04.ru/contact-us/feedback
  robots: index, follow
  yandex-verification: ''
  geo.region: RU-MOW
  geo.placename: Москва
  author: Service04
---
<div class="container py-4">

    <div class="card shadow-sm border-0 mb-5">
        <div class="card-body p-4">
            <h1 class="h4 text-center mb-3">Связаться с нами</h1>
            <p class="text-center text-muted mb-4">
                Страница «Обратная связь» на сервисе <a href="https://service04.ru/" target="_blank" rel="noopener" class="text-decoration-none">service04.ru</a> создана для того, чтобы вы могли оставлять отзывы, задавать вопросы или предлагать идеи.
            </p>
            
            <div class="mt-4">
                <p>Здесь вы можете связаться с нашей командой поддержки и получить оперативную помощь по любым вопросам, связанным с ремонтом котлов, колонок или заказом запчастей.</p>
                
                <h2 class="h5 mt-4 fw-bold">Что можно сделать на этой странице:</h2>
                <ol class="list-group list-group-numbered border-0">
                    <li class="list-group-item border-0 ps-0"><strong>Оставить отзыв</strong> — поделитесь своим опытом работы с нашим сервисом.</li>
                    <li class="list-group-item border-0 ps-0"><strong>Предложить улучшение</strong> — у вас есть идея? Расскажите нам!</li>
                    <li class="list-group-item border-0 ps-0"><strong>Задать вопрос</strong> — если возникла проблема или неясность, опишите её — мы поможем.</li>
                    <li class="list-group-item border-0 ps-0"><strong>Уточнить контакты</strong> — все способы связи собраны на странице <a href="https://service04.ru/contact-us" class="text-decoration-none">Контакты</a>.</li>
                    <li class="list-group-item border-0 ps-0"><strong>Ознакомиться с правилами</strong> — пожалуйста, прочитайте условия перед отправкой запроса.</li>
                </ol>
                
                <p class="mt-4 mb-0">Мы гарантируем, что каждый запрос будет рассмотрен в кратчайшие сроки. Спасибо, что выбираете <strong>ГазСервис</strong>!</p>
            </div>
        </div>
    </div>

    <div class="card shadow-sm border-0">
        <div class="card-header bg-white border-0 pt-4 pb-0 text-center">
            <h2 class="h4">Обратная связь</h2>
            <p class="text-muted small">Оставьте заявку — мы перезвоним в течение 10–15 минут!</p>
        </div>
        
        <div class="card-body p-4">
            <form action="/feedback-handler.php" method="POST">
                
                <div class="mb-3">
                    <label for="formName" class="form-label">Имя</label>
                    <input type="text" class="form-control" id="formName" name="name" placeholder="Как вас зовут?" required>
                </div>

                <div class="mb-3">
                    <label for="formPhone" class="form-label">Телефон *</label>
                    <input type="tel" class="form-control" id="formPhone" name="phone" placeholder="+7 (926) 221-13-48" required>
                </div>

                <div class="mb-3">
                    <label for="formSubject" class="form-label">Тема обращения</label>
                    <select class="form-select" id="formSubject" name="subject">
                        <option value="remont">Ремонт котла / колонки</option>
                        <option value="zapchasti">Запчасти</option>
                        <option value="ustanovka">Установка оборудования</option>
                        <option value="other">Другое</option>
                    </select>
                </div>

                <div class="mb-3">
                    <label for="formMessage" class="form-label">Сообщение</label>
                    <textarea class="form-control" id="formMessage" name="message" rows="4" placeholder="Модель, симптомы, адрес, удобное время..."></textarea>
                </div>

                <div class="mb-4 form-check">
                    <input type="checkbox" class="form-check-input" id="formAgreement" name="agreement" required>
                    <label class="form-check-label user-select-none" for="formAgreement">
                        Согласен на обработку персональных данных
                    </label>
                </div>

                <div class="d-grid gap-2 col-md-6 mx-auto">
                    <button type="submit" class="btn btn-primary btn-lg">Отправить</button>
                </div>

            </form>
        </div>
    </div>

</div>