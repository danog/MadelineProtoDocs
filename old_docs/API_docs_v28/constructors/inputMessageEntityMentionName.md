---
title: inputMessageEntityMentionName
description: Message entity that can be used to create a user [user mention](https://core.telegram.org/api/mentions): received mentions use the [messageEntityMentionName](../constructors/messageEntityMentionName.md) constructor, instead.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMessageEntityMentionName  
[Back to constructors index](index.md)



Message entity that can be used to create a user [user mention](https://core.telegram.org/api/mentions): received mentions use the [messageEntityMentionName](../constructors/messageEntityMentionName.md) constructor, instead.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](../types/int.md) | Yes|Offset of message entity within message (in UTF-8 codepoints)|
|length|[int](../types/int.md) | Yes|Length of message entity within message (in UTF-8 codepoints)|
|user\_id|[InputUser](../types/InputUser.md) | Optional|Identifier of the user that was mentioned|



### Type: [MessageEntity](../types/MessageEntity.md)


### Example:

```php
$inputMessageEntityMentionName = ['_' => 'inputMessageEntityMentionName', 'offset' => int, 'length' => int, 'user_id' => InputUser];
```  


Or, if you're into Lua:

```lua
inputMessageEntityMentionName={_='inputMessageEntityMentionName', offset=int, length=int, user_id=InputUser}

```


