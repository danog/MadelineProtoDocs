---
title: messages.getStatsURL
description: Get stats URL
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getStatsURL  
[Back to methods index](index.md)


Get stats URL

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Peer | Optional|


### Return type: [StatsURL](../types/StatsURL.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$StatsURL = $MadelineProto->messages->getStatsURL(['peer' => InputPeer, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - messages.getStatsURL
* params - `{"peer": InputPeer, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/messages.getStatsURL`

Parameters:

peer - Json encoded InputPeer




Or, if you're into Lua:

```lua
StatsURL = messages.getStatsURL({peer=InputPeer, })
```

