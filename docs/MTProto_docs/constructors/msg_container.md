---
title: msg_container
description: msg_container attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: msg\_container  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|messages|Array of [MTmessage](../constructors/MTmessage.md) | Yes|



### Type: [MessageContainer](../types/MessageContainer.md)


### Example:

```php
$msg_container = ['_' => 'msg_container', 'messages' => [MTmessage, MTmessage]];
```  


Or, if you're into Lua:

```lua
msg_container={_='msg_container', messages={MTmessage}}

```


