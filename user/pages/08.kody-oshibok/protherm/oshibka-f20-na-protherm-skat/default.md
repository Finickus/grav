---
title: Ошибка F20 на Protherm Skat
metadata:
  description: Ошибка F20 на Protherm Skat Полное руководство для мастеров по устранению
    перегрева Код F20 сигнализирует о срабатывании аварийного термостата из-за...
  og:type: article
  og:title: Ошибка F20 на Protherm Skat - Service04
  og:description: Ошибка F20 на Protherm Skat Полное руководство для мастеров по устранению
    перегрева Код F20 сигнализирует о срабатывании аварийного термостата из-за...
  og:url: https://service04.ru/kody-oshibok/protherm/oshibka-f20-na-protherm-skat
  og:site_name: Service04
  og:locale: ru_RU
  og:image: https://service04.ru/kody-oshibok/protherm/oshibka-f20-na-protherm-skat/Screenshot_183(1).jpg
  og:image:width: '1200'
  og:image:height: '630'
  canonical: https://service04.ru/kody-oshibok/protherm/oshibka-f20-na-protherm-skat
  robots: index, follow
  yandex-verification: ''
  geo.region: RU-MOW
  geo.placename: Москва
  author: Service04
---
<div class="container my-5">
    <div class="p-5 mb-4 bg-danger text-white text-center rounded-3 shadow">
        <h1 class="display-5 fw-bold"><i class="fas fa-exclamation-triangle me-3"></i>Ошибка F20 на Protherm Skat</h1>
        <p class="lead">Полное руководство для мастеров по устранению перегрева</p>
    </div>

    <div class="card mb-4 shadow-sm border-0">
        <div class="card-body p-4">
            <p class="lead mb-0">
                Код <strong>F20</strong> сигнализирует о срабатывании аварийного термостата из-за перегрева теплообменника. Это происходит при достижении температуры выше 95-100°C, что вызвано отсутствием циркуляции или завоздушиванием системы.
            </p>
        </div>
    </div>

    <div class="row g-4 mb-4">
        <div class="col-md-6">
            <div class="card h-100 shadow-sm border-primary">
                <div class="card-header bg-primary text-white py-3">
                    <h2 class="h5 mb-0"><i class="fas fa-info-circle me-2"></i>1. Что это значит?</h2>
                </div>
                <div class="card-body">
                    <p>Аварийный термостат размыкает цепь безопасности, отключая питание ТЭНов. Котел блокируется. <strong>Важно:</strong> ошибка не исчезнет сама после остывания, требуется физический сброс кнопки.</p>
                </div>
            </div>
        </div>

        <div class="col-md-6">
            <div class="card h-100 shadow-sm border-warning">
                <div class="card-header bg-warning text-dark py-3">
                    <h2 class="h5 mb-0"><i class="fas fa-thermometer-three-quarters me-2"></i>2. Ручной сброс</h2>
                </div>
                <div class="card-body">
                    <p class="small fw-bold">Порядок действий:</p>
                    <ol class="small">
                        <li>Полностью обесточьте котел.</li>
                        <li>Найдите датчик на медной трубке (выход теплообменника).</li>
                        <li>Нажмите красную кнопку под резиновым колпачком до щелчка.</li>
                    </ol>
                    <img src="/kody-oshibok/protherm/oshibka-f20-na-protherm-skat/Screenshot_183(1).jpg" class="img-fluid rounded mt-2" alt="Сброс кнопки">
                </div>
            </div>
        </div>
    </div>

    <h2 class="h3 text-danger mb-4"><i class="fas fa-tools me-2"></i>3. Алгоритм диагностики</h2>
    
    <div class="accordion shadow-sm mb-5" id="f20AccordionBS5">
        <div class="accordion-item">
            <h2 class="accordion-header" id="headingOne">
                <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne">
                    <i class="fas fa-water me-2 text-primary"></i> 3.1 Проверка циркуляции и воздуха
                </button>
            </h2>
            <div id="collapseOne" class="accordion-collapse collapse show" data-bs-parent="#f20AccordionBS5">
                <div class="accordion-body">
                    <div class="row align-items-center">
                        <div class="col-sm-8">
                            <h6>Воздух в системе:</h6>
                            <ul class="small">
                                <li>Стравите воздух через автоматический воздухоотводчик на насосе.</li>
                                <li>Проверьте радиаторы и "майевские".</li>
                                <li><strong>Насос:</strong> Проверьте, не заклинило ли вал (прокрутите отверткой через центральную пробку).</li>
                            </ul>
                        </div>
                        <div class="col-sm-4 text-center">
                            <img src="/kody-oshibok/protherm/oshibka-f20-na-protherm-skat/Screenshot_191(1).jpg" class="img-thumbnail" alt="Воздух">
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="headingTwo">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo">
                    <i class="fas fa-microchip me-2 text-info"></i> 3.2 Предохранители и плата
                </button>
            </h2>
            <div id="collapseTwo" class="accordion-collapse collapse" data-bs-parent="#f20AccordionBS5">
                <div class="accordion-body">
                    <p class="small">Если насос не запускается при подаче команды, проверьте плавкий предохранитель на плате управления (обычно 80mA). Осмотрите дорожки платы на наличие следов подгара в зоне реле насоса.</p>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="headingThree">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree">
                    <i class="fas fa-cog me-2 text-success"></i> 3.3 Сервисный параметр d.19
                </button>
            </h2>
            <div id="collapseThree" class="accordion-collapse collapse" data-bs-parent="#f20AccordionBS5">
                <div class="accordion-body">
                    <p class="small">Зайдите в сервисное меню и проверьте параметр <strong>d.19</strong>. Установите значение <strong>0</strong> или <strong>2</strong> для обеспечения постоянной или автоматической скорости насоса на максимуме при нагреве.</p>
                </div>
            </div>
        </div>
    </div>

    <div class="card bg-primary text-white shadow-lg border-0 mb-5">
        <div class="card-body p-5 text-center">
            <h3 class="fw-bold mb-3">Нужна профессиональная диагностика?</h3>
            <p class="lead mb-4">Наши инженеры специализируются на котлах Protherm. Устраним ошибку F20 за один визит!</p>
            <div class="row g-3 justify-content-center">
                <div class="col-auto">
                    <a href="tel:+79262211348" class="btn btn-light btn-lg px-4 fw-bold shadow">
                        <i class="fas fa-phone me-2"></i>Позвонить
                    </a>
                </div>
                <div class="col-auto">
                    <a href="https://service04.ru/contact-us/feedback" class="btn btn-warning btn-lg px-4 fw-bold shadow text-dark">
                        <i class="fas fa-envelope me-2"></i>Заявка мастеру
                    </a>
                </div>
            </div>
            <div class="mt-4 small opacity-75">
                <img src="/home/whatsapp.svg" alt="WhatsApp" style="width: 24px; height: 24px; vertical-align: middle;"> WhatsApp: +7 (926) 221-13-48 | <i class="fas fa-globe ms-3 me-1"></i> Service04.ru
            </div>
        </div>
    </div>
</div>

