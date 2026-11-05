# stories.getChatsToSend

> Obtain a list of channels where the user can post [stories](https://core.telegram.org/api/stories)

[Back to methods index](index.html)



Obtain a list of channels where the user can post [stories](https://core.telegram.org/api/stories)



### Return type: [messages.Chats](/API_docs/types/messages.Chats.html)

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

$messages_Chats = $MadelineProto->stories->getChatsToSend();
```
