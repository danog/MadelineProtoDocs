---
title: "decryptedMessageActionNotifyLayer"
description: "A notification stating the API layer that is used by the client. You should use your current layer and take notice of the layer used on the other side of a conversation when sending messages."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageActionNotifyLayer\_17  
[Back to constructors index](index.md)



A notification stating the API layer that is used by the client. You should use your current layer and take notice of the layer used on the other side of a conversation when sending messages.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|layer|[int](../types/int.md) | Yes|Layer number, must be **17** or higher (this contructor was introduced in [Layer 17](https://core.telegram.org/api/layers#layer-17)).|



### Type: [DecryptedMessageAction](../types/DecryptedMessageAction.md)


### Example:

```php
$decryptedMessageActionNotifyLayer_17 = ['_' => 'decryptedMessageActionNotifyLayer', 'layer' => int];
```  


Or, if you're into Lua:

```lua
decryptedMessageActionNotifyLayer_17={_='decryptedMessageActionNotifyLayer', layer=int}

```


