---
title: langpack.getDifference
description: Get new strings in languagepack
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/langpack_getDifference.html
---
# Method: langpack.getDifference
[Back to methods index](index.md)



Get new strings in languagepack

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|from\_version|[int](../types/int.md) | Previous localization pack version | Yes|


### Return type: [LangPackDifference](../types/LangPackDifference.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$LangPackDifference = $MadelineProto->langpack->getDifference(['from_version' => int, ]);
```

Or, if you're into Lua:

```lua
LangPackDifference = langpack.getDifference({from_version=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|LANG_PACK_INVALID|The provided language pack is invalid|


