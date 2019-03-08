---
title: sendMessageUploadDocumentAction
description: Send message upload document action
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: sendMessageUploadDocumentAction  
[Back to constructors index](index.md)



Send message upload document action

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|progress|[int](../types/int.md) | Yes|Progress|



### Type: [SendMessageAction](../types/SendMessageAction.md)


### Example:

```php
$sendMessageUploadDocumentAction = ['_' => 'sendMessageUploadDocumentAction', 'progress' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "sendMessageUploadDocumentAction", "progress": int}
```


Or, if you're into Lua:

```lua
sendMessageUploadDocumentAction={_='sendMessageUploadDocumentAction', progress=int}

```


