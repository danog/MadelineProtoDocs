---
title: "decryptedMessageActionCommitKey"
description: "Commit new key, see rekeying process"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageActionCommitKey\_20  
[Back to constructors index](/API_docs/constructors/index.html)



Commit new key, see [rekeying process](https://core.telegram.org/api/end-to-end/pfs)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|exchange\_id|[long](/API_docs/types/long.html) | Yes|Exchange ID, see [rekeying process](https://core.telegram.org/api/end-to-end/pfs)|
|key\_fingerprint|[long](/API_docs/types/long.html) | Yes|Key fingerprint, see [rekeying process](https://core.telegram.org/api/end-to-end/pfs)|



### Type: [DecryptedMessageAction](/API_docs/types/DecryptedMessageAction.html)


### Example:

```
$decryptedMessageActionCommitKey_20 = ['_' => 'decryptedMessageActionCommitKey', 'exchange_id' => long, 'key_fingerprint' => long];
```  
