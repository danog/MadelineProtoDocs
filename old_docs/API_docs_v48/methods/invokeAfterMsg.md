---
title: invokeAfterMsg
description: Invokes a query after successfull completion of one of the previous queries.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: invokeAfterMsg
[Back to methods index](index.md)



Invokes a query after successfull completion of one of the previous queries.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|msg\_id|[long](../types/long.md) | Message identifier on which a current query depends | Yes|
|query|[!X](../types/!X.md) | The query itself | Yes|


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

$X = $MadelineProto->invokeAfterMsg(['msg_id' => long, 'query' => !X, ]);
```

Or, if you're into Lua:

```lua
X = invokeAfterMsg({msg_id=long, query=!X, })
```

