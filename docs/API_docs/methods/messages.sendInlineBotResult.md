---
title: "messages.sendInlineBotResult"
description: "Send a result obtained using [messages.getInlineBotResults](../methods/messages.getInlineBotResults.html)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_sendInlineBotResult.html
---
# Method: messages.sendInlineBotResult
[Back to methods index](index.html)



Send a result obtained using [messages.getInlineBotResults](../methods/messages.getInlineBotResults.html).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|silent|[Bool](/API_docs/types/Bool.html) | Whether to send the message silently (no notification will be triggered on the other client) | Optional|
|background|[Bool](/API_docs/types/Bool.html) | Whether to send the message in background | Optional|
|clear\_draft|[Bool](/API_docs/types/Bool.html) | Whether to clear the [draft](https://core.telegram.org/api/drafts) | Optional|
|hide\_via|[Bool](/API_docs/types/Bool.html) | Whether to hide the `via @botname` in the resulting message (only for bot usernames encountered in the [config](../constructors/config.html)) | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Destination | Optional|
|reply\_to\_msg\_id|[int](/API_docs/types/int.html) | ID of the message this message should reply to | Optional|
|query\_id|[long](/API_docs/types/long.html) | Query ID from [messages.getInlineBotResults](../methods/messages.getInlineBotResults.html) | Yes|
|id|[string](/API_docs/types/string.html) | Result ID from [messages.getInlineBotResults](../methods/messages.getInlineBotResults.html) | Yes|
|schedule\_date|[int](/API_docs/types/int.html) | Scheduled message date for scheduled messages | Optional|
|send\_as|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Send this message as the specified peer | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

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
$Updates = $MadelineProto->messages->sendInlineBotResult(silent: Bool, background: Bool, clear_draft: Bool, hide_via: Bool, peer: InputPeer, reply_to_msg_id: int, query_id: long, id: 'string', schedule_date: int, send_as: InputPeer, );
```

