---
title: sendMessageUploadVideoAction
description: User is uploading a video.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: sendMessageUploadVideoAction  
[Back to constructors index](index.md)



User is uploading a video.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|progress|[int](../types/int.md) | Yes|Progress percentage|



### Type: [SendMessageAction](../types/SendMessageAction.md)


### Example:

```php
$sendMessageUploadVideoAction = ['_' => 'sendMessageUploadVideoAction', 'progress' => int];
```  


Or, if you're into Lua:

```lua
sendMessageUploadVideoAction={_='sendMessageUploadVideoAction', progress=int}

```


