---
title: inputBotInlineMessageText
description: Bot inline message text
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineMessageText  
[Back to constructors index](index.md)



Bot inline message text

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|no\_webpage|[Bool](../types/Bool.md) | Optional|No webpage?|
|message|[string](../types/string.md) | Yes|Message|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Optional|Entities|



### Type: [InputBotInlineMessage](../types/InputBotInlineMessage.md)


### Example:

```php
$inputBotInlineMessageText = ['_' => 'inputBotInlineMessageText', 'no_webpage' => Bool, 'message' => 'string', 'entities' => [MessageEntity, MessageEntity]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputBotInlineMessageText", "no_webpage": Bool, "message": "string", "entities": [MessageEntity]}
```


Or, if you're into Lua:

```lua
inputBotInlineMessageText={_='inputBotInlineMessageText', no_webpage=Bool, message='string', entities={MessageEntity}}

```


