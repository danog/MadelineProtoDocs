---
title: "invokeWithTakeout"
description: "Invoke a method within a takeout session"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: invokeWithTakeout
[Back to methods index](index.md)



Invoke a method within a takeout session

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|takeout\_id|[long](../types/long.md) | Takeout session ID | Yes|
|query|[!X](../types/!X.md) | Query | Yes|


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

$X = $MadelineProto->invokeWithTakeout(['takeout_id' => long, 'query' => !X, ]);
```

Or, if you're into Lua:

```lua
X = invokeWithTakeout({takeout_id=long, query=!X, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|INPUT_FETCH_FAIL|Failed deserializing TL payload|


