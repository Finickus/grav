---
title: 'Коды ошибок котлов Kentatsu'
---

<div class="container py-5">

    <div class="p-5 mb-5 text-white text-center rounded-3 shadow-sm" style="background-color: #009688;">
        <h1 class="display-5 fw-bold">
            <i class="fas fa-exclamation-triangle me-3"></i>Коды ошибок котлов Kentatsu
        </h1>
        <p class="lead">Диагностика и устранение неисправностей газовых котлов Кентатсу</p>
    </div>

    <div class="card mb-5 shadow-sm border-0">
        <div class="card-body p-4">
            <p class="fs-6">Газовые котлы <strong>Kentatsu (Кентатсу)</strong> – надежное отопительное оборудование, но иногда могут сигнализировать о неисправностях с помощью кодов ошибок. Понимание этих кодов помогает быстро диагностировать проблему и принять меры для устранения.</p>
            <p class="mb-0">На этой странице представлены основные коды ошибок, которые могут появиться на дисплее вашего котла Kentatsu, их возможные причины и рекомендуемые действия.</p>
            <div class="alert alert-danger mt-4 shadow-sm d-flex align-items-start" role="alert">
                <i class="fas fa-exclamation-triangle fs-4 me-3 mt-1 text-white"></i>
                <div>
                    <h5 class="alert-heading fw-bold text-white">Предупреждение о безопасности</h5>
                    <p class="mb-0 text-white">Работы с газовым оборудованием требуют квалификации. При отсутствии опыта или если ошибка сохраняется после выполнения рекомендованных действий, <strong>вызывайте сервисного инженера</strong>.</p>
                </div>
            </div>
        </div>
    </div>

    <div class="card mb-5 shadow-sm border-info">
        <div class="card-header bg-info text-white py-3">
            <h4 class="h5 mb-0"><i class="fas fa-list me-2"></i>Основные коды ошибок котлов Kentatsu</h4>
        </div>
        <div class="card-body p-4">
            <div class="accordion" id="accordionKentatsuErrors">
                
                <div class="accordion-item">
                    <h2 class="accordion-header" id="headingBC">
                        <button class="accordion-button fw-bold text-warning" type="button" data-bs-toggle="collapse" data-bs-target="#collapseBC" aria-expanded="true">
                            <i class="fas fa-fire-extinguisher me-2"></i> Ошибка bC - Не выполняется разжигание котла Кентатсу
                        </button>
                    </h2>
                    <div id="collapseBC" class="accordion-collapse collapse show" aria-labelledby="headingBC" data-bs-parent="#accordionKentatsuErrors">
                        <div class="accordion-body bg-light">
                            <p class="fw-bold small">Описание: Не идет топливо на блок горелки. Розжиг не происходит.</p>
                            <h6 class="fw-bold text-warning">Возможные причины и решения:</h6>
                            <div class="row g-3 small">
                                <div class="col-md-6">
                                    <ul class="list-unstyled ms-3">
                                        <li class="mb-2"><i class="fas fa-valve me-2 text-primary"></i> <strong>Перекрыт запорный кран</strong> → Открыть кран.</li>
                                        <li class="mb-2"><i class="fas fa-wind me-2 text-info"></i> <strong>Воздух в трубопроводе</strong> → Стравить воздух (при первом запуске).</li>
                                        <li class="mb-2"><i class="fas fa-tachometer-alt me-2 text-success"></i> <strong>Низкое давление газа</strong> → Проверить давление (номинал 18-21 мбар).</li>
                                        <li><i class="fas fa-valve me-2 text-danger"></i> <strong>Повреждение газового клапана</strong> → Проверить, заменить.</li>
                                    </ul>
                                </div>
                                <div class="col-md-6">
                                    <ul class="list-unstyled ms-3">
                                        <li class="mb-2"><i class="fas fa-bolt me-2 text-primary"></i> <strong>Проблемы с электродом розжига</strong> → Очистить, проверить зазор.</li>
                                        <li class="mb-2"><i class="fas fa-coils me-2 text-info"></i> <strong>Обрыв/замыкание в катушках клапана</strong> → Проверить.</li>
                                        <li><i class="fas fa-microchip me-2 text-danger"></i> <strong>Неисправна плата управления</strong> → Перезапустить, при повторении - заменить.</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="alert alert-warning mt-4 p-2 small">
                                <h6 class="fw-bold"><i class="fas fa-info-circle me-2 text-info"></i> Конденсат и электроника</h6>
                                <ul class="list-unstyled ms-3 mb-0">
                                    <li class="mb-1"><i class="fas fa-tint me-2 text-info"></i> Переизбыток влаги → Очистить топочную камеру, электрод.</li>
                                    <li><i class="fas fa-bolt me-2 text-danger"></i> Электрод касается горелки → Устранить контакт.</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <h2 class="accordion-header" id="headingHL">
                        <button class="accordion-button collapsed fw-bold text-danger" type="button" data-bs-toggle="collapse" data-bs-target="#collapseHL">
                            <i class="fas fa-thermometer-full me-2"></i> Ошибка HL - Котел Kentatsu перегрет
                        </button>
                    </h2>
                    <div id="collapseHL" class="accordion-collapse collapse" aria-labelledby="headingHL" data-bs-parent="#accordionKentatsuErrors">
                        <div class="accordion-body bg-light">
                            <p class="fw-bold small">Описание: Температура защитного термореле больше 105 °C. Котел блокируется.</p>
                            <h6 class="fw-bold text-danger">Возможные причины и решения:</h6>
                            <div class="row g-3 small">
                                <div class="col-md-6">
                                    <ul class="list-unstyled ms-3">
                                        <li class="mb-2"><i class="fas fa-thermometer-half me-2 text-danger"></i> <strong>Срабатывание термостата защиты</strong> → Дождаться остывания, перезапустить.</li>
                                        <li class="mb-2"><i class="fas fa-pump me-2 text-primary"></i> <strong>Плохая циркуляция</strong> → Проверить давление (1.2 бар), удалить воздух.</li>
                                        <li><i class="fas fa-valve me-2 text-info"></i> <strong>Закрытые вентили</strong> → Открыть для циркуляции.</li>
                                    </ul>
                                </div>
                                <div class="col-md-6">
                                    <ul class="list-unstyled ms-3">
                                        <li class="mb-2"><i class="fas fa-pump me-2 text-warning"></i> <strong>Проблемы с циркуляционным насосом</strong> → Проверить напряжение, обмотки, крыльчатку.</li>
                                        <li><i class="fas fa-sync me-2 text-success"></i> <strong>Заклинивание насоса</strong> → Провернуть вал ротора.</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <h2 class="accordion-header" id="headingLP">
                        <button class="accordion-button collapsed fw-bold text-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseLP">
                            <i class="fas fa-tachometer-alt me-2"></i> Ошибка LP - Пониженное давление в системе
                        </button>
                    </h2>
                    <div id="collapseLP" class="accordion-collapse collapse" aria-labelledby="headingLP" data-bs-parent="#accordionKentatsuErrors">
                        <div class="accordion-body bg-light">
                            <p class="fw-bold small">Описание: Признак пониженного давления в системе отопления.</p>
                            <h6 class="fw-bold text-primary">Возможные причины и решения:</h6>
                            <div class="row g-3 small">
                                <div class="col-md-6">
                                    <ul class="list-unstyled ms-3">
                                        <li class="mb-2"><i class="fas fa-tachometer-alt me-2 text-primary"></i> <strong>Низкое давление</strong> → Проверить манометр, долить через кран подпитки.</li>
                                        <li><i class="fas fa-tint me-2 text-info"></i> <strong>Утечка теплоносителя</strong> → Найти и устранить утечку.</li>
                                    </ul>
                                </div>
                                <div class="col-md-6">
                                    <ul class="list-unstyled ms-3">
                                        <li class="mb-2"><i class="fas fa-plug me-2 text-success"></i> <strong>Нарушение контакта прессостата</strong> → Проверить соединение с платой.</li>
                                        <li><i class="fas fa-valve me-2 text-warning"></i> <strong>Неисправно реле давления</strong> → Заменить прессостат.</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="alert alert-info mt-4 p-2 small">
                                <h6 class="fw-bold"><i class="fas fa-info-circle me-2 text-info"></i> Совет</h6>
                                <p class="mb-0">Часто неполадку устраняют при помощи подпиточного крана. Если сбой повторяется, возможно, есть утечка воды.</p>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <h2 class="accordion-header" id="headingAF">
                        <button class="accordion-button collapsed fw-bold text-warning" type="button" data-bs-toggle="collapse" data-bs-target="#collapseAF">
                            <i class="fas fa-wind me-2"></i> Ошибка AF - Отсутствует тяга
                        </button>
                    </h2>
                    <div id="collapseAF" class="accordion-collapse collapse" aria-labelledby="headingAF" data-bs-parent="#accordionKentatsuErrors">
                        <div class="accordion-body bg-light">
                            <p class="fw-bold small">Описание: Котел блокируется при проблемах с удалением продуктов сгорания.</p>
                            <h6 class="fw-bold text-warning">Возможные причины и решения:</h6>
                            <div class="row g-3 small">
                                <div class="col-md-6">
                                    <ul class="list-unstyled ms-3">
                                        <li class="mb-2"><i class="fas fa-border-all me-2 text-primary"></i> <strong>Недостаточный размер дымохода</strong> → Прочистить, устранить лед.</li>
                                        <li><i class="fas fa-arrows-alt-h me-2 text-danger"></i> <strong>Слишком длинный дымоход</strong> или большой горизонтальный участок.</li>
                                    </ul>
                                </div>
                                <div class="col-md-6">
                                    <ul class="list-unstyled ms-3">
                                        <li class="mb-2"><i class="fas fa-tachometer-alt me-2 text-warning"></i> <strong>Неисправность датчика тяги</strong> → Проверить контакты, конденсат в трубках.</li>
                                        <li><i class="fas fa-fan me-2 text-danger"></i> <strong>Проблемы с вентилятором</strong> → Очистить крыльчатку, проверить смазку.</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <h2 class="accordion-header" id="headingOther">
                        <button class="accordion-button collapsed fw-bold text-secondary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOther">
                            <i class="fas fa-thermometer-half me-2"></i> Прочие неисправности (Hb, db, GI)
                        </button>
                    </h2>
                    <div id="collapseOther" class="accordion-collapse collapse" aria-labelledby="headingOther" data-bs-parent="#accordionKentatsuErrors">
                        <div class="accordion-body bg-light">
                            <div class="table-responsive">
                                <table class="table table-bordered table-striped small">
                                    <thead class="bg-light">
                                        <tr>
                                            <th style="width: 15%;">Код</th>
                                            <th style="width: 45%;">Неисправность</th>
                                            <th style="width: 40%;">Решение</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td><strong>Hb</strong></td>
                                            <td>Повреждение датчика NTC отопления</td>
                                            <td>Проверить/заменить датчик.</td>
                                        </tr>
                                        <tr>
                                            <td><strong>db</strong></td>
                                            <td>Поломка датчика NTC ГВС</td>
                                            <td>Проверить/заменить датчик.</td>
                                        </tr>
                                        <tr>
                                            <td><strong>GI</strong></td>
                                            <td>Проблемы с розжигом / Срыв пламени</td>
                                            <td>Проверить соединения розжига, датчика пламени, газового клапана. Проверить тягу (см. AF).</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </div>

    <div class="p-5 rounded-3 text-center text-white shadow-sm mt-5" style="background-color: #009688;">
        <h3 class="h4 mb-3"><i class="fas fa-user-md me-2"></i>Нужна помощь с котлом Kentatsu?</h3>
        <p class="lead mb-4">Наши специалисты помогут диагностировать и устранить неисправность!</p>
        <div class="row justify-content-center g-3">
            <div class="col-12 col-md-4">
                <a href="tel:+79262211348" class="btn btn-light btn-lg w-100 fw-bold">
                    <i class="fas fa-phone me-2"></i> <span>Позвонить</span>
                </a>
            </div>
            <div class="col-12 col-md-4">
                <a href="https://service04.ru/contact-us/feedback" class="btn btn-warning btn-lg w-100 fw-bold text-dark">
                    <i class="fas fa-envelope me-2"></i> <span>Оставить заявку</span>
                </a>
            </div>
        </div>
    </div>

</div>