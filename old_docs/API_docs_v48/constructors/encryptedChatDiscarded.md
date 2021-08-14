---
title: encryptedChatDiscarded
description: Discarded or deleted chat.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: encryptedChatDiscarded  
[Back to constructors index](index.md)



Discarded or deleted chat.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|history\_deleted|[Bool](../types/Bool.md) | Optional|
|id|[int](../types/int.md) | Yes|Chat ID|



### Type: [EncryptedChat](../types/EncryptedChat.md)


### Example:

```php
$encryptedChatDiscarded = ['_' => 'encryptedChatDiscarded', 'history_deleted' => Bool, 'id' => int];
```  


Or, if you're into Lua:

```lua
encryptedChatDiscarded={_='encryptedChatDiscarded', history_deleted=Bool, id=int}

```


