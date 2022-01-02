---
title: "account.getThemes"
description: "Get installed themes"
grand_parent: "Telegram RPC API"
parent: "Methods"
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
|hash|[long](../types/long.md) |  | Yes|


### Return type: [account.Themes](../types/account.Themes.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$account_Themes = $MadelineProto->account->getThemes(['format' => 'string', 'hash' => long, ]);
```

Or, if you're into Lua:

```lua
account_Themes = account.getThemes({format='string', hash=long, })
```

