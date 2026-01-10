<?php

/**
 * @package   Gantry5
 * @author    Tiger12 http://tiger12.com
 * @originalCreator  RocketTheme (Gantry Framework) 
 * @currentDeveloper  Tiger12, LLC 
 * @copyright Copyright (C) 2007 - 2022 Tiger12, LLC
 * @license   MIT
 *
 * http://opensource.org/licenses/MIT
 */

namespace Grav\Theme;

use Gantry\Framework\Gantry;
use Gantry\Framework\Theme as GantryTheme;
use Grav\Common\Theme;
use RocketTheme\Toolbox\ResourceLocator\UniformResourceLocator;

/**
 * Class G5_Helium
 * @package Grav\Theme
 */
class G5_Helium extends Theme
{
    /** @var string */
    public $gantry = '5.5';
    /** @var GantryTheme */
    protected $theme;

    /**
     * @return array
     */
    public static function getSubscribedEvents()
    {
        return [
            'onThemeInitialized' => ['onThemeInitialized', 0],
            'onTwigSiteVariables' => ['onTwigSiteVariables', 0]
        ];
    }

    public function onThemeInitialized()
    {
        if (defined('GRAV_CLI') && GRAV_CLI) {
            return;
        }

        /** @var UniformResourceLocator $locator */
        $locator = $this->grav['locator'];
        $path = $locator('theme://');
        $name = $this->name;

        if (!class_exists('\Gantry5\Loader')) {
            if ($this->isAdmin()) {
                $messages = $this->grav['messages'];
                $messages->add('Please enable Gantry 5 plugin in order to use current theme!', 'error');
                return;
            }

            throw new \LogicException('Please install and enable Gantry 5 Framework plugin!');
        }

        // Setup Gantry 5 Framework or throw exception.
        \Gantry5\Loader::setup();

        // Get Gantry instance.
        $gantry = Gantry::instance();

        // Set the theme path from Grav variable.
        $gantry['theme.path'] = $path;
        $gantry['theme.name'] = $name;

        // Define the template.
        require $locator('theme://includes/theme.php');

        // Define Gantry services.
        $gantry['theme'] = static function ($c) {
            return new \Gantry\Theme\G5_Helium($c['theme.path'], $c['theme.name']);
        };
    }

    /**
     * Добавление ProductDiv для авторизованных администраторов
     */
    public function onTwigSiteVariables()
    {
        // Проверяем авторизацию пользователя
        $user = $this->grav['user'];
        
        // Расширенная диагностика
        $isAuthenticated = $user->authenticated ?? false;
        $username = $user->username ?? 'not logged in';
        $hasAdminAccess = false;
        
        // Пробуем разные методы проверки прав администратора
        try {
            $hasAdminAccess = $user->authorize('admin.login') ?? false;
        } catch (\Exception $e) {
            // Если этот метод не работает, пробуем альтернативный
            $access = $user->get('access');
            $hasAdminAccess = isset($access['admin']['login']) && $access['admin']['login'] === true;
        }
        
        // Добавляем отладочную информацию
        $this->grav['assets']->addInlineJs("
            console.log('🔍 ProductDiv Debug Info:');
            console.log('User authenticated: " . ($isAuthenticated ? "YES" : "NO") . "');
            console.log('User username: " . $username . "');
            console.log('Admin access: " . ($hasAdminAccess ? "YES" : "NO") . "');
            console.log('User object exists: " . (isset($user) ? "YES" : "NO") . "');
        ", ['group' => 'bottom']);
        
        // Загружаем ProductDiv только для авторизованных администраторов
        // ВРЕМЕННО: отключаем проверку для тестирования
        // if ($isAuthenticated && $hasAdminAccess) {
        if (true) { // ТЕСТОВЫЙ РЕЖИМ - ProductDiv загружается всегда!
            $this->grav['assets']->addInlineJs("
                console.log('✅ Условия выполнены - загружаем ProductDiv');
            ", ['group' => 'bottom']);
            
            // Получаем абсолютный URL для скрипта
            $productdivUrl = $this->grav['base_url_absolute'] . '/user/themes/g5_helium/js/productdiv.js';
            $configUrl = $this->grav['base_url_absolute'] . '/user/themes/g5_helium/js/productdiv-config.js';
            
            $this->grav['assets']->addInlineJs("
                console.log('📂 ProductDiv URL:', '" . $productdivUrl . "');
                console.log('📂 Config URL:', '" . $configUrl . "');
            ", ['group' => 'bottom']);
            
            // Подключаем ProductDiv локально с абсолютным путём
            $this->grav['assets']->addJs($productdivUrl, ['group' => 'bottom']);
            
            // Подключаем конфигурацию ProductDiv
            $this->grav['assets']->addJs($configUrl, ['group' => 'bottom']);
            
            // Инициализация ProductDiv
            $this->grav['assets']->addInlineJs("
                (function() {
                    console.log('🚀 Начало инициализации ProductDiv');
                    
                    // Ожидаем полной загрузки DOM
                    if (document.readyState === 'loading') {
                        document.addEventListener('DOMContentLoaded', initProductDiv);
                    } else {
                        initProductDiv();
                    }
                    
                    function initProductDiv() {
                        try {
                            console.log('📦 ProductDiv доступен:', typeof window.ProductDiv !== 'undefined');
                            console.log('📦 ProductDivConfig доступен:', typeof window.ProductDivConfig !== 'undefined');
                            
                            if (typeof window.ProductDivConfig !== 'undefined' && typeof window.ProductDiv !== 'undefined') {
                                window.ProductDiv(window.ProductDivConfig.configuration, window.ProductDivConfig.editorOptions);
                                console.log('✅ ProductDiv успешно инициализирован');
                            } else {
                                console.warn('⚠️ ProductDiv или конфигурация не загружены');
                                if (typeof window.ProductDiv !== 'undefined') {
                                    window.ProductDiv({
                                        treeViewIgnoreQuerySelectors: ['script', 'style', 'link', '[data-productdiv=\"true\"]', 'svg'],
                                        utilityClasses: [],
                                        templates: []
                                    });
                                    console.log('✅ ProductDiv инициализирован с базовыми настройками');
                                }
                            }
                        } catch (error) {
                            console.error('❌ Ошибка инициализации ProductDiv:', error);
                        }
                    }
                })();
            ", ['group' => 'bottom']);
        } else {
            $this->grav['assets']->addInlineJs("
                console.log('❌ Условия НЕ выполнены - ProductDiv не загружается');
                console.log('Причина: пользователь не авторизован или нет прав администратора');
            ", ['group' => 'bottom']);
        }
    }
}
