---
title: "encryptedChatDiscarded"
description: "Discarded or deleted chat."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: encryptedChatDiscarded  
[Back to constructors index](/API_docs/constructors/index.html)



Discarded or deleted chat.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|history\_deleted|[Bool](/API_docs/types/Bool.html) | Optional|
|id|[int](/API_docs/types/int.html) | Yes|Chat ID|



### Type: [EncryptedChat](/API_docs/types/EncryptedChat.html)


### Example:

```php
$encryptedChatDiscarded = ['_' => 'encryptedChatDiscarded', 'history_deleted' => Bool, 'id' => int];
```  
