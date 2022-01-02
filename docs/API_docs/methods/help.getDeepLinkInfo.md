---
title: "help.getDeepLinkInfo"
description: "Get info about a `t.me` link"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_getDeepLinkInfo.html
---
# Method: help.getDeepLinkInfo
[Back to methods index](index.md)



Get info about a `t.me` link

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|path|[string](../types/string.md) | Path in `t.me/path` | Yes|


### Return type: [help.DeepLinkInfo](../types/help.DeepLinkInfo.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$help_DeepLinkInfo = $MadelineProto->help->getDeepLinkInfo(['path' => 'string', ]);
```

Or, if you're into Lua:

```lua
help_DeepLinkInfo = help.getDeepLinkInfo({path='string', })
```

