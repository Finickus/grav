---
title: 'Ошибки котлов Sime'
---

<div class="container py-5">

    <div class="p-5 mb-5 text-white text-center rounded-3 shadow-sm" style="background-color: #009688;">
        <h1 class="display-5 fw-bold">
            <i class="fas fa-exclamation-triangle me-3"></i>Ошибки котлов Sime
        </h1>
        <p class="lead">Диагностика и устранение неисправностей</p>
    </div>

    <div class="card shadow-sm border-0 mb-5">
        <div class="card-body p-4">
            <p class="fs-6">Котлы Sime оснащены системой самодиагностики, которая при возникновении неисправности отображает коды ошибок. Это позволяет быстро определить причину поломки и принять меры для её устранения.</p>
            <div class="alert alert-warning mt-4 shadow-sm d-flex align-items-start" role="alert">
                <i class="fas fa-exclamation-triangle fs-4 me-3 mt-1 text-dark"></i>
                <div>
                    <h5 class="alert-heading fw-bold text-dark">Предупреждение о безопасности</h5>
                    <p class="mb-0 small text-dark">Работы с газовым оборудованием требуют квалификации. При отсутствии опыта или если ошибка сохраняется после выполнения рекомендованных действий, <strong>вызывайте сервисного инженера</strong>.</p>
                </div>
            </div>
        </div>
    </div>

    <div class="accordion" id="errorsAccordion">
        
        <div class="accordion-item">
            <h2 class="accordion-header" id="headingAL01">
                <button class="accordion-button fw-bold text-danger" type="button" data-bs-toggle="collapse" data-bs-target="#collapseAL01" aria-expanded="true">
                    <i class="fas fa-wind me-2"></i> Ошибка AL 01: Неудовлетворительная тяга
                </button>
            </h2>
            <div id="collapseAL01" class="accordion-collapse collapse show" aria-labelledby="headingAL01" data-bs-parent="#errorsAccordion">
                <div class="accordion-body bg-danger-subtle">
                    <p class="fw-bold small">Описание: Срабатывает датчик тяги, и котел прекращает работу из-за проблем с отводом продуктов сгорания.</p>
                    <h6 class="fw-bold mt-4 text-info"><i class="fas fa-list me-2"></i>Вероятные источники отсутствия тяги:</h6>
                    <div class="row g-3 small">
                        <div class="col-md-6">
                            <ul class="list-unstyled ms-3">
                                <li class="mb-2"><i class="fas fa-ruler-horizontal me-2 text-primary"></i> Недостаточный размер дымоотводящего канала (загрязнение, обледенение).</li>
                                <li class="mb-2"><i class="fas fa-arrows-alt-h me-2 text-danger"></i> Длина трубы дымохода превышена или горизонтальный отрезок слишком длинный.</li>
                                <li><i class="fas fa-thermometer-half me-2 text-success"></i> <strong>Прессостат-датчик тяги сломан.</strong> (Слышен характерный щелчок при образовании разряжения).</li>
                            </ul>
                        </div>
                        <div class="col-md-6">
                            <ul class="list-unstyled ms-3">
                                <li class="mb-2"><i class="fas fa-plug me-2 text-warning"></i> Нет контакта между датчиком-реле тяги и платой.</li>
                                <li class="mb-2"><i class="fas fa-fan me-2 text-danger"></i> <strong>Проблемы при работе вентилятора</strong> (засор крыльчатки, отсутствие смазки).</li>
                                <li><i class="fas fa-plug me-2 text-danger"></i> Нарушен контакт между вентилятором и платой.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="headingAL02">
                <button class="accordion-button collapsed fw-bold text-warning" type="button" data-bs-toggle="collapse" data-bs-target="#collapseAL02">
                    <i class="fas fa-tint me-2"></i> Ошибка AL 02: Низкое давление в системе
                </button>
            </h2>
            <div id="collapseAL02" class="accordion-collapse collapse" aria-labelledby="headingAL02" data-bs-parent="#errorsAccordion">
                <div class="accordion-body bg-warning-subtle">
                    <p class="fw-bold small">Описание: Уровень давления системы низкий.</p>
                    <h5 class="fw-bold mt-4 text-info"><i class="fas fa-list me-2"></i>Основные факторы:</h5>
                    <ul class="list-unstyled ms-3 small">
                        <li class="mb-2"><i class="fas fa-arrow-down me-2 text-primary"></i> <strong>Понижение давления воды</strong> в отопительной системе.</li>
                        <li class="mb-2"><i class="fas fa-plug me-2 text-warning"></i> Нет контакта между платой и реле минимального давления.</li>
                        <li><i class="fas fa-thermometer-half me-2 text-danger"></i> Неисправность реле минимального давления.</li>
                    </ul>
                    <h5 class="fw-bold mt-4 text-success"><i class="fas fa-wrench me-2"></i>Решение:</h5>
                    <ul class="list-unstyled ms-3 small">
                        <li class="mb-2"><i class="fas fa-eye me-2 text-info"></i> Проконтролируйте показания манометра.</li>
                        <li class="mb-2"><i class="fas fa-tint me-2 text-primary"></i> <strong>Устраните сбой при помощи подпитывающего крана.</strong></li>
                        <li><i class="fas fa-tint-slash me-2 text-danger"></i> Если сбой возникает снова, <strong>ищите протечку воды</strong> (теплообменник, насос, прокладки, кран подпитки).</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="headingAL04">
                <button class="accordion-button collapsed fw-bold text-info" type="button" data-bs-toggle="collapse" data-bs-target="#collapseAL04">
                    <i class="fas fa-shower me-2"></i> Ошибка AL 04: Неисправность термодатчика ГВС
                </button>
            </h2>
            <div id="collapseAL04" class="accordion-collapse collapse" aria-labelledby="headingAL04" data-bs-parent="#errorsAccordion">
                <div class="accordion-body bg-info-subtle">
                    <p class="fw-bold small">Описание: Терморезистор контура ГВС поврежден (обрыв или замыкание). Горелка не будет работать на приготовление горячей воды.</p>
                    <p class="fw-bold text-danger">Решение: <strong>Требуется замена терморезистора контура ГВС.</strong></p>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="headingAL05">
                <button class="accordion-button collapsed fw-bold text-success" type="button" data-bs-toggle="collapse" data-bs-target="#collapseAL05">
                    <i class="fas fa-thermometer-empty me-2"></i> Ошибка AL 05: Неисправность температурного датчика отопления
                </button>
            </h2>
            <div id="collapseAL05" class="accordion-collapse collapse" aria-labelledby="headingAL05" data-bs-parent="#errorsAccordion">
                <div class="accordion-body bg-success-subtle">
                    <p class="fw-bold small">Описание: Возникает разрыв или короткое замыкание датчика NTC контура отопления. Управляющая плата приостанавливает работу горелочного механизма.</p>
                    <p class="fw-bold text-danger">Решение: <strong>Требуется замена температурного датчика отопительного контура.</strong></p>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="headingAL06">
                <button class="accordion-button collapsed fw-bold text-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseAL06">
                    <i class="fas fa-fire me-2"></i> Ошибка AL 06: Отсутствие розжига
                </button>
            </h2>
            <div id="collapseAL06" class="accordion-collapse collapse" aria-labelledby="headingAL06" data-bs-parent="#errorsAccordion">
                <div class="accordion-body bg-primary-subtle">
                    <p class="fw-bold small">Описание: Отсутствие розжига котла Sime. Не поступает газовая смесь в горелочный узел.</p>
                    <h5 class="fw-bold mt-4 text-info"><i class="fas fa-list me-2"></i>Возможные причины:</h5>
                    <div class="row g-3 small">
                        <div class="col-md-6">
                            <ul class="list-unstyled ms-3">
                                <li class="mb-2"><i class="fas fa-lock me-2 text-danger"></i> <strong>Закрыт запорный вентиль</strong> (открыть).</li>
                                <li class="mb-2"><i class="fas fa-wind me-2 text-warning"></i> Воздух в трубопроводе при первичном запуске (удалить).</li>
                                <li class="mb-2"><i class="fas fa-tachometer-alt me-2 text-primary"></i> Низкий показатель давления газового топлива (~20 мбар).</li>
                                <li class="mb-2"><i class="fas fa-magnet me-2 text-info"></i> <strong>Клапан газа поврежден или залипает</strong> (заменить).</li>
                                <li><i class="fas fa-bolt me-2 text-danger"></i> <strong>Электрод контроля пламени неисправен</strong> (очистить, настроить зазор).</li>
                            </ul>
                        </div>
                        <div class="col-md-6">
                            <ul class="list-unstyled ms-3">
                                <li class="mb-2"><i class="fas fa-bolt me-2 text-info"></i> <strong>Неполная мощность розжига</strong> (настроить).</li>
                                <li class="mb-2"><i class="fas fa-microchip me-2 text-danger"></i> <strong>Выход из строя управляющей платы.</strong> (Поменять).</li>
                                <li class="mb-2"><i class="fas fa-bolt me-2 text-warning"></i> Не функционирует разжигающий трансформатор.</li>
                                <li class="mb-2"><i class="fas fa-plug me-2 text-primary"></i> <strong>Проверить заземление.</strong></li>
                                <li><i class="fas fa-tint me-2 text-info"></i> <strong>Избыток конденсата</strong> в топке (очистить).</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="headingAL07">
                <button class="accordion-button collapsed fw-bold text-secondary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseAL07">
                    <i class="fas fa-thermometer-full me-2"></i> Ошибка AL 07: Перегрев котла
                </button>
            </h2>
            <div id="collapseAL07" class="accordion-collapse collapse" aria-labelledby="headingAL07" data-bs-parent="#errorsAccordion">
                <div class="accordion-body bg-secondary-subtle">
                    <p class="fw-bold small">Описание: Котел Sime перегрелся. Температура аварийного термореле не менее 105 °C.</p>
                    <h5 class="fw-bold mt-4 text-info"><i class="fas fa-list me-2"></i>Возможные причины:</h5>
                    <div class="row g-3 small">
                        <div class="col-md-6">
                            <ul class="list-unstyled ms-3">
                                <li class="mb-2"><i class="fas fa-thermometer-half me-2 text-danger"></i> <strong>Срабатывает термодатчик по перегреву</strong> (свыше 105 °C).</li>
                                <li class="mb-2"><i class="fas fa-sync me-2 text-warning"></i> <strong>Сбой работы аварийного термостата.</strong> (Требуется замена).</li>
                                <li class="mb-2"><i class="fas fa-tint me-2 text-info"></i> <strong>Незначительная циркуляция</strong> воды (проверить давление, устранить воздух).</li>
                                <li><i class="fas fa-wind me-2 text-danger"></i> Есть воздух в трубах.</li>
                            </ul>
                        </div>
                        <div class="col-md-6">
                            <h6 class="fw-bold text-info">Проблемы с циркуляционным насосом:</h6>
                            <ul class="list-unstyled ms-3">
                                <li class="mb-2"><i class="fas fa-tachometer-alt me-2 text-warning"></i> <strong>Насос нестабилен</strong> (проверить напряжение/обороты).</li>
                                <li class="mb-2"><i class="fas fa-ruler-vertical me-2 text-danger"></i> На крыльчатке присутствуют износы (напор слабый).</li>
                                <li class="mb-2"><i class="fas fa-sync me-2 text-primary"></i> <strong>Насос заклинило</strong> (прокрутить вал ротора).</li>
                                <li><i class="fas fa-microchip me-2 text-danger"></i> Нарушение работы управляющей платы.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <h2 class="accordion-header" id="headingAL08">
                <button class="accordion-button collapsed fw-bold text-dark" type="button" data-bs-toggle="collapse" data-bs-target="#collapseAL08">
                    <i class="fas fa-fire-alt me-2"></i> Ошибка AL 08: Проблемы при выполнении розжига
                </button>
            </h2>
            <div id="collapseAL08" class="accordion-collapse collapse" aria-labelledby="headingAL08" data-bs-parent="#errorsAccordion">
                <div class="accordion-body bg-dark-subtle">
                    <p class="fw-bold small">Описание: Проблемы при выполнении розжига (розжиг не действует или имеется отрыв пламени).</p>
                    <h5 class="fw-bold mt-4 text-info"><i class="fas fa-wrench me-2"></i>Решение:</h5>
                    <ul class="list-unstyled ms-3 small">
                        <li class="mb-2"><i class="fas fa-search me-2 text-primary"></i> Осмотреть соединения между механизмом розжига и датчиком пламени.</li>
                        <li><i class="fas fa-wind me-2 text-warning"></i> Основным фактором срыва пламени может быть <strong>слабая тяга</strong> (проверить дымоход).</li>
                    </ul>
                </div>
            </div>
        </div>

    </div>

    <div class="p-5 rounded-3 text-center text-white shadow-sm mt-5" style="background-color: #009688;">
        <h3 class="h4 mb-3"><i class="fas fa-user-md me-2"></i>Нужна помощь с котлом Sime?</h3>
        <p class="lead mb-4">Наши специалисты помогут диагностировать и устранить неисправность!</p>
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