---
title: ping_delay_disconnect
description: Pings the server and causes disconection if the same method is not called within ping_disconnect_delay
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: ping\_delay\_disconnect  
[Back to methods index](index.md)


Pings the server and causes disconection if the same method is not called within ping_disconnect_delay

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|ping\_id|[long](../types/long.md) | Ping ID | Yes|
|disconnect\_delay|[int](../types/int.md) | Disconection delay | Yes|


### Return type: [Pong](../types/Pong.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Pong = $MadelineProto->ping_delay_disconnect(['ping_id' => long, 'disconnect_delay' => int, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - ping_delay_disconnect
* params - `{"ping_id": long, "disconnect_delay": int, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/ping_delay_disconnect`

Parameters:

ping_id - Json encoded long

disconnect_delay - Json encoded int




Or, if you're into Lua:

```lua
Pong = ping_delay_disconnect({ping_id=long, disconnect_delay=int, })
```

