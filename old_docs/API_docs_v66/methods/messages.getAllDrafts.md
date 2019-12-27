---
title: messages.getAllDrafts
description: Save get all message [drafts](https://core.telegram.org/api/drafts).
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getAllDrafts.html
---
# Method: messages.getAllDrafts  
[Back to methods index](index.md)


Save get all message [drafts](https://core.telegram.org/api/drafts).



### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->getAllDrafts();
```

Or, if you're into Lua:

```lua
Updates = messages.getAllDrafts({})
```

