---
title: "messageEntityMentionName"
description: "Message entity representing a user mention: for creating a mention use inputMessageEntityMentionName."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityMentionName  
[Back to constructors index](index.md)



Message entity representing a [user mention](https://core.telegram.org/api/mentions): for *creating* a mention use [inputMessageEntityMentionName](../constructors/inputMessageEntityMentionName.md).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](../types/int.md) | Yes|Offset of message entity within message (in UTF-8 codepoints)|
|length|[int](../types/int.md) | Yes|Length of message entity within message (in UTF-8 codepoints)|
|user\_id|[long](../types/long.md) | Yes|



### Type: [MessageEntity](../types/MessageEntity.md)


### Example:

```php
$messageEntityMentionName = ['_' => 'messageEntityMentionName', 'offset' => int, 'length' => int, 'user_id' => long];
```  


Or, if you're into Lua:

```lua
messageEntityMentionName={_='messageEntityMentionName', offset=int, length=int, user_id=long}

```


