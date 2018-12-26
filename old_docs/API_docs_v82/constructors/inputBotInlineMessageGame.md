---
title: inputBotInlineMessageGame
description: Bot inline message game
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineMessageGame  
[Back to constructors index](index.md)



Bot inline message game

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|reply\_markup|[ReplyMarkup](../types/ReplyMarkup.md) | Optional|Reply markup|



### Type: [InputBotInlineMessage](../types/InputBotInlineMessage.md)


### Example:

```php
$inputBotInlineMessageGame = ['_' => 'inputBotInlineMessageGame', 'reply_markup' => ReplyMarkup];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputBotInlineMessageGame", "reply_markup": ReplyMarkup}
```


Or, if you're into Lua:

```lua
inputBotInlineMessageGame={_='inputBotInlineMessageGame', reply_markup=ReplyMarkup}

```



## Usage of reply_markup

You can provide bot API reply_markup objects here.  


