---
title: pageBlockChannel
description: pageBlockChannel attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockChannel  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|channel|[Chat](../types/Chat.md) | Optional|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```
$pageBlockChannel = ['_' => 'pageBlockChannel', 'channel' => Chat];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "pageBlockChannel", "channel": Chat}
```


Or, if you're into Lua:  


```
pageBlockChannel={_='pageBlockChannel', channel=Chat}

```


