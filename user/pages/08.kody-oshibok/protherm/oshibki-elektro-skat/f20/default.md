---
title: F20
metadata:
  description: Ошибка F20 на Protherm Skat Полное руководство для мастеров Код F20
    сигнализирует о срабатывании аварийного термостата из-за перегрева теплообменника,...
  og:type: article
  og:title: F20 - Service04
  og:description: Ошибка F20 на Protherm Skat Полное руководство для мастеров Код
    F20 сигнализирует о срабатывании аварийного термостата из-за перегрева теплообменника,...
  og:url: https://service04.ru/kody-oshibok/protherm/oshibki-elektro-skat/f20
  og:site_name: Service04
  og:locale: ru_RU
  og:image: https://service04.ru/images/og-default.jpg
  og:image:width: '1200'
  og:image:height: '630'
  canonical: https://service04.ru/kody-oshibok/protherm/oshibki-elektro-skat/f20
  robots: index, follow
  yandex-verification: ''
  geo.region: RU-MOW
  geo.placename: Москва
  author: Service04
---
<div class="container py-5">
    <div class="p-5 mb-5 text-white text-center rounded-3 shadow-sm" style="background-color: #009688;">
        <h1 class="display-4 fw-bold">
            <i class="fas fa-exclamation-triangle me-3"></i>Ошибка F20 на Protherm Skat
        </h1>
        <p class="lead">Полное руководство для мастеров</p>
        
    </div>

    <div class="card mb-4 shadow-sm border-0">
        <div class="card-body">
            <p class="lead">Код <strong>F20</strong> сигнализирует о срабатывании аварийного термостата из-за перегрева теплообменника, вызванного недостаточной циркуляцией теплоносителя или блокировкой контура. Диагностика включает проверку циркуляции, насоса, термостата, электроники и настроек котла.</p>
        </div>
    </div>

    <div class="card mb-4 shadow-sm border-primary">
        <div class="card-header bg-primary text-white">
            <h2 class="h5 mb-0"><i class="fas fa-info-circle me-2"></i>1. Общая характеристика</h2>
        </div>
        <div class="card-body">
            <p>Код <strong>F20</strong> означает «перегрев»: аварийный термостат на выходной трубе теплообменника разомкнул цепь безопасности, остановил ТЭНы и заблокировал работу котла. Самосброса нет — требуется ручной сброс.</p>
        </div>
    </div>

    <div class="card mb-4 shadow-sm border-warning">
        <div class="card-header bg-warning text-dark">
            <h2 class="h5 mb-0"><i class="fas fa-thermometer-three-quarters me-2"></i>2. Сброс аварийного термостата</h2>
        </div>
        <div class="card-body">
            <p><strong>Расположение:</strong> под резиновым колпачком на выходной трубе теплообменника.</p>
            <ol class="ms-3">
                <li>Отключить котёл от сети.</li>
                <li>Снять резиновый колпачок.</li>
                <li>Нажать красную кнопку термостата.</li>
                <li>Установить колпачок и включить котёл.</li>
            </ol>
            <p class="text-muted small">Примечание: без термопасты датчик теряет чувствительность и вызывает ложное срабатывание.</p>
            
        </div>
    </div>

    <h2 class="h3 text-danger mb-3"><i class="fas fa-tools me-2"></i>3. Алгоритм диагностики</h2>
    <div class="accordion mb-4" id="f20Accordion">

        <div class="accordion-item">
            <h2 class="accordion-header" id="headingCirculation">
                <button class="accordion-button text-danger fw-bold" type="button" data-bs-toggle="collapse" data-bs-target="#collapseCirculation" aria-expanded="true" aria-controls="collapseCirculation">
                    <i class="fas fa-water me-2"></i>3.1 Проверка циркуляции теплоносителя
                </button>
            </h2>
            <div id="collapseCirculation" class="accordion-collapse collapse show" aria-labelledby="headingCirculation" data-bs-parent="#f20Accordion">
                <div class="accordion-body">
                    <h6 class="text-primary fw-bold">Воздух в системе</h6>
                    <ul class="ms-3">
                        <li>Стравить воздух из теплообменника, радиаторов, автоматических воздухоотводчиков. </li>
                        <li>Прокрутить вал насоса вручную.</li>
                    </ul>
                    
                    <h6 class="text-primary fw-bold mt-3">Насос отопления</h6>
                    <ul class="ms-3">
                        <li>Проверить питание и контакты.</li>
                        <li>Разобрать, очистить крыльчатку и ротор.</li>
                        <li>Измерить ёмкость пускового конденсатора, заменить при отклонении.</li>
                        <li>При дефектах заменить насос.</li>
                    </ul>
                    
                    <h6 class="text-primary fw-bold mt-3">Теплоноситель</h6>
                    <ul class="ms-3">
                        <li>Слить и промыть систему.</li>
                        <li>Залить рекомендованный производителем теплоноситель.</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="headingThermostat">
                <button class="accordion-button collapsed text-warning fw-bold" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThermostat" aria-expanded="false" aria-controls="collapseThermostat">
                    <i class="fas fa-temperature-high me-2"></i>3.2 Термостат перегрева
                </button>
            </h2>
            <div id="collapseThermostat" class="accordion-collapse collapse" aria-labelledby="headingThermostat" data-bs-parent="#f20Accordion">
                <div class="accordion-body">
                    <p>Срабатывание при температуре >95 °C. Проверить наличие термопасты, отсутствие повреждений, сбросить вручную.</p>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="headingElectronics">
                <button class="accordion-button collapsed text-info fw-bold" type="button" data-bs-toggle="collapse" data-bs-target="#collapseElectronics" aria-expanded="false" aria-controls="collapseElectronics">
                    <i class="fas fa-microchip me-2"></i>3.3 Электроника и предохранители
                </button>
            </h2>
            <div id="collapseElectronics" class="accordion-collapse collapse" aria-labelledby="headingElectronics" data-bs-parent="#f20Accordion">
                <div class="accordion-body">
                    <h6 class="text-primary fw-bold">Предохранители</h6>
                    <p>Низкоамперный предохранитель 80 mA на плате: заменить при перегорании.</p>
                    <h6 class="text-primary fw-bold mt-3">Плата управления</h6>
                    <ul class="ms-3">
                        <li>Осмотреть на конденсат, оплавление дорожек, коррозию.</li>
                        <li>Очистить и высушить; при дефектах — сервисная диагностика.</li>
                    </ul>
                    
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="headingSettings">
                <button class="accordion-button collapsed text-success fw-bold" type="button" data-bs-toggle="collapse" data-bs-target="#collapseSettings" aria-expanded="false" aria-controls="collapseSettings">
                    <i class="fas fa-cog me-2"></i>3.4 Настройки управления
                </button>
            </h2>
            <div id="collapseSettings" class="accordion-collapse collapse" aria-labelledby="headingSettings" data-bs-parent="#f20Accordion">
                <div class="accordion-body">
                    <p>Параметр <strong>d.19</strong> (скорость насоса). При недостаточной циркуляции установить <strong>d.19 = 0</strong> для увеличения оборотов насоса.</p>
                </div>
            </div>
        </div>
    </div>

    <div class="card mb-4 shadow-sm border-warning">
        <div class="card-header bg-warning text-dark">
            <h2 class="h5 mb-0"><i class="fas fa-comments me-2"></i>4. Типичные «форумные» кейсы</h2>
        </div>
        <div class="card-body">
            <ul class="ms-3">
                <li><strong>После простоя:</strong> засохший насос, залипшие сёдла — прокрутить вал вручную.</li>
                <li><strong>«Рандомно» в течение дня:</strong> нестабильное напряжение, плохое заземление — использовать ИБП/стабилизатор.</li>
                <li><strong>В холодное время:</strong> перегрев из-за грязных радиаторов и обмерзших узлов — очистить или заменить радиаторы.</li>
            </ul>
        </div>
    </div>

    <div class="card mb-4 shadow-sm border-success">
        <div class="card-header bg-success text-white">
            <h2 class="h5 mb-0"><i class="fas fa-calendar-check me-2"></i>5. Профилактика</h2>
        </div>
        <div class="card-body">
            <ul class="ms-3">
                <li>Ежегодное ТО: чистка теплообменника, воздухоотводка, насос, замена предохранителей, проверка платы.</li>
                <li>Контроль теплоносителя: замена и промывка системы.</li>
                <li>Защита питания: ИБП/стабилизатор с «чистой синусоидой».</li>
                <li>Регулярный сброс воздуха после пуска и в процессе эксплуатации.</li>
            </ul>
        </div>
    </div>

    <div class="card mb-5 shadow-sm border-danger">
        <div class="card-header bg-danger text-white">
            <h2 class="h5 mb-0"><i class="fas fa-headset me-2"></i>6. Когда обращаться в сервис</h2>
        </div>
        <div class="card-body">
            <ul class="ms-3">
                <li>Неисправны предохранители или плата управления.</li>
                <li>Реальная поломка насоса или термостата.</li>
                <li>Отсутствие необходимого инструмента и опыта.</li>
            </ul>
        </div>
    </div>

    <div class="card text-white shadow" style="background-color: #009688;">
        <div class="card-body text-center">
            <h3 class="card-title h4"><i class="fas fa-phone-alt me-2"></i>Нужна помощь?</h3>
            <p class="lead">Свяжитесь с нами для диагностики и ремонта!</p>
            <div class="row justify-content-center mb-3 g-3">
                <div class="col-md-3"><a href="tel:+79262211348" class="btn btn-light btn-lg w-100 fw-bold"> <i class="fas fa-phone me-2"></i>Позвонить </a></div>
                <div class="col-md-3"><a href="mailto:89262211348@mail.ru" class="btn btn-warning btn-lg w-100 text-dark fw-bold"> <i class="fas fa-envelope me-2"></i>Написать </a></div>
                <div class="col-md-3"><a href="https://service04.ru/contact-us/feedback" class="btn btn-success btn-lg w-100 fw-bold"> <i class="fas fa-file-alt me-2"></i>Заявка </a></div>
            </div>
            <p class="mb-1 small"><img src="/home/whatsapp.svg" alt="WhatsApp" style="width: 24px; height: 24px; vertical-align: middle;">WhatsApp/Telegram: +7 926 221-13-48</p>
            <p class="mb-1 small"><i class="fas fa-globe me-2"></i>Сайт: Service04.ru</p>
            <p class="mb-0 small"><i class="fas fa-envelope me-2"></i>E-mail: 89262211348@mail.ru</p>
        </div>
    </div>
</div>