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
|format|[string](/API_docs/types/string.html) | Theme format, a string that identifies the theming engines supported by the client | Optional|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) | [Hash used for caching, for more info click here](https://core.telegram.org/api/offsets#hash-generation). | Optional|


### Return type: [account.Themes](/API_docs/types/account.Themes.html)

### Can userbots use this method: **YES**

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$account_Themes = $MadelineProto->account->getThemes(format: 'string', hash: [$long\|string, $long\|string], );
```

