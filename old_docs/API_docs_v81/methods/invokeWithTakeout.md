---
title: invokeWithTakeout
description: Invoke method from takeout session
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: invokeWithTakeout  
[Back to methods index](index.md)


Invoke method from takeout session

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|takeout\_id|[long](../types/long.md) | The takeout session ID | Yes|
|query|[!X](../types/!X.md) | The query | Yes|


### Return type: [X](../types/X.md)

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

$X = $MadelineProto->invokeWithTakeout(['takeout_id' => long, 'query' => !X, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - invokeWithTakeout
* params - `{"takeout_id": long, "query": !X, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/invokeWithTakeout`

Parameters:

takeout_id - Json encoded long

query - Json encoded !X




Or, if you're into Lua:

```lua
X = invokeWithTakeout({takeout_id=long, query=!X, })
```

