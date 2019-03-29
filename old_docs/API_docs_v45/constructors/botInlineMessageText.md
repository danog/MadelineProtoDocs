---
title: botInlineMessageText
description: Bot inline message text
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botInlineMessageText  
[Back to constructors index](index.md)



Bot inline message text

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|no\_webpage|[Bool](../types/Bool.md) | Optional|No webpage?|
|message|[string](../types/string.md) | Yes|Message|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Optional|Entities|



### Type: [BotInlineMessage](../types/BotInlineMessage.md)


### Example:

```php
$botInlineMessageText = ['_' => 'botInlineMessageText', 'no_webpage' => Bool, 'message' => 'string', 'entities' => [MessageEntity, MessageEntity]];
```  


Or, if you're into Lua:

```lua
botInlineMessageText={_='botInlineMessageText', no_webpage=Bool, message='string', entities={MessageEntity}}

```


