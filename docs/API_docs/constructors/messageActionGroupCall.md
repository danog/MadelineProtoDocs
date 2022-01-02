---
title: "messageActionGroupCall"
description: "messageActionGroupCall attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionGroupCall  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|call|[InputGroupCall](../types/InputGroupCall.md) | Yes|
|duration|[int](../types/int.md) | Optional|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionGroupCall = ['_' => 'messageActionGroupCall', 'call' => InputGroupCall, 'duration' => int];
```  


Or, if you're into Lua:

```lua
messageActionGroupCall={_='messageActionGroupCall', call=InputGroupCall, duration=int}

```


