---
title: "messages.setChatAvailableReactions"
description: "Change the set of [message reactions »](https://core.telegram.org/api/reactions) that can be used in a certain group, supergroup or channel"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_setChatAvailableReactions.html
---
# Method: messages.setChatAvailableReactions
[Back to methods index](index.html)



Change the set of [message reactions »](https://core.telegram.org/api/reactions) that can be used in a certain group, supergroup or channel

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Group where to apply changes | Optional|
|available\_reactions|[ChatReactions](/API_docs/types/ChatReactions.html) | Allowed reaction emojis | Yes|
|reactions\_limit|[int](/API_docs/types/int.html) | This flag may be used to impose a custom limit of unique reactions (i.e. a customizable version of [appConfig.reactions\_uniq\_max](https://core.telegram.org/api/config#reactions-uniq-max)); this field and the other info set by the method will then be available to users in [channelFull](../constructors/channelFull.html) and [chatFull](../constructors/chatFull.html). <br>If this flag is not set, the previously configured `reactions_limit` will not be altered. | Optional|
|paid\_enabled|[Bool](/API_docs/types/Bool.html) | If this flag is set and a [Bool](../types/Bool.html) is passed, the method will enable or disable [paid message reactions »](https://core.telegram.org/api/reactions#paid-reactions). If this flag is not set, the previously stored setting will not be changed. | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

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

$Updates = $MadelineProto->messages->setChatAvailableReactions(peer: $InputPeer, available_reactions: $ChatReactions, reactions_limit: $int, paid_enabled: $Bool, );
```

