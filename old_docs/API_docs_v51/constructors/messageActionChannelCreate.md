---
title: messageActionChannelCreate
description: messageActionChannelCreate attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionChannelCreate  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|title|[string](../types/string.md) | Yes|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```
$messageActionChannelCreate = ['_' => 'messageActionChannelCreate', 'title' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageActionChannelCreate", "title": "string"}
```


Or, if you're into Lua:  


```
messageActionChannelCreate={_='messageActionChannelCreate', title='string'}

```


