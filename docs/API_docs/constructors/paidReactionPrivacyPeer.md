---
title: "paidReactionPrivacyPeer"
description: "Send paid reactions as the specified peer, fetched using channels.getSendAs."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: paidReactionPrivacyPeer  
[Back to constructors index](/API_docs/constructors/index.html)



Send paid reactions as the specified peer, fetched using [channels.getSendAs](../methods/channels.getSendAs.html).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[InputPeer](/API_docs/types/InputPeer.html) | Optional|The peer to send reactions as.|



### Type: [PaidReactionPrivacy](/API_docs/types/PaidReactionPrivacy.html)


### Example:

```
$paidReactionPrivacyPeer = ['_' => 'paidReactionPrivacyPeer', 'peer' => InputPeer];
```  
