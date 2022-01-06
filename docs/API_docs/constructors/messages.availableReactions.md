---
title: "messages.availableReactions"
description: "messages.availableReactions attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_availableReactions.html
---
# Constructor: messages.availableReactions  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|hash|[int](../types/int.md) | Yes|
|reactions|Array of [AvailableReaction](../types/AvailableReaction.md) | Yes|



### Type: [messages.AvailableReactions](../types/messages.AvailableReactions.md)


### Example:

```php
$messages_availableReactions = ['_' => 'messages.availableReactions', 'hash' => int, 'reactions' => [AvailableReaction, AvailableReaction]];
```  


Or, if you're into Lua:

```lua
messages_availableReactions={_='messages.availableReactions', hash=int, reactions={AvailableReaction}}

```


