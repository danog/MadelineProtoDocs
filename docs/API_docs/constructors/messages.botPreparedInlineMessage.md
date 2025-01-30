---
title: "messages.botPreparedInlineMessage"
description: "Represents a prepared inline message saved by a bot, to be sent to the user via a web app »"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_botPreparedInlineMessage.html
---
# Constructor: messages.botPreparedInlineMessage  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a [prepared inline message saved by a bot, to be sent to the user via a web app »](https://core.telegram.org/api/bots/inline#21-using-a-prepared-inline-message)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](/API_docs/types/string.html) | Yes|The ID of the saved message, to be passed to the `id` field of the [web\_app\_send\_prepared\_message event »](https://core.telegram.org/api/web-events#web-app-send-prepared-message)|
|expire\_date|[int](/API_docs/types/int.html) | Yes|Expiration date of the message|



### Type: [messages.BotPreparedInlineMessage](/API_docs/types/messages.BotPreparedInlineMessage.html)


### Example:

```
$messages_botPreparedInlineMessage = ['_' => 'messages.botPreparedInlineMessage', 'id' => 'string', 'expire_date' => int];
```  
