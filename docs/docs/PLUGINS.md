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
  * [Limitations](#limitations)
  * [Namespace requirements](#namespace-requirements)
  * [Distribution](#distribution)
  * [Full plugin example](#full-plugin-example)

## Installing plugins

Plugins can be installed by simply placing their files in the plugin path, or by installing them through composer.  

### Simple installation

To install a plugin, copy the plugin's files into a `plugins/` folder, and use the following base code:

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
    public function getPluginPaths(): array|string|null
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
    public function getPlugins(): array
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

### Limitations

Plugins can handle updates, include other plugins using `getPlugins()` and store persistent data to the session using `__sleep`, [just like any non-plugin event handler](https://docs.madelineproto.xyz/docs/UPDATES.html).  

However, unlike normal event handlers, plugins can require other plugins using **only** `getPlugins()`, not `getPluginPaths()`.  

Also, plugins can only interact with the filesystem using MadelineProto's download and upload functions.  

For performance reasons, your plugin **must not** read files from the filesystem: configuration can be done entirely using in-memory persistent properties, for example:

```php
<?php

// WRONG!
if (!file_exists('online.txt')) {
    file_put_contents('online.txt', 'on');
}

class OnlinePlugin extends PluginEventHandler
{
    #[Cron(period: 60.0)]
    public function cron(): void
    {
        // WRONG!
        if (file_get_contents('online.txt') === 'on') {
            $this->account->updateStatus(offline: false);
        } else {
            $this->account->updateStatus(offline: true);
        }
    }
}
```

Do this, instead:

<!-- cut_here examples/plugins/Danogentili/OnlinePlugin.php -->

```php
<?php

use danog\MadelineProto\EventHandler\Attributes\Cron;
use danog\MadelineProto\EventHandler\Filter\FilterCommand;
use danog\MadelineProto\EventHandler\Message;
use danog\MadelineProto\EventHandler\SimpleFilter\FromAdmin;
use danog\MadelineProto\EventHandler\SimpleFilter\Incoming;
use danog\MadelineProto\PluginEventHandler;

class OnlinePlugin extends PluginEventHandler
{
    private bool $isOnline = true;

    public function setOnline(bool $online): void
    {
        $this->isOnline = $online;
    }

    public function isPluginEnabled(): bool
    {
        // Only users can be online/offline
        return $this->getSelf()['bot'] === false;
    }

    #[Cron(period: 60.0)]
    public function cron(): void
    {
        $this->account->updateStatus(offline: !$this->isOnline);
    }

    #[FilterCommand('online')]
    public function toggleOnline(Incoming&Message&FromAdmin $message): void
    {
        $this->isOnline = true;
    }

    #[FilterCommand('offline')]
    public function toggleOffline(Incoming&Message&FromAdmin $message): void
    {
        $this->isOnline = false;
    }
}
```

<!-- cut_here_end examples/plugins/Danogentili/OnlinePlugin.php -->

And, to toggle the settings from the outside of the bot (for example using a helper bot, or another program):

```
<?php

$online = true;
//$online = false;

$API = new \danog\MadelineProto\API('session.madeline');
$API->getEventHandler(\MadelinePlugin\Danogentili\OnlinePlugin::class)->setOnline($online);
```


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
     * include 'vendor/autoload.php';
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

<a href="https://docs.madelineproto.xyz/docs/DATABASE.html">Next section</a>