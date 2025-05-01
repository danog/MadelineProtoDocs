---
title: "updateGroupCallChainBlocks"
description: "updateGroupCallChainBlocks attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateGroupCallChainBlocks  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | Yes|
|sub\_chain\_id|[int](/API_docs/types/int.html) | Yes|
|blocks|Array of [bytes](/API_docs/types/bytes.html) | Yes|
|next\_offset|[int](/API_docs/types/int.html) | Yes|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateGroupCallChainBlocks = ['_' => 'updateGroupCallChainBlocks', 'call' => InputGroupCall, 'sub_chain_id' => int, 'blocks' => ['bytes', 'bytes'], 'next_offset' => int];
```  
