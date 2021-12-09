---
title: stickers.suggestShortName
description: stickers.suggestShortName parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stickers_suggestShortName.html
---
# Method: stickers.suggestShortName
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|title|[string](../types/string.md) | Yes|


### Return type: [stickers.SuggestedShortName](../types/stickers.SuggestedShortName.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$stickers_SuggestedShortName = $MadelineProto->stickers->suggestShortName(['title' => 'string', ]);
```

Or, if you're into Lua:

```lua
stickers_SuggestedShortName = stickers.suggestShortName({title='string', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|TITLE_INVALID|The specified stickerpack title is invalid|


