---
title: sendMessageUploadVideoAction
description: Send message upload video action
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: sendMessageUploadVideoAction  
[Back to constructors index](index.md)



Send message upload video action

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|progress|[int](../types/int.md) | Yes|Progress|



### Type: [SendMessageAction](../types/SendMessageAction.md)


### Example:

```php
$sendMessageUploadVideoAction = ['_' => 'sendMessageUploadVideoAction', 'progress' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "sendMessageUploadVideoAction", "progress": int}
```


Or, if you're into Lua:

```lua
sendMessageUploadVideoAction={_='sendMessageUploadVideoAction', progress=int}

```


