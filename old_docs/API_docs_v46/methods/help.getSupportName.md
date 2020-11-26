---
title: help.getSupportName
description: Get localized name of the telegram support user
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_getSupportName.html
---
# Method: help.getSupportName
[Back to methods index](index.md)



Get localized name of the telegram support user



### Return type: [help.SupportName](../types/help.SupportName.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$help.SupportName = $MadelineProto->help->getSupportName();
```

Or, if you're into Lua:

```lua
help.SupportName = help.getSupportName({})
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|403|USER_INVALID|Invalid user provided|


