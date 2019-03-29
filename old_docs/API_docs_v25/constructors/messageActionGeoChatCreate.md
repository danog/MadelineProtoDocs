---
title: messageActionGeoChatCreate
description: Message action geo chat create
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionGeoChatCreate  
[Back to constructors index](index.md)



Message action geo chat create

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|title|[string](../types/string.md) | Yes|Title|
|address|[string](../types/string.md) | Yes|Address|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionGeoChatCreate = ['_' => 'messageActionGeoChatCreate', 'title' => 'string', 'address' => 'string'];
```  


Or, if you're into Lua:

```lua
messageActionGeoChatCreate={_='messageActionGeoChatCreate', title='string', address='string'}

```


