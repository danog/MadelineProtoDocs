---
title: account.updateTheme
description: Update theme
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_updateTheme.html
---
# Method: account.updateTheme
[Back to methods index](index.md)



Update theme

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|format|[string](../types/string.md) | Theme format, a string that identifies the theming engines supported by the client | Yes|
|theme|[InputTheme](../types/InputTheme.md) | Theme to update | Yes|
|slug|[string](../types/string.md) | Unique theme ID | Optional|
|title|[string](../types/string.md) | Theme name | Optional|
|document|[MessageMedia, Update, Message or InputDocument](../types/InputDocument.md) | Theme file | Optional|
|settings|Array of [InputThemeSettings](../types/InputThemeSettings.md) |  | Optional|


### Return type: [Theme](../types/Theme.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Theme = $MadelineProto->account->updateTheme(['format' => 'string', 'theme' => InputTheme, 'slug' => 'string', 'title' => 'string', 'document' => InputDocument, 'settings' => [InputThemeSettings, InputThemeSettings], ]);
```

Or, if you're into Lua:

```lua
Theme = account.updateTheme({format='string', theme=InputTheme, slug='string', title='string', document=InputDocument, settings={InputThemeSettings}, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|THEME_INVALID|Invalid theme provided|


