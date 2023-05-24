---
title: "channels.toggleForum"
description: "Enable or disable [forum functionality](https://core.telegram.org/api/forum) in a supergroup."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_toggleForum.html
---
# Method: channels.toggleForum
[Back to methods index](index.html)



Enable or disable [forum functionality](https://core.telegram.org/api/forum) in a supergroup.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | Supergroup ID | Optional|
|enabled|[Bool](/API_docs/types/Bool.html) | Enable or disable forum functionality | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->channels->toggleForum(channel: InputChannel, enabled: Bool, );
```

