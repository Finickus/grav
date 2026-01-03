---
title: 'Ошибка F20 на Protherm Skat'
---

<p>.<img src="https://service04.ru/bl-content/uploads/pages/13b1ab15669c527985553ca0367048a1/Screenshot_188.jpg" alt=""></p>
<div class="container my-5"><!-- Заголовок -->
<div class="jumbotron bg-danger text-white text-center py-4 mb-4">

<p class="lead">Полное руководство для мастеров</p>
</div>
<!-- Основной вывод -->
<div class="card mb-4 shadow-sm">
<div class="card-body">
<p class="lead">Код <strong>F20</strong> сигнализирует о срабатывании аварийного термостата из-за перегрева теплообменника, вызванного недостаточной циркуляцией теплоносителя или блокировкой контура. Диагностика включает проверку циркуляции, насоса, термостата, электроники и настроек котла.</p>
</div>
</div>
<!-- 1. Общая характеристика -->
<div class="card mb-4 shadow-sm border-primary">
<div class="card-header bg-primary text-white">
<h2 class="h5 mb-0"><i class="fas fa-info-circle me-2"></i>1. Общая характеристика</h2>
</div>
<div class="card-body">
<p>Код <strong>F20</strong> означает «перегрев»: аварийный термостат на выходной трубе теплообменника разомкнул цепь безопасности, остановил ТЭНы и заблокировал работу котла. Самосброса нет — требуется ручной сброс.</p>
</div>
</div>
<!-- 2. Сброс термостата -->
<div class="card mb-4 shadow-sm border-warning">
<div class="card-header bg-warning text-dark">
<h2 class="h5 mb-0"><i class="fas fa-thermometer-three-quarters me-2"></i>2. Сброс аварийного термостата</h2>
</div>
<div class="card-body">
<p><strong>Расположение:</strong> под резиновым колпачком на выходной трубе теплообменника.</p>
<ol>
<li>Отключить котёл от сети.</li>
<li>Снять резиновый колпачок.</li>
<li>Нажать красную кнопку термостата.</li>
<li>Установить колпачок и включить котёл.</li>
</ol>
<p class="text-muted">Примечание: без термопасты датчик теряет чувствительность и ложится срабатывание.</p>
<p class="text-muted"><img src="https://service04.ru/bl-content/uploads/pages/13b1ab15669c527985553ca0367048a1/Screenshot_183(1).jpg" alt=""></p>
</div>
</div>
<!-- Аккордеон алгоритма -->
<h2 class="h3 text-danger mb-3"><i class="fas fa-tools me-2"></i>3. Алгоритм диагностики</h2>
<div id="f20Accordion" class="accordion mb-4"><!-- 3.1 Циркуляция -->
<div class="card">
<div class="card-header bg-light" id="headingCirculation">
<h5 class="mb-0"><btn btn-primary class="btn btn-link text-danger" data-toggle="collapse" data-target="#collapseCirculation" aria-expanded="true"> <i class="fas fa-water me-2"></i>3.1 Проверка циркуляции теплоносителя </btn btn-primary></h5>
</div>
<div id="collapseCirculation" class="collapse show" data-parent="#f20Accordion">
<div class="card-body">
<h6 class="text-primary">Воздух в системе</h6>
<ul>
<li>Стравить воздух из теплообменника, радиаторов, автоматических воздухоотводчиков.</li>
<li><a href="https://service04.ru/bl-content/uploads/image/Protherm/Screenshot_191%20(1).jpg"><img src="https://service04.ru/bl-content/uploads/pages/13b1ab15669c527985553ca0367048a1/thumbnails/Screenshot_191(1).jpg" alt="" width="124" height="124"></a></li>
<li>Прокрутить вал насоса вручную.</li>
<li><a href="https://service04.ru/bl-content/uploads/image/Protherm/Screenshot_186%20(1).jpg"><img src="https://service04.ru/bl-content/uploads/pages/13b1ab15669c527985553ca0367048a1/thumbnails/Screenshot_186.jpg" alt="" width="122" height="122"></a></li>
</ul>
<h6 class="text-primary mt-3">Насос отопления</h6>
<ul>
<li>Проверить питание и контакты.</li>
<li>Разобрать, очистить крыльчатку и ротор.</li>
<li>Измерить ёмкость пускового конденсатора, заменить при отклонении.</li>
<li>При дефектах заменить насос.</li>
</ul>
<h6 class="text-primary mt-3">Теплоноситель</h6>
<ul>
<li>Слить и промыть систему.</li>
<li>Залить рекомендованный производителем теплоноситель.</li>
</ul>
</div>
</div>
</div>
<!-- 3.2 Термостат -->
<div class="card">
<div class="card-header bg-light" id="headingThermostat">
<h5 class="mb-0"><btn btn-primary class="btn btn-link text-warning collapsed" data-toggle="collapse" data-target="#collapseThermostat"> <i class="fas fa-temperature-high me-2"></i>3.2 Термостат перегрева </btn btn-primary></h5>
</div>
<div id="collapseThermostat" class="collapse" data-parent="#f20Accordion">
<div class="card-body">
<p>Срабатывание при температуре &gt;95 °C. Проверить наличие термопасты, отсутствие повреждений, сбросить вручную.</p>
</div>
</div>
</div>
<!-- 3.3 Электроника -->
<div class="card">
<div class="card-header bg-light" id="headingElectronics">
<h5 class="mb-0"><btn btn-primary class="btn btn-link text-info collapsed" data-toggle="collapse" data-target="#collapseElectronics"> <i class="fas fa-microchip me-2"></i>3.3 Электроника и предохранители </btn btn-primary></h5>
</div>
<div id="collapseElectronics" class="collapse" data-parent="#f20Accordion">
<div class="card-body">
<h6 class="text-primary">Предохранители</h6>
<p>Низкоамперный предохранитель 80 mA на плате: заменить при перегорании.</p>
<h6 class="text-primary mt-3">Плата управления</h6>
<ul>
<li>Осмотреть на конденсат, оплавление дорожек, коррозию.</li>
<li>Очистить и высушить; при дефектах — сервисная диагностика.</li>
</ul>
</div>
</div>
</div>
<!-- 3.4 Настройки -->
<div class="card">
<div class="card-header bg-light" id="headingSettings">
<h5 class="mb-0"><btn btn-primary class="btn btn-link text-success collapsed" data-toggle="collapse" data-target="#collapseSettings"> <i class="fas fa-cog me-2"></i>3.4 Настройки управления </btn btn-primary></h5>
</div>
<div id="collapseSettings" class="collapse" data-parent="#f20Accordion">
<div class="card-body">
<p>Параметр <strong>d.19</strong> (скорость насоса). При недостаточной циркуляции установить <strong>d.19 = 0</strong> для увеличения оборотов насоса.</p>
</div>
</div>
</div>
</div>
<!-- 4. Форумные кейсы -->
<div class="card mb-4 shadow-sm border-warning">
<div class="card-header bg-warning text-dark">
<h2 class="h5 mb-0"><i class="fas fa-comments me-2"></i>4. Типичные «форумные» кейсы</h2>
</div>
<div class="card-body">
<ul>
<li><strong>После простоя:</strong> засохший насос, залипшие сёдла — прокрутить вал вручную.</li>
<li><strong>«Рандомно» в течение дня:</strong> нестабильное напряжение, плохое заземление — использовать ИБП/стабилизатор.</li>
<li><strong>В холодное время:</strong> перегрев из-за грязных радиаторов и обмерзших узлов — очистить или заменить радиаторы.</li>
</ul>
</div>
</div>
<!-- 5. Профилактика -->
<div class="card mb-4 shadow-sm border-success">
<div class="card-header bg-success text-white">
<h2 class="h5 mb-0"><i class="fas fa-calendar-check me-2"></i>5. Профилактика</h2>
</div>
<div class="card-body">
<ul>
<li>Ежегодное ТО: чистка теплообменника, воздухоотводка, насос, замена предохранителей, проверка платы.</li>
<li>Контроль теплоносителя: замена и промывка системы.</li>
<li>Защита питания: ИБП/стабилизатор с «чистой синусоидой».</li>
<li>Регулярный сброс воздуха после пуска и в процессе эксплуатации.</li>
</ul>
</div>
</div>
<!-- 6. Когда обращаться в сервис -->
<div class="card mb-5 shadow-sm border-danger">
<div class="card-header bg-danger text-white">
<h2 class="h5 mb-0"><i class="fas fa-headset me-2"></i>6. Когда обращаться в сервис</h2>
</div>
<div class="card-body">
<ul>
<li>Неисправны предохранители или плата управления.</li>
<li>Реальная поломка насоса или термостата.</li>
<li>Отсутствие необходимого инструмента и опыта.</li>
</ul>
</div>
</div>
<!-- Контакты -->
<div class="card bg-primary text-white shadow">
<div class="card-body text-center">
<h3 class="card-h3 h4"><i class="fas fa-phone-alt me-2"></i>Нужна помощь?</h3>
<p class="lead">Свяжитесь с нами для диагностики и ремонта!</p>
<div class="row justify-content-center mb-3">
<div class="col-md-3 mb-2"><a href="tel:+79262211348" class="btn btn-light btn-lg btn-block"> <i class="fas fa-phone me-2"></i>Позвонить </a></div>
<div class="col-md-3 mb-2"><a href="mailto:89262211348@mail.ru" class="btn btn-warning btn-lg btn-block text-dark"> <i class="fas fa-envelope me-2"></i>Написать </a></div>
<div class="col-md-3 mb-2"><a href="https://service04.ru/contact-us/feedback" class="btn btn-success btn-lg btn-block"> <i class="fas fa-file-alt me-2"></i>Заявка </a></div>
</div>
<p class="mb-1"><i class="fab fa-whatsapp me-2"></i>WhatsApp/Telegram: +7 926 221-13-48</p>
<p class="mb-1"><i class="fas fa-globe me-2"></i>Сайт: Service04.ru</p>
<p><i class="fas fa-envelope me-2"></i>E-mail: 89262211348@mail.ru</p>
</div>
</div>
</div>
<p>
<script>
  $(document).on('click', '[data-toggle="lightcard"]', function(e) {
    e.preventDefault();
    $(this).ekkoLightcard();
  });
</script>
</p>