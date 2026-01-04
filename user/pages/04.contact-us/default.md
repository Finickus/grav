---
title: Контакты
process:
    twig: true
    markdown: false
---

<style>
    /* Небольшие стили для выравнивания иконок внутри кнопок */
    .btn-social {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        font-weight: bold;
    }
    /* Чтобы карточки были одинаковой высоты */
    .h-100 { height: 100%; }
</style>

<section class="py-5 text-white text-center mb-4" style="background-color: #0d6efd;">
    <div class="container">
        <h1 class="fw-bold">Контакты</h1>
        <p class="lead mb-0">Свяжитесь с нами удобным для вас способом</p>
    </div>
</section>

<div class="card shadow-sm border-0 p-4 mb-5">
    <div class="row g-3 justify-content-center mb-5">
        <div class="col-md-4">
            <a href="https://tlgg.ru/GazService04" target="_blank" rel="noopener" class="btn btn-outline-info btn-lg w-100 btn-social">
                <img src="telega.svg" width="24" height="24" alt="Telegram">
                <span>Telegram</span>
            </a>
        </div>
        <div class="col-md-4">
            <a href="https://wa.me/79262211348?text=Здравствуйте,%20у%20меня%20вопрос%20по%20поводу" target="_blank" rel="noopener" class="btn btn-outline-success btn-lg w-100 btn-social">
                <img src="whatsapp.svg" width="24" height="24" alt="WhatsApp">
                <span>WhatsApp</span>
            </a>
        </div>
        <div class="col-md-4">
            <a href="https://vk.com/service_04" target="_blank" rel="noopener" class="btn btn-outline-primary btn-lg w-100 btn-social">
                <img src="vk122.svg" width="24" height="24" alt="VK">
                <span>VKontakte</span>
            </a>
        </div>
    </div>

    <div class="row g-4">
        <div class="col-md-6">
            <div class="card h-100 text-center p-3" style="border: 1px solid #e37a25;">
                <div class="card-body">
                    <h5 class="card-title fw-bold" style="color: #e37a25;">Телефоны</h5>
                    <p class="card-text fs-5">
                        <strong>+7 (926) 221-13-48</strong>
                    </p>
                    <a href="tel:+79262211348" class="btn btn-primary w-100">Позвонить</a>
                </div>
            </div>
        </div>
        <div class="col-md-6">
            <div class="card h-100 text-center p-3" style="border: 1px solid #e37a25;">
                <div class="card-body">
                    <h5 class="card-title fw-bold" style="color: #e37a25;">Email</h5>
                    <p class="card-text fs-5">
                        <a href="mailto:89262211348@mail.ru" class="text-dark text-decoration-none">89262211348@mail.ru</a>
                    </p>
                    <a href="mailto:89262211348@mail.ru" class="btn btn-success w-100">Написать</a>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="card shadow-sm border-0 p-4 mb-5">
    <h2 class="h4 mb-4" style="color: #ffc107;">Важная информация</h2>
    
    <div class="alert alert-danger text-center" role="alert">
        <h4 class="alert-heading h5 fw-bold">ЗАРАНЕЕ ДОГОВАРИВАЙТЕСЬ О ВИЗИТЕ</h4>
        <p class="mb-0 fw-bold">ТРЕБУЕТСЯ ПРОПУСК</p>
    </div>

    <div class="row g-4">
        <div class="col-md-6">
            <div class="card h-100 p-3" style="border: 1px solid #e37a25;">
                <div class="card-body">
                    <h5 class="card-title fw-bold" style="color: #e37a25;">Режим работы</h5>
                    <ul class="list-unstyled mb-0">
                        <li class="mb-2"><strong>• Магазин работает с 10:00 до 17:00 без обеда</strong></li>
                        <li class="mb-2"><strong>• Продажа возможна в нерабочее время и в выходные</strong></li>
                        <li class="mb-2"><strong>• Склад можно открыть в выходные и после 17:00</strong></li>
                        <li><strong>• Стоимость услуги — 1000 руб.</strong></li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="col-md-6">
            <div class="card h-100 p-3" style="border: 1px solid #e37a25;">
                <div class="card-body">
                    <h5 class="card-title fw-bold" style="color: #e37a25;">О компании</h5>
                    <p class="card-text">Наш сервисный центр предлагает полный спектр услуг по ремонту газовых котлов и техническому обслуживанию котельного оборудования по стандартам производителя. Все сотрудники — сертифицированные специалисты.</p>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="card shadow-sm border-0 p-4 mb-5">
    <h3 class="h4 mb-4 text-info">Наши адреса</h3> 
    <div class="table-responsive">
        <table class="table table-bordered table-striped table-hover align-middle">
            <thead class="table-light">
                <tr>
                    <th scope="col" style="width: 120px;">Фото</th>
                    <th scope="col">Адрес</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="text-center">
                        <img src="2020-01-17_210058-min.png" alt="Офис" width="100" height="100" style="object-fit: cover;">
                    </td>
                    <td><strong>ОФИС г. Москва, Щелковское шоссе, д. 100</strong></td>
                </tr>
                <tr>
                    <td class="text-center">
                        <img src="2020-01-17_212607-min.png" alt="Склад" width="100" height="100" style="object-fit: cover;">
                    </td>
                    <td><strong>СКЛАД г. Москва, 16-я Парковая, д. 36, стр. А<br><span class="text-muted">(для навигатора: д. 36, стр. 4)</span></strong></td>
                </tr>
                <tr>
                    <td class="text-center">
                        <img src="flot.jpg" alt="Дополнительный склад" width="100" height="100" style="object-fit: cover;">
                    </td>
                    <td><strong>ДОПОЛНИТЕЛЬНЫЙ СКЛАД г. Москва, ул. Флотская, 7, корп. 3</strong></td>
                </tr>
            </tbody>
        </table>
    </div>
