# messages.installStickerSet

> Install a stickerset

[Back to methods index](index.html)



Install a stickerset

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|stickerset|[InputStickerSet](/API_docs/types/InputStickerSet.html) | Stickerset to install | Optional|
|archived|[Bool](/API_docs/types/Bool.html) | Whether to archive stickerset | Yes|


### Return type: [messages.StickerSetInstallResult](/API_docs/types/messages.StickerSetInstallResult.html)

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

$messages_StickerSetInstallResult = $MadelineProto->messages->installStickerSet(stickerset: $InputStickerSet, archived: $Bool, );
```
