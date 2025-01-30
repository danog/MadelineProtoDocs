---
title: "messages.getPaidReactionPrivacy"
description: "Fetches an [updatePaidReactionPrivacy](../constructors/updatePaidReactionPrivacy.html) update with the current [default paid reaction privacy, see here »](https://core.telegram.org/api/reactions#paid-reactions) for more info."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getPaidReactionPrivacy.html
---
# Method: messages.getPaidReactionPrivacy
[Back to methods index](index.html)



Fetches an [updatePaidReactionPrivacy](../constructors/updatePaidReactionPrivacy.html) update with the current [default paid reaction privacy, see here »](https://core.telegram.org/api/reactions#paid-reactions) for more info.



### Return type: [Updates](/API_docs/types/Updates.html)

### Can userbots use this method: **YES**

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->getPaidReactionPrivacy();
```

