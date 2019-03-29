---
title: msg_container
description: Msg container
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: msg\_container  
[Back to constructors index](index.md)



Msg container

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|messages|Array of [MTmessage](../constructors/MTmessage.md) | Yes|Messages|



### Type: [MessageContainer](../types/MessageContainer.md)


### Example:

```php
$msg_container = ['_' => 'msg_container', 'messages' => [MTmessage, MTmessage]];
```  


Or, if you're into Lua:

```lua
msg_container={_='msg_container', messages={MTmessage}}

```


