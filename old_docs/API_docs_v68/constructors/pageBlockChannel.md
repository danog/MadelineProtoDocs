---
title: pageBlockChannel
description: Page block channel
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockChannel  
[Back to constructors index](index.md)



Page block channel

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel|[Chat](../types/Chat.md) | Optional|Channel|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockChannel = ['_' => 'pageBlockChannel', 'channel' => Chat];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "pageBlockChannel", "channel": Chat}
```


Or, if you're into Lua:

```lua
pageBlockChannel={_='pageBlockChannel', channel=Chat}

```


