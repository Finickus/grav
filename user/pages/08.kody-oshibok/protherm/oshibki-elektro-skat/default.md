---
title: 'Ошибки электро котла Protherm skat'
---

<div class="container py-5">

    <div class="p-5 mb-5 text-white text-center rounded-3 shadow-sm" style="background-color: #009688;">
        <h1 class="display-5 fw-bold">
            <i class="fas fa-exclamation-triangle me-3"></i>Ошибки электрического котла Протерм Скат (версия 13)
        </h1>
        <p class="lead">Сообщения об ошибках - код F. Диагностика и устранение</p>
    </div>

    <div class="card shadow-sm border-0 mb-5">
        <div class="card-body p-4">
            <p class="lead fs-6">При индикации состояний неисправности котла посредством изображения кода ошибки на дисплее начинает мигать буква <strong>«F»</strong> вместе с соответствующим двузначным числом. В данном случае это означает, что котел вышел из строя, и необходим вызов квалифицированного специалиста.</p>
        </div>
    </div>

    <div class="card shadow-sm border-0 mb-5">
        <div class="card-header bg-danger text-white py-3">
            <h4 class="h5 mb-0"><i class="fas fa-table me-2"></i>Сводная таблица кодов ошибок Protherm Skat</h4>
        </div>
        <div class="card-body p-0">
            <div class="table-responsive">
                <table class="table table-bordered table-striped table-hover align-middle mb-0">
                    <thead class="bg-dark text-white">
                        <tr>
                            <th style="width: 10%;">Код</th>
                            <th style="width: 40%;">Значение</th>
                            <th style="width: 50%;">Устранение (Первые шаги)</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="table-info-subtle">
                            <td>F.00/F.10/F.13/F.19</td>
                            <td>Ошибка датчика температуры (NTC)</td>
                            <td>Проверьте кабельные соединения. Замените датчик или электронную плату.</td>
                        </tr>
                        <tr>
                            <td><a href="#F20" class="text-danger fw-bold">F.20</a></td>
                            <td>Защитное отключение: предохранительный ограничитель температуры (Перегрев)</td>
                            <td>Снова включите котел. Проверьте и закоротите/замените предохранительный ограничитель температуры. Найдите причину перегрева.</td>
                        </tr>
                        <tr>
                            <td><a href="#F22" class="text-primary fw-bold">F.22</a></td>
                            <td>Сухой старт / Недостаточное давление воды (&lt; 0,6 бар)</td>
                            <td>Проверьте давление воды. Проверьте герметичность, расширительный бак, удалите воздух из системы. Повысьте давление.</td>
                        </tr>
                        <tr>
                            <td><a href="#F41" class="text-warning fw-bold">F.41</a></td>
                            <td>Заедание реле (HDO)</td>
                            <td>Выключите и снова включите котел. Верните настройки к заводским (D.096). Обратитесь в сервисную службу.</td>
                        </tr>
                        <tr>
                            <td>F.55</td>
                            <td>Заедание контактора или реле</td>
                            <td>Обесточьте котел. Проверьте контакторы и реле на предмет дефектов и при необходимости замените.</td>
                        </tr>
                        <tr>
                            <td><a href="#F63" class="text-danger fw-bold">F.63</a></td>
                            <td>Сбой связи с EEPROM</td>
                            <td>Верните настройки изделия к заводским (D.096) и перезапустите котел.</td>
                        </tr>
                        <tr>
                            <td><a href="#F73" class="text-primary fw-bold">F.73/F.74</a></td>
                            <td>Сигнал датчика давления воды вне верном диапазоне (обрыв/КЗ)</td>
                            <td>Проверьте провод к датчику давления. Замените датчик давления воды.</td>
                        </tr>
                        <tr>
                            <td><a href="#F85" class="text-danger fw-bold">F.85</a></td>
                            <td>Замерзла вода в котле</td>
                            <td>Котел автоматически отключится при &lt; 3°C и включится при &gt; 4°C. Выявите причину замерзания.</td>
                        </tr>
                        <tr>
                            <td><a href="#F86" class="text-danger fw-bold">F.86</a></td>
                            <td>Замерз внешний водонагреватель</td>
                            <td>Котел автоматически отключится при &lt; 3°C и включится при &gt; 4°C. Проверьте внешнюю систему ГВС.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <div class="card shadow-sm border-0 mb-5">
        <div class="card-header bg-info text-white py-3">
            <h4 class="h5 mb-0"><i class="fas fa-search me-2"></i>Детализация неисправностей (F-коды)</h4>
        </div>
        <div class="card-body p-4">
            
            <div class="accordion" id="prothermErrorsAccordion">

                <div class="accordion-item">
                    <h2 class="accordion-header" id="headingF00">
                        <button class="accordion-button fw-bold text-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseF00" aria-expanded="true">
                            F.00 / F.10 / F.13 / F.19 — Ошибки датчиков температуры NTC (ОВ, ГВС, наружный)
                        </button>
                    </h2>
                    <div id="collapseF00" class="accordion-collapse collapse show" data-bs-parent="#prothermErrorsAccordion">
                        <div class="accordion-body">
                            <p class="mb-3">Эти ошибки указывают на обрыв или короткое замыкание в цепи одного из температурных датчиков NTC. Размыкание цепи (F.00) регистрируется при напряжении > 4,75 В; короткое замыкание (F.10, F.13, F.19) — при напряжении < 0,45 В.</p>
                            
                            <h6 class="fw-bold mt-3">Детали ошибок:</h6>
                            <ul class="list-unstyled ms-3 small">
                                <li><strong>F.00</strong>: Размыкание цепи NTC датчика на выводе ОВ.</li>
                                <li><strong>F.10</strong>: Короткое замыкание NTC датчика на выводе ОВ.</li>
                                <li><strong>F.13</strong>: Короткое замыкание NTC датчика внешнего накопительного бака ГВС.</li>
                                <li><strong>F.19</strong>: Короткое замыкание датчика наружной температуры (игнорируется при неактивном эквитермическом регулировании).</li>
                            </ul>
                            
                            <h6 class="fw-bold text-danger mt-3">РЕКОМЕНДАЦИИ:</h6>
                            <ul class="list-unstyled ms-3">
                                <li>Проверьте соединение и кабели датчиков на плате.</li>
                                <li>Проверьте датчик мультиметром (сопротивление NTC). Замените при необходимости.</li>
                            </ul>
                            
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <h2 class="accordion-header" id="headingF20">
                        <button class="accordion-button collapsed fw-bold text-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseF20" id="F20">
                            F.20 — Защитное отключение: Сработал предохранительный ограничитель температуры
                        </button>
                    </h2>
                    <div id="collapseF20" class="accordion-collapse collapse" data-bs-parent="#prothermErrorsAccordion">
                        <div class="accordion-body">
                            <p class="mb-3">Неисправность индицируется при активации аварийного термостата в результате перегрева котла. **Требуется найти и устранить причину перегрева!**</p>

                            <h6 class="fw-bold">Действия для сброса (старые модели):</h6>
                            <ul class="list-unstyled ms-3">
                                <li>Найдите аварийный термостат (на медной трубе или теплообменнике).</li>
                                <li>Снимите защитную оболочку и нажмите красную кнопку для сброса.</li>
                            </ul>
                            
                            <h6 class="fw-bold text-danger mt-3">Возможные причины перегрева:</h6>
                            <ul class="list-unstyled ms-3">
                                <li>Воздух в теплообменнике котла.</li>
                                <li>Блокировка циркуляционного насоса (нет протока через аппарат).</li>
                                <li>Неисправность термостата перегрева (нужна замена).</li>
                            </ul>
                            
                            <h6 class="fw-bold text-info mt-3">Проверка циркуляции:</h6>
                            <ul class="list-unstyled ms-3">
                                <li>Проверьте насос (Wilo): открутите заглушку для стравливания воздуха и проверьте вращение вала. При неисправности замените насос или его голову.</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <h2 class="accordion-header" id="headingF22">
                        <button class="accordion-button collapsed fw-bold text-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseF22" id="F22">
                            F.22 — Потеря воды / Сухой старт: Недостаточное давление воды
                        </button>
                    </h2>
                    <div id="collapseF22" class="accordion-collapse collapse" data-bs-parent="#prothermErrorsAccordion">
                        <div class="accordion-body">
                            <p class="mb-3">Ошибка индицируется, если давление воды в системе отопления снижается ниже **0,6 баров**. Сообщение автоматически удаляется после повышения давления выше 0,6 бар (подпитка).</p>

                            <h6 class="fw-bold text-danger">Принцип действия датчика давления:</h6>
                            <p class="small">Датчик (на основе эффекта Холла) измеряет изменение магнитного поля, связанное с объемом мембраны (давлением воды). Контрольные значения: 1 бар / 1,7 В DC; 1,5 бара / 2 В DC; 2 бара / 2,3 В DC.</p>

                            <h6 class="fw-bold text-success mt-3">РЕКОМЕНДАЦИИ:</h6>
                            <ul class="list-unstyled ms-3">
                                <li><strong>Подпитка:</strong> Слишком низкое давление (< 0.3 Бар). Заполните котел водой (кнопка RESET не требуется).</li>
                                <li><strong>Утечки:</strong> Проверьте утечки в котле и системе отопления.</li>
                                <li><strong>Неисправности:</strong> Проверьте насос (возможна блокировка). Замените датчик давления воды, если он неисправен.</li>
                            </ul>
                            
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <h2 class="accordion-header" id="headingF41">
                        <button class="accordion-button collapsed fw-bold text-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseF41" id="F41">
                            F.41 — «Залипшее» реле (HDO)
                        </button>
                    </h2>
                    <div id="collapseF41" class="accordion-collapse collapse" data-bs-parent="#prothermErrorsAccordion">
                        <div class="accordion-body">
                            <p class="mb-3">Сообщение появляется после **5 неудачных попыток котла "разлепить" реле**. Котел работает на минимальный нагрев. После отключения и повторного включения котел запустится, но проблема будет сигнализироваться миганием светодиода HDO.</p>
                            
                            <h6 class="fw-bold text-danger">Проверка:</h6>
                            <ul class="list-unstyled ms-3">
                                <li>Проблема связана с состоянием функции отопления, когда нагревательные элементы должны быть отключены.</li>
                                <li>Функция активируется, когда температура превышает заданное значение на 5 °C.</li>
                            </ul>

                            <h6 class="fw-bold text-warning mt-3">УСТРАНЕНИЕ:</h6>
                            <ul class="list-unstyled ms-3">
                                <li>Выключите и снова включите котел.</li>
                                <li>Верните настройки изделия к заводским (код D.096).</li>
                                <li>Если ошибка повторяется, **обратитесь в специализированную сервисную организацию**.</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <h2 class="accordion-header" id="headingF63">
                        <button class="accordion-button collapsed fw-bold text-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseF63" id="F63">
                            F.63 — Ошибка памяти EEPROM
                        </button>
                    </h2>
                    <div id="collapseF63" class="accordion-collapse collapse" data-bs-parent="#prothermErrorsAccordion">
                        <div class="accordion-body">
                            <p class="mb-3">Сообщение появляется при возникновении проблем с данными, уложенными в памяти EEPROM, или ошибке в коммуникации EEPROM.</p>
                            
                            <h6 class="fw-bold text-warning">РЕКОМЕНДАЦИИ:</h6>
                            <ol class="ms-3">
                                <li><strong>Обновление заводских настроек (D.096):</strong> Перепрограммируйте заводские настройки (код d.96).</li>
                                <li><strong>Настройка мощности:</strong> Настройте мощность котла (код d.93) согласно инструкции (1 для 6 кВт, 8 для 28 кВт и т.д.).</li>
                                <li>Полностью отключите котел на 5 минут и включите вновь.</li>
                            </ol>
                            <p class="mt-3 text-danger fw-bold">Если это не дало требуемого результата, необходимо обратиться в сервисный центр.</p>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <h2 class="accordion-header" id="headingF73">
                        <button class="accordion-button collapsed fw-bold text-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseF73" id="F73">
                            F.73 / F.74 — Короткое замыкание / Размыкание цепи датчика давления ОВ
                        </button>
                    </h2>
                    <div id="collapseF73" class="accordion-collapse collapse" data-bs-parent="#prothermErrorsAccordion">
                        <div class="accordion-body">
                            <p class="mb-3">Эти ошибки указывают на выход сигнала датчика давления за пределы допустимого диапазона (вне 1 В - 4 В), что часто связано с неисправностью самого датчика или проводки.</p>
                            
                            <h6 class="fw-bold mt-3">Детали ошибок:</h6>
                            <ul class="list-unstyled ms-3 small">
                                <li><strong>F.73</strong>: Короткое замыкание (сигнал — GND) или размыкание цепи (напряжение < 1 В).</li>
                                <li><strong>F.74</strong>: Короткое замыкание (сигнал — +5 В) (напряжение > 4 В).</li>
                            </ul>

                            <h6 class="fw-bold text-danger mt-3">РЕКОМЕНДАЦИИ:</h6>
                            <ul class="list-unstyled ms-3">
                                <li>Проверьте разъем и проводку датчика.</li>
                                <li>Нажмите RESET. Если ошибка повторяется, <strong>замените датчик давления</strong>.</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <h2 class="accordion-header" id="headingF85">
                        <button class="accordion-button collapsed fw-bold text-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseF85" id="F85">
                            F.85 / F.86 — Замерзание воды в котле / накопительном баке ГВС
                        </button>
                    </h2>
                    <div id="collapseF85" class="accordion-collapse collapse" data-bs-parent="#prothermErrorsAccordion">
                        <div class="accordion-body">
                            <p class="mb-3">Сообщение появляется при падении температуры, отображаемой NTC датчиком, ниже **3 °C**.</p>
                            <p class="mb-3">Котел автоматически заблокируется. Разблокировка происходит автоматически при повышении температуры воды свыше **4 °C**.</p>

                            <h6 class="fw-bold text-danger">РЕКОМЕНДАЦИИ:</h6>
                            <ul class="list-unstyled ms-3">
                                <li><strong>Отогрев:</strong> Используйте фен для прогрева верхней части котла, где установлен датчик. Можно отключить датчик и прогреть его в руке.</li>
                                <li><strong>Причина:</strong> Немедленно выясните причину остановки котла и замерзания (например, отключение электричества).</li>
                            </ul>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </div>

    <div class="p-5 rounded-3 text-center text-white" style="background-color: #009688;">
        <h3 class="h4 mb-3"><i class="fas fa-user-md me-2"></i>Нужна помощь с котлом Protherm Skat?</h3>
        <p class="lead mb-4">Наши специалисты помогут диагностировать и устранить неисправность!</p>
        <div class="row justify-content-center g-3">
            <div class="col-12 col-md-4">
                <a href="tel:+79262211348" class="btn btn-light btn-lg w-100 fw-bold">
                    <i class="fas fa-phone me-2"></i> Позвонить
                </a>
            </div>
            <div class="col-12 col-md-4">
                <a href="https://service04.ru/contact-us/feedback" class="btn btn-warning btn-lg w-100 fw-bold text-dark">
                    <i class="fas fa-envelope me-2"></i> Оставить заявку
                </a>
            </div>
        </div>
    </div>

</div>