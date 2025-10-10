---
title: "messages.toggleTodoCompleted"
description: "Mark one or more items of a [todo list »](https://core.telegram.org/api/todo) as completed or not completed."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_toggleTodoCompleted.html
---
# Method: messages.toggleTodoCompleted
[Back to methods index](index.html)



Mark one or more items of a [todo list »](https://core.telegram.org/api/todo) as completed or not completed.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer where the todo list was posted. | Optional|
|msg\_id|[int](/API_docs/types/int.html) | ID of the message with the todo list. | Optional|
|completed|Array of [int](/API_docs/types/int.html) | Items to mark as completed. | Yes|
|incompleted|Array of [int](/API_docs/types/int.html) | Items to mark as not completed. | Yes|


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

$Updates = $MadelineProto->messages->toggleTodoCompleted(peer: $InputPeer, msg_id: $int, completed: [$int, $int], incompleted: [$int, $int], );
```

