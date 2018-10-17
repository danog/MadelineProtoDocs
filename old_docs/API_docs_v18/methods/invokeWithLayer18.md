---
title: invokeWithLayer18
description: Invoke this method with layer 18
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: invokeWithLayer18  
[Back to methods index](index.md)


Invoke this method with layer 18

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|query|[!X](../types/!X.md) | The method call | Yes|


### Return type: [X](../types/X.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$X = $MadelineProto->invokeWithLayer18(['query' => !X, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - invokeWithLayer18
* params - `{"query": !X, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/invokeWithLayer18`

Parameters:

query - Json encoded !X




Or, if you're into Lua:

```lua
X = invokeWithLayer18({query=!X, })
```

