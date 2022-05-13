---
title: "botInlineMessageText"
description: "Send a simple text message"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botInlineMessageText  
[Back to constructors index](/API_docs/constructors/index.html)



Send a simple text message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|no\_webpage|[Bool](/API_docs/types/Bool.html) | Optional|Disable webpage preview|
|message|[string](/API_docs/types/string.html) | Yes|The message|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | Optional|[Message entities for styled text](https://core.telegram.org/api/entities)|
|reply\_markup|[ReplyMarkup](/API_docs/types/ReplyMarkup.html) | Optional|Inline keyboard|



### Type: [BotInlineMessage](/API_docs/types/BotInlineMessage.html)



## Usage of reply_markup

You can provide bot API reply_markup objects here.  


### Example:

```
$botInlineMessageText = ['_' => 'botInlineMessageText', 'no_webpage' => Bool, 'message' => 'string', 'entities' => [MessageEntity, MessageEntity], 'reply_markup' => ReplyMarkup];
```  
