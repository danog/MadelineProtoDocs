---
title: sendMessageUploadDocumentAction
description: User is uploading a file.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: sendMessageUploadDocumentAction  
[Back to constructors index](index.md)



User is uploading a file.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|progress|[int](../types/int.md) | Yes|Progress percentage|



### Type: [SendMessageAction](../types/SendMessageAction.md)


### Example:

```php
$sendMessageUploadDocumentAction = ['_' => 'sendMessageUploadDocumentAction', 'progress' => int];
```  


Or, if you're into Lua:

```lua
sendMessageUploadDocumentAction={_='sendMessageUploadDocumentAction', progress=int}

```


