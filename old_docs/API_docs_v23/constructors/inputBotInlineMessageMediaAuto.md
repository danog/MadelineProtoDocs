---
title: inputBotInlineMessageMediaAuto
description: A media
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineMessageMediaAuto  
[Back to constructors index](index.md)



A media

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|caption|[string](../types/string.md) | Yes|
|reply\_markup|[ReplyMarkup](../types/ReplyMarkup.md) | Optional|Inline keyboard|



### Type: [InputBotInlineMessage](../types/InputBotInlineMessage.md)


### Example:

```php
$inputBotInlineMessageMediaAuto = ['_' => 'inputBotInlineMessageMediaAuto', 'caption' => 'string', 'reply_markup' => ReplyMarkup];
```  


Or, if you're into Lua:

```lua
inputBotInlineMessageMediaAuto={_='inputBotInlineMessageMediaAuto', caption='string', reply_markup=ReplyMarkup}

```



## Usage of reply_markup

You can provide bot API reply_markup objects here.  


