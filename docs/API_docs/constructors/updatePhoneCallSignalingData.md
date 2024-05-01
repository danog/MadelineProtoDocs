---
title: "updatePhoneCallSignalingData"
description: "Incoming phone call signaling payload"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePhoneCallSignalingData  
[Back to constructors index](/API_docs/constructors/index.html)



Incoming phone call signaling payload

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone\_call\_id|[long](/API_docs/types/long.html) | Yes|Phone call ID|
|data|[bytes](/API_docs/types/bytes.html) | Yes|Signaling payload|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updatePhoneCallSignalingData = ['_' => 'updatePhoneCallSignalingData', 'phone_call_id' => long, 'data' => 'bytes'];
```  
