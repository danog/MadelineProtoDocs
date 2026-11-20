# messages.createChat

> Creates a new chat.

[Back to methods index](index.html)



Creates a new chat.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|users|Array of [Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | List of user IDs to be invited | Yes|
|title|[string](/API_docs/types/string.html) | Chat name | Optional|
|ttl\_period|[int](/API_docs/types/int.html) | Time-to-live of all messages that will be sent in the chat: once message.date+message.ttl\_period === time(), the message will be deleted on the server, and must be deleted locally as well. You can use [messages.setDefaultHistoryTTL](../methods/messages.setDefaultHistoryTTL.html) to edit this value later. | Optional|


### Return type: [messages.InvitedUsers](/API_docs/types/messages.InvitedUsers.html)

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

$messages_InvitedUsers = $MadelineProto->messages->createChat(users: [$InputUser, $InputUser], title: 'string', ttl_period: $int, );
```
