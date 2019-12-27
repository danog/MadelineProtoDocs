---
title: pageBlockChannel
description: Reference to a telegram channel
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockChannel  
[Back to constructors index](index.md)



Reference to a telegram channel

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel|[Chat](../types/Chat.md) | Optional|The channel/supergroup/chat|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockChannel = ['_' => 'pageBlockChannel', 'channel' => Chat];
```  


Or, if you're into Lua:

```lua
pageBlockChannel={_='pageBlockChannel', channel=Chat}

```


