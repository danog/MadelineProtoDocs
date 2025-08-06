---
title: "messages.toggleDialogFilterTags"
description: "Enable or disable [folder tags »](https://core.telegram.org/api/folders#folder-tags)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_toggleDialogFilterTags.html
---
# Method: messages.toggleDialogFilterTags
[Back to methods index](index.html)



Enable or disable [folder tags »](https://core.telegram.org/api/folders#folder-tags).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|enabled|[Bool](/API_docs/types/Bool.html) | Enable or disable folder tags. | Yes|


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

$Bool = $MadelineProto->messages->toggleDialogFilterTags(enabled: $Bool, );
```

