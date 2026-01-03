---
title: 'Контент'
---

<!DOCTYPE html>
<html>
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .col-lg-9 { border-right: 1px solid #ddd; padding-right: 15px; }
        .col-lg-3 {
            position: sticky;
            top: 70px;
            height: fit-content;
            max-height: calc(100vh - 100px);
            overflow-y: auto;
            background: #f8f9fa;
            padding: 10px;
        }
        .row { align-items: start; }
        body { padding-top: 70px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-lg-9">
                
                <?php for ($i=0; $i<50; $i++) echo "<p>Строка $i</p>"; ?>
            </div>
            <aside class="col-lg-3">
                <h5>Сайдбар</h5>
                <?php for ($i=0; $i<20; $i++) echo "<p>Пункт $i</p>"; ?>
            </aside>
        </div>
    </div>
</body>
</html>