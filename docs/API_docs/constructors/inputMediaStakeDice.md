---
title: "inputMediaStakeDice"
description: "inputMediaStakeDice attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaStakeDice  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|game\_hash|[string](/API_docs/types/string.html) | Yes|
|ton\_amount|[long](/API_docs/types/long.html) | Yes|
|client\_seed|[bytes](/API_docs/types/bytes.html) | Yes|



### Type: [InputMedia](/API_docs/types/InputMedia.html)


### Example:

```
$inputMediaStakeDice = ['_' => 'inputMediaStakeDice', 'game_hash' => 'string', 'ton_amount' => long, 'client_seed' => 'bytes'];
```  
