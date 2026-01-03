---
title: 'Коды ошибок котлов Ariston'
---

<div class="container-fluid mt-5 mb-5">
<section class="bg-primary text-white fw-bold mb-5">
<div class="py-5">
<div class="container text-center">

<p class="h4 lead text-white">Полное руководство по диагностике и устранению неисправностей котлов Аристон</p>
</div>
</div>
</section>
<div class="tabs is-carded is-medium">
<ul id="errorTabs">
<li class="is-active" data-tab-target="#heating"><a>Отопительный контур</a></li>
<li data-tab-target="#dhw"><a>ГВС</a></li>
<li data-tab-target="#board"><a>Электронная плата</a></li>
<li data-tab-target="#ignition"><a>Розжиг</a></li>
<li data-tab-target="#ventilation"><a>Вентиляция</a></li>
<li data-tab-target="#zones"><a>Температурные зоны</a></li>
</ul>
</div>
<div id="errorTabsContent" class="tab-content">
<div id="heating" class="tab-pane is-active">
<div class="card mt-3"><header class="card-header bg-danger text-white">
<p class="card-h3 text-white fs-5"><span class="icon me-2"><i class="fas fa-thermometer-three-quarters"></i></span>Ошибки отопительного контура</p>
</header>
<div class="card-body p-0">
<div class="table-container">
<table class="table is-striped is-bordered w-100 mb-0">
<thead class="bg-dark text-white">
<tr>
<th>Код</th>
<th>Описание</th>
<th>Возможные причины и решения</th>
</tr>
</thead>
<tbody>
<tr>
<td><span class="tag is-danger is-medium">101</span></td>
<td>Перегрев первичного теплообменника</td>
<td class="content fs-6">Проверить газовый клапан, прочистить фильтр, мойка/замена теплообменника, проверить циркуляционный насос. (T датчика NTC &gt; 102°C).</td>
</tr>
<tr>
<td><span class="tag is-danger is-medium">103</span></td>
<td>Недостаточная циркуляция (рост T подачи &gt; 7°C/сек)</td>
<td class="content fs-6">Проверить давление/удалить воздух, чистка/замена фильтра, проверить циркуляционный насос.</td>
</tr>
<tr>
<td><span class="tag is-danger is-medium">108</span></td>
<td>Низкое давление в контуре отопления</td>
<td class="content fs-6">Проверить давление (1-1.5 bar), проверить герметичность контура, чистка фильтра.</td>
</tr>
<tr>
<td><span class="tag is-danger is-medium">110</span></td>
<td>Датчик NTC1 разомкнут или короткое замыкание</td>
<td class="content fs-6">Проверить контакты и произвести замену датчика температуры NTC1.</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
<div id="dhw" class="tab-pane">
<div class="card mt-3"><header class="card-header bg-warning text-dark">
<p class="card-h3 text-dark fs-5"><span class="icon me-2"><i class="fas fa-shower"></i></span>Ошибки контура ГВС</p>
</header>
<div class="card-body p-0">
<div class="table-container">
<table class="table is-striped is-bordered w-100 mb-0">
<thead class="bg-dark text-white">
<tr>
<th>Код</th>
<th>Описание</th>
<th>Возможные причины</th>
</tr>
</thead>
<tbody>
<tr>
<td><span class="tag is-warning is-medium">201</span></td>
<td>Короткое замыкание или обрыв датчика температуры ГВС (NTCs)</td>
<td class="content fs-6">Проверить электрическую цепь датчика, заменить датчик при необходимости.</td>
</tr>
<tr>
<td><span class="tag is-warning is-medium">209</span></td>
<td>Перегрев санитарной воды в бойлере</td>
<td class="content fs-6">Проверить термостат и датчик температуры бойлера, проверить настройки температуры ГВС.</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
<div id="board" class="tab-pane">
<div class="card mt-3"><header class="card-header bg-info text-white">
<p class="card-h3 text-white fs-5"><span class="icon me-2"><i class="fas fa-microchip"></i></span>Ошибки электронной платы</p>
</header>
<div class="card-body p-0">
<div class="table-container">
<table class="table is-striped is-bordered w-100 mb-0">
<thead class="bg-dark text-white">
<tr>
<th>Код</th>
<th>Описание</th>
<th>Возможные причины и решения</th>
</tr>
</thead>
<tbody>
<tr>
<td><span class="tag is-info is-medium">301</span></td>
<td>Ошибка программы платы дисплея</td>
<td class="content fs-6">Отсутствует контакт между платами, проверить установку EEPROM ключа, заменить плату дисплея.</td>
</tr>
<tr>
<td><span class="tag is-info is-medium">303</span></td>
<td>Неисправность основной платы</td>
<td class="content fs-6">Плохой контакт между платами, проверить/заменить основную плату.</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
<div id="ignition" class="tab-pane">
<div class="card mt-3"><header class="card-header bg-success text-white">
<p class="card-h3 text-white fs-5"><span class="icon me-2"><i class="fas fa-fire"></i></span>Ошибки розжига и контроля пламени</p>
</header>
<div class="card-body p-0">
<div class="table-container">
<table class="table is-striped is-bordered w-100 mb-0">
<thead class="bg-dark text-white">
<tr>
<th>Код</th>
<th>Описание</th>
<th>Возможные причины и решения</th>
</tr>
</thead>
<tbody>
<tr>
<td><span class="tag is-success is-medium">501</span></td>
<td>Не найдено пламя в момент розжига</td>
<td class="content fs-6">Отсутствие газа, проблемы с заземлением (&gt;10V), неисправность электрода ионизации, проверить регулировку плавного розжига.</td>
</tr>
<tr>
<td><span class="tag is-success is-medium">502</span></td>
<td>Пламя при закрытом газовом клапане</td>
<td class="content fs-6">Заменить электрод ионизации, просушить электрод (влага), заменить газовый клапан, проверить заземление.</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
<div id="ventilation" class="tab-pane">
<div class="card mt-3"><header class="card-header bg-secondary text-white">
<p class="card-h3 text-white fs-5"><span class="icon me-2"><i class="fas fa-fan"></i></span>Ошибки вентиляции и дымоудаления</p>
</header>
<div class="card-body p-0">
<div class="table-container">
<table class="table is-striped is-bordered w-100 mb-0">
<thead class="bg-dark text-white">
<tr>
<th>Код</th>
<th>Описание</th>
<th>Возможные причины</th>
</tr>
</thead>
<tbody>
<tr>
<td><span class="tag is-secondary is-medium">601</span></td>
<td>Срабатывание датчика тяги</td>
<td class="content fs-6">Только в моделях с открытой камерой. Проверить дымоход и тягу.</td>
</tr>
<tr>
<td><span class="tag is-secondary is-medium">604</span></td>
<td>Работа вентилятора с малой скоростью</td>
<td class="content fs-6">Скорость менее 1775 об/мин. Неисправность датчика Холла. Проверить вентилятор и электродвигатель.</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
<div id="zones" class="tab-pane">
<div class="card mt-3"><header class="card-header bg-dark text-white">
<p class="card-h3 text-white fs-5"><span class="icon me-2"><i class="fas fa-temperature-high"></i></span>Ошибки температурных зон</p>
</header>
<div class="card-body p-0">
<div class="table-container">
<table class="table is-striped is-bordered w-100 mb-0">
<thead class="bg-dark text-white">
<tr>
<th>Код</th>
<th>Описание</th>
<th>Возможные причины</th>
</tr>
</thead>
<tbody>
<tr>
<td><span class="tag is-dark is-medium">701</span></td>
<td>Короткое замыкание или обрыв датчика зоны 2</td>
<td class="content fs-6">Проверить электрическую цепь температурного датчика подающей линии зоны 2.</td>
</tr>
<tr>
<td><span class="tag is-dark is-medium">706</span></td>
<td>Перегрев в температурной зоне 2</td>
<td class="content fs-6">Проверить систему отопления зоны 2, проверить настройки термостата зоны.</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
</div>
<div class="notification is-danger mt-5">
<h4 class="h4 display-4 text-white"><span class="icon me-2"><i class="fas fa-exclamation-triangle"></i></span>Важно!</h4>
<p class="mb-3 fs-6">При возникновении ошибок котла Ariston:</p>
<div class="content fs-6">
<ul class="ml-4">
<li>**Не пытайтесь самостоятельно ремонтировать газовое оборудование**</li>
<li>**Немедленно обратитесь к квалифицированным специалистам**</li>
<li>Сохраните код ошибки для быстрой диагностики мастером</li>
</ul>
</div>
</div>
<div class="card bg-primary text-white shadow p-5 mt-5">
<div class="text-center">
<h3 class="h4 display-4 text-white"><span class="icon me-2"><i class="fas fa-headset"></i></span>Нужна профессиональная помощь?</h3>
<p class="h5 lead text-white">Наши специалисты быстро диагностируют и устранят любую неисправность котла Ariston</p>
<div class="row is-centered mt-4">
<div class="col-lg-4 is-half-mobile mb-2"><a href="tel:+79262211348" class="btn btn-success btn-lg w-100"> <span class="icon me-2"><i class="fas fa-phone"></i></span> <span>Позвонить сейчас</span> </a></div>
<div class="col-lg-4 is-half-mobile"><a href="https://service04.ru/contact-us/feedback" class="btn btn-light btn-lg w-100"> <span class="icon me-2"><i class="fas fa-calendar-check"></i></span> <span>Записаться на выезд</span> </a></div>
</div>
</div>
</div>
</div>
<script>
    document.addEventListener('DOMContentLoaded', () => {
        const tabs = document.querySelectorAll('.tabs li');
        const tabContents = document.querySelectorAll('.tab-content .tab-pane');

        // Function to handle tab switching
        const activateTab = (targetId) => {
            tabs.forEach(tab => {
                if (tab.dataset.tabTarget === targetId) {
                    tab.classList.add('is-active');
                } else {
                    tab.classList.remove('is-active');
                }
            });

            tabContents.forEach(content => {
                if ('#' + content.id === targetId) {
                    content.classList.add('is-active');
                } else {
                    content.classList.remove('is-active', 'show'); // Remove 'show' for Bulma/plain JS compatibility
                }
            });
        };

        // Event listener for tab clicks
        tabs.forEach(tab => {
            tab.addEventListener('click', (event) => {
                event.preventDefault();
                const targetId = tab.dataset.tabTarget;
                activateTab(targetId);
            });
        });

        // Initial activation of the active tab (Optional, but good practice)
        const activeTab = document.querySelector('.tabs li.is-active');
        if (activeTab) {
            activateTab(activeTab.dataset.tabTarget);
        } else if (tabs.length > 0) {
            // Default to the first tab if none are marked active
            tabs[0].classList.add('is-active');
            activateTab(tabs[0].dataset.tabTarget);
        }
    });
</script>