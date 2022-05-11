---
title: "account.updateTheme"
description: "Update theme"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_updateTheme.html
---
# Method: account.updateTheme
[Back to methods index](index.html)



Update theme

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|format|[string](/API_docs/types/string.html) | Theme format, a string that identifies the theming engines supported by the client | Yes|
|theme|[InputTheme](/API_docs/types/InputTheme.html) | Theme to update | Yes|
|slug|[string](/API_docs/types/string.html) | Unique theme ID | Optional|
|title|[string](/API_docs/types/string.html) | Theme name | Optional|
|document|[MessageMedia, Update, Message or InputDocument](/API_docs/types/InputDocument.html) | Theme file | Optional|
|settings|Array of [InputThemeSettings](/API_docs/types/InputThemeSettings.html) | Theme settings | Optional|


### Return type: [Theme](/API_docs/types/Theme.html)

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
$Theme = $MadelineProto->account->updateTheme(format: 'string', theme: InputTheme, slug: 'string', title: 'string', document: InputDocument, settings: [InputThemeSettings, InputThemeSettings], );
```

