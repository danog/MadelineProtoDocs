---
title: "decryptedMessageLayer"
description: "Sets the layer number for the contents of an encrypted message."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageLayer\_17  
[Back to constructors index](/API_docs/constructors/index.html)



Sets the layer number for the contents of an encrypted message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|layer|[int](/API_docs/types/int.html) | Yes|Layer number. Mimimal value - **17** (the layer in which the constructor was added).|
|in\_seq\_no|[int](/API_docs/types/int.html) | Yes|2x the number of messages in the sender's inbox (including deleted and service messages), incremented by 1 if current user was not the chat creator<br>Parameter added in [Layer 17](https://core.telegram.org/api/layers#layer-17).|
|out\_seq\_no|[int](/API_docs/types/int.html) | Yes|2x the number of messages in the recipient's inbox (including deleted and service messages), incremented by 1 if current user was the chat creator<br>Parameter added in [Layer 17](https://core.telegram.org/api/layers#layer-17).|
|message|[DecryptedMessage](/API_docs/types/DecryptedMessage.html) | Yes|The content of message itself|



### Type: [DecryptedMessageLayer](/API_docs/types/DecryptedMessageLayer.html)


### Example:

```
$decryptedMessageLayer_17 = ['_' => 'decryptedMessageLayer', 'layer' => int, 'in_seq_no' => int, 'out_seq_no' => int, 'message' => DecryptedMessage];
```  
