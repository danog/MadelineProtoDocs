---
title: "updateInlineBotCallbackQuery"
description: "This notification is received by bots when a button is pressed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateInlineBotCallbackQuery  
[Back to constructors index](/API_docs/constructors/index.html)



This notification is received by bots when a button is pressed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|query\_id|[long](/API_docs/types/long.html) | Yes|Query ID|
|user\_id|[long](/API_docs/types/long.html) | Yes|ID of the user that pressed the button|
|msg\_id|[InputBotInlineMessageID](/API_docs/types/InputBotInlineMessageID.html) | Yes|ID of the inline message with the button|
|chat\_instance|[long](/API_docs/types/long.html) | Yes|Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in games.|
|data|[bytes](/API_docs/types/bytes.html) | Optional|Data associated with the callback button. Be aware that a bad client can send arbitrary data in this field.|
|game\_short\_name|[string](/API_docs/types/string.html) | Optional|Short name of a Game to be returned, serves as the unique identifier for the game|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateInlineBotCallbackQuery = ['_' => 'updateInlineBotCallbackQuery', 'query_id' => long, 'user_id' => long, 'msg_id' => InputBotInlineMessageID, 'chat_instance' => long, 'data' => 'bytes', 'game_short_name' => 'string'];
```  
