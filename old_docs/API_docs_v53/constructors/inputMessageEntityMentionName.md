---
title: inputMessageEntityMentionName
description: inputMessageEntityMentionName attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMessageEntityMentionName  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|offset|[int](../types/int.md) | Yes|
|length|[int](../types/int.md) | Yes|
|user\_id|[InputUser](../types/InputUser.md) | Optional|



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


