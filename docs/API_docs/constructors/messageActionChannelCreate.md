---
title: "messageActionChannelCreate"
description: "The channel was created"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionChannelCreate  
[Back to constructors index](index.md)



The channel was created

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|title|[string](../types/string.md) | Yes|Original channel/supergroup title|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionChannelCreate = ['_' => 'messageActionChannelCreate', 'title' => 'string'];
```  


Or, if you're into Lua:

```lua
messageActionChannelCreate={_='messageActionChannelCreate', title='string'}

```


