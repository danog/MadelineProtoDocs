---
title: decryptedMessageActionResend
description: decryptedMessageActionResend attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageActionResend\_17  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|start\_seq\_no|[int](../types/int.md) | Yes|
|end\_seq\_no|[int](../types/int.md) | Yes|



### Type: [DecryptedMessageAction](../types/DecryptedMessageAction.md)


### Example:

```php
$decryptedMessageActionResend_17 = ['_' => 'decryptedMessageActionResend', 'start_seq_no' => int, 'end_seq_no' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "decryptedMessageActionResend", "start_seq_no": int, "end_seq_no": int}
```


Or, if you're into Lua:

```lua
decryptedMessageActionResend_17={_='decryptedMessageActionResend', start_seq_no=int, end_seq_no=int}

```


