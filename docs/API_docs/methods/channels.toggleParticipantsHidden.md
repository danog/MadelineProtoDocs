---
title: "channels.toggleParticipantsHidden"
description: "Hide or display the participants list in a [supergroup](https://core.telegram.org/api/channel)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_toggleParticipantsHidden.html
---
# Method: channels.toggleParticipantsHidden
[Back to methods index](index.html)



Hide or display the participants list in a [supergroup](https://core.telegram.org/api/channel).

The supergroup must have at least `hidden_members_group_size_min` participants in order to use this method, as specified by the [client configuration parameters »](https://core.telegram.org/api/config#client-configuration).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | Supergroup ID | Optional|
|enabled|[Bool](/API_docs/types/Bool.html) | If true, will hide the participants list; otherwise will unhide it. | Yes|


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

$Updates = $MadelineProto->channels->toggleParticipantsHidden(channel: InputChannel, enabled: Bool, );
```

