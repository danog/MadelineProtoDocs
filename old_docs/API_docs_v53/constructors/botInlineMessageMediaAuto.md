---
title: botInlineMessageMediaAuto
description: Send whatever media is attached to the [botInlineMediaResult](../constructors/botInlineMediaResult.md)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botInlineMessageMediaAuto  
[Back to constructors index](index.md)



Send whatever media is attached to the [botInlineMediaResult](../constructors/botInlineMediaResult.md)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|caption|[string](../types/string.md) | Yes|Caption|
|reply\_markup|[ReplyMarkup](../types/ReplyMarkup.md) | Optional|Inline keyboard|



### Type: [BotInlineMessage](../types/BotInlineMessage.md)


### Example:

```php
$botInlineMessageMediaAuto = ['_' => 'botInlineMessageMediaAuto', 'caption' => 'string', 'reply_markup' => ReplyMarkup];
```  


Or, if you're into Lua:

```lua
botInlineMessageMediaAuto={_='botInlineMessageMediaAuto', caption='string', reply_markup=ReplyMarkup}

```



## Usage of reply_markup

You can provide bot API reply_markup objects here.  


