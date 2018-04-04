---
title: messages.dhConfigNotModified
description: messages_dhConfigNotModified attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.dhConfigNotModified  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|random|[bytes](../types/bytes.md) | Yes|



### Type: [messages\_DhConfig](../types/messages_DhConfig.md)


### Example:

```
$messages_dhConfigNotModified = ['_' => 'messages.dhConfigNotModified', 'random' => 'bytes'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messages.dhConfigNotModified", "random": "bytes"}
```


Or, if you're into Lua:  


```
messages_dhConfigNotModified={_='messages.dhConfigNotModified', random='bytes'}

```


