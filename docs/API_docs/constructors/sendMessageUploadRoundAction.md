---
title: "sendMessageUploadRoundAction"
description: "User is uploading a round video"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: sendMessageUploadRoundAction  
[Back to constructors index](index.md)



User is uploading a round video

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|progress|[int](../types/int.md) | Yes|Progress percentage|



### Type: [SendMessageAction](../types/SendMessageAction.md)


### Example:

```php
$sendMessageUploadRoundAction = ['_' => 'sendMessageUploadRoundAction', 'progress' => int];
```  


Or, if you're into Lua:

```lua
sendMessageUploadRoundAction={_='sendMessageUploadRoundAction', progress=int}

```


