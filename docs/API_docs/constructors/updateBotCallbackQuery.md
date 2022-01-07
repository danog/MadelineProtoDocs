---
title: "updateBotCallbackQuery"
description: "A callback button was pressed, and the button data was sent to the bot that created the button"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotCallbackQuery  
[Back to constructors index](/API_docs/constructors/index.md)



A callback button was pressed, and the button data was sent to the bot that created the button

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|query\_id|[long](/API_docs/types/long.md) | Yes|Query ID|
|user\_id|[long](/API_docs/types/long.md) | Yes|
|peer|[Peer](/API_docs/types/Peer.md) | Yes|Chat where the inline keyboard was sent|
|msg\_id|[int](/API_docs/types/int.md) | Yes|Message ID|
|chat\_instance|[long](/API_docs/types/long.md) | Yes|Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in games.|
|data|[bytes](/API_docs/types/bytes.md) | Optional|Callback data|
|game\_short\_name|[string](/API_docs/types/string.md) | Optional|Short name of a Game to be returned, serves as the unique identifier for the game|



### Type: [Update](/API_docs/types/Update.md)


### Example:

```php
$updateBotCallbackQuery = ['_' => 'updateBotCallbackQuery', 'query_id' => long, 'user_id' => long, 'peer' => Peer, 'msg_id' => int, 'chat_instance' => long, 'data' => 'bytes', 'game_short_name' => 'string'];
```  
