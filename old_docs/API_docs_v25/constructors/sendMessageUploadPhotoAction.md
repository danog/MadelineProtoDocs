---
title: sendMessageUploadPhotoAction
description: User is uploading a photo.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: sendMessageUploadPhotoAction  
[Back to constructors index](index.md)



User is uploading a photo.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|progress|[int](../types/int.md) | Yes|Progress percentage|



### Type: [SendMessageAction](../types/SendMessageAction.md)


### Example:

```php
$sendMessageUploadPhotoAction = ['_' => 'sendMessageUploadPhotoAction', 'progress' => int];
```  


Or, if you're into Lua:

```lua
sendMessageUploadPhotoAction={_='sendMessageUploadPhotoAction', progress=int}

```


