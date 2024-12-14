---
title: "updates.getState"
description: "You cannot use this method directly, please use the [event handler](https://docs.madelineproto.xyz/docs/UPDATES.html), instead."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/updates_getState.html
---
# Method: updates.getState
[Back to methods index](index.html)



# Warning: this is a low-level, complex method that **must never** be used directly.
The [event handler](https://docs.madelineproto.xyz/docs/UPDATES.html) provides a high-level abstraction that **must** be used instead of this method to fetch updates.
If you want to fetch all users of a bot using a bot token, use [getDialogIds](https://docs.madelineproto.xyz/docs/DIALOGS.html) or the high-level [broadcast API](https://docs.madelineproto.xyz/docs/BROADCAST.html), instead.

You cannot use this method directly, please use the [event handler](https://docs.madelineproto.xyz/docs/UPDATES.html), instead.



### Return type: [updates.State](/API_docs/types/updates.State.html)

### Can userbots use this method: **YES**

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$updates_State = $MadelineProto->updates->getState();
```

