---
title: messageActionInviteToGroupCall
description: messageActionInviteToGroupCall attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionInviteToGroupCall  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|call|[InputGroupCall](../types/InputGroupCall.md) | Yes|
|users|Array of [long](../types/long.md) | Yes|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionInviteToGroupCall = ['_' => 'messageActionInviteToGroupCall', 'call' => InputGroupCall, 'users' => [long, long]];
```  


Or, if you're into Lua:

```lua
messageActionInviteToGroupCall={_='messageActionInviteToGroupCall', call=InputGroupCall, users={long}}

```


