---
title: "account.saveRingtone"
description: "Save or remove saved notification sound."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_saveRingtone.html
---
# Method: account.saveRingtone
[Back to methods index](index.html)



Save or remove saved notification sound.

If the notification sound is already in MP3 format, [account.savedRingtone](../constructors/account.savedRingtone.html) will be returned.  
Otherwise, it will be automatically converted and a [account.savedRingtoneConverted](../constructors/account.savedRingtoneConverted.html) will be returned, containing a new [document](../constructors/document.html) object that should be used to refer to the ringtone from now on (ie when deleting it using the `unsave` parameter, or when downloading it).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|[MessageMedia, Update, Message or InputDocument](/API_docs/types/InputDocument.html) | Notification sound uploaded using [account.uploadRingtone](../methods/account.uploadRingtone.html) | Optional|
|unsave|[Bool](/API_docs/types/Bool.html) | Whether to add or delete the notification sound | Yes|


### Return type: [account.SavedRingtone](/API_docs/types/account.SavedRingtone.html)

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

$account_SavedRingtone = $MadelineProto->account->saveRingtone(id: $InputDocument, unsave: $Bool, );
```

