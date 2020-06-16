---
title: invokeWithoutUpdates
description: Invoke a request without subscribing the used connection for [updates](https://core.telegram.org/api/updates) (this is enabled by default for [file queries](https://core.telegram.org/api/files)).
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: invokeWithoutUpdates
[Back to methods index](index.md)



Invoke a request without subscribing the used connection for [updates](https://core.telegram.org/api/updates) (this is enabled by default for [file queries](https://core.telegram.org/api/files)).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
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

$X = $MadelineProto->invokeWithoutUpdates(['query' => !X, ]);
```

Or, if you're into Lua:

```lua
X = invokeWithoutUpdates({query=!X, })
```

