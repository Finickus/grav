---
title: 'Стоимость ремонта котельного оборудования'
---

<!-- Заголовок -->
<section class="section" style="background-color: #009688; color: white; border-radius: 8px; margin-bottom: 2rem;">
<div class="container text-center">

<p class="h5 lead">Прозрачные и выгодные цены на услуги наших мастеров</p>
</div>
</section>
<!-- Вступление -->
<div class="card mb-5">
<p class="h5 lead">Наша компания предлагает <strong>профессиональный ремонт котельного оборудования</strong> по <strong>прозрачным и выгодным ценам</strong>.</p>
<p>Мы работаем оперативно и качественно, чтобы ваше оборудование снова работало без перебоев!</p>
</div>
<!-- Стоимость работ -->
<div class="card mb-5">
<h2 class="h4 display-4 mb-4" style="color: #17a2b8;"><i class="fas fa-ruble-sign"></i> Стоимость работ (без учета запчастей)</h2>
<div class="row g-3 is-centered"><!-- Выезд мастера -->
<div class="col-md-12 is-6-desktop">
<div class="price-card" style="border: 2px solid #009688;">
<h5><i class="fas fa-truck-loading price-primary"></i> Выезд мастера</h5>
<p>До 15 км от МКАД</p>
<div class="price price-primary">5 000 ₽</div>
</div>
</div>
<!-- Доплата за километраж -->
<div class="col-md-12 is-6-desktop">
<div class="price-card" style="border: 2px solid #17a2b8;">
<h5><i class="fas fa-road price-info"></i> Доплата за километраж</h5>
<p>Свыше 15 км от МКАД</p>
<div class="price price-info">50 ₽/км</div>
</div>
</div>
<!-- Первые 2 часа -->
<div class="col-md-12 is-6-desktop">
<div class="price-card" style="border: 2px solid #28a745;">
<h5><i class="fas fa-clock price-success"></i> Первые 2 часа работы</h5>
<p>Включает диагностику и начало ремонта</p>
<div class="price price-success">4 000 ₽</div>
</div>
</div>
<!-- Каждый последующий час -->
<div class="col-md-12 is-6-desktop">
<div class="price-card" style="border: 2px solid #ffc107; color: #333;">
<h5><i class="fas fa-history price-warning"></i> Каждый последующий час</h5>
<p>После первых двух часов</p>
<div class="price price-warning">2 500 ₽</div>
</div>
</div>
</div>
</div>
<!-- Особые условия (аккордеон без JS) -->
<div class="card mb-5">
<h3 class="h5 mb-3" style="color: #e37a25;"><i class="fas fa-exclamation-circle"></i> Особые условия</h3>
<!-- Срочный выезд -->
<div class="accordion-header" onclick="toggleAccordion('urgent')"><i class="fas fa-ambulance me-3"></i> Срочный выезд, праздничные дни</div>
<div class="accordion-content" id="content-urgent">
<p><strong>Двойной тариф</strong> применяется ко всем видам работ при срочном выезде или в праздничные дни.</p>
</div>
<!-- Выходные дни -->
<div class="accordion-header" onclick="toggleAccordion('weekend')"><i class="fas fa-calendar-week me-3"></i> Выходные дни</div>
<div class="accordion-content hidden" id="content-weekend">
<p>К стоимости работ применяется <strong>наценка +50%</strong> в выходные дни (суббота, воскресенье).</p>
</div>
</div>
<!-- Призыв к действию -->
<div class="card bg-primary text-white text-center">
<h3 class="h4 display-4"><i class="fas fa-phone-alt"></i> Нужен ремонт котельного оборудования?</h3>
<p class="h5 lead">Звоните для консультации и вызова мастера!</p>
<div class="row justify-content-center">
<div class="col-4"><a href="tel:+79262211348" class="btn btn-light w-100 btn-lg"> <i class="fas fa-phone me-3"></i> Позвонить </a></div>
<div class="col-4"><a href="https://service04.ru/contact-us/feedback" class="btn btn-warning w-100 btn-lg" style="color: #333;"> <i class="fas fa-envelope me-3"></i> Оставить заявку </a></div>
</div>
</div>
<!-- Простой аккордеон на чистом JS -->
<script>
  function toggleAccordion(id) {
    const content = document.getElementById('content-' + id);
    content.classList.toggle('hidden');
  }
</script>