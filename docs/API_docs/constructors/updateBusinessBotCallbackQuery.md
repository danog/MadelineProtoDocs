---
title: "updateBusinessBotCallbackQuery"
description: "A callback button sent via a business connection was pressed, and the button data was sent to the bot that created the button."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBusinessBotCallbackQuery  
[Back to constructors index](/API_docs/constructors/index.html)



A callback button sent via a [business connection](https://core.telegram.org/api/business#connected-bots) was pressed, and the button data was sent to the bot that created the button.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|query\_id|[long](/API_docs/types/long.html) | Yes|Query ID|
|user\_id|[long](/API_docs/types/long.html) | Yes|ID of the user that pressed the button|
|connection\_id|[string](/API_docs/types/string.html) | Yes|[Business connection ID](https://core.telegram.org/api/business#connected-bots)|
|message|[Message](/API_docs/types/Message.html) | Optional|Message that contains the keyboard (also contains info about the chat where the message was sent).|
|reply\_to\_message|[Message](/API_docs/types/Message.html) | Optional|The message that `message` is replying to.|
|chat\_instance|[long](/API_docs/types/long.html) | Yes|Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in games.|
|data|[bytes](/API_docs/types/bytes.html) | Optional|Callback data|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateBusinessBotCallbackQuery = ['_' => 'updateBusinessBotCallbackQuery', 'query_id' => long, 'user_id' => long, 'connection_id' => 'string', 'message' => Message, 'reply_to_message' => Message, 'chat_instance' => long, 'data' => 'bytes'];
```  
