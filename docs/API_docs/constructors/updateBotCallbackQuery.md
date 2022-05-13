---
title: "updateBotCallbackQuery"
description: "A callback button was pressed, and the button data was sent to the bot that created the button"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotCallbackQuery  
[Back to constructors index](/API_docs/constructors/index.html)



A callback button was pressed, and the button data was sent to the bot that created the button

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|query\_id|[long](/API_docs/types/long.html) | Yes|Query ID|
|user\_id|[long](/API_docs/types/long.html) | Yes|ID of the user that pressed the button|
|peer|[Peer](/API_docs/types/Peer.html) | Yes|Chat where the inline keyboard was sent|
|msg\_id|[int](/API_docs/types/int.html) | Yes|Message ID|
|chat\_instance|[long](/API_docs/types/long.html) | Yes|Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in games.|
|data|[bytes](/API_docs/types/bytes.html) | Optional|Callback data|
|game\_short\_name|[string](/API_docs/types/string.html) | Optional|Short name of a Game to be returned, serves as the unique identifier for the game|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateBotCallbackQuery = ['_' => 'updateBotCallbackQuery', 'query_id' => long, 'user_id' => long, 'peer' => Peer, 'msg_id' => int, 'chat_instance' => long, 'data' => 'bytes', 'game_short_name' => 'string'];
```  
