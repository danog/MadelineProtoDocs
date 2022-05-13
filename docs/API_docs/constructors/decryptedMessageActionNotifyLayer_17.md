---
title: "decryptedMessageActionNotifyLayer"
description: "A notification stating the API layer that is used by the client. You should use your current layer and take notice of the layer used on the other side of a conversation when sending messages."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageActionNotifyLayer\_17  
[Back to constructors index](/API_docs/constructors/index.html)



A notification stating the API layer that is used by the client. You should use your current layer and take notice of the layer used on the other side of a conversation when sending messages.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|layer|[int](/API_docs/types/int.html) | Yes|Layer number, must be **17** or higher (this constructor was introduced in [Layer 17](https://core.telegram.org/api/layers#layer-17)).|



### Type: [DecryptedMessageAction](/API_docs/types/DecryptedMessageAction.html)


### Example:

```
$decryptedMessageActionNotifyLayer_17 = ['_' => 'decryptedMessageActionNotifyLayer', 'layer' => int];
```  
