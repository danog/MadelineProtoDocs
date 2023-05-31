---
title: "Database"
description: "By default madelineProto keeps all data and caches in memory: chats, file references, username cache, etc.  "
nav_order: 12
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Database

By default madelineProto keeps all data and caches in memory: chats, file references, username cache, etc.  
This data can require up to 1Gb of ram and more on certain accounts.  
MadelineProto can keep part of this data in a database, such as mysql, mariadb, postgres or redis (you can also [add your own](https://github.com/danog/MadelineProto/tree/v8/src/Db)!).   

On first start after switching type all data will be migrated from the previous backend to the new one. 
Database to memory migration is also supported.

Databases and tables will be created automatically.  

You can also directly connect the [event handler](/docs/UPDATES.html#built-in-database-driver) using the same async MySQL/Postgres/Redis ORM used by MadelineProto internally.  

Related settings:  

* [\danog\MadelineProto\Settings\Database\Memory: Memory backend settings.](../PHP/danog/MadelineProto/Settings/Database/Memory.html)
* [\danog\MadelineProto\Settings\Database\Mysql: MySQL backend settings.](../PHP/danog/MadelineProto/Settings/Database/Mysql.html) MariaDb 10.2+ or Mysql 5.6+ required.
* [\danog\MadelineProto\Settings\Database\Postgres: Postgres backend settings.](../PHP/danog/MadelineProto/Settings/Database/Postgres.html)
* [\danog\MadelineProto\Settings\Database\Redis: Redis backend settings.](../PHP/danog/MadelineProto/Settings/Database/Redis.html)

See [the settings documentation for more info](SETTINGS.html).  

### Mysql example (low memory usage):

```php
$settings = (new \danog\MadelineProto\Settings\Database\Mysql)
    ->setUri('tcp://localhost')
    ->setPassword('pass');

$API = new \danog\MadelineProto\API('session.madeline', $settings);
```

### Postgres example (low memory usage):

```php
$settings = (new \danog\MadelineProto\Settings\Database\Postgres)
    ->setUri('tcp://localhost')
    ->setPassword('pass');
```

### Redis example (medium memory usage, faster access):

```php
$settings = (new \danog\MadelineProto\Settings\Database\Redis)
    ->setUri('redis://127.0.0.1')
    ->setPassword('pass');
```

### Memory example (medium-high memory usage, fastest access):

```php
$settings = new \danog\MadelineProto\Settings\Database\Memory;
```

<a href="https://docs.madelineproto.xyz/docs/SETTINGS.html">Next section</a>