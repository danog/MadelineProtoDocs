---
title: "account.reportProfilePhoto"
description: "Report a profile photo of a dialog"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_reportProfilePhoto.html
---
# Method: account.reportProfilePhoto
[Back to methods index](index.html)



Report a profile photo of a dialog

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The dialog | Optional|
|photo\_id|[MessageMedia, Update, Message or InputPhoto](/API_docs/types/InputPhoto.html) | Dialog photo ID | Optional|
|reason|[ReportReason](/API_docs/types/ReportReason.html) | Report reason | Yes|
|message|[string](/API_docs/types/string.html) | Comment for report moderation | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

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
$Bool = $MadelineProto->account->reportProfilePhoto(peer: InputPeer, photo_id: InputPhoto, reason: ReportReason, message: 'string', );
```


## Return value 

If the length of the provided message is bigger than 4096, the message will be split in chunks and the method will be called multiple times, with the same parameters (except for the message), and an array of [Bool](../types/Bool.html) will be returned instead.


