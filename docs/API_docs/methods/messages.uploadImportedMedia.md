---
title: "messages.uploadImportedMedia"
description: "messages.uploadImportedMedia parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_uploadImportedMedia.html
---
# Method: messages.uploadImportedMedia
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|import\_id|[long](/API_docs/types/long.html) | Yes|
|file\_name|[string](/API_docs/types/string.html) | Yes|
|media|[MessageMedia, Update, Message or InputMedia](/API_docs/types/InputMedia.html) | Optional|


### Return type: [MessageMedia](/API_docs/types/MessageMedia.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$MessageMedia = $MadelineProto->messages->uploadImportedMedia(['peer' => InputPeer, 'import_id' => long, 'file_name' => 'string', 'media' => InputMedia, ]);
```

