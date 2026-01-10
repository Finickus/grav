/**
 * ProductDiv Configuration для Grav CMS с Bootstrap 5.3
 * Конфигурация включает utility classes и готовые шаблоны компонентов
 */

window.ProductDivConfig = {
    configuration: {
        // Элементы, игнорируемые в Tree View
        treeViewIgnoreQuerySelectors: [
            'script',
            'style',
            'link',
            '[data-productdiv="true"]',
            'svg',
            'noscript',
            'meta'
        ],

        // Bootstrap 5.3 Utility Classes
        utilityClasses: [
            // === SPACING ===
            {
                name: 'Margin',
                type: 'selectMany',
                classes: [
                    'm-(0|1|2|3|4|5|auto)',
                    'mt-(0|1|2|3|4|5|auto)',
                    'mb-(0|1|2|3|4|5|auto)',
                    'ms-(0|1|2|3|4|5|auto)',
                    'me-(0|1|2|3|4|5|auto)',
                    'mx-(0|1|2|3|4|5|auto)',
                    'my-(0|1|2|3|4|5|auto)',
                    'm-(sm|md|lg|xl|xxl)-(0|1|2|3|4|5|auto)',
                ],
                tags: ['Spacing', 'Margin'],
                documentationLink: 'https://getbootstrap.com/docs/5.3/utilities/spacing/'
            },
            {
                name: 'Padding',
                type: 'selectMany',
                classes: [
                    'p-(0|1|2|3|4|5)',
                    'pt-(0|1|2|3|4|5)',
                    'pb-(0|1|2|3|4|5)',
                    'ps-(0|1|2|3|4|5)',
                    'pe-(0|1|2|3|4|5)',
                    'px-(0|1|2|3|4|5)',
                    'py-(0|1|2|3|4|5)',
                    'p-(sm|md|lg|xl|xxl)-(0|1|2|3|4|5)',
                ],
                tags: ['Spacing', 'Padding'],
                documentationLink: 'https://getbootstrap.com/docs/5.3/utilities/spacing/'
            },

            // === COLORS ===
            {
                name: 'Background Color',
                type: 'selectOne',
                classes: [
                    'bg-(primary|secondary|success|danger|warning|info|light|dark|body|white|transparent)',
                    'bg-opacity-(10|25|50|75|100)',
                    'bg-gradient'
                ],
                tags: ['Colors', 'Background'],
                documentationLink: 'https://getbootstrap.com/docs/5.3/utilities/background/'
            },
            {
                name: 'Text Color',
                type: 'selectMany',
                classes: [
                    'text-(primary|secondary|success|danger|warning|info|light|dark|body|muted|white|black-50|white-50)',
                    'text-opacity-(25|50|75|100)'
                ],
                tags: ['Colors', 'Text'],
                documentationLink: 'https://getbootstrap.com/docs/5.3/utilities/colors/'
            },

            // === TYPOGRAPHY ===
            {
                name: 'Font Size',
                type: 'selectOne',
                classes: ['fs-(1|2|3|4|5|6)'],
                tags: ['Typography', 'Size'],
                documentationLink: 'https://getbootstrap.com/docs/5.3/utilities/text/'
            },
            {
                name: 'Font Weight',
                type: 'selectOne',
                classes: ['fw-(light|lighter|normal|bold|bolder|semibold)'],
                tags: ['Typography', 'Weight'],
                documentationLink: 'https://getbootstrap.com/docs/5.3/utilities/text/'
            },
            {
                name: 'Text Alignment',
                type: 'selectOne',
                classes: [
                    'text-(start|end|center)',
                    'text-(sm|md|lg|xl|xxl)-(start|end|center)'
                ],
                tags: ['Typography', 'Alignment'],
                documentationLink: 'https://getbootstrap.com/docs/5.3/utilities/text/'
            },
            {
                name: 'Text Transform',
                type: 'selectOne',
                classes: ['text-(lowercase|uppercase|capitalize)'],
                tags: ['Typography', 'Transform'],
                documentationLink: 'https://getbootstrap.com/docs/5.3/utilities/text/'
            },
            {
                name: 'Line Height',
                type: 'selectOne',
                classes: ['lh-(1|sm|base|lg)'],
                tags: ['Typography', 'Line Height'],
                documentationLink: 'https://getbootstrap.com/docs/5.3/utilities/text/'
            },

            // === BORDERS ===
            {
                name: 'Border',
                type: 'selectMany',
                classes: [
                    'border',
                    'border-(top|end|bottom|start)',
                    'border-(0|1|2|3|4|5)',
                    'border-(primary|secondary|success|danger|warning|info|light|dark|white)'
                ],
                tags: ['Borders'],
                documentationLink: 'https://getbootstrap.com/docs/5.3/utilities/borders/'
            },
            {
                name: 'Border Radius',
                type: 'selectMany',
                classes: [
                    'rounded',
                    'rounded-(0|1|2|3|4|5)',
                    'rounded-(top|end|bottom|start|circle|pill)',
                    'rounded-(top|end|bottom|start)-(0|1|2|3|4|5)'
                ],
                tags: ['Borders', 'Radius'],
                documentationLink: 'https://getbootstrap.com/docs/5.3/utilities/borders/'
            },

            // === SHADOWS ===
            {
                name: 'Shadow',
                type: 'selectOne',
                classes: ['shadow-none', 'shadow-sm', 'shadow', 'shadow-lg'],
                tags: ['Shadow', 'Effects'],
                documentationLink: 'https://getbootstrap.com/docs/5.3/utilities/shadows/'
            },

            // === DISPLAY ===
            {
                name: 'Display',
                type: 'selectOne',
                classes: [
                    'd-(none|inline|inline-block|block|grid|table|table-cell|table-row|flex|inline-flex)',
                    'd-(sm|md|lg|xl|xxl)-(none|inline|inline-block|block|grid|table|flex|inline-flex)'
                ],
                tags: ['Display', 'Layout'],
                documentationLink: 'https://getbootstrap.com/docs/5.3/utilities/display/'
            },

            // === FLEXBOX ===
            {
                name: 'Flex Direction',
                type: 'selectOne',
                classes: [
                    'flex-(row|row-reverse|column|column-reverse)',
                    'flex-(sm|md|lg|xl|xxl)-(row|row-reverse|column|column-reverse)'
                ],
                tags: ['Flexbox', 'Layout'],
                selectors: ['.d-flex', '.d-inline-flex'],
                documentationLink: 'https://getbootstrap.com/docs/5.3/utilities/flex/'
            },
            {
                name: 'Justify Content',
                type: 'selectOne',
                classes: [
                    'justify-content-(start|end|center|between|around|evenly)',
                    'justify-content-(sm|md|lg|xl|xxl)-(start|end|center|between|around|evenly)'
                ],
                tags: ['Flexbox', 'Alignment'],
                selectors: ['.d-flex', '.d-inline-flex'],
                documentationLink: 'https://getbootstrap.com/docs/5.3/utilities/flex/'
            },
            {
                name: 'Align Items',
                type: 'selectOne',
                classes: [
                    'align-items-(start|end|center|baseline|stretch)',
                    'align-items-(sm|md|lg|xl|xxl)-(start|end|center|baseline|stretch)'
                ],
                tags: ['Flexbox', 'Alignment'],
                selectors: ['.d-flex', '.d-inline-flex'],
                documentationLink: 'https://getbootstrap.com/docs/5.3/utilities/flex/'
            },
            {
                name: 'Flex Wrap',
                type: 'selectOne',
                classes: ['flex-(nowrap|wrap|wrap-reverse)'],
                tags: ['Flexbox', 'Layout'],
                selectors: ['.d-flex', '.d-inline-flex'],
                documentationLink: 'https://getbootstrap.com/docs/5.3/utilities/flex/'
            },
            {
                name: 'Gap',
                type: 'selectOne',
                classes: ['gap-(0|1|2|3|4|5)'],
                tags: ['Flexbox', 'Spacing'],
                selectors: ['.d-flex', '.d-inline-flex', '.d-grid'],
                documentationLink: 'https://getbootstrap.com/docs/5.3/utilities/spacing/'
            },

            // === WIDTH & HEIGHT ===
            {
                name: 'Width',
                type: 'selectOne',
                classes: ['w-(25|50|75|100|auto)'],
                tags: ['Sizing', 'Width'],
                documentationLink: 'https://getbootstrap.com/docs/5.3/utilities/sizing/'
            },
            {
                name: 'Height',
                type: 'selectOne',
                classes: ['h-(25|50|75|100|auto)'],
                tags: ['Sizing', 'Height'],
                documentationLink: 'https://getbootstrap.com/docs/5.3/utilities/sizing/'
            },

            // === POSITION ===
            {
                name: 'Position',
                type: 'selectOne',
                classes: ['position-(static|relative|absolute|fixed|sticky)'],
                tags: ['Position', 'Layout'],
                documentationLink: 'https://getbootstrap.com/docs/5.3/utilities/position/'
            },

            // === BUTTON SPECIFIC ===
            {
                name: 'Button Style',
                type: 'selectOne',
                classes: [
                    'btn-primary',
                    'btn-secondary',
                    'btn-success',
                    'btn-danger',
                    'btn-warning',
                    'btn-info',
                    'btn-light',
                    'btn-dark',
                    'btn-link',
                    'btn-outline-(primary|secondary|success|danger|warning|info|light|dark)'
                ],
                tags: ['Button', 'Colors'],
                selectors: ['.btn', 'button', 'a.btn'],
                documentationLink: 'https://getbootstrap.com/docs/5.3/components/buttons/'
            },
            {
                name: 'Button Size',
                type: 'selectOne',
                classes: ['btn-sm', 'btn-lg'],
                tags: ['Button', 'Size'],
                selectors: ['.btn', 'button', 'a.btn'],
                documentationLink: 'https://getbootstrap.com/docs/5.3/components/buttons/'
            }
        ],

        // Готовые шаблоны компонентов
        templates: [
            // === LAYOUT ===
            {
                name: 'Container',
                htmlTemplate: `<div class="container">
    <div class="productdiv-drop-container"></div>
</div>`,
                tags: ['Layout'],
                previewWidth: '100%'
            },
            {
                name: 'Container Fluid',
                htmlTemplate: `<div class="container-fluid">
    <div class="productdiv-drop-container"></div>
</div>`,
                tags: ['Layout'],
                previewWidth: '100%'
            },
            {
                name: 'Row',
                htmlTemplate: `<div class="row">
    <div class="productdiv-drop-container"></div>
</div>`,
                tags: ['Layout', 'Grid']
            },
            {
                name: '2 Columns',
                htmlTemplate: `<div class="row">
    <div class="col-md-6">
        <div class="productdiv-drop-container"></div>
    </div>
    <div class="col-md-6">
        <div class="productdiv-drop-container"></div>
    </div>
</div>`,
                tags: ['Layout', 'Grid']
            },
            {
                name: '3 Columns',
                htmlTemplate: `<div class="row">
    <div class="col-md-4">
        <div class="productdiv-drop-container"></div>
    </div>
    <div class="col-md-4">
        <div class="productdiv-drop-container"></div>
    </div>
    <div class="col-md-4">
        <div class="productdiv-drop-container"></div>
    </div>
</div>`,
                tags: ['Layout', 'Grid']
            },
            {
                name: 'Section',
                htmlTemplate: `<section class="py-5">
    <div class="container">
        <div class="productdiv-drop-container"></div>
    </div>
</section>`,
                tags: ['Layout']
            },

            // === COMPONENTS ===
            {
                name: 'Card',
                htmlTemplate: `<div class="card">
    <div class="card-body">
        <h5 class="card-title">Заголовок карточки</h5>
        <p class="card-text">Текст карточки. Замените этот текст на свой контент.</p>
        <a href="#" class="btn btn-primary">Подробнее</a>
    </div>
</div>`,
                tags: ['Components', 'Card']
            },
            {
                name: 'Card with Image',
                htmlTemplate: `<div class="card">
    <img src="https://via.placeholder.com/400x200" class="card-img-top" alt="Изображение">
    <div class="card-body">
        <h5 class="card-title">Заголовок</h5>
        <p class="card-text">Описание карточки с изображением.</p>
        <a href="#" class="btn btn-primary">Подробнее</a>
    </div>
</div>`,
                tags: ['Components', 'Card']
            },
            {
                name: 'Alert',
                htmlTemplate: `<div class="alert alert-primary" role="alert">
    Это важное сообщение для пользователя.
</div>`,
                tags: ['Components', 'Alert']
            },
            {
                name: 'Button',
                htmlTemplate: `<button type="button" class="btn btn-primary">Кнопка</button>`,
                tags: ['Components', 'Button']
            },
            {
                name: 'Button Group',
                htmlTemplate: `<div class="btn-group" role="group">
    <button type="button" class="btn btn-primary">Левая</button>
    <button type="button" class="btn btn-primary">Средняя</button>
    <button type="button" class="btn btn-primary">Правая</button>
</div>`,
                tags: ['Components', 'Button']
            },

            // === CONTENT ===
            {
                name: 'Heading H2',
                htmlTemplate: `<h2>Заголовок второго уровня</h2>`,
                tags: ['Content', 'Typography']
            },
            {
                name: 'Heading H3',
                htmlTemplate: `<h3>Заголовок третьего уровня</h3>`,
                tags: ['Content', 'Typography']
            },
            {
                name: 'Paragraph',
                htmlTemplate: `<p>Это обычный параграф текста. Замените его на свой контент.</p>`,
                tags: ['Content', 'Typography']
            },
            {
                name: 'Lead Text',
                htmlTemplate: `<p class="lead">Это выделенный текст (lead paragraph).</p>`,
                tags: ['Content', 'Typography']
            },
            {
                name: 'Image',
                htmlTemplate: `<img src="https://via.placeholder.com/800x400" class="img-fluid rounded shadow-sm" alt="Изображение">`,
                tags: ['Content', 'Media']
            },
            {
                name: 'Blockquote',
                htmlTemplate: `<blockquote class="blockquote">
    <p>Цитата или важное высказывание.</p>
    <footer class="blockquote-footer">Автор цитаты</footer>
</blockquote>`,
                tags: ['Content', 'Typography']
            },

            // === LISTS ===
            {
                name: 'List Group',
                htmlTemplate: `<ul class="list-group">
    <li class="list-group-item">Первый элемент</li>
    <li class="list-group-item">Второй элемент</li>
    <li class="list-group-item">Третий элемент</li>
</ul>`,
                tags: ['Components', 'List']
            },

            // === UTILITIES ===
            {
                name: 'Divider',
                htmlTemplate: `<hr class="my-4">`,
                tags: ['Utilities']
            },
            {
                name: 'Spacer',
                htmlTemplate: `<div class="py-3"></div>`,
                tags: ['Utilities', 'Spacing']
            }
        ]
    },

    // Опции редактора
    editorOptions: {
        // Предотвращение ухода со страницы после открытия редактора
        preventPageLeave: true,
        
        // Предотвращение ухода через history push (для SPA)
        preventHistoryLeave: true,
        
        // Форматирование HTML при копировании
        htmlFormatter: function(html) {
            // Базовое форматирование: удаление лишних пробелов
            return html.trim();
        }
    }
};
