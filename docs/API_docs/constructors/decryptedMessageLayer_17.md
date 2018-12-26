---
title: decryptedMessageLayer
description: Decrypted message layer
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageLayer\_17  
[Back to constructors index](index.md)



Decrypted message layer

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|layer|[int](../types/int.md) | Yes|Layer|
|in\_seq\_no|[int](../types/int.md) | Yes|In seq no|
|out\_seq\_no|[int](../types/int.md) | Yes|Out seq no|
|message|[DecryptedMessage](../types/DecryptedMessage.md) | Yes|Message|



### Type: [DecryptedMessageLayer](../types/DecryptedMessageLayer.md)


### Example:

```php
$decryptedMessageLayer_17 = ['_' => 'decryptedMessageLayer', 'layer' => int, 'in_seq_no' => int, 'out_seq_no' => int, 'message' => DecryptedMessage];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "decryptedMessageLayer", "layer": int, "in_seq_no": int, "out_seq_no": int, "message": DecryptedMessage}
```


Or, if you're into Lua:

```lua
decryptedMessageLayer_17={_='decryptedMessageLayer', layer=int, in_seq_no=int, out_seq_no=int, message=DecryptedMessage}

```


