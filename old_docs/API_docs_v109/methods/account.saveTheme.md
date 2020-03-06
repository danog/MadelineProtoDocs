---
title: account.saveTheme
description: Save a theme
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_saveTheme.html
---
# Method: account.saveTheme  
[Back to methods index](index.md)


Save a theme

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|theme|[InputTheme](../types/InputTheme.md) | Theme to save | Yes|
|unsave|[Bool](../types/Bool.md) | Unsave | Yes|


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

