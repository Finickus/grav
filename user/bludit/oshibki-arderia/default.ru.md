---
title: 'Коды ошибок котлов Arderia'
---

<div class="container-fluid mt-5 mb-5">
<section class="bg-primary text-white fw-bold mb-5">
<div class="py-5">
<div class="container text-center">

<p class="h4 lead text-white">Руководство по диагностике и устранению неисправностей котлов Ардерия</p>
</div>
</div>
</section>
<div class="row">
<div class="col is-full">
<div class="card mb-5"><header class="card-header bg-danger text-white">
<p class="card-h3 text-white fs-5"><span class="icon me-2"><i class="fas fa-list"></i></span>Коды ошибок A1 - AA (Критические)</p>
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
<td><span class="tag is-danger is-medium">A1</span></td>
<td>Датчик давления воздуха замкнут</td>
<td class="content fs-6">Задувание/блокировка дымохода, обледенение выходного отверстия.</td>
</tr>
<tr>
<td><span class="tag is-danger is-medium">A2</span></td>
<td>Вентилятор работает с малой скоростью</td>
<td class="content fs-6">Недостаточный контакт/подключение проводов, недостаточная скорость вращения (посторонние предметы).</td>
</tr>
<tr>
<td><span class="tag is-danger is-medium">A4</span></td>
<td>Срабатывание датчика по перегреву</td>
<td class="content fs-6">Закрыты запорные краны, засор фильтра, неисправен насос/3-х ходовой клапан, повреждение датчика протока ГВС.</td>
</tr>
<tr>
<td><span class="tag is-danger is-medium">A5</span></td>
<td>Пониженное давление теплоносителя</td>
<td class="content fs-6">Малый объем воды, наличие воздуха, неисправен насос/датчик напора, утечка воды в системе.</td>
</tr>
<tr>
<td><span class="tag is-danger is-medium">A6</span></td>
<td>Неисправность розжига</td>
<td class="content fs-6">Дымоход заблокирован, низкое давление газа, неисправен газовый клапан/трансформатор.</td>
</tr>
<tr>
<td><span class="tag is-danger is-medium">A8</span></td>
<td>Остаточное пламя</td>
<td class="content fs-6">Остаточное пламя при отсутствии напряжения, повреждение диафрагмы газового клапана.</td>
</tr>
<tr>
<td><span class="tag is-danger is-medium">A9</span></td>
<td>Замерзание</td>
<td class="content fs-6">Снижение температуры воды до 5°C.</td>
</tr>
<tr>
<td><span class="tag is-danger is-medium">AA</span></td>
<td>Закипание (Перегрев)</td>
<td class="content fs-6">Закрыты отопительные контуры, засор фильтра, повреждение насоса/трехходового клапана.</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
<div class="card mb-5"><header class="card-header bg-warning text-dark">
<p class="card-h3 text-dark fs-5"><span class="icon me-2"><i class="fas fa-list"></i></span>Коды ошибок AB - AE (Датчики/Дымоход)</p>
</header>
<div class="card-body p-0">
<div class="table-container">
<table class="table is-striped is-bordered w-100 mb-0">
<tbody>
<tr>
<td><span class="tag is-warning is-medium">AB, AC</span></td>
<td>Повреждение термостата</td>
<td class="content fs-6">Короткое замыкание в термостате, некорректное соединение контактов.</td>
</tr>
<tr>
<td><span class="tag is-warning is-medium">AE</span></td>
<td>Дымоход заблокирован</td>
<td class="content fs-6">Посторонние предметы в газоходе, деформация газохода.</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
<div class="card mb-5"><header class="card-header bg-info text-white">
<p class="card-h3 text-white fs-5"><span class="icon me-2"><i class="fas fa-info-circle"></i></span>Диагностика и устранение (Коды E0-E3)</p>
</header>
<div class="card-body content">
<div id="errorAccordion"><details class="card mb-3 p-0 bg-light">
<summary class="h5 has-text-secondary mb-0"><span class="tag is-secondary is-medium me-2">E0</span> Ошибка режима антизамерзание</summary>
<div class="p-4 fs-6">
<p class="has-text-weight-bold">Описание: Ошибка активна, если после перерыва подачи электроэнергии температура систем отопления или ГВС ниже +1 °С.</p>
<p class="has-text-weight-bold mt-2">Решение:</p>
<ul class="ml-4 list-unstyled">
<li>Убедитесь в целостности магистралей. Блокировка автоматически снимется при повышении температуры выше +1°C.</li>
</ul>
</div>
</details><details class="card mb-3 p-0 bg-light">
<summary class="h5 has-text-secondary mb-0"><span class="tag is-secondary is-medium me-2">E1</span> Ошибка датчика ионизации</summary>
<div class="p-4 fs-6">
<p class="has-text-weight-bold">Описание: Отображается при неудачном розжиге котла или после неожиданного срыва пламени.</p>
<p class="has-text-weight-bold mt-2">Решение:</p>
<ul class="ml-4 list-unstyled">
<li>Проверьте наличие подачи газа. Система будет пытаться восстановить работу 60 минут. Снять блокировку можно нажатием кнопки MODE.</li>
</ul>
</div>
</details><details class="card mb-3 p-0 bg-light">
<summary class="h5 has-text-secondary mb-0"><span class="tag is-secondary is-medium me-2">E2</span> Ошибка дифференциального датчика давления воздуха</summary>
<div class="p-4 fs-6">
<p class="has-text-weight-bold">Описание: Отображается в ситуации ненормальной тяги, неисправностью вентилятора или датчика давления воздуха.</p>
<p class="has-text-weight-bold mt-2">Решение:</p>
<ul class="ml-4 list-unstyled">
<li>Убедитесь в нормальном состоянии дымохода. Если через 15 минут ошибка не устраняется, обратитесь в сервисную службу.</li>
</ul>
</div>
</details><details class="card mb-3 p-0 bg-light">
<summary class="h5 has-text-secondary mb-0"><span class="tag is-secondary is-medium me-2">E3</span> Ошибка защитного термостата перегрева</summary>
<div class="p-4 fs-6">
<p class="has-text-weight-bold">Описание: Отображается в ситуациях отсутствия теплоносителя или его циркуляции.</p>
<p class="has-text-weight-bold mt-2">Решение:</p>
<ul class="ml-4 list-unstyled">
<li>Откройте кран разбора горячей воды для понижения температуры, проверьте состояние вентилей и магистралей отопления. Снять блокировку можно нажатием кнопки MODE.</li>
</ul>
</div>
</details></div>
</div>
</div>
<div class="card mb-5"><header class="card-header bg-success text-white">
<p class="card-h3 text-white fs-5"><span class="icon me-2"><i class="fas fa-wrench"></i></span>Возможные неполадки и их устранения</p>
</header>
<div class="card-body content">
<div id="troubleshootingAccordion"><details class="card mb-3 p-0 bg-light">
<summary class="h5 text-dark mb-0">Вентилятор начал работать, но пламя не появляется</summary>
<div class="p-4 fs-6">
<ul class="ml-4">
<li>Не срабатывает реле давления воздуха / Блокировка дымохода / Утечка в системе отвода продуктов сгорания.</li>
<li>Напряжение электропитания ниже 170 В - <span class="text-danger">Установите стабилизатор напряжения.</span></li>
<li><span class="has-text-weight-bold">Решение:</span> Немедленно обратитесь в сервисный центр для диагностики.</li>
</ul>
</div>
</details><details class="card mb-3 p-0 bg-light">
<summary class="h5 text-dark mb-0">Неправильное горение: цвет пламени желтый или красный</summary>
<div class="p-4 fs-6">
<ul class="ml-4">
<li>Горелка загрязнена / Неправильное функционирование дымохода / Неверная настройка газового клапана.</li>
</ul>
</div>
</details><details class="card mb-3 p-0 bg-light">
<summary class="h5 text-dark mb-0">Котел Ардерия часто выключается</summary>
<div class="p-4 fs-6">
<ul class="ml-4">
<li>Недостаточное давление/утечки / Наличие воздуха в системе / Вал насоса заблокирован.</li>
<li><span class="has-text-weight-bold">Решение:</span> Проверьте давление (1-1.2 bar), удалите воздух, поднимите давление в расширительном баке до 1.0 bar.</li>
</ul>
</div>
</details></div>
</div>
</div>
</div>
</div>
<div class="card bg-dark text-white shadow p-5 mt-5">
<div class="text-center">
<h3 class="h4 display-4 text-white"><span class="icon me-2"><i class="fas fa-phone"></i></span>Нужна помощь специалиста?</h3>
<p class="h5 lead text-white">Не занимайтесь самостоятельным ремонтом газового оборудования!</p>
<div class="row is-centered mt-4">
<div class="col-lg-4 is-half-mobile mb-2"><a href="tel:+79262211348" class="btn btn-success btn-lg w-100"> <span class="icon me-2"><i class="fas fa-headset"></i></span> <span>Вызвать мастера</span> </a></div>
</div>
</div>
</div>
</div>