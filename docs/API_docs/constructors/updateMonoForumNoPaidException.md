---
title: "updateMonoForumNoPaidException"
description: "An admin has (un)exempted this monoforum topic » from payment to send messages using account.toggleNoPaidMessagesException."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateMonoForumNoPaidException  
[Back to constructors index](/API_docs/constructors/index.html)



An admin has (un)exempted this [monoforum topic »](https://core.telegram.org/api/monoforum) from payment to send messages using [account.toggleNoPaidMessagesException](../methods/account.toggleNoPaidMessagesException.html).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|exception|[Bool](/API_docs/types/Bool.html) | Optional|If set, an admin has exempted this peer, otherwise the peer was unexempted.|
|channel\_id|[long](/API_docs/types/long.html) | Yes|The monoforum ID.|
|saved\_peer\_id|[Peer](/API_docs/types/Peer.html) | Yes|The peer/topic ID.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateMonoForumNoPaidException = ['_' => 'updateMonoForumNoPaidException', 'exception' => Bool, 'channel_id' => long, 'saved_peer_id' => Peer];
```  
