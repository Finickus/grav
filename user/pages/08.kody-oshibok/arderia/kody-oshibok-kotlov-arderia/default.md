---
title: 'Коды ошибок котлов Arderia'
---

<div class="container py-5">

    <div class="p-5 mb-5 text-white text-center rounded-3 shadow-sm" style="background-color: #009688;">
        <h1 class="display-5 fw-bold">
            <i class="fas fa-exclamation-triangle me-3"></i>Коды ошибок котлов Arderia
        </h1>
        <p class="lead">Руководство по диагностике и устранению неисправностей котлов Ардерия</p>
    </div>

    <div class="row">
        <div class="col-lg-12">
            
            <div class="card mb-5 shadow-sm border-0">
                <div class="card-header bg-danger text-white py-3">
                    <h4 class="h5 mb-0"><i class="fas fa-list me-2"></i>Коды ошибок A1 - AA (Критические)</h4>
                </div>
                <div class="card-body p-0">
                    <div class="table-responsive">
                        <table class="table table-striped table-bordered align-middle mb-0">
                            <thead class="bg-dark text-white">
                                <tr>
                                    <th style="width: 10%;">Код</th>
                                    <th style="width: 35%;">Описание</th>
                                    <th style="width: 55%;">Возможные причины</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><span class="badge bg-danger">A1</span></td>
                                    <td>Датчик давления воздуха замкнут</td>
                                    <td class="small">Задувание/блокировка дымохода, обледенение выходного отверстия.</td>
                                </tr>
                                <tr>
                                    <td><span class="badge bg-danger">A2</span></td>
                                    <td>Вентилятор работает с малой скоростью</td>
                                    <td class="small">Недостаточный контакт/подключение проводов, недостаточная скорость вращения (посторонние предметы).</td>
                                </tr>
                                <tr>
                                    <td><span class="badge bg-danger">A4</span></td>
                                    <td>Срабатывание датчика по перегреву</td>
                                    <td class="small">Закрыты запорные краны, засор фильтра, неисправен насос/3-х ходовой клапан, повреждение датчика протока ГВС.</td>
                                </tr>
                                <tr>
                                    <td><span class="badge bg-danger">A5</span></td>
                                    <td>Пониженное давление теплоносителя</td>
                                    <td class="small">Малый объем воды, наличие воздуха, неисправен насос/датчик напора, утечка воды в системе.</td>
                                </tr>
                                <tr>
                                    <td><span class="badge bg-danger">A6</span></td>
                                    <td>Неисправность розжига</td>
                                    <td class="small">Дымоход заблокирован, низкое давление газа, неисправен газовый клапан/трансформатор.</td>
                                </tr>
                                <tr>
                                    <td><span class="badge bg-danger">A8</span></td>
                                    <td>Остаточное пламя</td>
                                    <td class="small">Остаточное пламя при отсутствии напряжения, повреждение диафрагмы газового клапана.</td>
                                </tr>
                                <tr>
                                    <td><span class="badge bg-danger">A9</span></td>
                                    <td>Замерзание</td>
                                    <td class="small">Снижение температуры воды до 5°C.</td>
                                </tr>
                                <tr>
                                    <td><span class="badge bg-danger">AA</span></td>
                                    <td>Закипание (Перегрев)</td>
                                    <td class="small">Закрыты отопительные контуры, засор фильтра, повреждение насоса/трехходового клапана.</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            <div class="card mb-5 shadow-sm border-0">
                <div class="card-header bg-warning text-dark py-3">
                    <h4 class="h5 mb-0"><i class="fas fa-list me-2"></i>Коды ошибок AB - AE (Датчики/Дымоход)</h4>
                </div>
                <div class="card-body p-0">
                    <div class="table-responsive">
                        <table class="table table-striped table-bordered align-middle mb-0">
                            <tbody>
                                <tr>
                                    <td><span class="badge bg-warning text-dark">AB, AC</span></td>
                                    <td>Повреждение термостата</td>
                                    <td class="small">Короткое замыкание в термостате, некорректное соединение контактов.</td>
                                </tr>
                                <tr>
                                    <td><span class="badge bg-warning text-dark">AE</span></td>
                                    <td>Дымоход заблокирован</td>
                                    <td class="small">Посторонние предметы в газоходе, деформация газохода.</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            <div class="card mb-5 shadow-sm border-0">
                <div class="card-header bg-info text-white py-3">
                    <h4 class="h5 mb-0"><i class="fas fa-info-circle me-2"></i>Диагностика и устранение (Коды E0-E3)</h4>
                </div>
                <div class="card-body p-4">
                    <div class="accordion" id="errorAccordion">
                        
                        <div class="accordion-item">
                            <h2 class="accordion-header" id="headingE0">
                                <button class="accordion-button collapsed fw-bold text-secondary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseE0">
                                    <span class="badge bg-secondary me-2">E0</span> Ошибка режима антизамерзание
                                </button>
                            </h2>
                            <div id="collapseE0" class="accordion-collapse collapse" aria-labelledby="headingE0" data-bs-parent="#errorAccordion">
                                <div class="accordion-body bg-light small">
                                    <p class="fw-bold">Описание: Ошибка активна, если после перерыва подачи электроэнергии температура систем отопления или ГВС ниже +1 °С.</p>
                                    <p class="fw-bold mt-2">Решение:</p>
                                    <ul class="list-unstyled ms-3">
                                        <li>Убедитесь в целостности магистралей. Блокировка автоматически снимется при повышении температуры выше +1°C.</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        
                        <div class="accordion-item">
                            <h2 class="accordion-header" id="headingE1">
                                <button class="accordion-button collapsed fw-bold text-secondary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseE1">
                                    <span class="badge bg-secondary me-2">E1</span> Ошибка датчика ионизации
                                </button>
                            </h2>
                            <div id="collapseE1" class="accordion-collapse collapse" aria-labelledby="headingE1" data-bs-parent="#errorAccordion">
                                <div class="accordion-body bg-light small">
                                    <p class="fw-bold">Описание: Отображается при неудачном розжиге котла или после неожиданного срыва пламени.</p>
                                    <p class="fw-bold mt-2">Решение:</p>
                                    <ul class="list-unstyled ms-3">
                                        <li>Проверьте наличие подачи газа. Система будет пытаться восстановить работу 60 минут. Снять блокировку можно нажатием кнопки MODE.</li>
                                    </ul>
                                </div>
                            </div>
                        </div>

                        <div class="accordion-item">
                            <h2 class="accordion-header" id="headingE2">
                                <button class="accordion-button collapsed fw-bold text-secondary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseE2">
                                    <span class="badge bg-secondary me-2">E2</span> Ошибка дифференциального датчика давления воздуха
                                </button>
                            </h2>
                            <div id="collapseE2" class="accordion-collapse collapse" aria-labelledby="headingE2" data-bs-parent="#errorAccordion">
                                <div class="accordion-body bg-light small">
                                    <p class="fw-bold">Описание: Отображается в ситуации ненормальной тяги, неисправностью вентилятора или датчика давления воздуха.</p>
                                    <p class="fw-bold mt-2">Решение:</p>
                                    <ul class="list-unstyled ms-3">
                                        <li>Убедитесь в нормальном состоянии дымохода. Если через 15 минут ошибка не устраняется, обратитесь в сервисную службу.</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        
                        <div class="accordion-item">
                            <h2 class="accordion-header" id="headingE3">
                                <button class="accordion-button collapsed fw-bold text-secondary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseE3">
                                    <span class="badge bg-secondary me-2">E3</span> Ошибка защитного термостата перегрева
                                </button>
                            </h2>
                            <div id="collapseE3" class="accordion-collapse collapse" aria-labelledby="headingE3" data-bs-parent="#errorAccordion">
                                <div class="accordion-body bg-light small">
                                    <p class="fw-bold">Описание: Отображается в ситуациях отсутствия теплоносителя или его циркуляции.</p>
                                    <p class="fw-bold mt-2">Решение:</p>
                                    <ul class="list-unstyled ms-3">
                                        <li>Откройте кран разбора горячей воды для понижения температуры, проверьте состояние вентилей и магистралей отопления. Снять блокировку можно нажатием кнопки MODE.</li>
                                    </ul>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>
            </div>

            <div class="card mb-5 shadow-sm border-0">
                <div class="card-header bg-success text-white py-3">
                    <h4 class="h5 mb-0"><i class="fas fa-wrench me-2"></i>Возможные неполадки и их устранения</h4>
                </div>
                <div class="card-body p-4">
                    <div class="accordion" id="troubleshootingAccordion">
                        
                        <div class="accordion-item">
                            <h2 class="accordion-header" id="headingTrouble1">
                                <button class="accordion-button collapsed fw-bold text-dark" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTrouble1">
                                    Вентилятор начал работать, но пламя не появляется
                                </button>
                            </h2>
                            <div id="collapseTrouble1" class="accordion-collapse collapse" aria-labelledby="headingTrouble1" data-bs-parent="#troubleshootingAccordion">
                                <div class="accordion-body bg-light small">
                                    <ul class="list-unstyled ms-3">
                                        <li>Не срабатывает реле давления воздуха / Блокировка дымохода / Утечка в системе отвода продуктов сгорания.</li>
                                        <li>Напряжение электропитания ниже 170 В - <span class="text-danger">Установите стабилизатор напряжения.</span></li>
                                        <li><span class="fw-bold">Решение:</span> Немедленно обратитесь в сервисный центр для диагностики.</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        
                        <div class="accordion-item">
                            <h2 class="accordion-header" id="headingTrouble2">
                                <button class="accordion-button collapsed fw-bold text-dark" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTrouble2">
                                    Неправильное горение: цвет пламени желтый или красный
                                </button>
                            </h2>
                            <div id="collapseTrouble2" class="accordion-collapse collapse" aria-labelledby="headingTrouble2" data-bs-parent="#troubleshootingAccordion">
                                <div class="accordion-body bg-light small">
                                    <ul class="list-unstyled ms-3">
                                        <li>Горелка загрязнена / Неправильное функционирование дымохода / Неверная настройка газового клапана.</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        
                        <div class="accordion-item">
                            <h2 class="accordion-header" id="headingTrouble3">
                                <button class="accordion-button collapsed fw-bold text-dark" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTrouble3">
                                    Котел Ардерия часто выключается
                                </button>
                            </h2>
                            <div id="collapseTrouble3" class="accordion-collapse collapse" aria-labelledby="headingTrouble3" data-bs-parent="#troubleshootingAccordion">
                                <div class="accordion-body bg-light small">
                                    <ul class="list-unstyled ms-3">
                                        <li>Недостаточное давление/утечки / Наличие воздуха в системе / Вал насоса заблокирован.</li>
                                        <li><span class="fw-bold">Решение:</span> Проверьте давление (1-1.2 bar), удалите воздух, поднимите давление в расширительном баке до 1.0 bar.</li>
                                    </ul>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>
            </div>

        </div>
    </div>

    <div class="p-5 rounded-3 text-center text-white shadow-lg mt-5" style="background-color: #009688;">
        <h3 class="h4 mb-3"><i class="fas fa-phone me-2"></i>Нужна помощь специалиста?</h3>
        <p class="lead mb-4">Не занимайтесь самостоятельным ремонтом газового оборудования!</p>
        <div class="row justify-content-center g-3">
            <div class="col-12 col-md-4">
                <a href="tel:+79262211348" class="btn btn-success btn-lg w-100 fw-bold">
                    <i class="fas fa-headset me-2"></i> <span>Вызвать мастера</span>
                </a>
            </div>
        </div>
    </div>

</div>