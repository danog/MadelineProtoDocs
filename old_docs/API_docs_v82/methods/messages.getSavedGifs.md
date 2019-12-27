---
title: messages.getSavedGifs
description: Get saved GIFs
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getSavedGifs  
[Back to methods index](index.md)


Get saved GIFs

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [int](../types/int.md) |  the hash parameter of the previous result of this method | Optional|


### Return type: [messages\_SavedGifs](../types/messages_SavedGifs.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_SavedGifs = $MadelineProto->messages->getSavedGifs(['hash' => [int, int], ]);
```

Or, if you're into Lua:

```lua
messages_SavedGifs = messages.getSavedGifs({hash={int}, })
```

