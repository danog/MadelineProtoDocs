---
title: messages.getSavedGifs
description: Get saved GIFs
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getSavedGifs.html
---
# Method: messages.getSavedGifs
[Back to methods index](index.md)



Get saved GIFs

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [int](../types/int.md) | [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation) | Optional|


### Return type: [messages.SavedGifs](../types/messages.SavedGifs.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages.SavedGifs = $MadelineProto->messages->getSavedGifs(['hash' => [int, int], ]);
```

Or, if you're into Lua:

```lua
messages.SavedGifs = messages.getSavedGifs({hash={int}, })
```

