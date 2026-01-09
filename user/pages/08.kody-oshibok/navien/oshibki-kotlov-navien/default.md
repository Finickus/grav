---
title: Ошибки котлов Navien
metadata:
  description: 'Ошибки котлов Navien Навьен и их устранение Руководство по устранению
    неисправностей Поиск по кодам ошибок Введите код ошибки (например: 02, 03, 16):...'
  og:type: article
  og:title: Ошибки котлов Navien - Service04
  og:description: 'Ошибки котлов Navien Навьен и их устранение Руководство по устранению
    неисправностей Поиск по кодам ошибок Введите код ошибки (например: 02, 03, 16):...'
  og:url: https://service04.ru/kody-oshibok/navien/oshibki-kotlov-navien
  og:site_name: Service04
  og:locale: ru_RU
  og:image: https://service04.ru/images/og-default.jpg
  og:image:width: '1200'
  og:image:height: '630'
  canonical: https://service04.ru/kody-oshibok/navien/oshibki-kotlov-navien
  robots: index, follow
  yandex-verification: ''
  geo.region: RU-MOW
  geo.placename: Москва
  author: Service04
---
<div class="container py-5">

    <div class="p-5 mb-5 text-white text-center rounded-3 shadow-sm" style="background-color: #009688;">
        <h1 class="display-5 fw-bold">
            <i class="fas fa-exclamation-triangle me-3"></i>Ошибки котлов Navien Навьен и их устранение
        </h1>
        <p class="lead">Руководство по устранению неисправностей</p>
    </div>

    <div class="card mb-5 shadow-sm border-info">
        <div class="card-header bg-info text-white py-3">
            <h4 class="h5 mb-0"><i class="fas fa-search me-2"></i>Поиск по кодам ошибок</h4>
        </div>
        <div class="card-body">
            <div class="mb-3">
                <label for="errorSearch" class="form-label h6"><i class="fas fa-keyboard me-1"></i> Введите код ошибки (например: 02, 03, 16):</label>
                <input type="text" class="form-control form-control-lg" id="errorSearch" placeholder="Введите код ошибки...">
            </div>
            <button class="btn btn-primary btn-lg w-100" onclick="searchError()"><i class="fas fa-search me-2"></i>Найти ошибку</button>
            <div id="searchResult" class="mt-4"></div>
        </div>
    </div>

    <div class="card mb-5 shadow-sm border-0">
        <div class="card-body p-4">
            <p class="fs-6">Котлы <strong>Navien (Навьен)</strong> оснащены системой самодиагностики, которая при возникновении неисправности отображает коды ошибок. Это позволяет быстро определить причину поломки и принять меры для её устранения.</p>
            <div class="alert alert-danger mt-4 shadow-sm d-flex align-items-start" role="alert">
                <i class="fas fa-exclamation-triangle fs-4 me-3 mt-1 text-white"></i>
                <div>
                    <h5 class="alert-heading fw-bold text-white">Предупреждение о безопасности</h5>
                    <p class="mb-0 text-white">Работы с газовым оборудованием требуют квалификации. При отсутствии опыта или если ошибка сохраняется после выполнения рекомендованных действий, <strong>вызывайте сервисного инженера</strong>.</p>
                </div>
            </div>
        </div>
    </div>

    <div class="accordion" id="errorsAccordion">
        
        <div class="accordion-item">
            <h2 class="accordion-header" id="heading02">
                <button class="accordion-button fw-bold text-danger" type="button" data-bs-toggle="collapse" data-bs-target="#collapse02" aria-expanded="true">
                    <i class="fas fa-tint me-2"></i> Ошибка 02: Малый объём воды в отопительной системе или разрыв цепи датчика протока
                </button>
            </h2>
            <div id="collapse02" class="accordion-collapse collapse show" aria-labelledby="heading02" data-bs-parent="#errorsAccordion">
                <div class="accordion-body bg-danger-subtle">
                    <p class="fw-bold small">Описание: Малый объём воды в отопительной системе или разрыв цепи датчика протока (модели Navien Ace)</p>
                    <h6 class="fw-bold mt-4 text-success"><i class="fas fa-wrench me-2"></i>Решение:</h6>
                    <ul class="list-unstyled ms-3 small">
                        <li class="mb-2"><i class="fas fa-tachometer-alt me-2 text-primary"></i> Заполните систему отопления водой до рабочего давления <strong>1,22–1,51 бар</strong>. </li>
                        <li class="mb-2"><i class="fas fa-wind me-2 text-warning"></i> Удалите воздух из системы отопления.</li>
                        <li class="mb-2"><i class="fas fa-power-off me-2 text-success"></i> Включите котел в проверочном режиме на 1–2 часа.</li>
                        <li class="mb-2"><i class="fas fa-door-open me-2 text-secondary"></i> Откройте запорные и распределительные краны.</li>
                        <li class="mb-2"><i class="fas fa-cogs me-2 text-danger"></i> Проверьте исправность циркуляционного насоса и замените его. </li>
                        <li class="mb-2"><i class="fas fa-plug me-2 text-primary"></i> Проверьте питание насоса и устраните проблемы с электропитанием.</li>
                        <li class="mb-2"><i class="fas fa-filter me-2 text-warning"></i> Очистите фильтр.</li>
                        <li><i class="fas fa-snowflake me-2 text-info"></i> Исключите использование антифриза.</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="heading03">
                <button class="accordion-button collapsed fw-bold text-warning" type="button" data-bs-toggle="collapse" data-bs-target="#collapse03">
                    <i class="fas fa-fire me-2"></i> Ошибка 03: Отсутствие сигнала о наличии пламени или разрыв цепи датчика пламени
                </button>
            </h2>
            <div id="collapse03" class="accordion-collapse collapse" aria-labelledby="heading03" data-bs-parent="#errorsAccordion">
                <div class="accordion-body bg-warning-subtle">
                    <p class="fw-bold small">Описание: Отсутствие сигнала о наличии пламени или разрыв цепи датчика пламени</p>
                    <h6 class="fw-bold mt-4 text-success"><i class="fas fa-wrench me-2"></i>Решение:</h6>
                    <ul class="list-unstyled ms-3 small">
                        <li class="mb-2"><i class="fas fa-gas-pump me-2 text-danger"></i> Проверьте входящее давление газа (NG: 10–25 мбар, LPG: 28–37 мбар).</li>
                        <li class="mb-2"><i class="fas fa-sliders-h me-2 text-info"></i> Настройте максимальные и минимальные значения давления газа на форсунках. </li>
                        <li class="mb-2"><i class="fas fa-eye me-2 text-primary"></i> Осмотрите расположение ионизационного электрода.</li>
                        <li><i class="fas fa-ban me-2 text-warning"></i> Проверяйте подачу газа и работоспособность газового клапана.</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="heading04">
                <button class="accordion-button collapsed fw-bold text-info" type="button" data-bs-toggle="collapse" data-bs-target="#collapse04">
                    <i class="fas fa-fire-alt me-2"></i> Ошибка 04: Ложный сигнал о наличии пламени или короткое замыкание цепи датчика пламени
                </button>
            </h2>
            <div id="collapse04" class="accordion-collapse collapse" aria-labelledby="heading04" data-bs-parent="#errorsAccordion">
                <div class="accordion-body bg-info-subtle">
                    <p class="fw-bold small">Описание: Ложный сигнал о наличии пламени или короткое замыкание цепи датчика пламени</p>
                    <h6 class="fw-bold mt-4 text-success"><i class="fas fa-wrench me-2"></i>Решение:</h6>
                    <ul class="list-unstyled ms-3 small">
                        <li class="mb-2"><i class="fas fa-ban me-2 text-danger"></i> Устраните короткое замыкание («Ионизационный электрод — Блок управления»).</li>
                        <li class="mb-2"><i class="fas fa-bolt me-2 text-warning"></i> Убедитесь, что ионизационный электрод не контактирует с корпусом котла.</li>
                        <li><i class="fas fa-sync me-2 text-success"></i> Перезагрузите котел, при повторении ошибки замените плату управления.</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="heading05">
                <button class="accordion-button collapsed fw-bold text-success" type="button" data-bs-toggle="collapse" data-bs-target="#collapse05">
                    <i class="fas fa-thermometer-empty me-2"></i> Ошибка 05: Обрыв цепи датчика температуры отопительной воды
                </button>
            </h2>
            <div id="collapse05" class="accordion-collapse collapse" aria-labelledby="heading05" data-bs-parent="#errorsAccordion">
                <div class="accordion-body bg-success-subtle">
                    <p class="fw-bold small">Описание: Обрыв цепи датчика температуры отопительной воды</p>
                    <h6 class="fw-bold mt-4 text-success"><i class="fas fa-wrench me-2"></i>Решение:</h6>
                    <ul class="list-unstyled ms-3 small">
                        <li class="mb-2"><i class="fas fa-search me-2 text-primary"></i> Проверьте и замените датчик температуры отопительной воды.</li>
                        <li><i class="fas fa-plug me-2 text-warning"></i> Удостоверьтесь в надежности соединений контактов датчика.</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="heading06">
                <button class="accordion-button collapsed fw-bold text-secondary" type="button" data-bs-toggle="collapse" data-bs-target="#collapse06">
                    <i class="fas fa-thermometer-full me-2"></i> Ошибка 06: Короткое замыкание цепи датчика температуры отопительной воды
                </button>
            </h2>
            <div id="collapse06" class="accordion-collapse collapse" aria-labelledby="heading06" data-bs-parent="#errorsAccordion">
                <div class="accordion-body bg-secondary-subtle">
                    <p class="fw-bold small">Описание: Короткое замыкание цепи датчика температуры отопительной воды</p>
                    <h6 class="fw-bold mt-4 text-success"><i class="fas fa-wrench me-2"></i>Решение:</h6>
                    <ul class="list-unstyled ms-3 small">
                        <li class="mb-2"><i class="fas fa-sync me-2 text-danger"></i> Замените поврежденный датчик температуры.</li>
                        <li><i class="fas fa-search me-2 text-warning"></i> Найдите и устраните короткое замыкание в цепи датчика.</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="heading07">
                <button class="accordion-button collapsed fw-bold text-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapse07">
                    <i class="fas fa-shower me-2"></i> Ошибка 07: Обрыв цепи датчика температуры горячей хозяйственной воды
                </button>
            </h2>
            <div id="collapse07" class="accordion-collapse collapse" aria-labelledby="heading07" data-bs-parent="#errorsAccordion">
                <div class="accordion-body bg-primary-subtle">
                    <p class="fw-bold small">Описание: Обрыв цепи датчика температуры горячей хозяйственной воды</p>
                    <h6 class="fw-bold mt-4 text-success"><i class="fas fa-wrench me-2"></i>Решение:</h6>
                    <ul class="list-unstyled ms-3 small">
                        <li class="mb-2"><i class="fas fa-search me-2 text-primary"></i> Проверьте и замените датчик температуры горячей воды.</li>
                        <li><i class="fas fa-plug me-2 text-warning"></i> Протестируйте контакты датчика и блока управления.</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="heading08">
                <button class="accordion-button collapsed fw-bold text-dark" type="button" data-bs-toggle="collapse" data-bs-target="#collapse08">
                    <i class="fas fa-bath me-2"></i> Ошибка 08: Короткое замыкание цепи датчика температуры горячей хозяйственной воды
                </button>
            </h2>
            <div id="collapse08" class="accordion-collapse collapse" aria-labelledby="heading08" data-bs-parent="#errorsAccordion">
                <div class="accordion-body bg-dark-subtle">
                    <p class="fw-bold small">Описание: Короткое замыкание цепи датчика температуры горячей хозяйственной воды</p>
                    <h6 class="fw-bold mt-4 text-success"><i class="fas fa-wrench me-2"></i>Решение:</h6>
                    <ul class="list-unstyled ms-3 small">
                        <li class="mb-2"><i class="fas fa-sync me-2 text-danger"></i> Замените неисправный датчик температуры.</li>
                        <li><i class="fas fa-search me-2 text-warning"></i> Устраните короткое замыкание в цепи датчика.</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="heading09">
                <button class="accordion-button collapsed fw-bold text-danger" type="button" data-bs-toggle="collapse" data-bs-target="#collapse09">
                    <i class="fas fa-fan me-2"></i> Ошибка 09: Сбой в работе вентилятора (только в моделях Navien Ace и Ace Coaxial)
                </button>
            </h2>
            <div id="collapse09" class="accordion-collapse collapse" aria-labelledby="heading09" data-bs-parent="#errorsAccordion">
                <div class="accordion-body bg-danger-subtle">
                    <p class="fw-bold small">Описание: Сбой в работе вентилятора</p>
                    <h6 class="fw-bold mt-4 text-success"><i class="fas fa-wrench me-2"></i>Решение:</h6>
                    <ul class="list-unstyled ms-3 small">
                        <li class="mb-2"><i class="fas fa-cogs me-2 text-primary"></i> Проверьте обмотку двигателя вентилятора на предмет повреждений.</li>
                        <li class="mb-2"><i class="fas fa-plug me-2 text-warning"></i> Проверьте подключение и функционирование вентилятора.</li>
                        <li><i class="fas fa-sync me-2 text-danger"></i> Замените вентилятор при выявлении дефектов.</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="heading10">
                <button class="accordion-button collapsed fw-bold text-warning" type="button" data-bs-toggle="collapse" data-bs-target="#collapse10">
                    <i class="fas fa-wind me-2"></i> Ошибка 10: Сбой в работе системы дымоудаления
                </button>
            </h2>
            <div id="collapse10" class="accordion-collapse collapse" aria-labelledby="heading10" data-bs-parent="#errorsAccordion">
                <div class="accordion-body bg-warning-subtle">
                    <p class="fw-bold small">Описание: Сбой в работе системы дымоудаления</p>
                    <h6 class="fw-bold mt-4 text-success"><i class="fas fa-wrench me-2"></i>Решение:</h6>
                    <ul class="list-unstyled ms-3 small">
                        <li class="mb-2"><i class="fas fa-broom me-2 text-primary"></i> Проверьте систему дымоудаления на предмет засорений.</li>
                        <li class="mb-2"><i class="fas fa-ruler-horizontal me-2 text-warning"></i> Оцените длину системы дымоудаления и ее соответствие рекомендациям.</li>
                        <li><i class="fas fa-info-circle me-2 text-info"></i> Проанализируйте влияние сильных ветров.</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="heading13">
                <button class="accordion-button collapsed fw-bold text-info" type="button" data-bs-toggle="collapse" data-bs-target="#collapse13">
                    <i class="fas fa-tint me-2"></i> Ошибка 13: Короткое замыкание цепи датчика протока отопительной воды
                </button>
            </h2>
            <div id="collapse13" class="accordion-collapse collapse" aria-labelledby="heading13" data-bs-parent="#errorsAccordion">
                <div class="accordion-body bg-info-subtle">
                    <p class="fw-bold small">Описание: Короткое замыкание цепи датчика протока отопительной воды (только модели Ace)</p>
                    <h6 class="fw-bold mt-4 text-success"><i class="fas fa-wrench me-2"></i>Решение:</h6>
                    <ul class="list-unstyled ms-3 small">
                        <li class="mb-2"><i class="fas fa-search me-2 text-primary"></i> Выполните прозвонку цепи датчика протока.</li>
                        <li><i class="fas fa-broom me-2 text-warning"></i> Очистите механизм датчика протока или слегка постучите по нему.</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="heading15">
                <button class="accordion-button collapsed fw-bold text-success" type="button" data-bs-toggle="collapse" data-bs-target="#collapse15">
                    <i class="fas fa-microchip me-2"></i> Ошибка 15: Сбой в работе или неисправность платы управления
                </button>
            </h2>
            <div id="collapse15" class="accordion-collapse collapse" aria-labelledby="heading15" data-bs-parent="#errorsAccordion">
                <div class="accordion-body bg-success-subtle">
                    <p class="fw-bold small">Описание: Сбой в работе или неисправность платы управления</p>
                    <h6 class="fw-bold mt-4 text-success"><i class="fas fa-wrench me-2"></i>Решение:</h6>
                    <ul class="list-unstyled ms-3 small">
                        <li class="mb-2"><i class="fas fa-plug me-2 text-primary"></i> Проверьте подключения всех элементов к плате управления.</li>
                        <li class="mb-2"><i class="fas fa-sliders-h me-2 text-warning"></i> Убедитесь в правильной установке DIP-переключателей. </li>
                        <li><i class="fas fa-sync me-2 text-success"></i> Перезагрузите котел, при повторении ошибки замените плату управления.</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="heading16">
                <button class="accordion-button collapsed fw-bold text-secondary" type="button" data-bs-toggle="collapse" data-bs-target="#collapse16">
                    <i class="fas fa-thermometer-high me-2"></i> Ошибка 16: Перегрев котла
                </button>
            </h2>
            <div id="collapse16" class="accordion-collapse collapse" aria-labelledby="heading16" data-bs-parent="#errorsAccordion">
                <div class="accordion-body bg-secondary-subtle">
                    <p class="fw-bold small">Описание: Перегрев котла</p>
                    <h6 class="fw-bold mt-4 text-success"><i class="fas fa-wrench me-2"></i>Решение:</h6>
                    <ul class="list-unstyled ms-3 small">
                        <li class="mb-2"><i class="fas fa-snowflake me-2 text-primary"></i> Дождитесь охлаждения котла и перезапустите его.</li>
                        <li class="mb-2"><i class="fas fa-thermometer-half me-2 text-warning"></i> Испытайте датчик по перегреву и произведите его замену.</li>
                        <li><i class="fas fa-valve me-2 text-danger"></i> Проверьте трехходовой кран на предмет блокировки.</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="heading18">
                <button class="accordion-button collapsed fw-bold text-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapse18">
                    <i class="fas fa-thermometer-full me-2"></i> Ошибка 18: Перегрев датчика дымоудаления (Navien Ace атмосферный)
                </button>
            </h2>
            <div id="collapse18" class="accordion-collapse collapse" aria-labelledby="heading18" data-bs-parent="#errorsAccordion">
                <div class="accordion-body bg-primary-subtle">
                    <p class="fw-bold small">Описание: Перегрев датчика дымоудаления</p>
                    <h6 class="fw-bold mt-4 text-success"><i class="fas fa-wrench me-2"></i>Решение:</h6>
                    <ul class="list-unstyled ms-3 small">
                        <li class="mb-2"><i class="fas fa-snowflake me-2 text-primary"></i> После остывания датчика перезапустите котел.</li>
                        <li><i class="fas fa-broom me-2 text-warning"></i> Определите причину повышенного пневмосопротивления в системе дымоудаления и примите меры по чистке.</li>
                    </ul>
                </div>
            </div>
        </div>

    </div>

    <div class="p-5 rounded-3 text-center text-white shadow-sm mt-5" style="background-color: #009688;">
        <h3 class="h4 mb-3"><i class="fas fa-phone me-2"></i>Нужна помощь специалиста?</h3>
        <p class="lead mb-4">Свяжитесь с нами для профессиональной диагностики и ремонта:</p>
        <div class="row justify-content-center g-3">
            <div class="col-12 col-md-4">
                <a href="tel:+79262211348" class="btn btn-light btn-lg w-100 fw-bold">
                    <i class="fas fa-phone me-2"></i> <span>+7(926) 221-13-48</span>
                </a>
            </div>
            <div class="col-12 col-md-4">
                <a href="https://service04.ru/contact-us/feedback" class="btn btn-warning btn-lg w-100 fw-bold text-dark">
                    <i class="fas fa-envelope me-2"></i> <span>Написать нам</span>
                </a>
            </div>
        </div>
    </div>

