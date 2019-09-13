---
title: account.saveTheme
description: account.saveTheme parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.saveTheme  
[Back to methods index](index.md)


### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|theme|[InputTheme](../types/InputTheme.md) | Yes|
|unsave|[Bool](../types/Bool.md) | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->account->saveTheme(['theme' => InputTheme, 'unsave' => Bool, ]);
```

Or, if you're into Lua:

```lua
Bool = account.saveTheme({theme=InputTheme, unsave=Bool, })
```

