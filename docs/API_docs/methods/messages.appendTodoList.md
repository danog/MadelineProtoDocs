---
title: "messages.appendTodoList"
description: "Appends one or more items to a [todo list »](https://core.telegram.org/api/todo)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_appendTodoList.html
---
# Method: messages.appendTodoList
[Back to methods index](index.html)



Appends one or more items to a [todo list »](https://core.telegram.org/api/todo).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer where the todo list was posted. | Optional|
|msg\_id|[int](/API_docs/types/int.html) | ID of the message with the todo list. | Optional|
|list|Array of [TodoItem](/API_docs/types/TodoItem.html) | Items to append. | Yes|


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

$Updates = $MadelineProto->messages->appendTodoList(peer: $InputPeer, msg_id: $int, list: [$TodoItem, $TodoItem], );
```

