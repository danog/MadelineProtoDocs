---
title: help.getDeepLinkInfo
description: Get deep link info
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: help.getDeepLinkInfo  
[Back to methods index](index.md)


Get deep link info

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|path|[string](../types/string.md) | Deep link | Yes|


### Return type: [help\_DeepLinkInfo](../types/help_DeepLinkInfo.md)

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

$help_DeepLinkInfo = $MadelineProto->help->getDeepLinkInfo(['path' => 'string', ]);
```

Or, if you're into Lua:

```lua
help_DeepLinkInfo = help.getDeepLinkInfo({path='string', })
```

