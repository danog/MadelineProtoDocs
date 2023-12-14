---
title: "Database"
description: "MadelineProto optionally can keep some of its internal data in a database, such as mysql, mariadb, postgres or redis (you can also add your own!), reducing RAM usage.   "
nav_order: 14
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Database

MadelineProto *optionally* can keep some of its internal data in a database, such as mysql, mariadb, postgres or redis (you can also [add your own](https://github.com/danog/MadelineProto/tree/v8/src/Db)!), reducing RAM usage.   

On first start after switching type all data will be migrated from the previous backend to the new one. 
Database to memory migration is also supported.

Databases and tables will be created automatically.  

You can also directly connect the [event handler](/docs/UPDATES.html#built-in-orm) using the same async MySQL/Postgres/Redis ORM used by MadelineProto internally.  

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

**WARNING**: Make sure to run `SET GLOBAL max_connections = 100000;` as root in the mysql/mariadb console, **regardless of the limit you set in the MadelineProto settings**.  
Make sure to run the command **after every system restart**, or modify the database configuration file to set the maximum connection limit to `100000`.  

MadelineProto can also be configured to run on ephemeral filesystems (i.e. docker containers with no volumes, storing all data on MySQL) by setting a table prefix manually in the settings, as specified [here &raquo;](#ephemeral-filesystems).  


### Postgres example (low memory usage):

```php
$settings = (new \danog\MadelineProto\Settings\Database\Postgres)
    ->setUri('tcp://localhost')
    ->setPassword('pass');
```

MadelineProto can also be configured to run on ephemeral filesystems (i.e. docker containers with no volumes, storing all data on Postgres) by setting a table prefix manually in the settings, as specified [here &raquo;](#ephemeral-filesystems).  

### Redis example (medium memory usage, faster access):

```php
$settings = (new \danog\MadelineProto\Settings\Database\Redis)
    ->setUri('redis://127.0.0.1')
    ->setPassword('pass');
```

MadelineProto can also be configured to run on ephemeral filesystems (i.e. docker containers with no volumes, storing all data on Redis) by setting a table prefix manually in the settings, as specified [here &raquo;](#ephemeral-filesystems).  

### Memory example (medium-high memory usage, fastest access):

```php
$settings = new \danog\MadelineProto\Settings\Database\Memory;
```

This mode, unlike [mysql](#mysql-example-low-memory-usage), [postgres](#postgres-example-low-memory-usage) and [redis](#redis-example-medium-memory-usage-faster-access) does not support [ephemeral filesystems](#ephemeral-filesystems), thus a persistent filesystem must be used for the session folder.  

### Ephemeral filesystems

MadelineProto can also be configured to run on ephemeral filesystems (i.e. docker containers with no volumes, storing all data on [MySQL](#mysql-example-low-memory-usage)/[Postgres](#postgres-example-low-memory-usage)/[Redis](#redis-example-medium-memory-usage-faster-access)) by setting a table prefix manually in the settings:

```php
$settings = (new \danog\MadelineProto\Settings\Database\Mysql)
    ->setUri('tcp://localhost')
    ->setPassword('pass')
    ->setEphemeralFilesystemPrefix('session_1');

$API = new \danog\MadelineProto\API('session.madeline', $settings);
```

The `setEphemeralFilesystemPrefix` setting indicates that the filesystem is ephemeral, and thus session files will not be used to store persistent data.  

The prefix must contain a unique string, used as prefix for database tables, different for every session.  
The prefix may be the same if different databases are used.  

This is useful when running MadelineProto inside docker containers without volumes, using just a database.  

Note that the session folder must still NEVER be deleted *if* MadelineProto is running, or else the session will be dropped from the database due to `AUTH_KEY_DUPLICATED` errors.  

Stopping the container gracefully and then deleting the session folder (i.e. by deleting or recreating the container itself) is 100% OK though.  

<a href="https://docs.madelineproto.xyz/docs/SETTINGS.html">Next section</a>