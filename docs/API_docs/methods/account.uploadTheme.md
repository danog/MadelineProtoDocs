---
title: "account.uploadTheme"
description: "Upload theme"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_uploadTheme.html
---
# Method: account.uploadTheme
[Back to methods index](index.html)



Upload theme

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|file|[File path or InputFile](/API_docs/types/InputFile.html) | Theme file uploaded as described in [files »](https://core.telegram.org/api/files) | Yes|
|thumb|[File path or InputFile](/API_docs/types/InputFile.html) | Thumbnail | Optional|
|file\_name|[string](/API_docs/types/string.html) | File name | Yes|
|mime\_type|[string](/API_docs/types/string.html) | MIME type, must be `application/x-tgtheme-{format}`, where `format` depends on the client | Yes|


### Return type: [Document](/API_docs/types/Document.html)

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
$Document = $MadelineProto->account->uploadTheme(file: InputFile, thumb: InputFile, file_name: 'string', mime_type: 'string', );
```

