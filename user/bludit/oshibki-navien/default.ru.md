---
title: 'Ошибки котлов Navien Навьен и их устранение'
---

<div class="container-fluid mt-5 mb-5">
<section class="bg-primary text-white fw-bold mb-5">
<div class="py-5">
<div class="container text-center">

<p class="h4 lead text-white">Руководство по устранению неисправностей</p>
</div>
</div>
</section>
<div class="card mb-5 shadow"><header class="card-header bg-info text-white">
<p class="card-h3 text-white fs-5"><span class="icon me-2"><i class="fas fa-search"></i></span>Поиск по кодам ошибок</p>
</header>
<div class="card-body">
<div class="field"><label for="errorSearch" class="label"><span class="icon mr-1"><i class="fas fa-keyboard"></i></span> Введите код ошибки (например: 02, 03, 16):</label>
<div class="control"><input type="text" class="input btn-lg" id="errorSearch" placeholder="Введите код ошибки..."></div>
</div>
<btn btn-primary class="btn btn-primary btn-lg w-100" onclick="searchError()"><span class="icon me-2"><i class="fas fa-search"></i></span>Найти ошибку</btn btn-primary>
<div id="searchResult" class="mt-4"></div>
</div>
</div>
<div class="card mb-5">
<div class="card-body">
<p class="fs-5">Котлы **Navien (Навьен)** оснащены системой самодиагностики, которая при возникновении неисправности отображает коды ошибок. Это позволяет быстро определить причину поломки и принять меры для её устранения.</p>
<div class="notification is-danger mt-4">
<h5 class="h6 text-white"><span class="icon me-2"><i class="fas fa-exclamation-triangle"></i></span>Предупреждение о безопасности</h5>
<p class="mb-0">Работы с газовым оборудованием требуют квалификации. При отсутствии опыта или если ошибка сохраняется после выполнения рекомендованных действий, **вызывайте сервисного инженера**.</p>
</div>
</div>
</div>
<div id="errorsAccordion" class="content"><details open="" class="card mb-3 p-0 bg-danger-light">
<p class="card-h3 text-white fs-5"><span class="icon me-2"><i class="fas fa-tint"></i></span> Ошибка 02: Малый объём воды в отопительной системе или разрыв цепи датчика протока</p>
<div class="card-body">
<p class="has-text-weight-bold">Описание: Малый объём воды в отопительной системе или разрыв цепи датчика протока (модели Navien Ace)</p>
<h6 class="h6 mt-4 text-success"><span class="icon me-2"><i class="fas fa-wrench"></i></span>Решение:</h6>
<ul class="ml-4 list-unstyled fs-6">
<li class="mb-2"><span class="icon me-2 text-primary"><i class="fas fa-tachometer-alt"></i></span> Заполните систему отопления водой до рабочего давления **1,22–1,51 бар**.</li>
<li class="mb-2"><span class="icon me-2 text-warning"><i class="fas fa-wind"></i></span> Удалите воздух из системы отопления.</li>
<li class="mb-2"><span class="icon me-2 text-success"><i class="fas fa-power-off"></i></span> Включите котел в проверочном режиме на 1–2 часа.</li>
<li class="mb-2"><span class="icon me-2 has-text-secondary"><i class="fas fa-door-open"></i></span> Откройте запорные и распределительные краны.</li>
<li class="mb-2"><span class="icon me-2 text-danger"><i class="fas fa-cogs"></i></span> Проверьте исправность циркуляционного насоса и замените его.</li>
<li class="mb-2"><span class="icon me-2 text-primary"><i class="fas fa-plug"></i></span> Проверьте питание насоса и устраните проблемы с электропитанием.</li>
<li class="mb-2"><span class="icon me-2 text-warning"><i class="fas fa-filter"></i></span> Очистите фильтр.</li>
<li class="mb-2"><span class="icon me-2 text-info"><i class="fas fa-snowflake"></i></span> Исключите использование антифриза.</li>
</ul>
</div>
</details><details class="card mb-3 p-0 bg-warning-light">
<p class="card-h3 text-dark fs-5"><span class="icon me-2"><i class="fas fa-fire"></i></span> Ошибка 03: Отсутствие сигнала о наличии пламени или разрыв цепи датчика пламени</p>
<div class="card-body">
<p class="has-text-weight-bold">Описание: Отсутствие сигнала о наличии пламени или разрыв цепи датчика пламени</p>
<h6 class="h6 mt-4 text-success"><span class="icon me-2"><i class="fas fa-wrench"></i></span>Решение:</h6>
<ul class="ml-4 list-unstyled fs-6">
<li class="mb-2"><span class="icon me-2 text-danger"><i class="fas fa-gas-pump"></i></span> Проверьте входящее давление газа (NG: 10–25 мбар, LPG: 28–37 мбар).</li>
<li class="mb-2"><span class="icon me-2 text-info"><i class="fas fa-sliders-h"></i></span> Настройте максимальные и минимальные значения давления газа на форсунках.</li>
<li class="mb-2"><span class="icon me-2 text-primary"><i class="fas fa-eye"></i></span> Осмотрите расположение ионизационного электрода.</li>
<li class="mb-2"><span class="icon me-2 text-warning"><i class="fas fa-ban"></i></span> Проверяйте подачу газа и работоспособность газового клапана.</li>
</ul>
</div>
</details><details class="card mb-3 p-0 bg-info-light">
<p class="card-h3 text-white fs-5"><span class="icon me-2"><i class="fas fa-fire-alt"></i></span> Ошибка 04: Ложный сигнал о наличии пламени или короткое замыкание цепи датчика пламени</p>
<div class="card-body">
<p class="has-text-weight-bold">Описание: Ложный сигнал о наличии пламени или короткое замыкание цепи датчика пламени</p>
<h6 class="h6 mt-4 text-success"><span class="icon me-2"><i class="fas fa-wrench"></i></span>Решение:</h6>
<ul class="ml-4 list-unstyled fs-6">
<li class="mb-2"><span class="icon me-2 text-danger"><i class="fas fa-ban"></i></span> Устраните короткое замыкание («Ионизационный электрод — Блок управления»).</li>
<li class="mb-2"><span class="icon me-2 text-warning"><i class="fas fa-bolt"></i></span> Убедитесь, что ионизационный электрод не контактирует с корпусом котла.</li>
<li class="mb-2"><span class="icon me-2 text-success"><i class="fas fa-sync"></i></span> Перезагрузите котел, при повторении ошибки замените плату управления.</li>
</ul>
</div>
</details><details class="card mb-3 p-0 bg-success-light">
<p class="card-h3 text-white fs-5"><span class="icon me-2"><i class="fas fa-thermometer-empty"></i></span> Ошибка 05: Обрыв цепи датчика температуры отопительной воды</p>
<div class="card-body">
<p class="has-text-weight-bold">Описание: Обрыв цепи датчика температуры отопительной воды</p>
<h6 class="h6 mt-4 text-success"><span class="icon me-2"><i class="fas fa-wrench"></i></span>Решение:</h6>
<ul class="ml-4 list-unstyled fs-6">
<li class="mb-2"><span class="icon me-2 text-primary"><i class="fas fa-search"></i></span> Проверьте и замените датчик температуры отопительной воды.</li>
<li class="mb-2"><span class="icon me-2 text-warning"><i class="fas fa-plug"></i></span> Удостоверьтесь в надежности соединений контактов датчика.</li>
</ul>
</div>
</details><details class="card mb-3 p-0 bg-secondary-light">
<p class="card-h3 text-white fs-5"><span class="icon me-2"><i class="fas fa-thermometer-full"></i></span> Ошибка 06: Короткое замыкание цепи датчика температуры отопительной воды</p>
<div class="card-body">
<p class="has-text-weight-bold">Описание: Короткое замыкание цепи датчика температуры отопительной воды</p>
<h6 class="h6 mt-4 text-success"><span class="icon me-2"><i class="fas fa-wrench"></i></span>Решение:</h6>
<ul class="ml-4 list-unstyled fs-6">
<li class="mb-2"><span class="icon me-2 text-danger"><i class="fas fa-sync"></i></span> Замените поврежденный датчик температуры.</li>
<li class="mb-2"><span class="icon me-2 text-warning"><i class="fas fa-search"></i></span> Найдите и устраните короткое замыкание в цепи датчика.</li>
</ul>
</div>
</details><details class="card mb-3 p-0 bg-primary-light">
<p class="card-h3 text-white fs-5"><span class="icon me-2"><i class="fas fa-shower"></i></span> Ошибка 07: Обрыв цепи датчика температуры горячей хозяйственной воды</p>
<div class="card-body">
<p class="has-text-weight-bold">Описание: Обрыв цепи датчика температуры горячей хозяйственной воды</p>
<h6 class="h6 mt-4 text-success"><span class="icon me-2"><i class="fas fa-wrench"></i></span>Решение:</h6>
<ul class="ml-4 list-unstyled fs-6">
<li class="mb-2"><span class="icon me-2 text-primary"><i class="fas fa-search"></i></span> Проверьте и замените датчик температуры горячей воды.</li>
<li class="mb-2"><span class="icon me-2 text-warning"><i class="fas fa-plug"></i></span> Протестируйте контакты датчика и блока управления.</li>
</ul>
</div>
</details><details class="card mb-3 p-0 bg-dark-light">
<p class="card-h3 text-white fs-5"><span class="icon me-2"><i class="fas fa-bath"></i></span> Ошибка 08: Короткое замыкание цепи датчика температуры горячей хозяйственной воды</p>
<div class="card-body">
<p class="has-text-weight-bold">Описание: Короткое замыкание цепи датчика температуры горячей хозяйственной воды</p>
<h6 class="h6 mt-4 text-success"><span class="icon me-2"><i class="fas fa-wrench"></i></span>Решение:</h6>
<ul class="ml-4 list-unstyled fs-6">
<li class="mb-2"><span class="icon me-2 text-danger"><i class="fas fa-sync"></i></span> Замените неисправный датчик температуры.</li>
<li class="mb-2"><span class="icon me-2 text-warning"><i class="fas fa-search"></i></span> Устраните короткое замыкание в цепи датчика.</li>
</ul>
</div>
</details><details class="card mb-3 p-0 bg-danger-light">
<p class="card-h3 text-white fs-5"><span class="icon me-2"><i class="fas fa-fan"></i></span> Ошибка 09: Сбой в работе вентилятора (только в моделях Navien Ace и Ace Coaxial)</p>
<div class="card-body">
<p class="has-text-weight-bold">Описание: Сбой в работе вентилятора</p>
<h6 class="h6 mt-4 text-success"><span class="icon me-2"><i class="fas fa-wrench"></i></span>Решение:</h6>
<ul class="ml-4 list-unstyled fs-6">
<li class="mb-2"><span class="icon me-2 text-primary"><i class="fas fa-cogs"></i></span> Проверьте обмотку двигателя вентилятора на предмет повреждений.</li>
<li class="mb-2"><span class="icon me-2 text-warning"><i class="fas fa-plug"></i></span> Проверьте подключение и функционирование вентилятора.</li>
<li class="mb-2"><span class="icon me-2 text-danger"><i class="fas fa-sync"></i></span> Замените вентилятор при выявлении дефектов.</li>
</ul>
</div>
</details><details class="card mb-3 p-0 bg-warning-light">
<p class="card-h3 text-dark fs-5"><span class="icon me-2"><i class="fas fa-wind"></i></span> Ошибка 10: Сбой в работе системы дымоудаления</p>
<div class="card-body">
<p class="has-text-weight-bold">Описание: Сбой в работе системы дымоудаления</p>
<h6 class="h6 mt-4 text-success"><span class="icon me-2"><i class="fas fa-wrench"></i></span>Решение:</h6>
<ul class="ml-4 list-unstyled fs-6">
<li class="mb-2"><span class="icon me-2 text-primary"><i class="fas fa-broom"></i></span> Проверьте систему дымоудаления на предмет засорений.</li>
<li class="mb-2"><span class="icon me-2 text-warning"><i class="fas fa-ruler-horizontal"></i></span> Оцените длину системы дымоудаления и ее соответствие рекомендациям.</li>
<li class="mb-2"><span class="icon me-2 text-info"><i class="fas fa-wind"></i></span> Проанализируйте влияние сильных ветров.</li>
</ul>
</div>
</details><details class="card mb-3 p-0 bg-info-light">
<p class="card-h3 text-white fs-5"><span class="icon me-2"><i class="fas fa-tint"></i></span> Ошибка 13: Короткое замыкание цепи датчика протока отопительной воды</p>
<div class="card-body">
<p class="has-text-weight-bold">Описание: Короткое замыкание цепи датчика протока отопительной воды (только модели Ace)</p>
<h6 class="h6 mt-4 text-success"><span class="icon me-2"><i class="fas fa-wrench"></i></span>Решение:</h6>
<ul class="ml-4 list-unstyled fs-6">
<li class="mb-2"><span class="icon me-2 text-primary"><i class="fas fa-search"></i></span> Выполните прозвонку цепи датчика протока.</li>
<li class="mb-2"><span class="icon me-2 text-warning"><i class="fas fa-broom"></i></span> Очистите механизм датчика протока или слегка постучите по нему.</li>
</ul>
</div>
</details><details class="card mb-3 p-0 bg-success-light">
<p class="card-h3 text-white fs-5"><span class="icon me-2"><i class="fas fa-microchip"></i></span> Ошибка 15: Сбой в работе или неисправность платы управления</p>
<div class="card-body">
<p class="has-text-weight-bold">Описание: Сбой в работе или неисправность платы управления</p>
<h6 class="h6 mt-4 text-success"><span class="icon me-2"><i class="fas fa-wrench"></i></span>Решение:</h6>
<ul class="ml-4 list-unstyled fs-6">
<li class="mb-2"><span class="icon me-2 text-primary"><i class="fas fa-plug"></i></span> Проверьте подключения всех элементов к плате управления.</li>
<li class="mb-2"><span class="icon me-2 text-warning"><i class="fas fa-sliders-h"></i></span> Убедитесь в правильной установке DIP-переключателей.</li>
<li class="mb-2"><span class="icon me-2 text-success"><i class="fas fa-sync"></i></span> Перезагрузите котел, при повторении ошибки замените плату управления.</li>
</ul>
</div>
</details><details class="card mb-3 p-0 bg-secondary-light">
<p class="card-h3 text-white fs-5"><span class="icon me-2"><i class="fas fa-thermometer-high"></i></span> Ошибка 16: Перегрев котла</p>
<div class="card-body">
<p class="has-text-weight-bold">Описание: Перегрев котла</p>
<h6 class="h6 mt-4 text-success"><span class="icon me-2"><i class="fas fa-wrench"></i></span>Решение:</h6>
<ul class="ml-4 list-unstyled fs-6">
<li class="mb-2"><span class="icon me-2 text-primary"><i class="fas fa-snowflake"></i></span> Дождитесь охлаждения котла и перезапустите его.</li>
<li class="mb-2"><span class="icon me-2 text-warning"><i class="fas fa-thermometer-half"></i></span> Испытайте датчик по перегреву и произведите его замену.</li>
<li class="mb-2"><span class="icon me-2 text-danger"><i class="fas fa-valve"></i></span> Проверьте трехходовой кран на предмет блокировки.</li>
</ul>
</div>
</details><details class="card mb-3 p-0 bg-primary-light">
<p class="card-h3 text-white fs-5"><span class="icon me-2"><i class="fas fa-thermometer-full"></i></span> Ошибка 18: Перегрев датчика дымоудаления (Navien Ace атмосферный)</p>
<div class="card-body">
<p class="has-text-weight-bold">Описание: Перегрев датчика дымоудаления</p>
<h6 class="h6 mt-4 text-success"><span class="icon me-2"><i class="fas fa-wrench"></i></span>Решение:</h6>
<ul class="ml-4 list-unstyled fs-6">
<li class="mb-2"><span class="icon me-2 text-primary"><i class="fas fa-snowflake"></i></span> После остывания датчика перезапустите котел.</li>
<li class="mb-2"><span class="icon me-2 text-warning"><i class="fas fa-broom"></i></span> Определите причину повышенного пневмосопротивления в системе дымоудаления и примите меры по чистке.</li>
</ul>
</div>
</details></div>
<div class="card bg-primary text-white p-5 mt-5">
<div class="text-center">
<h3 class="h4 display-4 text-white"><span class="icon me-2"><i class="fas fa-phone"></i></span>Нужна помощь специалиста?</h3>
<p class="h5 lead text-white">Свяжитесь с нами для профессиональной диагностики и ремонта:</p>
<div class="row is-centered mt-4">
<div class="col-lg-4 is-half-mobile mb-2"><a href="tel:+79262211348" class="btn btn-light btn-lg w-100"> <span class="icon me-2"><i class="fas fa-phone"></i></span> <span>+7(926) 221-13-48</span> </a></div>
<div class="col-lg-4 is-half-mobile"><a href="https://service04.ru/contact-us/feedback" class="btn btn-warning btn-lg w-100 text-dark"> <span class="icon me-2"><i class="fas fa-envelope"></i></span> <span>Написать нам</span> </a></div>
</div>
</div>
</div>
</div>
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
        resultDiv.innerHTML = '<div class="notification is-warning"><span class="icon me-2"><i class="fas fa-exclamation-triangle"></i></span>Пожалуйста, введите код ошибки для поиска.</div>';
        return;
    }
    
    const errorCode = searchTerm.replace('ERROR ', '').replace('ОШИБКА ', '').replace('E', '');
    const errorInfo = errorDatabase[errorCode];
    
    if (errorInfo) {
        let solutionList = '';
        errorInfo.solution.forEach(step => {
            // Преобразуем иконки Bootstrap/Font Awesome в Bulma span.icon
            let formattedStep = step;
            formattedStep = formattedStep.replace(/<i class="fas fa-([a-z-]+) (text-([a-z]+))? me-2"><\/i>/g, '<span class="icon me-2 has-$2"><i class="fas fa-$1"></i></span>');

            solutionList += `<li class="mb-2 fs-6">${formattedStep}</li>`;
        });
        
        resultDiv.innerHTML = `
            <div class="card has-border-primary">
                <header class="card-header bg-primary text-white">
                    <p class="card-h3 text-white"><span class="icon me-2"><i class="fas fa-search"></i></span>Результаты поиска для ошибки <strong>${errorCode}</strong></p>
                </header>
                <div class="card-body">
                    <h6 class="h6 mb-3 text-muted-dark"><span class="icon mr-1"><i class="fas fa-tag"></i></span> ${errorInfo.category}</h6>
                    <div class="content">
                        <h6 class="h6"><span class="icon mr-1"><i class="fas fa-file-alt"></i></span> Описание:</h6>
                        <p>${errorInfo.description}</p>
                        <h6 class="h6"><span class="icon mr-1"><i class="fas fa-wrench"></i></span> Решение:</h6>
                        <ul class="ml-4 list-unstyled">
                            ${solutionList}
                        </ul>
                        <div class="notification is-info mt-4">
                            <h6 class="h6"><span class="icon me-2"><i class="fas fa-info-circle"></i></span>Информация:</h6>
                            <p class="mb-0 fs-6">Эта информация предоставлена для ознакомления. Для сложных неисправностей рекомендуется обратиться к квалифицированному специалисту.</p>
                        </div>
                    </div>
                </div>
            </div>
        `;
        // Прокрутить к результатам поиска
        document.getElementById('searchResult').scrollIntoView({ behavior: 'smooth' });
    } else {
        resultDiv.innerHTML = `
            <div class="notification is-danger">
                <h5 class="h6 text-white"><span class="icon me-2"><i class="fas fa-exclamation-circle"></i></span>Ошибка не найдена</h5>
                <p class="mb-0 fs-6">Информация по коду ошибки <strong>${errorCode}</strong> в нашей базе отсутствует. Пожалуйста, сверьтесь с инструкцией к вашему котлу или обратитесь к специалисту.</p>
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