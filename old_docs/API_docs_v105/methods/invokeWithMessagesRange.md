---
title: invokeWithMessagesRange
description: Invoke with messages range
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: invokeWithMessagesRange  
[Back to methods index](index.md)


Invoke with messages range

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|range|[MessageRange](../types/MessageRange.md) | The range | Yes|
|query|[!X](../types/!X.md) | The query | Yes|


### Return type: [X](../types/X.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$X = $MadelineProto->invokeWithMessagesRange(['range' => MessageRange, 'query' => !X, ]);
```

Or, if you're into Lua:

```lua
X = invokeWithMessagesRange({range=MessageRange, query=!X, })
```