</div>

<div class="card shadow-sm border-0 p-4 mb-5">
    <h4 class="h4 mb-4 text-success">Реквизиты компании</h4>
    <div class="row g-4">
        <div class="col-md-6">
            <h5 class="fw-bold" style="color: #e37a25;">Индивидуальный предприниматель</h5>
            <p class="fw-bold mb-2">КОРОЛЕВ ВЯЧЕСЛАВ ВАЛЕРЬЕВИЧ (ИП)</p>
            <ul class="list-unstyled">
                <li><strong>ОГРИП:</strong> 313500130300024</li>
                <li><strong>Выдан:</strong> 30 октября 2013, серия 50 № 013913076</li>
                <li><strong>ИНН:</strong> 504306407027</li>
                <li><strong>ОКПО:</strong> 0187959347</li>
            </ul>
        </div>
        <div class="col-md-6">
            <h5 class="fw-bold" style="color: #e37a25;">Банковские реквизиты</h5>
            <ul class="list-unstyled">
                <li><strong>Банк:</strong> ОАО АКБ "АВАНГАРД"</li>
                <li><strong>Р/с:</strong> 40802810600120017070</li>
                <li><strong>К/с:</strong> 30101810000000000201</li>
                <li><strong>БИК:</strong> 044525201</li>
            </ul>
        </div>
    </div>
</div>

<div class="card shadow-sm border-0 p-4">
    <h5 class="h4 mb-3 text-secondary">Юридический адрес</h5>
    <div itemscope itemtype="http://schema.org/Organization">
        <span itemprop="name" class="fw-bold">ГазСервис</span><br>
        <div itemprop="address" itemscope itemtype="http://schema.org/PostalAddress" class="mb-1">
            Адрес: <span itemprop="addressLocality">Москва</span>, <span itemprop="streetAddress">16-я Парковая, д. 36А</span>
        </div>
        Телефон: <span itemprop="telephone"><a href="tel:+79262211348" class="text-decoration-none text-dark">+7 926 221–13–48</a></span>
    </div>
</div>
