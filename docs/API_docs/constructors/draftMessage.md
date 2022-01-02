---
title: "draftMessage"
description: "Represents a message draft."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: draftMessage  
[Back to constructors index](index.md)



Represents a message [draft](https://core.telegram.org/api/drafts).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|no\_webpage|[Bool](../types/Bool.md) | Optional|Whether no webpage preview will be generated|
|reply\_to\_msg\_id|[int](../types/int.md) | Optional|The message this message will reply to|
|message|[string](../types/string.md) | Yes|The draft|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Optional|Message [entities](https://core.telegram.org/api/entities) for styled text.|
|date|[int](../types/int.md) | Yes|Date of last update of the draft.|



### Type: [DraftMessage](../types/DraftMessage.md)


### Example:

```php
$draftMessage = ['_' => 'draftMessage', 'no_webpage' => Bool, 'reply_to_msg_id' => int, 'message' => 'string', 'entities' => [MessageEntity, MessageEntity], 'date' => int];
```  


Or, if you're into Lua:

```lua
draftMessage={_='draftMessage', no_webpage=Bool, reply_to_msg_id=int, message='string', entities={MessageEntity}, date=int}

```


