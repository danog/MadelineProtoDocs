---
title: invokeWithMessagesRange
description: Invoke with messages range
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: invokeWithMessagesRange  
[Back to methods index](index.md)


Invoke with messages range

### Parameters:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|range|[MessageRange](../types/MessageRange.md) | Yes|The range|
|query|[!X](../types/!X.md) | Yes|The query|


### Return type: [X](../types/X.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$X = $MadelineProto->invokeWithMessagesRange(['range' => MessageRange, 'query' => !X, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - invokeWithMessagesRange
* params - `{"range": MessageRange, "query": !X, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/invokeWithMessagesRange`

Parameters:

range - Json encoded MessageRange

query - Json encoded !X




Or, if you're into Lua:

```
X = invokeWithMessagesRange({range=MessageRange, query=!X, })
```

