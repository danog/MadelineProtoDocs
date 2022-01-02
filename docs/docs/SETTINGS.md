---
title: "Settings"
description: "MadelineProto has lots of settings that can be used to modify the behaviour of the library.  "
nav_order: 11
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Settings

MadelineProto has lots of settings that can be used to modify the behaviour of the library.  
These settings are controlled by the following classes in the `\danog\MadelineProto\Settings` namespace:

* [AppInfo: App information.](../PHP/danog/MadelineProto/Settings/AppInfo.md)
* [Auth: Cryptography settings.](../PHP/danog/MadelineProto/Settings/Auth.md)
* [Connection: Connection settings.](../PHP/danog/MadelineProto/Settings/Connection.md)
* [Files: File management settings.](../PHP/danog/MadelineProto/Settings/Files.md)
* [Logger: Logger settings.](../PHP/danog/MadelineProto/Settings/Logger.md)
* [Peer: Peer database settings.](../PHP/danog/MadelineProto/Settings/Peer.md)
* [Pwr: PWRTelegram settings.](../PHP/danog/MadelineProto/Settings/Pwr.md)
* [RPC: RPC settings.](../PHP/danog/MadelineProto/Settings/RPC.md)
* [SecretChats: Secret chat settings.](../PHP/danog/MadelineProto/Settings/SecretChats.md)
* [Serialization: Serialization settings.](../PHP/danog/MadelineProto/Settings/Serialization.md)
* [TLSchema: TL schema settings.](../PHP/danog/MadelineProto/Settings/TLSchema.md)
* [Templates: Web and CLI template settings for login.](../PHP/danog/MadelineProto/Settings/Templates.md)
* [VoIP: VoIP settings.](../PHP/danog/MadelineProto/Settings/VoIP.md)
* [Database\Memory: Memory backend settings.](../PHP/danog/MadelineProto/Settings/Database/Memory.md)
* [Database\Mysql: MySQL backend settings.](../PHP/danog/MadelineProto/Settings/Database/Mysql.md)
* [Database\Postgres: Postgres backend settings.](../PHP/danog/MadelineProto/Settings/Database/Postgres.md)
* [Database\Redis: Redis backend settings.](../PHP/danog/MadelineProto/Settings/Database/Redis.md)

These classes can be instantiated and passed individually to MadelineProto:  
```php
$settings = (new Database\Mysql)
    ->setUri('tcp://localhost')
    ->setPassword('pass');

$API = new \danog\MadelineProto\API('session.madeline', $settings);
```

To modify the settings of an already created instance, `updateSettings` must be used, as passing them to the constructor won't work for performance reasons:  
```php
$settings = (new Database\Postgres)
    ->setUri('tcp://localhost')
    ->setPassword('pass');


$MadelineProto->updateSettings($settings);
```

It's recommended you create a separate file that accesses the session just to modify the settings, as it's a very rare operation.  

You can also group settings in a single [\danog\MadelineProto\Settings](../PHP/danog/MadelineProto/Settings.md) object, to quickly modify multiple settings:

```php
$settings = new \danog\MadelineProto\Settings;
$settings->setDb((new Database\Mysql)
    ->setUri('tcp://localhost')
    ->setPassword('pass')
);
$settings->getFiles()->setUploadParallelChunks(100);

$MadelineProto->updateSettings($settings);
```

<a href="https://docs.madelineproto.xyz/docs/SELF.html">Next section</a>