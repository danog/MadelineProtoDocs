---
title: "ping"
description: "ping parameters, return type and example"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: ping
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|ping\_id|[long](../types/long.md) | Yes|


### Return type: [Pong](../types/Pong.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Pong = $MadelineProto->ping(['ping_id' => long, ]);
```

Or, if you're into Lua:

```lua
Pong = ping({ping_id=long, })
```

