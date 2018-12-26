---
title: inputMessageEntityMentionName
description: Message entity mention name
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMessageEntityMentionName  
[Back to constructors index](index.md)



Message entity mention name

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](../types/int.md) | Yes|Offset|
|length|[int](../types/int.md) | Yes|Length|
|user\_id|[InputUser](../types/InputUser.md) | Optional|User ID|



### Type: [MessageEntity](../types/MessageEntity.md)


### Example:

```php
$inputMessageEntityMentionName = ['_' => 'inputMessageEntityMentionName', 'offset' => int, 'length' => int, 'user_id' => InputUser];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputMessageEntityMentionName", "offset": int, "length": int, "user_id": InputUser}
```


Or, if you're into Lua:

```lua
inputMessageEntityMentionName={_='inputMessageEntityMentionName', offset=int, length=int, user_id=InputUser}

```


