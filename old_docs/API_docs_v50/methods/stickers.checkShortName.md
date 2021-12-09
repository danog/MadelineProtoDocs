---
title: stickers.checkShortName
description: stickers.checkShortName parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stickers_checkShortName.html
---
# Method: stickers.checkShortName
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|short\_name|[string](../types/string.md) | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->stickers->checkShortName(['short_name' => 'string', ]);
```

Or, if you're into Lua:

```lua
Bool = stickers.checkShortName({short_name='string', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|SHORT_NAME_INVALID|The specified short name is invalid|
|400|SHORT_NAME_OCCUPIED|The specified short name is already in use|


