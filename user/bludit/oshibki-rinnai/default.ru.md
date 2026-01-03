---
title: 'Ошибки котлов Rinnai'
---

<div class="container-fluid mt-5 mb-5">
<section class="bg-primary text-white fw-bold mb-5">
<div class="py-5">
<div class="container text-center">

<p class="h4 lead text-white">Диагностика и устранение неисправностей</p>
</div>
</div>
</section>
<div class="card mb-5">
<div class="card-body">
<p class="fs-5">Котлы Rinnai оснащены системой самодиагностики, которая при возникновении неисправности отображает коды ошибок.</p>
<div class="notification is-danger mt-4">
<h5 class="h6 text-white"><span class="icon me-2"><i class="fas fa-exclamation-triangle"></i></span>Предупреждение о безопасности</h5>
<p class="mb-0">Работы с газовым оборудованием требуют квалификации. При отсутствии опыта или если ошибка сохраняется после выполнения рекомендованных действий, **вызывайте сервисного инженера**.</p>
</div>
<div class="text-center mt-4"><img src="https://service04.ru/bl-content/uploads/image/Rinnai/Screenshot_44.jpg" alt="Дисплей ошибок Rinnai" style="display: block; margin: 0 auto; max-width: 235px;"></div>
</div>
</div>
<div class="card mb-5"><header class="card-header bg-dark text-white">
<p class="card-h3 text-white fs-5"><span class="icon me-2"><i class="fas fa-list"></i></span>Коды ошибок</p>
</header>
<div class="card-body p-0">
<div class="table-container">
<table class="table is-bordered is-striped is-hoverable w-100 mb-0">
<thead class="bg-light text-dark">
<tr>
<th class="text-center">Код</th>
<th>Неисправность</th>
<th>Признаки</th>
<th>Способы устранения</th>
<th>Ключевые узлы для проверки</th>
</tr>
</thead>
<tbody>
<tr>
<td class="text-center"><span class="tag is-warning is-medium">7</span></td>
<td>Превышение времени работы</td>
<td>Расход тепла/воды &gt; 8 часов</td>
<td class="content fs-6">Проверить клапан подачи тепла/воды, переключатель потока воды, замерить напряжение на CN9 модуля.</td>
<td>Клапаны, электронный модуль</td>
</tr>
<tr>
<td class="text-center"><span class="tag is-danger is-medium">11</span></td>
<td>Проблема зажигания</td>
<td>Отсутствие реакции сенсора пламени</td>
<td class="content fs-6">Проверить сопротивление зажигания, убедиться в подаче газа, прочистить теплообменник и дымоход.</td>
<td>Сенсор пламени, горелка, дымоход</td>
</tr>
<tr>
<td class="text-center"><span class="tag is-danger is-medium">12</span></td>
<td>Частое затухание пламени</td>
<td>Пламя гаснет &gt; 20 раз/сутки</td>
<td class="content fs-6">Проверить давление газа, очистить теплообменник, проверить вентилятор и клапан.</td>
<td>Газовый тракт, вентилятор, пропорциональный клапан</td>
</tr>
<tr>
<td class="text-center"><span class="tag is-warning is-medium">14</span></td>
<td>Неисправность термопредохранителя</td>
<td>Срабатывание защиты</td>
<td class="content fs-6">Проверить на КЗ в термопредохранителе, заменить электронный модуль.</td>
<td>Термопредохранитель, плата управления</td>
</tr>
<tr>
<td class="text-center"><span class="tag is-danger is-medium">15</span></td>
<td>Перегрев из-за отсутствия воды</td>
<td>Перегрев теплообменника</td>
<td class="content fs-6">Проверить систему на утечки, исключить замерзание, проверить терморезистор.</td>
<td>Терморезистор, гидравлическая система</td>
</tr>
<tr>
<td class="text-center"><span class="tag is-danger is-medium">16</span></td>
<td>Перегрев системы отопления</td>
<td>Температура воды &gt;95°C &gt;3 сек</td>
<td class="content fs-6">Проверить циркуляционный насос, протестировать трехходовой клапан, очистить фильтры и трубы.</td>
<td>Насос, клапаны, фильтры, термистор</td>
</tr>
<tr>
<td class="text-center"><span class="tag is-warning is-medium">18</span></td>
<td>Замыкание на землю</td>
<td>Проблемы с изоляцией</td>
<td class="content fs-6">Замерить напряжение между CN3 и землей, проверить изоляцию кабелей.</td>
<td>Электропроводка, заземление</td>
</tr>
<tr>
<td class="text-center"><span class="tag is-info is-medium">20</span></td>
<td>Неправильные настройки DIP</td>
<td>Некорректная работа системы</td>
<td class="content fs-6">Проверить положение DIP-переключателей, установить правильные настройки.</td>
<td>DIP-переключатели на плате</td>
</tr>
<tr>
<td class="text-center"><span class="tag is-warning is-medium">28</span></td>
<td>Ошибка связи с пультом</td>
<td>Нет связи с управляющим блоком</td>
<td class="content fs-6">Проверить подключение пульта, убедиться в наличии питания.</td>
<td>Пульт управления, кабели связи</td>
</tr>
<tr>
<td class="text-center"><span class="tag is-warning is-medium">31</span></td>
<td>Неисправность терморезистора отопления</td>
<td>Некорректные показания температуры</td>
<td class="content fs-6">Проверить соединения, заменить термистор.</td>
<td>Терморезистор системы отопления</td>
</tr>
<tr>
<td class="text-center"><span class="tag is-warning is-medium">43</span></td>
<td>Низкий уровень воды</td>
<td>Отсутствие воды &gt;43 сек</td>
<td class="content fs-6">Проверить электроды уровня воды, очистить водоотделитель, проверить клапан подачи воды.</td>
<td>Датчики уровня, фильтры, клапаны</td>
</tr>
<tr>
<td class="text-center"><span class="tag is-danger is-medium">61</span></td>
<td>Неисправность вентилятора</td>
<td>Недостижение нужной скорости</td>
<td class="content fs-6">Проверить вентилятор, очистить теплообменник, проверить дымоход.</td>
<td>Вентилятор, дымоход, теплообменник</td>
</tr>
<tr>
<td class="text-center"><span class="tag is-danger is-medium">89</span></td>
<td>Замерзание системы</td>
<td>Полное замерзание контура</td>
<td class="content fs-6">Проверить термистор, прогреть систему, проверить на разрывы.</td>
<td>Термистор, теплообменник, трубы</td>
</tr>
<tr>
<td class="text-center"><span class="tag is-warning is-medium">90</span></td>
<td>Ошибка вентилятора</td>
<td>Некорректный ток вентилятора</td>
<td class="content fs-6">Проверить вентилятор, очистить теплообменник, проверить дымоход.</td>
<td>Вентилятор, теплообменник, дымоход</td>
</tr>
<tr>
<td class="text-center"><span class="tag is-warning is-medium">99</span></td>
<td>Закрытие выхлопа</td>
<td>Невозможность компенсации тока</td>
<td class="content fs-6">Проверить вентилятор, очистить теплообменник, проверить дымоход.</td>
<td>Вентилятор, дымоходная система</td>
</tr>
</tbody>
</table>
</div>
<div class="mt-4 p-3 bg-light rounded">
<h3 class="h6">Условные обозначения:</h3>
<div class="d-flex d-flex-wrap-wrap">
<div class="mr-3 mb-2"><span class="tag is-danger is-medium">Красный</span> - Критическая ошибка</div>
<div class="mr-3 mb-2"><span class="tag is-warning is-medium">Желтый</span> - Серьезная неисправность</div>
<div class="mr-3 mb-2"><span class="tag is-info is-medium">Синий</span> - Настройки/конфигурация</div>
</div>
</div>
</div>
</div>
</div>