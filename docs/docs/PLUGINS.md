---
title: "Plugins"
description: "MadelineProto offers a native plugin system, based on event handlers!"
nav_order: 13
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Plugins

MadelineProto offers a native plugin system, based on [event handlers](https://docs.madelineproto.xyz/docs/UPDATES.html)!

* [Installing plugins](#installing-plugins)
  * [Simple installation](#simple-installation)
  * [Composer installation](#composer-installation)
* [Creating plugins](#creating-plugins)
  * [Full plugin example](#full-plugin-example)
  * [Limitations](#limitations)
  * [Namespace requirements](#namespace-requirements)
  * [Distribution](#distribution)

## Installing plugins

Plugins can be installed by simply placing their files in the plugin path, or by installing them through composer.  

Plugins may be run either using a [plugin base &raquo;](https://github.com/danog/MadelineProto/raw/v8/examples/PluginBase.php), or directly (in which case they behave as normal bots).  

### Simple installation

To install a plugin, copy the plugin's files into a `plugins/` folder, and use the following base code ([download &raquo;](https://github.com/danog/MadelineProto/raw/v8/examples/PluginBase.php)):

<!-- cut_here examples/PluginBase.php -->

```php

<?php declare(strict_types=1);

use danog\MadelineProto\Logger;
use danog\MadelineProto\Settings;
use danog\MadelineProto\Settings\Database\Mysql;
use danog\MadelineProto\Settings\Database\Postgres;
use danog\MadelineProto\Settings\Database\Redis;
use danog\MadelineProto\SimpleEventHandler;

/** Base event handler class that only includes plugins */
class BaseHandler extends SimpleEventHandler
{
    public static function getPluginPaths(): array|string|null
    {
        return 'plugins/';
    }
}

$settings = new Settings;
$settings->getLogger()->setLevel(Logger::LEVEL_ULTRA_VERBOSE);

// You can also use Redis, MySQL or PostgreSQL
// $settings->setDb((new Redis)->setDatabase(0)->setPassword('pony'));
// $settings->setDb((new Postgres)->setDatabase('MadelineProto')->setUsername('daniil')->setPassword('pony'));
// $settings->setDb((new Mysql)->setDatabase('MadelineProto')->setUsername('daniil')->setPassword('pony'));

// For users or bots
BaseHandler::startAndLoop('bot.madeline', $settings);

// For bots only
// BaseHandler::startAndLoopBot('bot.madeline', 'bot token', $settings);

```

<!-- cut_here_end examples/PluginBase.php -->

Any other folder name may be used as well, and you can also return an array of folder names from `getPluginPaths()`.  

You can combine plugins installed with this mode with plugins installed using [composer](#composer-installation).  

### Composer installation

To install a plugin via composer, require it first:

```bash
composer require yournick/someplugin
```

Then return it from the `getPlugins` function of your base event handler:

```php
<?php declare(strict_types=1);

use danog\MadelineProto\Logger;
use danog\MadelineProto\Settings;
use danog\MadelineProto\Settings\Database\Mysql;
use danog\MadelineProto\Settings\Database\Postgres;
use danog\MadelineProto\Settings\Database\Redis;
use danog\MadelineProto\SimpleEventHandler;

use MadelinePlugin\YourNick\PluginName;

/** Base event handler class that includes plugins via Composer */
class BaseHandler extends SimpleEventHandler
{
    public static function getPlugins(): array
    {
        return [PluginName::class]
    }
}

$settings = new Settings;
$settings->getLogger()->setLevel(Logger::LEVEL_ULTRA_VERBOSE);

// You can also use Redis, MySQL or PostgreSQL
// $settings->setDb((new Redis)->setDatabase(0)->setPassword('pony'));
// $settings->setDb((new Postgres)->setDatabase('MadelineProto')->setUsername('daniil')->setPassword('pony'));
// $settings->setDb((new Mysql)->setDatabase('MadelineProto')->setUsername('daniil')->setPassword('pony'));

// For users or bots
BaseHandler::startAndLoop('bot.madeline', $settings);

// For bots only
// BaseHandler::startAndLoopBot('bot.madeline', 'bot token', $settings);
```

You can combine plugins installed with this mode with plugins installed using a [plugin path](#simple-installation).  

## Creating plugins

To create a plugin, simply create an [event handler](https://docs.madelineproto.xyz/docs/UPDATES.html) that extends the `PluginEventHandler` class.

### Full plugin example

Full example (file name `plugins/Danogentili/PingPlugin.php`):

<!-- cut_here examples/plugins/Danogentili/PingPlugin.php -->

```php
<?php declare(strict_types=1);

namespace MadelinePlugin\Danogentili;

use danog\MadelineProto\EventHandler\Attributes\Cron;
use danog\MadelineProto\EventHandler\Filter\FilterText;
use danog\MadelineProto\EventHandler\Message;
use danog\MadelineProto\EventHandler\SimpleFilter\Incoming;
use danog\MadelineProto\PluginEventHandler;

/**
 * Plugin event handler class.
 *
 * All properties returned by __sleep are automatically stored in the database.
 */
class PingPlugin extends PluginEventHandler
{
    private int $pingCount = 0;

    private string $pongText = 'pong';

    /**
     * You can set a custom pong text from the outside of the plugin:.
     *
     * ```
     * if (!file_exists('madeline.php')) {
     *     copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
     * }
     * include 'madeline.php';
     *
     * $a = new API('bot.madeline');
     * $plugin = $a->getPlugin(PingPlugin::class);
     *
     * $plugin->setPongText('UwU');
     * ```
     *
     * This will automatically connect to the running instance of the plugin and call the specified method.
     */
    public function setPongText(string $pong): void
    {
        $this->pongText = $pong;
    }

    /**
     * Returns a list of names for properties that will be automatically saved to the session database (MySQL/postgres/redis if configured, the session file otherwise).
     */
    public function __sleep(): array
    {
        return ['pingCount', 'pongText'];
    }
    /**
     * Initialization logic.
     */
    public function onStart(): void
    {
        $this->logger("The bot was started!");
        $this->logger($this->getFullInfo('MadelineProto'));

        $this->sendMessageToAdmins("The bot was started!");
    }

    /**
     * Plugins may be enabled or disabled at startup by returning true or false from this function.
     */
    public function isPluginEnabled(): bool
    {
        return true;
    }

    /**
     * This cron function will be executed forever, every 60 seconds.
     */
    #[Cron(period: 60.0)]
    public function cron1(): void
    {
        $this->sendMessageToAdmins("The ping plugin is online, total pings so far: ".$this->pingCount);
    }

    #[FilterText('ping')]
    public function pingCommand(Incoming&Message $message): void
    {
        $message->reply($this->pongText);
        $this->pingCount++;
    }
}

```

<!-- cut_here_end examples/plugins/Danogentili/PingPlugin.php -->

Plugins may be enabled or disabled at startup by returning `true` or `false` from `isPluginEnabled()`.

### Limitations

Plugins can handle updates, include other plugins using `getPlugins()` and store persistent data to the session using `__sleep`, [just like any non-plugin event handler](https://docs.madelineproto.xyz/docs/UPDATES.html).  

However, unlike normal event handlers, plugins can require other plugins using **only** `getPlugins()`, not `getPluginPaths()`.  

Also, plugins can only interact with the filesystem using MadelineProto's download and upload functions.  

For performance reasons, your plugin **should not** read files from the filesystem.  

Here's a list of common uses for files, and what they can be replaced with:

* [Configuration](https://docs.madelineproto.xyz/docs/UPDATES.html#configuration)
* [Creating and uploading text files](https://docs.madelineproto.xyz/docs/UPDATES.html#creating-and-uploading-text-files)
* [Logging](https://docs.madelineproto.xyz/docs/UPDATES.html#logging)

### Namespace requirements

Plugins must be located in the `MadelinePlugin` vendor namespace, preferrably in a custom subnamespace to avoid conflicts with other plugins.  

So for example, if your nickname is `@danogentili`, use `namespace MadelinePlugin\Danogentili;`.  

All the classes, interfaces, functions and traits defined by your plugin's code must be defined in the namespace you chose.  

The file layout must follow the [PSR-4 autoloading standard](https://www.php-fig.org/psr/psr-4/); for example, if you have the following classes:

* `MadelinePlugin\Danogentili\PingPlugin` - A ping plugin
* `MadelinePlugin\Danogentili\HelperPlugin` - A helper plugin
* `MadelinePlugin\Danogentili\CommonTrait` - A common trait with some tools, included by the plugins
* `MadelinePlugin\Danogentili\Internal\SomeOtherClass` - Some other class (not a plugin)

This will be the directory structure:

```
plugins/Danogentili/PingPlugin.php
plugins/Danogentili/HelperPlugin.php
plugins/Danogentili/CommonTrait.php
plugins/Danogentili/Internal/SomeOtherClass.php
```

If you want to define some functions, put them in `plugins/Danog/functions.php` (or any subdirectory, as long as the name of the file is `functions.php`).  

### Distribution

Plugins can be distributed in a simple zip file, or using composer.  

You can also distribute plugins as standalone files in the `MadelinePlugin` namespace (make sure to choose a really unique name!), for example `plugins/Danogentili.php`.  

<a href="https://docs.madelineproto.xyz/docs/DATABASE.html">Next section</a>