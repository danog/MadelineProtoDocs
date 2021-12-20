---
title: "inputMessageReplyTo"
description: "Message to which the specified message replies to"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMessageReplyTo  
[Back to constructors index](index.md)



Message to which the specified message replies to

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|ID of the message that replies to the message we need|



### Type: [InputMessage](../types/InputMessage.md)


### Example:

```php
$inputMessageReplyTo = ['_' => 'inputMessageReplyTo', 'id' => int];
```  


Or, if you're into Lua:

```lua
inputMessageReplyTo={_='inputMessageReplyTo', id=int}

```


