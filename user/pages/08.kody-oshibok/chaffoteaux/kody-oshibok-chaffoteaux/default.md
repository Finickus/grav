---
title: 'Коды ошибок Chaffoteaux'
---

<div class="container py-5">

    <div class="p-5 mb-5 text-white text-center rounded-3 shadow-sm" style="background-color: #009688;">
        <h1 class="display-5 fw-bold">
            <i class="fas fa-exclamation-triangle me-3"></i>Коды ошибок котлов Chaffoteaux
        </h1>
        <p class="lead">Полный гид по диагностике и ремонту</p>
    </div>

    <div class="card mb-5 shadow-sm border-0">
        <div class="card-body p-4">
            <p class="lead fs-6 mb-0">Котлы французской марки <strong>Chaffoteaux (Шафуто)</strong> отличаются надежностью, но могут выдавать различные ошибки в процессе эксплуатации. В этом подробном руководстве мы разберем все основные коды неисправностей, их причины и способы устранения.</p>
        </div>
    </div>

    <div class="card mb-5 shadow-sm border-info">
        <div class="card-header bg-info text-white py-3">
            <h4 class="h5 mb-0"><i class="fas fa-list me-2"></i>Основные ошибки и способы их устранения</h4>
        </div>
        <div class="card-body p-4">
            <div class="accordion" id="accordionChaffoErrors">
                
                <div class="accordion-item">
                    <h2 class="accordion-header" id="heading501">
                        <button class="accordion-button fw-bold text-warning" type="button" data-bs-toggle="collapse" data-bs-target="#collapse501" aria-expanded="true">
                            <i class="fas fa-fire me-2"></i> Ошибка 501 - Проблемы с розжигом
                        </button>
                    </h2>
                    <div id="collapse501" class="accordion-collapse collapse show" aria-labelledby="heading501" data-bs-parent="#accordionChaffoErrors">
                        <div class="accordion-body bg-light">
                            <h6 class="fw-bold text-warning">Причины и решения:</h6>
                            <div class="row g-3 small">
                                <div class="col-md-6">
                                    <p class="fw-bold">Проблемы с подачей газа:</p>
                                    <ul class="list-unstyled ms-3">
                                        <li class="mb-1"><i class="fas fa-gas-pump me-2 text-danger"></i> Проверить открытие газового вентиля</li>
                                        <li class="mb-1"><i class="fas fa-wind me-2 text-warning"></i> Удалить воздух из газопровода</li>
                                        <li><i class="fas fa-tachometer-alt me-2 text-primary"></i> Измерить давление газа (норма: 20 мбар)</li>
                                    </ul>
                                    <p class="fw-bold mt-3">Неисправность газового клапана:</p>
                                    <ul class="list-unstyled ms-3">
                                        <li class="mb-1"><i class="fas fa-bolt me-2 text-info"></i> Проверить катушки клапана</li>
                                        <li><i class="fas fa-tint me-2 text-success"></i> При залипании - подать давление через штуцер</li>
                                    </ul>
                                </div>
                                <div class="col-md-6">
                                    <p class="fw-bold">Проблемы с электродом ионизации:</p>
                                    <ul class="list-unstyled ms-3">
                                        <li class="mb-1"><i class="fas fa-broom me-2 text-warning"></i> Очистить от нагара</li>
                                        <li class="mb-1"><i class="fas fa-ruler me-2 text-primary"></i> Проверить зазор (3-5 мм)</li>
                                        <li><i class="fas fa-plug me-2 text-danger"></i> Проверить заземление</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <h2 class="accordion-header" id="heading101">
                        <button class="accordion-button collapsed fw-bold text-danger" type="button" data-bs-toggle="collapse" data-bs-target="#collapse101">
                            <i class="fas fa-thermometer-full me-2"></i> Ошибка 101 - Перегрев котла
                        </button>
                    </h2>
                    <div id="collapse101" class="accordion-collapse collapse" aria-labelledby="heading101" data-bs-parent="#accordionChaffoErrors">
                        <div class="accordion-body bg-light">
                            <h6 class="fw-bold text-danger">Что делать:</h6>
                            <ol class="list-unstyled ms-3 small">
                                <li class="mb-2"><i class="fas fa-snowflake me-2 text-primary"></i> <strong>1. Дать котлу остыть</strong></li>
                                <li class="mb-2"><i class="fas fa-search me-2 text-info"></i> <strong>2. Проверить:</strong>
                                    <ul class="list-unstyled ms-4">
                                        <li class="mb-1"><i class="fas fa-tachometer-alt me-2 text-success"></i> Давление в системе (1-1.5 бар)</li>
                                        <li class="mb-1"><i class="fas fa-pump me-2 text-warning"></i> Работу циркуляционного насоса</li>
                                        <li><i class="fas fa-thermometer-half me-2 text-danger"></i> Состояние термостата</li>
                                    </ul>
                                </li>
                                <li class="mb-2"><i class="fas fa-wind me-2 text-primary"></i> <strong>3. Удалить воздушные пробки</strong></li>
                                <li><i class="fas fa-exchange-alt me-2 text-info"></i> <strong>4. При повторении ошибки - заменить датчик перегрева</strong></li>
                            </ol>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <h2 class="accordion-header" id="heading110">
                        <button class="accordion-button collapsed fw-bold text-warning" type="button" data-bs-toggle="collapse" data-bs-target="#collapse110">
                            <i class="fas fa-thermometer-half me-2"></i> Ошибки 110/112 - Неисправность датчика температуры
                        </button>
                    </h2>
                    <div id="collapse110" class="accordion-collapse collapse" aria-labelledby="heading110" data-bs-parent="#accordionChaffoErrors">
                        <div class="accordion-body bg-light">
                            <h6 class="fw-bold text-warning">Диагностика:</h6>
                            <ol class="list-unstyled ms-3 small">
                                <li class="mb-2"><i class="fas fa-ruler me-2 text-primary"></i> <strong>1. Измерить сопротивление датчика:</strong> (При 20°C: ~10 кОм; При 80°C: ~1.5 кОм)</li>
                                <li class="mb-2"><i class="fas fa-plug me-2 text-warning"></i> <strong>2. Проверить целостность проводов</strong></li>
                                <li><i class="fas fa-exchange-alt me-2 text-danger"></i> <strong>3. При отклонениях - заменить датчик</strong></li>
                            </ol>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <h2 class="accordion-header" id="heading108">
                        <button class="accordion-button collapsed fw-bold text-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapse108">
                            <i class="fas fa-tachometer-alt me-2"></i> Ошибка 108 - Низкое давление
                        </button>
                    </h2>
                    <div id="collapse108" class="accordion-collapse collapse" aria-labelledby="heading108" data-bs-parent="#accordionChaffoErrors">
                        <div class="accordion-body bg-light">
                            <h6 class="fw-bold text-primary">Действия:</h6>
                            <ol class="list-unstyled ms-3 small">
                                <li class="mb-2"><i class="fas fa-tint me-2 text-primary"></i> <strong>1. Долить воду в систему</strong> (до 1.2-1.5 бар)</li>
                                <li class="mb-2"><i class="fas fa-search me-2 text-info"></i> <strong>2. Проверить на утечки:</strong> (Теплообменник, соединения, насос, клапан)</li>
                                <li><i class="fas fa-bolt me-2 text-danger"></i> <strong>3. Проверить работу реле давления</strong></li>
                            </ol>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <h2 class="accordion-header" id="heading6P1">
                        <button class="accordion-button collapsed fw-bold text-info" type="button" data-bs-toggle="collapse" data-bs-target="#collapse6P1">
                            <i class="fas fa-wind me-2"></i> Ошибка 6P1 (607) - Проблемы с тягой
                        </button>
                    </h2>
                    <div id="collapse6P1" class="accordion-collapse collapse" aria-labelledby="heading6P1" data-bs-parent="#accordionChaffoErrors">
                        <div class="accordion-body bg-light">
                            <h6 class="fw-bold text-info">Причины и устранение:</h6>
                            <ol class="list-unstyled ms-3 small">
                                <li class="mb-2"><i class="fas fa-broom me-2 text-info"></i> <strong>1. Проверить и очистить:</strong> Засорение дымохода, обледенение оголовка.</li>
                                <li class="mb-2"><i class="fas fa-broom me-2 text-danger"></i> <strong>2. Очистить дымоход</strong></li>
                                <li class="mb-2"><i class="fas fa-thermometer-half me-2 text-primary"></i> <strong>3. Проверить датчик тяги</strong></li>
                                <li><i class="fas fa-fan me-2 text-info"></i> <strong>4. Убедиться в исправности вентилятора</strong></li>
                            </ol>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <h2 class="accordion-header" id="heading1P2">
                        <button class="accordion-button collapsed fw-bold text-success" type="button" data-bs-toggle="collapse" data-bs-target="#collapse1P2">
                            <i class="fas fa-sync me-2"></i> Ошибка 1P2 (103) - Проблемы циркуляции
                        </button>
                    </h2>
                    <div id="collapse1P2" class="accordion-collapse collapse" aria-labelledby="heading1P2" data-bs-parent="#accordionChaffoErrors">
                        <div class="accordion-body bg-light">
                            <h6 class="fw-bold text-success">Решение:</h6>
                            <ol class="list-unstyled ms-3 small">
                                <li class="mb-2"><i class="fas fa-tachometer-alt me-2 text-primary"></i> <strong>1. Проверить давление</strong> (1.2 бар)</li>
                                <li class="mb-2"><i class="fas fa-wind me-2 text-info"></i> <strong>2. Удалить воздух из системы</strong></li>
                                <li class="mb-2"><i class="fas fa-valve me-2 text-success"></i> <strong>3. Открыть все запорные краны</strong></li>
                                <li><i class="fas fa-pump me-2 text-warning"></i> <strong>4. Проверить работу насоса</strong></li>
                            </ol>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <h2 class="accordion-header" id="headingOther">
                        <button class="accordion-button collapsed fw-bold text-secondary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOther">
                            <i class="fas fa-sync me-2"></i> Другие ошибки (201, 5P3, 104, 107...) - нажмите для просмотра
                        </button>
                    </h2>
                    <div id="collapseOther" class="accordion-collapse collapse" aria-labelledby="headingOther" data-bs-parent="#accordionChaffoErrors">
                        <div class="accordion-body bg-light small">
                            <p><strong>Ошибка 201 (Датчик ГВС):</strong> Проверить и заменить датчик, проверить накипь.</p>
                            <p><strong>Ошибка 5P3 (Розжиг):</strong> Проверить подачу газа, электроды, тягу.</p>
                            <p><strong>Ошибка 104 (Неисправность насоса):</strong> Проверить напряжение (220В), вращение вала, заменить насос.</p>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </div>

    <div class="card mb-5 shadow-sm border-success">
        <div class="card-header bg-success text-white py-3">
            <h4 class="h5 mb-0"><i class="fas fa-shield-alt me-2"></i>Профилактика и обслуживание</h4>
        </div>
        <div class="card-body">
            <div class="content">
                <p>Чтобы избежать большинства ошибок, соблюдайте эти простые правила:</p>
                <div class="row text-center g-4 small">
                    <div class="col-6 col-md-auto">
                        <i class="fas fa-tachometer-alt fa-2x mb-2 text-primary"></i>
                        <p class="mb-0">Регулярно проверяйте давление</p>
                    </div>
                    <div class="col-6 col-md-auto">
                        <i class="fas fa-calendar-check fa-2x mb-2 text-info"></i>
                        <p class="mb-0">Ежегодное обслуживание</p>
                    </div>
                    <div class="col-6 col-md-auto">
                        <i class="fas fa-filter fa-2x mb-2 text-success"></i>
                        <p class="mb-0">Очищайте фильтры</p>
                    </div>
                    <div class="col-6 col-md-auto">
                        <i class="fas fa-bolt fa-2x mb-2 text-warning"></i>
                        <p class="mb-0">Контролируйте электроды</p>
                    </div>
                    <div class="col-12 col-md-auto">
                        <i class="fas fa-user-md fa-2x mb-2 text-danger"></i>
                        <p class="mb-0">Обращайтесь к специалистам</p>
                    </div>
                </div>
                <div class="alert alert-danger mt-4 mb-0 small bg-opacity-10">
                    <h5 class="fw-bold text-danger"><i class="fas fa-exclamation-triangle me-2"></i>Важно!</h5>
                    <p class="mb-0">При сложных неисправностях, особенно связанных с газовой частью, рекомендуем обращаться к сертифицированным специалистам.</p>
                </div>
            </div>
        </div>
    </div>

    <div class="card mb-5 shadow-sm border-0">
        <div class="card-body p-4 small">
            <h6 class="fw-bold text-warning mb-2"><i class="fas fa-flag-checkered me-2"></i>Заключение</h6>
            <p class="mb-0">Это руководство поможет вам быстро диагностировать и устранить большинство неисправностей котлов Chaffoteaux. Для точного определения проблемы всегда сверяйтесь с технической документацией вашей конкретной модели.</p>
        </div>
    </div>

    <div class="p-5 rounded-3 text-center text-white shadow-sm" style="background-color: #009688;">
        <h3 class="h4 mb-3"><i class="fas fa-user-md me-2"></i>Нужна помощь с котлом Chaffoteaux?</h3>
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