---
title: Коды ошибок котлов Ariston
metadata:
  description: Коды ошибок котлов Ariston Полное руководство по диагностике и устранению
    неисправностей котлов Аристон Отопительный контур ГВС Электронная плата Розжиг...
  og:type: article
  og:title: Коды ошибок котлов Ariston - Service04
  og:description: Коды ошибок котлов Ariston Полное руководство по диагностике и устранению
    неисправностей котлов Аристон Отопительный контур ГВС Электронная плата Розжиг...
  og:url: https://service04.ru/kody-oshibok/ariston/kody-oshibok-kotlov-ariston
  og:site_name: Service04
  og:locale: ru_RU
  og:image: https://service04.ru/images/og-default.jpg
  og:image:width: '1200'
  og:image:height: '630'
  canonical: https://service04.ru/kody-oshibok/ariston/kody-oshibok-kotlov-ariston
  robots: index, follow
  yandex-verification: ''
  geo.region: RU-MOW
  geo.placename: Москва
  author: Service04
---
<div class="container py-5">

    <div class="p-5 mb-5 text-white text-center rounded-3 shadow-sm" style="background-color: #dc3545;">
        <h1 class="display-5 fw-bold">
            <i class="fas fa-exclamation-circle me-3"></i>Коды ошибок котлов Ariston
        </h1>
        <p class="lead">Полное руководство по диагностике и устранению неисправностей котлов Аристон</p>
    </div>

    <ul class="nav nav-tabs nav-fill mb-4" id="errorTabs" role="tablist">
        <li class="nav-item" role="presentation">
            <button class="nav-link active fw-bold" id="heating-tab" data-bs-toggle="tab" data-bs-target="#heating" type="button" role="tab" aria-controls="heating" aria-selected="true">Отопительный контур</button>
        </li>
        <li class="nav-item" role="presentation">
            <button class="nav-link fw-bold" id="dhw-tab" data-bs-toggle="tab" data-bs-target="#dhw" type="button" role="tab" aria-controls="dhw" aria-selected="false">ГВС</button>
        </li>
        <li class="nav-item" role="presentation">
            <button class="nav-link fw-bold" id="board-tab" data-bs-toggle="tab" data-bs-target="#board" type="button" role="tab" aria-controls="board" aria-selected="false">Электронная плата</button>
        </li>
        <li class="nav-item" role="presentation">
            <button class="nav-link fw-bold" id="ignition-tab" data-bs-toggle="tab" data-bs-target="#ignition" type="button" role="tab" aria-controls="ignition" aria-selected="false">Розжиг</button>
        </li>
        <li class="nav-item" role="presentation">
            <button class="nav-link fw-bold" id="ventilation-tab" data-bs-toggle="tab" data-bs-target="#ventilation" type="button" role="tab" aria-controls="ventilation" aria-selected="false">Вентиляция</button>
        </li>
        <li class="nav-item" role="presentation">
            <button class="nav-link fw-bold" id="zones-tab" data-bs-toggle="tab" data-bs-target="#zones" type="button" role="tab" aria-controls="zones" aria-selected="false">Температурные зоны</button>
        </li>
    </ul>

    <div class="tab-content" id="errorTabsContent">
        
        <div class="tab-pane fade show active" id="heating" role="tabpanel" aria-labelledby="heating-tab">
            <div class="card mt-3 shadow-sm border-0">
                <div class="card-header bg-danger text-white py-3">
                    <h4 class="h5 mb-0"><i class="fas fa-thermometer-three-quarters me-2"></i>Ошибки отопительного контура</h4>
                </div>
                <div class="card-body p-0">
                    <div class="table-responsive">
                        <table class="table table-striped table-bordered align-middle mb-0">
                            <thead class="bg-dark text-white">
                                <tr>
                                    <th style="width: 10%;">Код</th>
                                    <th style="width: 30%;">Описание</th>
                                    <th style="width: 60%;">Возможные причины и решения</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><span class="badge bg-danger">101</span></td>
                                    <td>Перегрев первичного теплообменника</td>
                                    <td class="small">Проверить газовый клапан, прочистить фильтр, мойка/замена теплообменника, проверить циркуляционный насос. (T датчика NTC > 102°C).</td>
                                </tr>
                                <tr>
                                    <td><span class="badge bg-danger">103</span></td>
                                    <td>Недостаточная циркуляция (рост T подачи > 7°C/сек)</td>
                                    <td class="small">Проверить давление/удалить воздух, чистка/замена фильтра, проверить циркуляционный насос.</td>
                                </tr>
                                <tr>
                                    <td><span class="badge bg-danger">108</span></td>
                                    <td>Низкое давление в контуре отопления</td>
                                    <td class="small">Проверить давление (1-1.5 bar), проверить герметичность контура, чистка фильтра.</td>
                                </tr>
                                <tr>
                                    <td><span class="badge bg-danger">110</span></td>
                                    <td>Датчик NTC1 разомкнут или короткое замыкание</td>
                                    <td class="small">Проверить контакты и произвести замену датчика температуры NTC1.</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>

        <div class="tab-pane fade" id="dhw" role="tabpanel" aria-labelledby="dhw-tab">
            <div class="card mt-3 shadow-sm border-0">
                <div class="card-header bg-warning text-dark py-3">
                    <h4 class="h5 mb-0"><i class="fas fa-shower me-2"></i>Ошибки контура ГВС</h4>
                </div>
                <div class="card-body p-0">
                    <div class="table-responsive">
                        <table class="table table-striped table-bordered align-middle mb-0">
                            <thead class="bg-dark text-white">
                                <tr>
                                    <th style="width: 10%;">Код</th>
                                    <th style="width: 30%;">Описание</th>
                                    <th style="width: 60%;">Возможные причины</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><span class="badge bg-warning text-dark">201</span></td>
                                    <td>Короткое замыкание или обрыв датчика температуры ГВС (NTCs)</td>
                                    <td class="small">Проверить электрическую цепь датчика, заменить датчик при необходимости.</td>
                                </tr>
                                <tr>
                                    <td><span class="badge bg-warning text-dark">209</span></td>
                                    <td>Перегрев санитарной воды в бойлере</td>
                                    <td class="small">Проверить термостат и датчик температуры бойлера, проверить настройки температуры ГВС.</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>

        <div class="tab-pane fade" id="board" role="tabpanel" aria-labelledby="board-tab">
            <div class="card mt-3 shadow-sm border-0">
                <div class="card-header bg-info text-white py-3">
                    <h4 class="h5 mb-0"><i class="fas fa-microchip me-2"></i>Ошибки электронной платы</h4>
                </div>
                <div class="card-body p-0">
                    <div class="table-responsive">
                        <table class="table table-striped table-bordered align-middle mb-0">
                            <thead class="bg-dark text-white">
                                <tr>
                                    <th style="width: 10%;">Код</th>
                                    <th style="width: 30%;">Описание</th>
                                    <th style="width: 60%;">Возможные причины и решения</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><span class="badge bg-info">301</span></td>
                                    <td>Ошибка программы платы дисплея</td>
                                    <td class="small">Отсутствует контакт между платами, проверить установку EEPROM ключа, заменить плату дисплея.</td>
                                </tr>
                                <tr>
                                    <td><span class="badge bg-info">303</span></td>
                                    <td>Неисправность основной платы</td>
                                    <td class="small">Плохой контакт между платами, проверить/заменить основную плату.</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>

        <div class="tab-pane fade" id="ignition" role="tabpanel" aria-labelledby="ignition-tab">
            <div class="card mt-3 shadow-sm border-0">
                <div class="card-header bg-success text-white py-3">
                    <h4 class="h5 mb-0"><i class="fas fa-fire me-2"></i>Ошибки розжига и контроля пламени</h4>
                </div>
                <div class="card-body p-0">
                    <div class="table-responsive">
                        <table class="table table-striped table-bordered align-middle mb-0">
                            <thead class="bg-dark text-white">
                                <tr>
                                    <th style="width: 10%;">Код</th>
                                    <th style="width: 30%;">Описание</th>
                                    <th style="width: 60%;">Возможные причины и решения</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><span class="badge bg-success">501</span></td>
                                    <td>Не найдено пламя в момент розжига</td>
                                    <td class="small">Отсутствие газа, проблемы с заземлением (&gt;10V), неисправность электрода ионизации, проверить регулировку плавного розжига.</td>
                                </tr>
                                <tr>
                                    <td><span class="badge bg-success">502</span></td>
                                    <td>Пламя при закрытом газовом клапане</td>
                                    <td class="small">Заменить электрод ионизации, просушить электрод (влага), заменить газовый клапан, проверить заземление.</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>

        <div class="tab-pane fade" id="ventilation" role="tabpanel" aria-labelledby="ventilation-tab">
            <div class="card mt-3 shadow-sm border-0">
                <div class="card-header bg-secondary text-white py-3">
                    <h4 class="h5 mb-0"><i class="fas fa-fan me-2"></i>Ошибки вентиляции и дымоудаления</h4>
                </div>
                <div class="card-body p-0">
                    <div class="table-responsive">
                        <table class="table table-striped table-bordered align-middle mb-0">
                            <thead class="bg-dark text-white">
                                <tr>
                                    <th style="width: 10%;">Код</th>
                                    <th style="width: 30%;">Описание</th>
                                    <th style="width: 60%;">Возможные причины</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><span class="badge bg-secondary">601</span></td>
                                    <td>Срабатывание датчика тяги</td>
                                    <td class="small">Только в моделях с открытой камерой. Проверить дымоход и тягу.</td>
                                </tr>
                                <tr>
                                    <td><span class="badge bg-secondary">604</span></td>
                                    <td>Работа вентилятора с малой скоростью</td>
                                    <td class="small">Скорость менее 1775 об/мин. Неисправность датчика Холла. Проверить вентилятор и электродвигатель.</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>

        <div class="tab-pane fade" id="zones" role="tabpanel" aria-labelledby="zones-tab">
            <div class="card mt-3 shadow-sm border-0">
                <div class="card-header bg-dark text-white py-3">
                    <h4 class="h5 mb-0"><i class="fas fa-temperature-high me-2"></i>Ошибки температурных зон</h4>
                </div>
                <div class="card-body p-0">
                    <div class="table-responsive">
                        <table class="table table-striped table-bordered align-middle mb-0">
                            <thead class="bg-dark text-white">
                                <tr>
                                    <th style="width: 10%;">Код</th>
                                    <th style="width: 30%;">Описание</th>
                                    <th style="width: 60%;">Возможные причины</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><span class="badge bg-dark">701</span></td>
                                    <td>Короткое замыкание или обрыв датчика зоны 2</td>
                                    <td class="small">Проверить электрическую цепь температурного датчика подающей линии зоны 2.</td>
                                </tr>
                                <tr>
                                    <td><span class="badge bg-dark">706</span></td>
                                    <td>Перегрев в температурной зоне 2</td>
                                    <td class="small">Проверить систему отопления зоны 2, проверить настройки термостата зоны.</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
        
    </div>
    
    <div class="alert alert-danger mt-5 shadow-sm p-4 text-white" role="alert">
        <h4 class="alert-heading fw-bold"><i class="fas fa-exclamation-triangle me-2"></i>Важно!</h4>
        <p class="mb-3 fs-6">При возникновении ошибок котла Ariston:</p>
        <div class="content small">
            <ul class="list-unstyled ms-3">
                <li><i class="fas fa-times-circle me-2"></i> <strong>Не пытайтесь самостоятельно ремонтировать газовое оборудование</strong></li>
                <li><i class="fas fa-user-md me-2"></i> <strong>Немедленно обратитесь к квалифицированным специалистам</strong></li>
                <li><i class="fas fa-clipboard-list me-2"></i> Сохраните код ошибки для быстрой диагностики мастером</li>
            </ul>
        </div>
    </div>

    <div class="p-5 rounded-3 text-center text-white shadow-sm mt-5" style="background-color: #009688;">
        <h3 class="h4 mb-3"><i class="fas fa-headset me-2"></i>Нужна профессиональная помощь?</h3>
        <p class="lead mb-4">Наши специалисты быстро диагностируют и устранят любую неисправность котла Ariston</p>
        <div class="row justify-content-center g-3">
            <div class="col-12 col-md-4">
                <a href="tel:+79262211348" class="btn btn-success btn-lg w-100 fw-bold">
                    <i class="fas fa-phone me-2"></i> <span>Позвонить сейчас</span>
                </a>
            </div>
            <div class="col-12 col-md-4">
                <a href="https://service04.ru/contact-us/feedback" class="btn btn-light btn-lg w-100 fw-bold">
                    <i class="fas fa-calendar-check me-2"></i> <span>Записаться на выезд</span>
                </a>
            </div>
        </div>
    </div>
</div>