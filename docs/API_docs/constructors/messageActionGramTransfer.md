---
title: "messageActionGramTransfer"
description: "messageActionGramTransfer attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionGramTransfer  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|amount|[long](/API_docs/types/long.html) | Yes|
|peer\_address|[string](/API_docs/types/string.html) | Yes|
|transaction\_id|[string](/API_docs/types/string.html) | Yes|
|comment|[string](/API_docs/types/string.html) | Optional|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionGramTransfer = ['_' => 'messageActionGramTransfer', 'amount' => long, 'peer_address' => 'string', 'transaction_id' => 'string', 'comment' => 'string'];
```  
