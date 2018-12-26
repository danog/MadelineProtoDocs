---
title: decryptedMessageActionResend
description: Decrypted message action resend
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageActionResend\_17  
[Back to constructors index](index.md)



Decrypted message action resend

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|start\_seq\_no|[int](../types/int.md) | Yes|Start seq no|
|end\_seq\_no|[int](../types/int.md) | Yes|End seq no|



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


