---
title: account.getTheme
description: Get theme information
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.getTheme  
[Back to methods index](index.md)


Get theme information

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|format|[string](../types/string.md) | Theme format, a string that identifies the theming engines supported by the client | Yes|
|theme|[InputTheme](../types/InputTheme.md) | Theme | Yes|
|document\_id|[long](../types/long.md) | Document ID | Yes|


### Return type: [Theme](../types/Theme.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Theme = $MadelineProto->account->getTheme(['format' => 'string', 'theme' => InputTheme, 'document_id' => long, ]);
```

Or, if you're into Lua:

```lua
Theme = account.getTheme({format='string', theme=InputTheme, document_id=long, })
```

