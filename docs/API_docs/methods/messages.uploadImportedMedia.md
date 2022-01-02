---
title: "messages.uploadImportedMedia"
description: "messages.uploadImportedMedia parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_uploadImportedMedia.html
---
# Method: messages.uploadImportedMedia
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Optional|
|import\_id|[long](../types/long.md) | Yes|
|file\_name|[string](../types/string.md) | Yes|
|media|[MessageMedia, Update, Message or InputMedia](../types/InputMedia.md) | Optional|


### Return type: [MessageMedia](../types/MessageMedia.md)

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

Or, if you're into Lua:

```lua
MessageMedia = messages.uploadImportedMedia({peer=InputPeer, import_id=long, file_name='string', media=InputMedia, })
```

