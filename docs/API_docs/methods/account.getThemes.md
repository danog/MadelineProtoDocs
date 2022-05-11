---
title: "account.getThemes"
description: "Get installed themes"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_getThemes.html
---
# Method: account.getThemes
[Back to methods index](index.html)



Get installed themes

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|format|[string](/API_docs/types/string.html) | Theme format, a string that identifies the theming engines supported by the client | Yes|
|hash|[long](/API_docs/types/long.html) | [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation) | Yes|


### Return type: [account.Themes](/API_docs/types/account.Themes.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$account_Themes = $MadelineProto->account->getThemes(format: 'string', hash: long, );
```

