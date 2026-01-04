---
title: Главная
body_classes: 'title-center title-h1h2'
process:
    twig: true
    markdown: false
---

<style>
    /* Небольшие стили для красоты, которых нет в базовом Bootstrap */
    .service-icon {
        height: 60px;
        width: 60px;
        margin-bottom: 1rem;
    }
    .hover-lift {
        transition: transform 0.2s;
    }
    .hover-lift:hover {
        transform: translateY(-5px);
    }
    .bg-gray-light {
        background-color: #f8f9fa; /* Светло-серый фон */
    }
    .step-number {
        font-size: 2rem;
        font-weight: bold;
        color: #0d6efd; /* Синий цвет Bootstrap */
    }
</style>

<section class="py-5 bg-light text-center border-bottom">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-10">
                <h1 class="display-5 fw-bold mb-3">Профессиональные услуги по ремонту котельного оборудования</h1>
                <p class="lead text-muted mb-4">Наш сервисный центр предлагает профессиональные услуги по ремонту котельного оборудования. Мы специализируемся на обслуживании и восстановлении работоспособности различных типов котлов, включая газовые, электрические и дизельные системы.</p>
                <a class="btn btn-primary btn-lg" href="/uslugi/remont-kotlov">Ремонт котлов »</a>
            </div>
        </div>
    </div>
</section>

<section class="py-5">
    <div class="container">
        <div class="row g-4 justify-content-center">
            <div class="col-md-4">
                <div class="card border-0 shadow-sm h-100 hover-lift">
                    <img src="Service04_3.jpg" class="card-img-top" alt="Исправление ошибок" style="height: 200px; object-fit: cover;">
                </div>
            </div>
            <div class="col-md-4">
                <div class="card border-0 shadow-sm h-100 hover-lift">
                    <img src="service04_1.jpg" class="card-img-top" alt="Диагностика" style="height: 200px; object-fit: cover;">
                </div>
            </div>
            <div class="col-md-4">
                <div class="card border-0 shadow-sm h-100 hover-lift">
                    <img src="service04_2.jpg" class="card-img-top" alt="Ремонт котлов" style="height: 200px; object-fit: cover;">
                </div>
            </div>
        </div>
    </div>
</section>

