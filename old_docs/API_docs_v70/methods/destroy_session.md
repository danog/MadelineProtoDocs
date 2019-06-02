---
title: destroy_session
description: Destroy the current MTProto session
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: destroy\_session  
[Back to methods index](index.md)


Destroy the current MTProto session

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|session\_id|[long](../types/long.md) | The session to destroy | Yes|


### Return type: [DestroySessionRes](../types/DestroySessionRes.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$DestroySessionRes = $MadelineProto->destroy_session(['session_id' => long, ]);
```

Or, if you're into Lua:

```lua
DestroySessionRes = destroy_session({session_id=long, })
```

