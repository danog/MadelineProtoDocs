---
title: sendMessageUploadRoundAction
description: Send message upload round action
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: sendMessageUploadRoundAction  
[Back to constructors index](index.md)



Send message upload round action

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|progress|[int](../types/int.md) | Yes|Progress|



### Type: [SendMessageAction](../types/SendMessageAction.md)


### Example:

```php
$sendMessageUploadRoundAction = ['_' => 'sendMessageUploadRoundAction', 'progress' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "sendMessageUploadRoundAction", "progress": int}
```


Or, if you're into Lua:

```lua
sendMessageUploadRoundAction={_='sendMessageUploadRoundAction', progress=int}

```


