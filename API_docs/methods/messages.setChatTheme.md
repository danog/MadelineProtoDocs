# messages.setChatTheme

> Change the chat theme of a certain chat, see [here »](https://core.telegram.org/api/themes#chat-themes) for more info.

[Back to methods index](index.html)



Change the chat theme of a certain chat, see [here »](https://core.telegram.org/api/themes#chat-themes) for more info.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Private chat where to change theme | Optional|
|theme|[InputChatTheme](/API_docs/types/InputChatTheme.html) | The theme to set. | Optional|


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

$Updates = $MadelineProto->messages->setChatTheme(peer: $InputPeer, theme: $InputChatTheme, );
```
