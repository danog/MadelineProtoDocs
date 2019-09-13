---
title: account.uploadTheme
description: Upload theme
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.uploadTheme  
[Back to methods index](index.md)


Upload theme

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|file|[File path or InputFile](../types/InputFile.md) | File | Yes|
|thumb|[File path or InputFile](../types/InputFile.md) | Thumb | Optional|
|file\_name|[string](../types/string.md) | File name | Yes|
|mime\_type|[string](../types/string.md) | Mime type | Yes|


### Return type: [Document](../types/Document.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Document = $MadelineProto->account->uploadTheme(['file' => InputFile, 'thumb' => InputFile, 'file_name' => 'string', 'mime_type' => 'string', ]);
```

Or, if you're into Lua:

```lua
Document = account.uploadTheme({file=InputFile, thumb=InputFile, file_name='string', mime_type='string', })
```

