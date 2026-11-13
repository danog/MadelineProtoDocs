# messages.saveRecentSticker

> Add/remove sticker from recent stickers list

[Back to methods index](index.html)



Add/remove sticker from recent stickers list

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|attached|[Bool](/API_docs/types/Bool.html) | Whether to add/remove stickers recently attached to photo or video files | Optional|
|id|[MessageMedia, Update, Message or InputDocument](/API_docs/types/InputDocument.html) | Sticker | Optional|
|unsave|[Bool](/API_docs/types/Bool.html) | Whether to save or unsave the sticker | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->saveRecentSticker(attached: $Bool, id: $InputDocument, unsave: $Bool, );
```
