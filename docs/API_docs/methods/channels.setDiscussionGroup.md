---
title: "channels.setDiscussionGroup"
description: "Associate a group to a channel as [discussion group](https://core.telegram.org/api/discussion) for that channel"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_setDiscussionGroup.html
---
# Method: channels.setDiscussionGroup
[Back to methods index](index.html)



Associate a group to a channel as [discussion group](https://core.telegram.org/api/discussion) for that channel

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|broadcast|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | Channel | Optional|
|group|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | [Discussion group](https://core.telegram.org/api/discussion) to associate to the channel | Optional|


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
$Bool = $MadelineProto->channels->setDiscussionGroup(broadcast: InputChannel, group: InputChannel, );
```

