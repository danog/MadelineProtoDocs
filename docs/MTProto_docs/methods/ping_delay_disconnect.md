---
title: "ping_delay_disconnect"
description: "ping_delay_disconnect parameters, return type and example"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: ping\_delay\_disconnect
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|ping\_id|[long](../types/long.md) | Yes|
|disconnect\_delay|[int](../types/int.md) | Yes|


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

$Pong = $MadelineProto->ping_delay_disconnect(['ping_id' => long, 'disconnect_delay' => int, ]);
```

Or, if you're into Lua:

```lua
Pong = ping_delay_disconnect({ping_id=long, disconnect_delay=int, })
```

