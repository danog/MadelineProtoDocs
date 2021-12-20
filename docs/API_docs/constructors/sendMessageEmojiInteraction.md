---
title: "sendMessageEmojiInteraction"
description: "sendMessageEmojiInteraction attributes, type and example"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: sendMessageEmojiInteraction  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|emoticon|[string](../types/string.md) | Yes|
|msg\_id|[int](../types/int.md) | Yes|
|interaction|[DataJSON](../types/DataJSON.md) | Yes|



### Type: [SendMessageAction](../types/SendMessageAction.md)


### Example:

```php
$sendMessageEmojiInteraction = ['_' => 'sendMessageEmojiInteraction', 'emoticon' => 'string', 'msg_id' => int, 'interaction' => DataJSON];
```  


Or, if you're into Lua:

```lua
sendMessageEmojiInteraction={_='sendMessageEmojiInteraction', emoticon='string', msg_id=int, interaction=DataJSON}

```


