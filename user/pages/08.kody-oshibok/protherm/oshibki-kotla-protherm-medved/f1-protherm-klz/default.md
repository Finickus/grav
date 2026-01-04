---
title: 'F1 Protherm KLZ'
---

<div class="container py-5">

    <div class="p-5 mb-5 text-white text-center rounded-3 shadow-sm bg-danger">
        <h1 class="display-5 fw-bold">
            <i class="fas fa-exclamation-triangle me-3"></i>Ошибка F1 на Protherm KLZ
        </h1>
        <p class="lead">Полное руководство по диагностике и устранению</p>
    </div>

    <div class="card mb-5 shadow-sm border-0">
        <div class="card-body p-4">
            <div class="row align-items-center g-4">
                <div class="col-lg-8">
                    <p class="lead fs-6 mb-0">Код <strong>F1</strong> означает <strong>потерю пламени</strong>: при открытом газовом клапане плата не получает сигнал от ионизационного электрода, автоматика блокирует розжиг и закрывает газовый клапан. Ошибку также провоцируют элементы безопасности (аварийный термостат), низкое давление газа, неправильная фаза/ноль и проблемы с тягой.</p>
                </div>
                <div class="col-lg-4 text-center">
                    <img src="/kody-oshibok/protherm/oshibki-kotla-protherm-medved/f1-protherm-klz/Screenshot_179.jpg" class="img-fluid rounded shadow-sm" alt="Котёл Protherm" style="max-width: 250px;">
                </div>
            </div>
        </div>
    </div>

    <div class="card mb-5 shadow-sm border-primary">
        <div class="card-header bg-primary text-white">
            <h2 class="h5 mb-0"><i class="fas fa-list-check me-2"></i>Быстрый чек-лист перед диагностикой</h2>
        </div>
        <div class="card-body">
            <div class="content">
                <ul class="list-unstyled ms-3">
                    <li class="mb-2"><i class="fas fa-check-circle me-2 text-success"></i>Сбросить ошибку кнопкой <strong>Reset</strong> и убедиться, что давление воды в котле <strong>1–2 бар</strong>.</li>
                    <li class="mb-2"><i class="fas fa-check-circle me-2 text-success"></i>Проверить подачу газа и что <strong>кран открыт</strong>; при сомнении — вызвать поставщика газа.</li>
                    <li class="mb-2"><i class="fas fa-check-circle me-2 text-success"></i>Отключить/включить питание, исключить «глюк» сети; при повторе — использовать <strong>стабилизатор/ИБП</strong>.</li>
                    <li><i class="fas fa-check-circle me-2 text-success"></i>Убедиться, что <strong>фаза и ноль</strong> подключены правильно, есть корректное <strong>заземление</strong>.</li>
                </ul>
                <div class="alert alert-warning mt-3 small"><i class="fas fa-info-circle me-2"></i>Если ошибка возвращается, следуйте сценариям диагностики ниже — от простых к более глубоким проверкам.</div>
            </div>
        </div>
    </div>

    <h2 class="h3 text-danger mb-4"><i class="fas fa-wrench me-2"></i>Сценарии диагностики и устранения</h2>
    
    <div class="accordion" id="scenariosAccordion">
        
        <div class="accordion-item">
            <h2 class="accordion-header" id="headingScenarioA">
                <button class="accordion-button fw-bold text-danger" type="button" data-bs-toggle="collapse" data-bs-target="#collapseScenarioA" aria-expanded="true">
                    <i class="fas fa-wind me-2"></i>Сценарий А: Нестабильная тяга/дымоход
                </button>
            </h2>
            <div id="collapseScenarioA" class="accordion-collapse collapse show" aria-labelledby="headingScenarioA" data-bs-parent="#scenariosAccordion">
                <div class="accordion-body bg-light">
                    <h6 class="text-primary fw-bold">Симптомы:</h6>
                    <p class="small">F1 чаще при переключении на ГВС, при сильной погодной нагрузке (ветер, иней), после нескольких циклов розжига.</p>
                    <h6 class="text-primary fw-bold mt-3">Что проверить:</h6>
                    <p class="small"><strong>Дымоход/коаксиал:</strong> засор (мусор, гнёзда), обмерзание, сужения, обратные уклоны. <strong>Воздуховод:</strong> смина/деформация гофры, неплотности.</p>
                    <h6 class="text-success fw-bold mt-3">Как устранить:</h6>
                    <p class="small">Очистить дымоход, восстановить геометрию, проверить датчик тяги. При надставке «полу-турбо» — применить правильные реле.</p>
                    <div class="alert alert-info mt-3 small mb-0"><strong>Контроль:</strong> запустить 3–5 циклов в отоплении и ГВС; если проблема исчезла — причина в тяге/надставке.</div>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="headingScenarioB">
                <button class="accordion-button collapsed fw-bold text-warning" type="button" data-bs-toggle="collapse" data-bs-target="#collapseScenarioB">
                    <i class="fas fa-fire me-2"></i>Сценарий B: Газ, давление, фильтры, настройки минимума
                </button>
            </h2>
            <div id="collapseScenarioB" class="accordion-collapse collapse" aria-labelledby="headingScenarioB" data-bs-parent="#scenariosAccordion">
                <div class="accordion-body bg-light">
                    <h6 class="text-primary fw-bold">Симптомы:</h6>
                    <p class="small">Пламя загорается и гаснет, F1 после 1–3 циклов; иногда F1 «рандомно» в течение суток.</p>
                    <h6 class="text-primary fw-bold mt-3">Пошаговая проверка:</h6>
                    <ol class="ms-3 small">
                        <li><strong>Давление газа на входе:</strong> измерить микроманометром при статике и работе (менее <strong>8 мм вод. ст.</strong> может давать потерю пламени).</li>
                        <li><strong>Сетчатые фильтры:</strong> снять, промыть, заменить при загрязнении.</li>
                        <li><strong>Регулировка мин. давления:</strong> слишком низкий стартовый газ вызывает «срыв» пламени. Корректировать только специалистом.</li>
                        <li><strong>Газовый клапан:</strong> проверить катушки, стабильность открытия.</li>
                    </ol>
                    <div class="alert alert-info mt-3 small mb-0"><strong>Контроль:</strong> 5–10 циклов работы в обоих режимах.</div>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="headingScenarioC">
                <button class="accordion-button collapsed fw-bold text-info" type="button" data-bs-toggle="collapse" data-bs-target="#collapseScenarioC">
                    <i class="fas fa-bolt me-2"></i>Сценарий C: Система розжига и контроль пламени
                </button>
            </h2>
            <div id="collapseScenarioC" class="accordion-collapse collapse" aria-labelledby="headingScenarioC" data-bs-parent="#scenariosAccordion">
                <div class="accordion-body bg-light">
                    <h6 class="text-primary fw-bold">Симптомы:</h6>
                    <p class="small">Искра слабая/прерывистая, следы подгорания на электроде, после чистки ошибка возвращается.</p>
                    <h6 class="text-primary fw-bold mt-3">Пошагово:</h6>
                    <ol class="ms-3 small">
                        <li><strong>Ионизационный электрод:</strong> очистить нагар, проверить позицию относительно горелки, проверить контактный провод (без подсосов к массе).</li>
                        <li><strong>Зазор розжига:</strong> корректный промежуток между электродом и горелкой критичен.</li>
                        <li><strong>Трансформатор розжига:</strong> при старении падает напряжение, искра «не держит» смесь — проверка и замена.</li>
                    </ol>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="headingScenarioD">
                <button class="accordion-button collapsed fw-bold text-success" type="button" data-bs-toggle="collapse" data-bs-target="#collapseScenarioD">
                    <i class="fas fa-plug me-2"></i>Сценарий D: Питание, фаза/ноль, заземление
                </button>
            </h2>
            <div id="collapseScenarioD" class="accordion-collapse collapse" aria-labelledby="headingScenarioD" data-bs-parent="#scenariosAccordion">
                <div class="accordion-body bg-light">
                    <h6 class="text-primary fw-bold">Симптомы:</h6>
                    <p class="small">Ошибка исчезает после перезапуска, появляется в «грязной» сети; отказ устойчивее вечером/при нагрузках сети.</p>
                    <h6 class="text-success fw-bold mt-3">Проверка и устранение:</h6>
                    <ul class="ms-3 small">
                        <li>Проверить правильность <strong>фазы/нуля</strong> на клеммах котла; поменять местами при ошибке.</li>
                        <li>Обеспечить <strong>заземление</strong> с низким сопротивлением.</li>
                        <li>Использовать <strong>ИБП/стабилизатор</strong>, совместимый с газовыми котлами (чистая синусоида).</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="headingScenarioE">
                <button class="accordion-button collapsed fw-bold text-secondary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseScenarioE">
                    <i class="fas fa-shield-alt me-2"></i>Сценарий E: Элементы безопасности и перегрев
                </button>
            </h2>
            <div id="collapseScenarioE" class="accordion-collapse collapse" aria-labelledby="headingScenarioE" data-bs-parent="#scenariosAccordion">
                <div class="accordion-body bg-light">
                    <h6 class="text-primary fw-bold">Симптомы:</h6>
                    <p class="small">«Выбивает» при интенсивной работе (ГВС), котёл успевает нагреться, после остывания — пускается.</p>
                    <h6 class="text-primary fw-bold mt-3">Что делать:</h6>
                    <ol class="ms-3 small">
                        <li>Проверить <strong>аварийный термостат</strong> и <strong>термостат дымовых газов</strong> (SKKT).</li>
                        <li><strong>Гидравлика:</strong> проверить <strong>циркуляционные насосы</strong>, удалить <strong>воздух</strong>, очистить <strong>фильтры</strong>.</li>
                        <li><strong>Трёхходовой клапан:</strong> залипание/неполный ход может вызывать перегрев при пусках ГВС.</li>
                    </ol>
                </div>
            </div>
        </div>

    </div>

    <div class="card mb-5 shadow-sm border-info">
        <div class="card-header bg-info text-white">
            <h4 class="card-header-title h5 mb-0"><i class="fas fa-tasks me-2"></i>Пошаговый алгоритм диагностики «от простого к сложному»</h4>
        </div>
        <div class="card-body">
            <ol class="ms-3">
                <li class="mb-3">
                    <span class="fw-bold">Безопасность и базовые условия</span>
                    <ul class="list-unstyled ms-4 small">
                        <li>Давление воды 1–2 бар; сброс Reset.</li>
                        <li>Подача газа открыта, проверка на утечки.</li>
                        <li>Визуальный осмотр, чистка камеры и горелки.</li>
                    </ul>
                </li>
                <li class="mb-3">
                    <span class="fw-bold">Электрика и питание</span>
                    <ul class="list-unstyled ms-4 small">
                        <li>Фаза/ноль, заземление, клеммы.</li>
                        <li>Сеть/ИБП: тест без ИБП, с ИБП «чистая синусоида».</li>
                    </ul>
                </li>
                <li class="mb-3">
                    <span class="fw-bold">Дымоход и приток воздуха</span>
                    <ul class="list-unstyled ms-4 small">
                        <li>Осмотр/прочистка; проверка датчика тяги.</li>
                    </ul>
                </li>
                <li class="mb-3">
                    <span class="fw-bold">Газовая часть</span>
                    <ul class="list-unstyled ms-4 small">
                        <li>Давление до и на котле (стат./динамика), сетчатые фильтры.</li>
                        <li>Минимальное/максимальное давление на клапане — по паспорту.</li>
                    </ul>
                </li>
                <li class="mb-3">
                    <span class="fw-bold">Розжиг и ионизация</span>
                    <ul class="list-unstyled ms-4 small">
                        <li>Чистка/позиция электрода, кабель, зазор; оценка искры.</li>
                        <li>Трансформатор розжига — замена при слабом HV.</li>
                    </ul>
                </li>
                <li class="mb-3">
                    <span class="fw-bold">Гидравлика и защита</span>
                    <ul class="list-unstyled ms-4 small">
                        <li>Насосы, воздушные пробки, фильтры, трёхходовой; аварийные/дымо-термостаты.</li>
                    </ul>
                </li>
            </ol>
            <div class="alert alert-success"><i class="fas fa-info-circle me-2"></i>После каждого шага сделать 3–5 запусков в отоплении и ГВС и зафиксировать результат.</div>
        </div>
    </div>

    <div class="card mb-5 shadow-sm border-danger">
        <div class="card-body">
            <h4 class="card-title h4 text-danger"><i class="fas fa-lightbulb me-2"></i>Быстрый итог</h4>
            <p>F1 — это не «одна причина», а узел из четырёх групп факторов: <strong>тяга/воздух</strong>, <strong>газ/давление/клапан</strong>, <strong>розжиг/ионизация</strong>, <strong>питание/фаза/защиты</strong>. Идите по алгоритму, фиксируйте изменения после каждого шага, и вы быстро сузите круг до конкретной неисправности.</p>
        </div>
    </div>

    <div class="p-5 rounded-3 text-center text-white shadow-lg" style="background-color: #009688;">
        <h3 class="h4 mb-3"><i class="fas fa-phone-alt me-2"></i>Нужна профессиональная помощь?</h3>
        <p class="lead mb-4">Свяжитесь с нами для диагностики и ремонта котлов Protherm!</p>
        <div class="row justify-content-center g-3">
            <div class="col-12 col-md-4">
                <a href="tel:+79262211348" class="btn btn-light btn-lg w-100 fw-bold">
                    <i class="fas fa-phone me-2"></i> <span>Позвонить</span>
                </a>
            </div>
            <div class="col-12 col-md-4">
                <a href="https://service04.ru/contact-us/feedback" class="btn btn-warning btn-lg w-100 fw-bold text-dark">
                    <i class="fas fa-envelope me-2"></i> <span>Заявка</span>
                </a>
            </div>
        </div>
    </div>

</div>