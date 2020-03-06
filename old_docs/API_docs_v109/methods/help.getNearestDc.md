---
title: help.getNearestDc
description: Returns info on data centre nearest to the user.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_getNearestDc.html
---
# Method: help.getNearestDc  
[Back to methods index](index.md)


Returns info on data centre nearest to the user.



### Return type: [NearestDc](../types/NearestDc.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$NearestDc = $MadelineProto->help->getNearestDc();
```

Or, if you're into Lua:

```lua
NearestDc = help.getNearestDc({})
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|


