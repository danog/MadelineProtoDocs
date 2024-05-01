---
title: "decryptedMessageActionResend"
description: "Request for the other party in a Secret Chat to automatically resend a contiguous range of previously sent messages, as explained in Sequence number is Secret Chats."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageActionResend\_17  
[Back to constructors index](/API_docs/constructors/index.html)



Request for the other party in a Secret Chat to automatically resend a contiguous range of previously sent messages, as explained in [Sequence number is Secret Chats](https://core.telegram.org/api/end-to-end/seq_no).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|start\_seq\_no|[int](/API_docs/types/int.html) | Yes|`out_seq_no` of the first message to be resent, with correct parity|
|end\_seq\_no|[int](/API_docs/types/int.html) | Yes|`out_seq_no` of the last message to be resent, with same parity.|



### Type: [DecryptedMessageAction](/API_docs/types/DecryptedMessageAction.html)


### Example:

```
$decryptedMessageActionResend_17 = ['_' => 'decryptedMessageActionResend', 'start_seq_no' => int, 'end_seq_no' => int];
```  
