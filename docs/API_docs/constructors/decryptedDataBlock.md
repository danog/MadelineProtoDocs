---
title: decryptedDataBlock
description: Decrypted data block
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedDataBlock  
[Back to constructors index](index.md)



Decrypted data block

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|voice\_call\_id|[int128](../types/int128.md) | Optional|Voice call ID|
|in\_seq\_no|[int](../types/int.md) | Optional|In seq no|
|out\_seq\_no|[int](../types/int.md) | Optional|Out seq no|
|recent\_received\_mask|[int](../types/int.md) | Optional|Recent received mask|
|proto|[int](../types/int.md) | Optional|Proto|
|extra|[string](../types/string.md) | Optional|Extra|
|raw\_data|[string](../types/string.md) | Optional|Raw data|



### Type: [DecryptedDataBlock](../types/DecryptedDataBlock.md)


### Example:

```php
$decryptedDataBlock = ['_' => 'decryptedDataBlock', 'voice_call_id' => int128, 'in_seq_no' => int, 'out_seq_no' => int, 'recent_received_mask' => int, 'proto' => int, 'extra' => 'string', 'raw_data' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "decryptedDataBlock", "voice_call_id": int128, "in_seq_no": int, "out_seq_no": int, "recent_received_mask": int, "proto": int, "extra": "string", "raw_data": "string"}
```


Or, if you're into Lua:

```lua
decryptedDataBlock={_='decryptedDataBlock', voice_call_id=int128, in_seq_no=int, out_seq_no=int, recent_received_mask=int, proto=int, extra='string', raw_data='string'}

```


