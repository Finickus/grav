---
title: Стоимость
login: {  }
process:
    twig: true
    markdown: false
---

<div class="container py-4">

    <div class="p-5 mb-4 text-white rounded-3 text-center" style="background-color: #009688;">
        <h1 class="display-6 fw-bold"><i class="fas fa-wrench"></i> Стоимость ремонта котельного оборудования</h1>
        <p class="lead">Прозрачные и выгодные цены на услуги наших мастеров</p>
    </div>

    <div class="card shadow-sm border-0 mb-5">
        <div class="card-body p-4 text-center">
            <h5 class="card-title">Профессиональный подход</h5>
            <p class="card-text">
                Наша компания предлагает <strong>профессиональный ремонт котельного оборудования</strong> по <strong>прозрачным и выгодным ценам</strong>.<br>
                Мы работаем оперативно и качественно, чтобы ваше оборудование снова работало без перебоев!
            </p>
        </div>
    </div>

    <div class="card shadow-sm border-0 mb-5">
        <div class="card-body">
            <h2 class="h4 mb-4 text-center" style="color: #17a2b8;">
                <i class="fas fa-ruble-sign"></i> Стоимость работ (без учета запчастей)
            </h2>
            
            <div class="row g-4 justify-content-center">
                <div class="col-12 col-md-6">
                    <div class="card h-100 text-center" style="border: 2px solid #009688;">
                        <div class="card-body">
                            <h5 class="card-title"><i class="fas fa-truck-loading text-success"></i> Выезд мастера</h5>
                            <p class="card-text text-muted">До 15 км от МКАД</p>
                            <div class="fs-4 fw-bold" style="color: #009688;">6500 ₽</div>
                        </div>
                    </div>
                </div>

                <div class="col-12 col-md-6">
                    <div class="card h-100 text-center" style="border: 2px solid #17a2b8;">
                        <div class="card-body">
                            <h5 class="card-title"><i class="fas fa-road text-info"></i> Доплата за километраж</h5>
                            <p class="card-text text-muted">Свыше 15 км от МКАД</p>
                            <div class="fs-4 fw-bold text-info">50 ₽/км</div>
                        </div>
                    </div>
                </div>

                <div class="col-12 col-md-6">
                    <div class="card h-100 text-center" style="border: 2px solid #28a745;">
                        <div class="card-body">
                            <h5 class="card-title"><i class="fas fa-clock text-success"></i> Первый час работы</h5>
                            <p class="card-text text-muted">Включает диагностику и начало ремонта</p>
                            <div class="fs-4 fw-bold text-success">3500 ₽</div>
                        </div>
                    </div>
                </div>

                <div class="col-12 col-md-6">
                    <div class="card h-100 text-center" style="border: 2px solid #ffc107;">
                        <div class="card-body">
                            <h5 class="card-title"><i class="fas fa-history text-warning"></i> Каждый последующий час</h5>
                            <p class="card-text text-muted">Последующий</p>
                            <div class="fs-4 fw-bold text-warning">4500 ₽ норма/час</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="card shadow-sm border-0 mb-5">
        <div class="card-body">
            <h3 class="h5 mb-3" style="color: #e37a25;"><i class="fas fa-exclamation-circle"></i> Особые условия</h3>
            
            <div class="accordion" id="accordionConditions">
                <div class="accordion-item">
                    <h2 class="accordion-header" id="headingUrgent">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseUrgent" aria-expanded="false" aria-controls="collapseUrgent">
                            <i class="fas fa-ambulance me-3 text-danger"></i> Срочный выезд, праздничные дни
                        </button>
                    </h2>
                    <div id="collapseUrgent" class="accordion-collapse collapse" aria-labelledby="headingUrgent" data-bs-parent="#accordionConditions">
                        <div class="accordion-body">
                            <strong>Двойной тариф</strong> применяется ко всем видам работ при срочном выезде или в праздничные дни.
                        </div>
                    </div>
                </div>
                
                <div class="accordion-item">
                    <h2 class="accordion-header" id="headingWeekend">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseWeekend" aria-expanded="false" aria-controls="collapseWeekend">
                            <i class="fas fa-calendar-week me-3 text-primary"></i> Выходные дни
                        </button>
                    </h2>
                    <div id="collapseWeekend" class="accordion-collapse collapse" aria-labelledby="headingWeekend" data-bs-parent="#accordionConditions">
                        <div class="accordion-body">
                            К стоимости работ применяется <strong>наценка +50%</strong> в выходные дни (суббота, воскресенье).
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="p-5 rounded-3 text-center text-white bg-success bg-gradient">
        <h3 class="h4 mb-3"><i class="fas fa-phone-alt"></i> Нужен ремонт котельного оборудования?</h3>
        <p class="lead mb-4">Звоните для консультации и вызова мастера!</p>
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