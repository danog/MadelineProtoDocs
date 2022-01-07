---
title: "account.createTheme"
description: "Create a theme"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_createTheme.html
---
# Method: account.createTheme
[Back to methods index](index.md)



Create a theme

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|slug|[string](/API_docs/types/string.md) | Unique theme ID | Yes|
|title|[string](/API_docs/types/string.md) | Theme name | Yes|
|document|[MessageMedia, Update, Message or InputDocument](/API_docs/types/InputDocument.md) | Theme file | Optional|
|settings|Array of [InputThemeSettings](/API_docs/types/InputThemeSettings.md) |  | Optional|


### Return type: [Theme](/API_docs/types/Theme.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Theme = $MadelineProto->account->createTheme(['slug' => 'string', 'title' => 'string', 'document' => InputDocument, 'settings' => [InputThemeSettings, InputThemeSettings], ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|THEME_MIME_INVALID|The theme's MIME type is invalid|


