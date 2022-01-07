---
title: "botInlineMessageMediaAuto"
description: "Send whatever media is attached to the botInlineMediaResult"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botInlineMessageMediaAuto  
[Back to constructors index](/API_docs/constructors/index.md)



Send whatever media is attached to the [botInlineMediaResult](../constructors/botInlineMediaResult.md)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[string](/API_docs/types/string.md) | Yes|Caption|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.md) | Optional|[Message entities for styled text](https://core.telegram.org/api/entities)|
|reply\_markup|[ReplyMarkup](/API_docs/types/ReplyMarkup.md) | Optional|Inline keyboard|



### Type: [BotInlineMessage](/API_docs/types/BotInlineMessage.md)


### Example:

```php
$botInlineMessageMediaAuto = ['_' => 'botInlineMessageMediaAuto', 'message' => 'string', 'entities' => [MessageEntity, MessageEntity], 'reply_markup' => ReplyMarkup];
```  

## Usage of reply_markup

You can provide bot API reply_markup objects here.  


