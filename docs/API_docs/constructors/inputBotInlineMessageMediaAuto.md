---
title: "inputBotInlineMessageMediaAuto"
description: "A media"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineMessageMediaAuto  
[Back to constructors index](index.md)



A media

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[string](../types/string.md) | Yes|Caption|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Optional|[Message entities for styled text](https://core.telegram.org/api/entities)|
|reply\_markup|[ReplyMarkup](../types/ReplyMarkup.md) | Optional|Inline keyboard|



### Type: [InputBotInlineMessage](../types/InputBotInlineMessage.md)


### Example:

```php
$inputBotInlineMessageMediaAuto = ['_' => 'inputBotInlineMessageMediaAuto', 'message' => 'string', 'entities' => [MessageEntity, MessageEntity], 'reply_markup' => ReplyMarkup];
```  


Or, if you're into Lua:

```lua
inputBotInlineMessageMediaAuto={_='inputBotInlineMessageMediaAuto', message='string', entities={MessageEntity}, reply_markup=ReplyMarkup}

```



## Usage of reply_markup

You can provide bot API reply_markup objects here.  


