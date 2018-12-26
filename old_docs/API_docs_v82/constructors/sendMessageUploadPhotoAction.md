---
title: sendMessageUploadPhotoAction
description: Send message upload photo action
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: sendMessageUploadPhotoAction  
[Back to constructors index](index.md)



Send message upload photo action

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|progress|[int](../types/int.md) | Yes|Progress|



### Type: [SendMessageAction](../types/SendMessageAction.md)


### Example:

```php
$sendMessageUploadPhotoAction = ['_' => 'sendMessageUploadPhotoAction', 'progress' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "sendMessageUploadPhotoAction", "progress": int}
```


Or, if you're into Lua:

```lua
sendMessageUploadPhotoAction={_='sendMessageUploadPhotoAction', progress=int}

```


