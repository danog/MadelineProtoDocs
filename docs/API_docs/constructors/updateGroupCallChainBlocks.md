---
title: "updateGroupCallChainBlocks"
description: "Contains updates to the blockchain of a conference call, see here » for more info."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateGroupCallChainBlocks  
[Back to constructors index](/API_docs/constructors/index.html)



Contains updates to the blockchain of a conference call, see [here »](https://core.telegram.org/api/end-to-end/group-calls) for more info.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | Yes|The conference call.|
|sub\_chain\_id|[int](/API_docs/types/int.html) | Yes|Subchain ID.|
|blocks|Array of [bytes](/API_docs/types/bytes.html) | Yes|Blocks.|
|next\_offset|[int](/API_docs/types/int.html) | Yes|Offset of the next block.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateGroupCallChainBlocks = ['_' => 'updateGroupCallChainBlocks', 'call' => InputGroupCall, 'sub_chain_id' => int, 'blocks' => ['bytes', 'bytes'], 'next_offset' => int];
```  
