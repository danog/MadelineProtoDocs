---
title: "account.installTheme"
description: "Install a theme"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_installTheme.html
---
# Method: account.installTheme
[Back to methods index](index.md)



Install a theme

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|dark|[Bool](/API_docs/types/Bool.md) | Whether to install the dark version | Optional|
|theme|[InputTheme](/API_docs/types/InputTheme.md) | Theme to install | Optional|
|format|[string](/API_docs/types/string.md) | Theme format, a string that identifies the theming engines supported by the client | Optional|
|base\_theme|[BaseTheme](/API_docs/types/BaseTheme.md) |  | Optional|


### Return type: [Bool](/API_docs/types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->account->installTheme(['dark' => Bool, 'theme' => InputTheme, 'format' => 'string', 'base_theme' => BaseTheme, ]);
```

