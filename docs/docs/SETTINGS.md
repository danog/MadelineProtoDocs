---
title: "Settings"
description: "MadelineProto has lots of settings that can be used to modify the behaviour of the library."
nav_order: 16
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Settings

MadelineProto has lots of settings that can be used to modify the behaviour of the library.  
These settings are controlled by the following classes in the `\danog\MadelineProto\Settings` namespace:

* [AppInfo: App information.](../PHP/danog/MadelineProto/Settings/AppInfo.html)
* [Auth: Cryptography settings.](../PHP/danog/MadelineProto/Settings/Auth.html)
* [Connection: Connection settings.](../PHP/danog/MadelineProto/Settings/Connection.html)
* [Files: File management settings.](../PHP/danog/MadelineProto/Settings/Files.html)
* [Logger: Logger settings.](../PHP/danog/MadelineProto/Settings/Logger.html)
* [Peer: Peer database settings.](../PHP/danog/MadelineProto/Settings/Peer.html)
* [Pwr: PWRTelegram settings.](../PHP/danog/MadelineProto/Settings/Pwr.html)
* [RPC: RPC settings.](../PHP/danog/MadelineProto/Settings/RPC.html)
* [SecretChats: Secret chat settings.](../PHP/danog/MadelineProto/Settings/SecretChats.html)
* [Serialization: Serialization settings.](../PHP/danog/MadelineProto/Settings/Serialization.html)
* [TLSchema: TL schema settings.](../PHP/danog/MadelineProto/Settings/TLSchema.html)
* [Templates: Web and CLI template settings for login.](../PHP/danog/MadelineProto/Settings/Templates.html)
* [VoIP: VoIP settings.](../PHP/danog/MadelineProto/Settings/VoIP.html)
* [Database\Memory: Memory backend settings.](../PHP/danog/MadelineProto/Settings/Database/Memory.html)
* [Database\Mysql: MySQL backend settings.](../PHP/danog/MadelineProto/Settings/Database/Mysql.html)
* [Database\Postgres: Postgres backend settings.](../PHP/danog/MadelineProto/Settings/Database/Postgres.html)
* [Database\Redis: Redis backend settings.](../PHP/danog/MadelineProto/Settings/Database/Redis.html)

These classes can be instantiated and passed individually to MadelineProto:  
```php
$settings = (new \danog\MadelineProto\Settings\AppInfo)
    ->setApiId(124)
    ->setApiHash('xx');

$API = new \danog\MadelineProto\API('session.madeline', $settings);
```

**It's heavily recommended** to remove (or pass null) the second `$settings` parameter passed to the constructor once the instance is logged in, to avoid the performance overhead of needlessly updating settings every time API is instantiated:  

To modify the settings of an already created instance, `updateSettings` should be used, instead:  
```php
$settings = (new \danog\MadelineProto\Settings\AppInfo)
    ->setApiId(124)
    ->setApiHash('xx');

$MadelineProto->updateSettings($settings);
```

It's recommended you create a separate file that accesses the session just to modify the settings, as it's a very rare operation.  

You can also group settings in a single [\danog\MadelineProto\Settings](../PHP/danog/MadelineProto/Settings.html) object, to quickly modify multiple settings:

**See [here &raquo;](../PHP/danog/MadelineProto/Settings.html) for more info on how to get and modify the instances of each subsetting class mentioned at the beginning of this page**.

```php
$settings = new \danog\MadelineProto\Settings;
$settings->setDb((new \danog\MadelineProto\Settings\Database\Mysql)
    ->setUri('tcp://localhost')
    ->setPassword('pass')
);
$settings->setAppInfo((new \danog\MadelineProto\Settings\AppInfo)
    ->setApiId(124)
    ->setApiHash('xx')
);
$settings->getFiles()->setUploadParallelChunks(100);

$MadelineProto->updateSettings($settings);
```

<a href="https://docs.madelineproto.xyz/docs/SELF.html">Next section</a>