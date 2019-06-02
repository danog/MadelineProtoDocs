---
title: ping
description: Pings the server
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: ping  
[Back to methods index](index.md)


Pings the server

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|ping\_id|[long](../types/long.md) | Ping ID | Yes|


### Return type: [Pong](../types/Pong.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Pong = $MadelineProto->ping(['ping_id' => long, ]);
```

Or, if you're into Lua:

```lua
Pong = ping({ping_id=long, })
```

