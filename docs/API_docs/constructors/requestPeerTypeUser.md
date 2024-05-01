---
title: "requestPeerTypeUser"
description: "Choose a user."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: requestPeerTypeUser  
[Back to constructors index](/API_docs/constructors/index.html)



Choose a user.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|bot|[Bool](/API_docs/types/Bool.html) | Optional|Whether to allow choosing only bots.|
|premium|[Bool](/API_docs/types/Bool.html) | Optional|Whether to allow choosing only [Premium](https://core.telegram.org/api/premium) users.|



### Type: [RequestPeerType](/API_docs/types/RequestPeerType.html)


### Example:

```
$requestPeerTypeUser = ['_' => 'requestPeerTypeUser', 'bot' => Bool, 'premium' => Bool];
```  
