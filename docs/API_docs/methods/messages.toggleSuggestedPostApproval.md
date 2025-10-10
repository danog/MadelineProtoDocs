---
title: "messages.toggleSuggestedPostApproval"
description: "Approve or reject a [suggested post »](https://core.telegram.org/api/suggested-posts)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_toggleSuggestedPostApproval.html
---
# Method: messages.toggleSuggestedPostApproval
[Back to methods index](index.html)



Approve or reject a [suggested post »](https://core.telegram.org/api/suggested-posts).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|reject|[Bool](/API_docs/types/Bool.html) | Reject the suggested post. | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Both for users and channels, must contain the ID of the [direct messages monoforum »](https://core.telegram.org/api/monoforum) (for channels, the topic ID is extracted automatically from the `msg_id`). | Optional|
|msg\_id|[int](/API_docs/types/int.html) | ID of the suggestion message. | Optional|
|schedule\_date|[int](/API_docs/types/int.html) | Custom scheduling date. | Optional|
|reject\_comment|[string](/API_docs/types/string.html) | Optional comment for rejections (can only be used if `reject` is set). | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can users use this method: **YES**


### Can bots use this method: **YES**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->toggleSuggestedPostApproval(reject: $Bool, peer: $InputPeer, msg_id: $int, schedule_date: $int, reject_comment: 'string', );
```

