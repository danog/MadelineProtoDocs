---
title: draftMessage
description: Draft message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: draftMessage  
[Back to constructors index](index.md)



Draft message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|no\_webpage|[Bool](../types/Bool.md) | Optional|No webpage?|
|reply\_to\_msg\_id|[int](../types/int.md) | Optional|Reply to msg ID|
|message|[string](../types/string.md) | Yes|Message|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Optional|Entities|
|date|[int](../types/int.md) | Yes|Date|



### Type: [DraftMessage](../types/DraftMessage.md)


### Example:

```php
$draftMessage = ['_' => 'draftMessage', 'no_webpage' => Bool, 'reply_to_msg_id' => int, 'message' => 'string', 'entities' => [MessageEntity, MessageEntity], 'date' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "draftMessage", "no_webpage": Bool, "reply_to_msg_id": int, "message": "string", "entities": [MessageEntity], "date": int}
```


Or, if you're into Lua:

```lua
draftMessage={_='draftMessage', no_webpage=Bool, reply_to_msg_id=int, message='string', entities={MessageEntity}, date=int}

```


