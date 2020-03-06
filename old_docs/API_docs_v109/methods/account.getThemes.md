---
title: account.getThemes
description: Get installed themes
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_getThemes.html
---
# Method: account.getThemes  
[Back to methods index](index.md)


Get installed themes

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|format|[string](../types/string.md) | Theme format, a string that identifies the theming engines supported by the client | Yes|
|hash|Array of [int](../types/int.md) | Hash for pagination | Optional|


### Return type: [account.Themes](../types/account.Themes.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$account.Themes = $MadelineProto->account->getThemes(['format' => 'string', 'hash' => [int, int], ]);
```

Or, if you're into Lua:

```lua
account.Themes = account.getThemes({format='string', hash={int}, })
```

