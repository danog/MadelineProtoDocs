---
title: messages.getWebPagePreview
description: Get preview of webpage
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getWebPagePreview  
[Back to methods index](index.md)


Get preview of webpage

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|message|[string](../types/string.md) | Message from which to extract the preview | Yes|


### Return type: [MessageMedia](../types/MessageMedia.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$MessageMedia = $MadelineProto->messages->getWebPagePreview(['message' => 'string', ]);
```

Or, if you're into Lua:

```lua
MessageMedia = messages.getWebPagePreview({message='string', })
```


## Return value 

If the length of the provided message is bigger than 4096, the message will be split in chunks and the method will be called multiple times, with the same parameters (except for the message), and an array of [MessageMedia](../types/MessageMedia.md) will be returned instead.


### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|MESSAGE_EMPTY|The provided message is empty|


