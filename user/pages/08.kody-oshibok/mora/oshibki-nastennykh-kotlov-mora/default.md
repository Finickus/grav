---
title: 'Ошибки настенных котлов Мора'
---

<div class="container py-5">
    <div class="text-center mb-5">
        <h1 class="fw-bold h2 text-dark">
            <i class="fas fa-exclamation-triangle text-danger me-3"></i>Ошибки настенных котлов Мора
        </h1>
        <p class="lead text-muted">Справочник по диагностике и устранению неисправностей линейки MORA Top</p>
    </div>

    <div class="card border-0 shadow-sm mb-5 bg-light">
        <div class="card-body">
            <h3 class="h5 fw-bold mb-4 text-center text-md-start"><i class="fas fa-book me-2"></i> Быстрая навигация</h3>
            <div class="d-flex flex-wrap justify-content-center gap-2" id="error-nav">
                <button class="btn btn-primary px-4 shadow-sm" data-target="e0">E0</button>
                <button class="btn btn-outline-primary px-4 shadow-sm" data-target="e1">E1</button>
                <button class="btn btn-outline-primary px-4 shadow-sm" data-target="e2">E2</button>
                <button class="btn btn-outline-primary px-4 shadow-sm" data-target="e3">E3</button>
                <button class="btn btn-outline-primary px-4 shadow-sm" data-target="e4">E4</button>
                <button class="btn btn-outline-primary px-4 shadow-sm" data-target="e5">E5</button>
                <button class="btn btn-outline-secondary px-3 shadow-sm" data-target="no-display">Без дисплея</button>
                <button class="btn btn-outline-success px-4 shadow-sm" data-target="service">ТО</button>
            </div>
        </div>
    </div>

    <div id="error-e0" class="error-section">
        <div class="card shadow border-0 mb-4 overflow-hidden">
            <div class="card-header bg-danger text-white py-3">
                <h3 class="h4 mb-0"><i class="fas fa-fire me-2"></i> Ошибка E0 — Горелка не запускается</h3>
            </div>
            <div class="card-body p-4 p-md-5">
                <div class="row g-4">
                    <div class="col-md-5 text-center">
                        <img src="1.jpg" alt="Ошибка E0" class="img-fluid rounded shadow-sm border">
                    </div>
                    <div class="col-md-7">
                        <p class="text-muted mb-4">Основная горелка потухла и не запускается, циркуляционный насос не функционирует. Элементы блока управления повреждены или дефектны.</p>
                        <h4 class="h5 fw-bold mb-3 text-danger">Причины:</h4>
                        <ul class="mb-4 small">
                            <li>Газовый клапан закрыт или неисправен.</li>
                            <li>Насос не циркулирует теплоноситель.</li>
                            <li>Неисправна основная плата управления.</li>
                        </ul>
                        <h4 class="h5 fw-bold mb-3 text-success">Устранение:</h4>
                        <ol class="small">
                            <li>Проверить подачу газа и катушку газового клапана.</li>
                            <li>Продиагностировать плату управления на наличие прогаров.</li>
                            <li>Вызвать мастера для профессиональной настройки.</li>
                        </ol>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div id="error-e1" class="error-section d-none">
        <div class="card shadow border-0 mb-4 overflow-hidden">
            <div class="card-header bg-primary text-white py-3">
                <h3 class="h4 mb-0"><i class="fas fa-tint me-2"></i> Ошибка E1 — Нет циркуляции / Давление</h3>
            </div>
            <div class="card-body p-4 p-md-5">
                <div class="row g-4 text-center text-md-start">
                    <div class="col-md-5">
                        <img src="2.jpg" alt="Ошибка E1" class="img-fluid rounded shadow-sm border">
                    </div>
                    <div class="col-md-7">
                        <h4 class="h5 fw-bold mb-3 text-primary">Почему возникла:</h4>
                        <ul class="mb-4 small">
                            <li>Низкое давление теплоносителя в системе.</li>
                            <li>Засорение фильтра грубой очистки.</li>
                            <li>Воздушная пробка в теплообменнике или насосе.</li>
                            <li>Заклинивание вала циркуляционного насоса.</li>
                        </ul>
                        <h4 class="h5 fw-bold mb-3 text-success">Как исправить:</h4>
                        <ol class="small">
                            <li>Долить воду в систему до 1.2 – 1.5 бар.</li>
                            <li>Прочистить сетчатый фильтр ("грязевик").</li>
                            <li>Проверить вращение вала насоса (прокрутить отверткой).</li>
                        </ol>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div id="error-e2" class="error-section d-none">
        <div class="card shadow border-0 mb-4 overflow-hidden text-center text-md-start">
            <div class="card-header bg-warning py-3">
                <h3 class="h4 mb-0 fw-bold"><i class="fas fa-bolt me-2"></i> Ошибка E2 — Срыв пламени</h3>
            </div>
            <div class="card-body p-4 p-md-5">
                <div class="row g-4">
                    <div class="col-md-5 text-center">
                        <img src="3.jpg" alt="Ошибка E2" class="img-fluid rounded shadow-sm border">
                    </div>
                    <div class="col-md-7">
                        <p class="text-muted small mb-4">Котел разжигается, но через несколько секунд тухнет. Блок управления не видит ионизацию (пламя).</p>
                        
                        <h4 class="h5 fw-bold mb-3">Возможные причины:</h4>
                        <ul class="small mb-4">
                            <li>Несоблюдение полярности (фаза/ноль) при включении в розетку.</li>
                            <li>Загрязнение электрода ионизации.</li>
                            <li>Проблемы с тягой (засорен дымоход).</li>
                        </ul>
                        <a href="tel:+79262211348" class="btn btn-dark shadow-sm">Нужна диагностика платы</a>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div id="error-e3" class="error-section d-none"><div class="alert alert-light border p-5 text-center shadow-sm"><h5>Информация по E3 подготавливается...</h5></div></div>
    <div id="error-e4" class="error-section d-none"><div class="alert alert-light border p-5 text-center shadow-sm"><h5>Информация по E4 подготавливается...</h5></div></div>
    <div id="error-e5" class="error-section d-none"><div class="alert alert-light border p-5 text-center shadow-sm"><h5>Информация по E5 подготавливается...</h5></div></div>

    <div id="error-no-display" class="error-section d-none">
        <div class="card shadow border-0 mb-4">
            <div class="card-header bg-secondary text-white py-3">
                <h3 class="h4 mb-0 fw-bold"><i class="fas fa-display me-2"></i> Котлы без цифрового табло</h3>
            </div>
            <div class="card-body p-4">
                <div class="row g-4 align-items-center mb-4">
                    <div class="col-md-4"><img src="7.jpg" alt="Котлы без цифрового табло" class="img-fluid rounded border shadow-sm"></div>
                    <div class="col-md-8">
                        <h5>Типичная проблема: Падение мощности</h5>
                        <p class="small text-muted">Котел работает, но не может прогреть радиаторы до нужной температуры.</p>
                    </div>
                </div>
                <div class="accordion border rounded overflow-hidden shadow-sm">
                    <details class="p-3 border-bottom bg-white">
                        <summary class="fw-bold cursor-pointer"><i class="fas fa-search me-2 text-primary"></i> Причины падения мощности</summary>
                        <div class="mt-3 small px-3">
                            <p>Зачастую это дефект модуляционной катушки газового клапана или сбитые настройки давления газа.</p>
                            <img src="8.jpg" alt="Типичная проблема: Падение мощности" class="img-fluid rounded mt-2 border" style="max-height: 200px;">
                        </div>
                    </details>
                    <details class="p-3 bg-white">
                        <summary class="fw-bold cursor-pointer"><i class="fas fa-water me-2 text-info"></i> Плохо греет горячую воду (ГВС)</summary>
                        <div class="mt-3 small px-3">
                            <p>Причина в 90% случаев — накипь во вторичном теплообменнике.</p>
                            <img src="9.jpg" alt="Типичная проблема: Падение мощности" class="img-fluid rounded mt-2 border" style="max-height: 200px;">
                        </div>
                    </details>
                </div>
            </div>
        </div>
    </div>

    <div id="error-service" class="error-section d-none">
        <div class="card shadow border-0 mb-4 border-start border-success border-5">
            <div class="card-body p-4 p-md-5">
                <div class="row g-4 align-items-center">
                    <div class="col-md-5">
                        <img src="10.jpg" alt="ТО" class="img-fluid rounded shadow-sm border">
                    </div>
                    <div class="col-md-7">
                        <h3 class="h4 fw-bold text-success mb-3">Профилактика и сервис</h3>
                        <p class="small">Для стабильной работы котлы Mora Top требуют ежегодной чистки горелки и проверки давления в расширительном баке.</p>
                        <div class="alert alert-info border-0 shadow-sm small">
                            <i class="fas fa-info-circle me-2"></i> Проводите ТО 1 раз в год перед началом сезона.
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="card bg-warning bg-opacity-10 border-warning border-start border-5 shadow-sm mt-5">
        <div class="card-body p-4">
            <h4 class="h5 fw-bold mb-4"><i class="fas fa-lightbulb me-2 text-warning"></i> Важные рекомендации</h4>
            <div class="row g-4 small">
                <div class="col-md-6 d-flex">
                    <i class="fas fa-shield-check text-success fs-3 me-3"></i>
                    <div>
                        <h5 class="h6 fw-bold">Безопасность</h5>
                        <p class="mb-0">При появлении запаха газа немедленно перекройте вентиль и обесточьте котел.</p>
                    </div>
                </div>
                <div class="col-md-6 d-flex">
                    <i class="fas fa-user-md text-primary fs-3 me-3"></i>
                    <div>
                        <h5 class="h6 fw-bold">Мастер на связи</h5>
                        <p class="mb-0">Самостоятельный ремонт газового оборудования может быть опасен. Консультация: <a href="tel:+79262211348">+7 (926) 221-13-48</a></p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('button[data-target]');
    const sections = document.querySelectorAll('.error-section');

    buttons.forEach(button => {
        button.addEventListener('click', function () {
            const target = this.getAttribute('data-target');

            // Скрыть все
            sections.forEach(s => s.classList.add('d-none'));

            // Показать нужную
            const targetSection = document.getElementById('error-' + target);
            if (targetSection) targetSection.classList.remove('d-none');

            // Стилизация кнопок
            buttons.forEach(btn => {
                btn.classList.remove('btn-primary', 'btn-secondary', 'btn-success');
                btn.classList.add('btn-outline-primary');
                if (btn.dataset.target === 'no-display') btn.classList.replace('btn-outline-primary', 'btn-outline-secondary');
                if (btn.dataset.target === 'service') btn.classList.replace('btn-outline-primary', 'btn-outline-success');
            });

            if (target === 'no-display') {
                this.classList.replace('btn-outline-secondary', 'btn-secondary');
            } else if (target === 'service') {
                this.classList.replace('btn-outline-success', 'btn-success');
            } else {
                this.classList.replace('btn-outline-primary', 'btn-primary');
            }
        });
    });
});
</script>

<style>
    .cursor-pointer { cursor: pointer; }
    .error-section { animation: fadeIn 0.4s ease-in-out; }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
</style>