<section class="py-5" style="background-color: #e9ecef;">
    <div class="container">
        <div class="text-center mb-5">
            <h2 class="fw-bold">Услуги сервисного центра</h2>
            <div class="col-lg-8 mx-auto">
                <p class="lead text-muted">Наш сервисный центр предлагает широкий спектр услуг по ремонту котельного оборудования.</p>
            </div>
        </div>
        <div class="row g-4 text-center">
            <div class="col-md-4">
                <div class="bg-white p-4 rounded shadow-sm h-100">
                    <img class="service-icon" src="arrows_question.svg" alt="Диагностика">
                    <h4>Диагностика котлов и систем</h4>
                    <p class="text-muted">Мы проводим тщательную диагностику вашего котельного оборудования для выявления возможных неисправностей.</p>
                </div>
            </div>
            <div class="col-md-4">
                <div class="bg-white p-4 rounded shadow-sm h-100">
                    <img class="service-icon" src="basic_settings.svg" alt="Ремонт">
                    <h4>Ремонт и замена запчастей</h4>
                    <p class="text-muted">Наша команда использует оригинальные запчасти от ведущих производителей для надежного восстановления.</p>
                </div>
            </div>
            <div class="col-md-4">
                <div class="bg-white p-4 rounded shadow-sm h-100">
                    <img class="service-icon" src="basic_message_multiple.svg" alt="Консультации">
                    <h4>Консультации и рекомендации</h4>
                    <p class="text-muted">Поможем разобраться с любыми вопросами по эксплуатации и обслуживанию оборудования.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="py-5">
    <div class="container">
        <div class="card shadow border-0 overflow-hidden">
            <div class="row g-0 align-items-center">
                <div class="col-lg-5 text-center bg-light">
                    <img src="avtoS04.jpg" alt="Сервис на выезде" class="img-fluid" style="max-height: 400px; object-fit: cover;">
                </div>
                <div class="col-lg-7 p-4 p-md-5">
                    <h3 class="fw-bold text-center mb-4">Почему выбирают нас:</h3>
                    <ul class="list-unstyled">
                        <li class="mb-2"><i class="fas fa-check-circle text-success me-2"></i><strong>Опыт и экспертиза:</strong> Многолетний опыт ремонта котлов.</li>
                        <li class="mb-2"><i class="fas fa-check-circle text-success me-2"></i><strong>Качество работы:</strong> Тщательная проверка после ремонта.</li>
                        <li class="mb-2"><i class="fas fa-check-circle text-success me-2"></i><strong>Быстрое реагирование:</strong> Выезд в день обращения.</li>
                        <li class="mb-2"><i class="fas fa-check-circle text-success me-2"></i><strong>Профессиональный подход:</strong> Полный спектр услуг.</li>
                        <li class="mb-2"><i class="fas fa-check-circle text-success me-2"></i><strong>Конкурентные цены:</strong> Доступные цены при высоком качестве.</li>
                    </ul>
                    <div class="alert alert-warning mt-3 mb-0" role="alert">
                        Если у вас возникли проблемы с котлом – не откладывайте! Обращайтесь к нам.
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="py-5">
    <div class="container">
        <div class="row justify-content-center g-4">
            <div class="col-md-5">
                <div class="p-4 bg-secondary text-white rounded h-100 shadow-sm">
                    <h4 class="fw-bold">Для вас бесплатно</h4>
                    <p class="mb-1">Выезд мастера<br>Диагностика</p>
                    <p class="mb-0">Подбор запчастей<br>Гарантия до 1 года</p>
                </div>
            </div>
            <div class="col-md-5">
                <div class="p-4 bg-info text-white rounded h-100 shadow-sm">
                    <h4 class="fw-bold">Профессиональный<br>ремонт</h4>
                    <p class="mb-0">Ремонт, установка и подключение котельной техники по стандартам качества производителя.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="py-5 bg-gray-light">
    <div class="container">
        <h3 class="text-center fw-bold mb-5" style="color: #3c4858;">Как вызвать мастера на дом?</h3>
        <div class="row g-4">
            <div class="col-md-3 col-sm-6">
                <div class="card h-100 border-0 shadow-sm p-3">
                    <span class="step-number">1.</span>
                    <p class="text-muted">Позвоните нам: <br><strong class="text-dark">+7 (926) 221-13-48</strong> или оставьте заявку.</p>
                    <div class="d-flex gap-3 fs-4 text-primary">
                        <a href="https://tlgg.ru/GazService04" target="_blank"><i class="fab fa-telegram"></i></a>
                        <a href="https://wa.me/79299053839" target="_blank"><i class="fab fa-whatsapp"></i></a>
                        <a href="https://vk.com/service_04" target="_blank"><i class="fab fa-vk"></i></a>
                    </div>
                </div>
            </div>
            <div class="col-md-3 col-sm-6">
                <div class="card h-100 border-0 shadow-sm p-3">
                    <span class="step-number">2.</span>
                    <p class="text-muted">Расскажите о поломке, назовите адрес и пришлите фото котла (для расчёта).</p>
                </div>
            </div>
            <div class="col-md-3 col-sm-6">
                <div class="card h-100 border-0 shadow-sm p-3">
                    <span class="step-number">3.</span>
                    <p class="text-muted">В течение 20–30 минут мастер свяжется с вами и согласует время.</p>
                </div>
            </div>
            <div class="col-md-3 col-sm-6">
                <div class="card h-100 border-0 shadow-sm p-3">
                    <span class="step-number">4.</span>
                    <p class="text-muted">Ремонт за 1 выезд. После ремонта — проверка и акт работ.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="py-5">
    <div class="container">
        <div class="row align-items-center g-4">
            <div class="col-md-4">
                <img src="Screenshot_35.jpg" class="img-fluid rounded shadow" alt="Сервисный центр">
            </div>
            <div class="col-md-8">
                <h4 class="fw-bold mb-3">Собственный сервисный центр</h4>
                <p><strong>Адрес:</strong> г. Москва, ул. 16-я Парковая, д. 36А</p>
                <p>Вы можете привезти технику к нам или вызвать мастера на дом. Наши специалисты используют только качественные запчасти.</p>
                <p><strong>Мы предлагаем:</strong></p>
                <ul class="list-group list-group-flush">
                    <li class="list-group-item border-0 px-0 py-1"><i class="fas fa-check text-primary me-2"></i>Диагностику и ремонт неисправностей</li>
                    <li class="list-group-item border-0 px-0 py-1"><i class="fas fa-check text-primary me-2"></i>Замену деталей и компонентов</li>
                    <li class="list-group-item border-0 px-0 py-1"><i class="fas fa-check text-primary me-2"></i>Чистку и обслуживание системы</li>
                </ul>
            </div>
        </div>
    </div>
</section>

<section class="py-5">
    <div class="container">
        <div class="p-5 bg-light border rounded-3 shadow-sm text-center">
            <h5 class="fw-bold mb-3">Зона обслуживания котельного оборудования</h5>
            <p class="mb-4">Работаем по Москве и всем городам Московской области: <strong>Апрелевка, Балашиха, Видное, Домодедово, Красногорск, Люберцы, Мытищи, Одинцово, Подольск, Химки, Щелково и др.</strong></p>
            <div class="d-inline-block p-3 border border-danger rounded mb-4">
                <p class="text-danger fw-bold mb-1">СНИЖЕНИЕ ЦЕН НА РЕМОНТ КОТЛОВ.</p>
                <p class="text-danger fw-bold mb-0 fs-5">ДИАГНОСТИКА + РЕМОНТ — 4600 руб.! Выезд — 50 руб/км!</p>
            </div>
            <div>
                <a class="btn btn-primary btn-lg" href="/contact-us">Вызвать мастера</a>
            </div>
        </div>
    </div>
</section>