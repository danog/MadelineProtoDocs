---
title: "messages.startHistoryImport"
description: "messages.startHistoryImport parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_startHistoryImport.html
---
# Method: messages.startHistoryImport
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.md) | Optional|
|import\_id|[long](/API_docs/types/long.md) | Yes|


### Return type: [Bool](/API_docs/types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->startHistoryImport(['peer' => InputPeer, 'import_id' => long, ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|IMPORT_ID_INVALID|The specified import ID is invalid|


