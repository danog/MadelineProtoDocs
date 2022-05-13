---
title: "messageFwdHeader"
description: "Info about a forwarded message"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageFwdHeader  
[Back to constructors index](/API_docs/constructors/index.html)



Info about a forwarded message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|imported|[Bool](/API_docs/types/Bool.html) | Optional|Whether this message was [imported from a foreign chat service, click here for more info »](https://core.telegram.org/api/import)|
|from\_id|[Peer](/API_docs/types/Peer.html) | Optional|The ID of the user that originally sent the message|
|from\_name|[string](/API_docs/types/string.html) | Optional|The name of the user that originally sent the message|
|date|[int](/API_docs/types/int.html) | Yes|When was the message originally sent|
|channel\_post|[int](/API_docs/types/int.html) | Optional|ID of the channel message that was forwarded|
|post\_author|[string](/API_docs/types/string.html) | Optional|For channels and if signatures are enabled, author of the channel message|
|saved\_from\_peer|[Peer](/API_docs/types/Peer.html) | Optional|Only for messages forwarded to the current user (inputPeerSelf), full info about the user/channel that originally sent the message|
|saved\_from\_msg\_id|[int](/API_docs/types/int.html) | Optional|Only for messages forwarded to the current user (inputPeerSelf), ID of the message that was forwarded from the original user/channel|
|psa\_type|[string](/API_docs/types/string.html) | Optional|PSA type|



### Type: [MessageFwdHeader](/API_docs/types/MessageFwdHeader.html)


### Example:

```
$messageFwdHeader = ['_' => 'messageFwdHeader', 'imported' => Bool, 'from_id' => Peer, 'from_name' => 'string', 'date' => int, 'channel_post' => int, 'post_author' => 'string', 'saved_from_peer' => Peer, 'saved_from_msg_id' => int, 'psa_type' => 'string'];
```  
