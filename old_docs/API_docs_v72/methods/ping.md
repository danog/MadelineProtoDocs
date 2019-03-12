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


### MadelineProto Example:


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

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - ping
* params - `{"ping_id": long, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/ping`

Parameters:

ping_id - Json encoded long




Or, if you're into Lua:

```lua
Pong = ping({ping_id=long, })
```

