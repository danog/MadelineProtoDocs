---
title: updateNewGeoChatMessage
description: updateNewGeoChatMessage attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateNewGeoChatMessage  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|message|[GeoChatMessage](../types/GeoChatMessage.md) | Optional|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateNewGeoChatMessage = ['_' => 'updateNewGeoChatMessage', 'message' => GeoChatMessage];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateNewGeoChatMessage", "message": GeoChatMessage}
```


Or, if you're into Lua:

```lua
updateNewGeoChatMessage={_='updateNewGeoChatMessage', message=GeoChatMessage}

```


