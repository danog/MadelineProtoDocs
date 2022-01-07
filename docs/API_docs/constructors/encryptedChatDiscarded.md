---
title: "encryptedChatDiscarded"
description: "Discarded or deleted chat."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: encryptedChatDiscarded  
[Back to constructors index](/API_docs/constructors/index.md)



Discarded or deleted chat.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|history\_deleted|[Bool](/API_docs/types/Bool.md) | Optional|
|id|[int](/API_docs/types/int.md) | Yes|Chat ID|



### Type: [EncryptedChat](/API_docs/types/EncryptedChat.md)


### Example:

```php
$encryptedChatDiscarded = ['_' => 'encryptedChatDiscarded', 'history_deleted' => Bool, 'id' => int];
```  