</div>
<p>
<script>
// База данных ошибок (скопирована из исходного кода)
const errorDatabase = {
    "02": {
        "category": "Ошибка 02: Малый объём воды в отопительной системе или разрыв цепи датчика протока (Navien Ace)",
        "description": "Малый объём воды в отопительной системе или разрыв цепи датчика протока (модели Navien Ace)",
        "solution": [
            "Заполните систему отопления водой до рабочего давления 1,22–1,51 бар, проверив давление на манометре.",
            "Удалите воздух из системы отопления.",
            "Включите котел в проверочном режиме на 1–2 часа, переведя первый переключатель DIP-Switch в положение «Включено».",
            "Откройте запорные и распределительные краны, препятствующие нормальной циркуляции воды.",
            "Проверьте исправность циркуляционного насоса и замените его при необходимости.",
            "Убедитесь, что питание подается на насос и устраните любые проблемы с электропитанием.",
            "Оцените состояние фильтра и очистите его.",
            "Исключите использование антифриза в качестве теплоносителя."
        ]
    },
    "03": {
        "category": "Ошибка 03: Отсутствие сигнала о наличии пламени или разрыв цепи датчика пламени",
        "description": "Отсутствие сигнала о наличии пламени или разрыв цепи датчика пламени",
        "solution": [
            "Проверьте входящее давление газа перед газовой арматурой (NG: 10–25 мбар, LPG: 28–37 мбар).",
            "Настройте максимальные и минимальные значения давления газа на форсунках.",
            "Осмотрите расположение ионизационного электрода относительно зоны пламени.",
            "Проверяйте подачу газа и работоспособность газового клапана.",
            "Замерьте сопротивления катушек газовых клапанов (5,5 кОм и 78 Ом соответственно).",
            "Проверьте работоспособность трансформатора розжига и наличие короткого замыкания.",
            "При необходимости замените электроды розжига и ионизации.",
            "Сделайте проверку работы платы управления и вентилятора."
        ]
    },
    "04": {
        "category": "Ошибка 04: Ложный сигнал о наличии пламени или короткое замыкание цепи датчика пламени",
        "description": "Ложный сигнал о наличии пламени или короткое замыкание цепи датчика пламени",
        "solution": [
            "Устраните короткое замыкание («Ионизационный электрод — Блок управления»).",
            "Убедитесь, что ионизационный электрод не контактирует с корпусом котла.",
            "Перезагрузите котел, при повторении ошибки замените плату управления."
        ]
    },
    "05": {
        "category": "Ошибка 05: Обрыв цепи датчика температуры отопительной воды",
        "description": "Обрыв цепи датчика температуры отопительной воды",
        "solution": [
            "Проверьте и замените датчик температуры отопительной воды.",
            "Удостоверьтесь в надежности соединений контактов датчика с блоком управления."
        ]
    },
    "06": {
        "category": "Ошибка 06: Короткое замыкание цепи датчика температуры отопительной воды",
        "description": "Короткое замыкание цепи датчика температуры отопительной воды",
        "solution": [
            "Замените поврежденный датчик температуры.",
            "Найдите и устраните короткое замыкание в цепи датчика."
        ]
    },
    "07": {
        "category": "Ошибка 07: Обрыв цепи датчика температуры горячей хозяйственной воды",
        "description": "Обрыв цепи датчика температуры горячей хозяйственной воды",
        "solution": [
            "Проверьте и замените датчик температуры горячей воды.",
            "Протестируйте контакты датчика и блока управления."
        ]
    },
    "08": {
        "category": "Ошибка 08: Короткое замыкание цепи датчика температуры горячей хозяйственной воды",
        "description": "Короткое замыкание цепи датчика температуры горячей хозяйственной воды",
        "solution": [
            "Замените неисправный датчик температуры.",
            "Устраните короткое замыкание в цепи датчика."
        ]
    },
    "09": {
        "category": "Ошибка 09: Сбой в работе вентилятора (только в моделях Navien Ace и Ace Coaxial)",
        "description": "Сбой в работе вентилятора (только в моделях Navien Ace и Ace Coaxial)",
        "solution": [
            "Проверьте обмотку двигателя вентилятора на предмет повреждений.",
            "Проверьте подключение и функционирование вентилятора.",
            "Замените вентилятор при выявлении дефектов.",
            "Обратитесь к специалистам, если проблема сохраняется после замены компонентов."
        ]
    },
    "10": {
        "category": "Ошибка 10: Сбой в работе системы дымоудаления (только в моделях Navien Ace и Ace Coaxial)",
        "description": "Сбой в работе системы дымоудаления (только в моделях Navien Ace и Ace Coaxial)",
        "solution": [
            "Проверьте систему дымоудаления на предмет засорений и загрязнений.",
            "Оцените длину системы дымоудаления и убедитесь, что она соответствует рекомендациям производителя.",
            "Проанализируйте влияние сильных ветров на эффективность удаления дыма."
        ]
    },
    "13": {
        "category": "Ошибка 13: Короткое замыкание цепи датчика протока отопительной воды (только модели Ace)",
        "description": "Короткое замыкание цепи датчика протока отопительной воды (только модели Ace)",
        "solution": [
            "Выполните прозвонку цепи датчика протока.",
            "Очистите механизм датчика протока или слегка постучите по нему для восстановления работоспособности."
        ]
    },
    "15": {
        "category": "Ошибка 15: Сбой в работе или неисправность платы управления",
        "description": "Сбой в работе или неисправность платы управления",
        "solution": [
            "Проверьте подключения всех элементов к плате управления.",
            "Убедитесь в правильной установке DIP-переключателей.",
            "Перезагрузите котел, при повторении ошибки замените плату управления."
        ]
    },
    "16": {
        "category": "Ошибка 16: Перегрев котла",
        "description": "Перегрев котла",
        "solution": [
            "Дождитесь охлаждения котла и перезапустите его.",
            "Испытайте датчик по перегреву и произведите его замену при необходимости.",
            "Проверьте трехходовой кран на предмет блокировки при подаче горячего водоснабжения."
        ]
    },
    "18": {
        "category": "Ошибка 18: Перегрев датчика дымоудаления (Navien Ace атмосферный)",
        "description": "Перегрев датчика дымоудаления (Navien Ace атмосферный)",
        "solution": [
            "После остывания датчика перезапустите котел.",
            "Определите причину повышенного пневмосопротивления в системе дымоудаления и примите меры по чистке."
        ]
    }
};

