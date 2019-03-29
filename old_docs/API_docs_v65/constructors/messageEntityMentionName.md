---
title: messageEntityMentionName
description: Message entity mention name
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityMentionName  
[Back to constructors index](index.md)



Message entity mention name

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](../types/int.md) | Yes|Offset|
|length|[int](../types/int.md) | Yes|Length|
|user\_id|[int](../types/int.md) | Yes|User ID|



### Type: [MessageEntity](../types/MessageEntity.md)


### Example:

```php
$messageEntityMentionName = ['_' => 'messageEntityMentionName', 'offset' => int, 'length' => int, 'user_id' => int];
```  


Or, if you're into Lua:

```lua
messageEntityMentionName={_='messageEntityMentionName', offset=int, length=int, user_id=int}

```


