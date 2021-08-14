---
title: messageActionGroupCallScheduled
description: messageActionGroupCallScheduled attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionGroupCallScheduled  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|call|[InputGroupCall](../types/InputGroupCall.md) | Yes|
|schedule\_date|[int](../types/int.md) | Yes|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionGroupCallScheduled = ['_' => 'messageActionGroupCallScheduled', 'call' => InputGroupCall, 'schedule_date' => int];
```  


Or, if you're into Lua:

```lua
messageActionGroupCallScheduled={_='messageActionGroupCallScheduled', call=InputGroupCall, schedule_date=int}

```


