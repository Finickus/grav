---
title: 'Ошибки котлов Thermex'
---

<div class="container py-5">

    <div class="p-5 mb-5 text-white text-center rounded-3 shadow-sm" style="background-color: #009688;">
        <h1 class="display-5 fw-bold">
            <i class="fas fa-exclamation-triangle me-3"></i>Ошибки котлов Thermex
        </h1>
        <p class="lead">Диагностика и устранение неисправностей</p>
    </div>

    <div class="card shadow-sm border-0 mb-5">
        <div class="card-body p-4">
            <p class="fs-6">Котлы Thermex оснащены системой самодиагностики, которая при возникновении неисправности отображает коды ошибок. Это позволяет быстро определить причину поломки и принять меры для её устранения.</p>
            <div class="alert alert-danger mt-4 shadow-sm d-flex align-items-start" role="alert">
                <i class="fas fa-exclamation-triangle fs-4 me-3 mt-1 text-white"></i>
                <div>
                    <h5 class="alert-heading fw-bold text-white">Предупреждение о безопасности</h5>
                    <p class="mb-0 small text-white">Работы с газовым оборудованием требуют квалификации. При отсутствии опыта или если ошибка сохраняется после выполнения рекомендованных действий, <strong>вызывайте сервисного инженера</strong>.</p>
                </div>
            </div>
        </div>
    </div>

    <div class="accordion" id="errorsAccordion">
        
        <div class="accordion-item">
            <h2 class="accordion-header" id="headingE06">
                <button class="accordion-button fw-bold text-danger" type="button" data-bs-toggle="collapse" data-bs-target="#collapseE06" aria-expanded="true">
                    <i class="fas fa-fire me-2"></i> Ошибка E06/E08: Не происходит розжиг котла
                </button>
            </h2>
            <div id="collapseE06" class="accordion-collapse collapse show" aria-labelledby="headingE06" data-bs-parent="#errorsAccordion">
                <div class="accordion-body bg-danger-subtle">
                    <p class="fw-bold small">Описание: Не идет топливо на блок горелки. Не происходит розжиг котла Thermex.</p>
                    <h5 class="fw-bold mt-4 text-info"><i class="fas fa-list me-2"></i>Возможные причины и устранение:</h5>
                    <div class="row g-3 small">
                        <div class="col-md-6">
                            <ul class="list-unstyled ms-3">
                                <li class="mb-2"><i class="fas fa-lock me-2 text-danger"></i> <strong>Запорный кран перекрыт.</strong> Нужно открыть кран.</li>
                                <li class="mb-2"><i class="fas fa-wind me-2 text-warning"></i> Удалить воздух из трубопровода при первичном запуске.</li>
                                <li class="mb-2"><i class="fas fa-tachometer-alt me-2 text-primary"></i> Проверить уровень давления газа (норма: ~20 Мбар).</li>
                                <li class="mb-2"><i class="fas fa-sliders-h me-2 text-info"></i> Провести наладку котла через сервисное меню (если требуется).</li>
                                <li class="mb-2"><i class="fas fa-magnet me-2 text-danger"></i> <strong>Клапан газа поврежден.</strong> Заменить газовый клапан.</li>
                                <li class="mb-2"><i class="fas fa-bolt me-2 text-warning"></i> <strong>Электрод контроля пламени неисправен.</strong> Очистить, настроить зазор.</li>
                                <li><i class="fas fa-gas-pump me-2 text-primary"></i> <strong>Газовая арматура неработоспособна.</strong> Проверить катушки (обрыв/замыкание), заменить клапан.</li>
                            </ul>
                        </div>
                        <div class="col-md-6">
                            <ul class="list-unstyled ms-3">
                                <li class="mb-2"><i class="fas fa-magnet me-2 text-info"></i> Клапан газа мог залипнуть. Организовать повышенное давление на штуцере.</li>
                                <li class="mb-2"><i class="fas fa-bolt me-2 text-danger"></i> <strong>Не хватает мощности для розжига.</strong> Провести настройку розжига по мощности.</li>
                                <li class="mb-2"><i class="fas fa-microchip me-2 text-warning"></i> <strong>Дефект платы управления.</strong> Провести рестарт. Если ошибка возобновляется, заменить плату.</li>
                                <li class="mb-2"><i class="fas fa-plug me-2 text-primary"></i> Провести проверку заземления.</li>
                                <li class="mb-2"><i class="fas fa-tint me-2 text-info"></i> <strong>Избыток влаги.</strong> Очистить камеру сгорания и электрод ионизации от конденсата.</li>
                                <li><i class="fas fa-bolt me-2 text-danger"></i> <strong>Сбой функций электрода розжига.</strong> Обследовать электропровода.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="headingE07">
                <button class="accordion-button collapsed fw-bold text-warning" type="button" data-bs-toggle="collapse" data-bs-target="#collapseE07">
                    <i class="fas fa-thermometer-full me-2"></i> Ошибка E07: Перегрев котла
                </button>
            </h2>
            <div id="collapseE07" class="accordion-collapse collapse" aria-labelledby="headingE07" data-bs-parent="#errorsAccordion">
                <div class="accordion-body bg-warning-subtle">
                    <p class="fw-bold small">Описание: Произошел перегрев котла Thermex. Температура предохранительного термостата около 105 °C.</p>
                    <h5 class="fw-bold mt-4 text-info"><i class="fas fa-info-circle me-2"></i>Условия срабатывания:</h5>
                    <ul class="list-unstyled ms-3 small">
                        <li class="mb-2"><i class="fas fa-ban me-2 text-danger"></i> Автоматика приостановит действия котла, если в продолжение 10 сек. температура защитного термореле достигнет более <strong>105 °C</strong>.</li>
                        <li><i class="fas fa-thermometer-half me-2 text-danger"></i> Если температура не снизится до 100 °C, электроника покажет ошибку.</li>
                    </ul>
                    <h5 class="fw-bold mt-4 text-info"><i class="fas fa-list me-2"></i>Возможные причины и устранение:</h5>
                    <div class="row g-3 small">
                        <div class="col-md-6">
                            <ul class="list-unstyled ms-3">
                                <li class="mb-2"><i class="fas fa-thermometer-half me-2 text-danger"></i> <strong>Сработал термостат по перегреву.</strong> Переждите, пока прибор остынет, и перезапускайте его.</li>
                                <li class="mb-2"><i class="fas fa-thermometer-empty me-2 text-primary"></i> <strong>Некорректная работа предохранительного термореле.</strong> Замените его.</li>
                                <li class="mb-2"><i class="fas fa-tint me-2 text-info"></i> <strong>Недостаток циркуляции.</strong> Проверить давление (норма: <strong>1.2 бар</strong> в ненагретой системе).</li>
                                <li class="mb-2"><i class="fas fa-wind me-2 text-danger"></i> Присутствие воздуха в трубах. Вывести из системы избыток воздуха.</li>
                                <li><i class="fas fa-door-open me-2 text-warning"></i> <strong>Пропала циркуляция.</strong> Открыть все запорные элементы.</li>
                            </ul>
                        </div>
                        <div class="col-md-6">
                            <ul class="list-unstyled ms-3">
                                <li class="mb-2"><i class="fas fa-tachometer-alt me-2 text-primary"></i> <strong>Нарушена работа циркуляционного насоса.</strong> Проверить вольтаж электросети и обороты насоса.</li>
                                <li class="mb-2"><i class="fas fa-tachometer-alt me-2 text-danger"></i> Крыльчатка насоса имеет поломку. Если определяется повреждение, <strong>насос требуется заменить</strong>.</li>
                                <li class="mb-2"><i class="fas fa-sync me-2 text-warning"></i> Насос заклинило. Прокрутить вал ротора электродвигателя.</li>
                                <li><i class="fas fa-microchip me-2 text-info"></i> <strong>Неполадки с управляющей платой.</strong> Когда проблема возвращается, замените электронную плату.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="headingE04">
                <button class="accordion-button collapsed fw-bold text-info" type="button" data-bs-toggle="collapse" data-bs-target="#collapseE04">
                    <i class="fas fa-shower me-2"></i> Ошибка E04: Неисправность датчика NTC ГВС
                </button>
            </h2>
            <div id="collapseE04" class="accordion-collapse collapse" aria-labelledby="headingE04" data-bs-parent="#errorsAccordion">
                <div class="accordion-body bg-info-subtle">
                    <p class="fw-bold small">Описание: Неполадка датчика NTC ГВС.</p>
                    <p class="fw-bold">Причины:</p>
                    <p class="small">Во время присутствия разрыва или замыкания электроцепи датчика температуры ГВС в промежутке пять секунд, газовая горелка не начнет работать в режиме ГВС.</p>
                    <p class="fw-bold text-danger">Решение: Датчик NTC линии ГВС неисправен. <strong>Требуется его замена.</strong></p>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="headingE05">
                <button class="accordion-button collapsed fw-bold text-success" type="button" data-bs-toggle="collapse" data-bs-target="#collapseE05">
                    <i class="fas fa-thermometer-empty me-2"></i> Ошибка E05: Неисправность температурного датчика отопления
                </button>
            </h2>
            <div id="collapseE05" class="accordion-collapse collapse" aria-labelledby="headingE05" data-bs-parent="#errorsAccordion">
                <div class="accordion-body bg-success-subtle">
                    <p class="fw-bold small">Описание: Температурный датчик отопительного контура вышел из строя.</p>
                    <p class="small">Возникает повреждение цепи или короткое замыкание датчика NTC отопительного контура. Когда нарушена электрическая цепь датчика, сигнал не поступает, и плата управления отключает газогорелочный механизм.</p>
                    <p class="fw-bold text-danger">Решение: <strong>Требуется замена температурного датчика отопительного контура.</strong></p>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="headingE02">
                <button class="accordion-button collapsed fw-bold text-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseE02">
                    <i class="fas fa-tint me-2"></i> Ошибка E02/E9: Слабое давление в системе
                </button>
            </h2>
            <div id="collapseE02" class="accordion-collapse collapse" aria-labelledby="headingE02" data-bs-parent="#errorsAccordion">
                <div class="accordion-body bg-primary-subtle">
                    <p class="fw-bold small">Описание: Говорит о том, что в системе слабое давление.</p>
                    <h5 class="fw-bold mt-4 text-info"><i class="fas fa-list me-2"></i>Возможные причины:</h5>
                    <ul class="list-unstyled ms-3 small">
                        <li class="mb-2"><i class="fas fa-arrow-down me-2 text-danger"></i> Понижение давления жидкости в системе.</li>
                        <li class="mb-2"><i class="fas fa-plug me-2 text-warning"></i> Нарушение контакта с реле минимального давления.</li>
                        <li><i class="fas fa-thermometer-half me-2 text-primary"></i> Неисправность реле минимального давления.</li>
                    </ul>
                    <h5 class="fw-bold mt-4 text-info"><i class="fas fa-wrench me-2"></i>Решение:</h5>
                    <ul class="list-unstyled ms-3 small">
                        <li class="mb-2"><i class="fas fa-eye me-2 text-success"></i> Проконтролировать показатели манометра.</li>
                        <li class="mb-2"><i class="fas fa-tint me-2 text-info"></i> Сбой устраняется с применением подпиточного крана.</li>
                        <li><i class="fas fa-tint-slash me-2 text-danger"></i> Если сбой возникает снова, <strong>искать утечку жидкости</strong> (теплообменник, насос, уплотнения).</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="headingE13">
                <button class="accordion-button collapsed fw-bold text-secondary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseE13">
                    <i class="fas fa-wind me-2"></i> Ошибка E13/E14: Недостаток тяги
                </button>
            </h2>
            <div id="collapseE13" class="accordion-collapse collapse" aria-labelledby="headingE13" data-bs-parent="#errorsAccordion">
                <div class="accordion-body bg-secondary-subtle">
                    <p class="small">Описание: Для стабильной и безопасной работы прибора необходимо создать тягу для вывода дымовых газов. Срабатывает датчик по тяге, и агрегат останавливает работу.</p>
                    <h5 class="fw-bold mt-4 text-info"><i class="fas fa-list me-2"></i>Главные факторы, при которых возникает отсутствие тяги:</h5>
                    <ul class="list-unstyled ms-3 small">
                        <li class="mb-2"><i class="fas fa-ruler-horizontal me-2 text-danger"></i> <strong>Недостаточный размер дымоотводящего канала</strong> (засорение, обледенение).</li>
                        <li class="mb-2"><i class="fas fa-arrows-alt-h me-2 text-primary"></i> Дымоходная труба <strong>слишком длинная</strong> или <strong>горизонтальный участок</strong> слишком большой.</li>
                        <li class="mb-2"><i class="fas fa-thermometer-half me-2 text-danger"></i> <strong>Прессостат-датчик тяги поврежден.</strong></li>
                        <li><i class="fas fa-plug me-2 text-warning"></i> Отсутствует контакт платы управления с пневмореле-датчиком тяги.</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="headingE15">
                <button class="accordion-button collapsed fw-bold text-dark" type="button" data-bs-toggle="collapse" data-bs-target="#collapseE15">
                    <i class="fas fa-fan me-2"></i> Ошибка E15: Неисправность вентилятора
                </button>
            </h2>
            <div id="collapseE15" class="accordion-collapse collapse" aria-labelledby="headingE15" data-bs-parent="#errorsAccordion">
                <div class="accordion-body bg-dark-subtle">
                    <p class="fw-bold small">Описание: Вентилятор имеет неисправность.</p>
                    <h5 class="fw-bold mt-4 text-info"><i class="fas fa-list me-2"></i>Возможные причины:</h5>
                    <ul class="list-unstyled ms-3 small">
                        <li class="mb-2"><i class="fas fa-broom me-2 text-danger"></i> Произошло <strong>засорение крыльчатки</strong> вентилятора.</li>
                        <li class="mb-2"><i class="fas fa-oil-can me-2 text-warning"></i> Отсутствие достаточной смазки вала вентилятора.</li>
                        <li><i class="fas fa-plug me-2 text-primary"></i> Нарушен контакт между вентилятором и электронной платой.</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="headingE41">
                <button class="accordion-button collapsed fw-bold text-warning" type="button" data-bs-toggle="collapse" data-bs-target="#collapseE41">
                    <i class="fas fa-fire-alt me-2"></i> Ошибка E41: Некорректный розжиг
                </button>
            </h2>
            <div id="collapseE41" class="accordion-collapse collapse" aria-labelledby="headingE41" data-bs-parent="#errorsAccordion">
                <div class="accordion-body bg-warning-subtle">
                    <p class="fw-bold small">Описание: Некорректный розжиг. Код может возникнуть, когда розжиг не действует или же происходит затухание пламени горелки.</p>
                    <h5 class="fw-bold mt-4 text-info"><i class="fas fa-wrench me-2"></i>Решение:</h5>
                    <ul class="list-unstyled ms-3 small">
                        <li class="mb-2"><i class="fas fa-search me-2 text-primary"></i> Осмотреть соединения между устройством розжига, электродом пламени, платой и газовым клапаном.</li>
                        <li><i class="fas fa-wind me-2 text-warning"></i> Основным фактором срыва пламени является <strong>неудовлетворительная тяга</strong> (проверить дымоход).</li>
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