function searchError() {
    const searchTerm = document.getElementById('errorSearch').value.trim().toUpperCase();
    const resultDiv = document.getElementById('searchResult');
    
    if (!searchTerm) {
        resultDiv.innerHTML = '<div class="alert alert-warning"><i class="fas fa-exclamation-triangle me-2"></i>Пожалуйста, введите код ошибки для поиска.</div>';
        return;
    }
    
    const errorCode = searchTerm.replace('ERROR ', '').replace('ОШИБКА ', '').replace('E', '');
    const errorInfo = errorDatabase[errorCode];
    
    if (errorInfo) {
        let solutionList = '';
        errorInfo.solution.forEach(step => {
            solutionList += `<li class="mb-2 small"><img src="/home/check-circle.svg" alt="" class="me-2" style="width: 20px; height: 20px; vertical-align: middle;">${step.trim()}</li>`;
        });
        
        resultDiv.innerHTML = `
            <div class="card border-primary">
                <header class="card-header bg-primary text-white">
                    <p class="card-header-title h5 mb-0"><i class="fas fa-search me-2"></i>Результаты поиска для ошибки <strong>${errorCode}</strong></p>
                </header>
                <div class="card-body">
                    <h6 class="h6 mb-3 text-secondary"><i class="fas fa-tag me-1"></i> ${errorInfo.category}</h6>
                    <div class="content">
                        <h6 class="h6 fw-bold"><i class="fas fa-file-alt me-1"></i> Описание:</h6>
                        <p>${errorInfo.description}</p>
                        <h6 class="h6 fw-bold"><i class="fas fa-wrench me-1"></i> Решение:</h6>
                        <ul class="list-unstyled ms-3">
                            ${solutionList}
                        </ul>
                        <div class="alert alert-info mt-4 p-2 small">
                            <h6 class="h6 fw-bold"><i class="fas fa-info-circle me-2"></i>Информация:</h6>
                            <p class="mb-0 small">Эта информация предоставлена для ознакомления. Для сложных неисправностей рекомендуется обратиться к квалифицированному специалисту.</p>
                        </div>
                    </div>
                </div>
            </div>
        `;
        // Прокрутить к результатам поиска
        document.getElementById('searchResult').scrollIntoView({ behavior: 'smooth' });
    } else {
        resultDiv.innerHTML = `
            <div class="alert alert-danger">
                <h5 class="h6 fw-bold text-danger"><i class="fas fa-exclamation-circle me-2"></i>Ошибка не найдена</h5>
                <p class="mb-0 small">Информация по коду ошибки <strong>${errorCode}</strong> в нашей базе отсутствует. Пожалуйста, сверьтесь с инструкцией к вашему котлу или обратитесь к специалисту.</p>
            </div>
        `;
    }
}

document.getElementById('errorSearch').addEventListener('keyup', function(event) {
    if (event.key === "Enter") {
        searchError();
    }
});
</script>
</p>