---
title: "inputBotInlineMessageMediaAuto"
description: "A media"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineMessageMediaAuto  
[Back to constructors index](/API_docs/constructors/index.html)



A media

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[string](/API_docs/types/string.html) | Yes|Caption|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | Optional|[Message entities for styled text](https://core.telegram.org/api/entities)|
|reply\_markup|[ReplyMarkup](/API_docs/types/ReplyMarkup.html) | Optional|Inline keyboard|



### Type: [InputBotInlineMessage](/API_docs/types/InputBotInlineMessage.html)



## Usage of reply_markup

You can provide bot API reply_markup objects here.  


### Example:

```
$inputBotInlineMessageMediaAuto = ['_' => 'inputBotInlineMessageMediaAuto', 'message' => 'string', 'entities' => [MessageEntity, MessageEntity], 'reply_markup' => ReplyMarkup];
```  
