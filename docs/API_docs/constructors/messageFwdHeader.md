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
|saved\_out|[Bool](/API_docs/types/Bool.html) | Optional|Only for messages forwarded to [saved messages »](https://core.telegram.org/api/saved-messages), set if the original message was outgoing (though the message may have been originally outgoing even if this flag is not set, if `from_id` points to the current user).|
|from\_id|[Peer](/API_docs/types/Peer.html) | Optional|The ID of the user that originally sent the message|
|from\_name|[string](/API_docs/types/string.html) | Optional|The name of the user that originally sent the message|
|date|[int](/API_docs/types/int.html) | Yes|When was the message originally sent|
|channel\_post|[int](/API_docs/types/int.html) | Optional|ID of the channel message that was forwarded|
|post\_author|[string](/API_docs/types/string.html) | Optional|For channels and if signatures are enabled, author of the channel message|
|saved\_from\_peer|[Peer](/API_docs/types/Peer.html) | Optional|Only for messages forwarded to [saved messages »](https://core.telegram.org/api/saved-messages), contains the dialog where the message was originally sent.|
|saved\_from\_msg\_id|[int](/API_docs/types/int.html) | Optional|Only for messages forwarded to [saved messages »](https://core.telegram.org/api/saved-messages), contains the original ID of the message in `saved_from_peer`.|
|saved\_from\_id|[Peer](/API_docs/types/Peer.html) | Optional|Only for forwarded messages reforwarded to [saved messages »](https://core.telegram.org/api/saved-messages), contains the sender of the original message (i.e. if user A sends a message, then user B forwards it somewhere, then user C saves it to saved messages, this field will contain the ID of user B and `from_id` will contain the ID of user A).|
|saved\_from\_name|[string](/API_docs/types/string.html) | Optional|Only for forwarded messages from users with forward privacy enabled, sent by users with forward privacy enabled, reforwarded to [saved messages »](https://core.telegram.org/api/saved-messages), contains the sender of the original message (i.e. if user A (fwd privacy enabled) sends a message, then user B (fwd privacy enabled) forwards it somewhere, then user C saves it to saved messages, this field will contain the name of user B and `from_name` will contain the name of user A).|
|saved\_date|[int](/API_docs/types/int.html) | Optional|Only for forwarded messages reforwarded to [saved messages »](https://core.telegram.org/api/saved-messages), indicates when was the original message sent (i.e. if user A sends a message @ unixtime 1, then user B forwards it somewhere @ unixtime 2, then user C saves it to saved messages @ unixtime 3, this field will contain 2, `date` will contain 1 and the `date` of the containing [message](../constructors/message.html) will contain 3).|
|psa\_type|[string](/API_docs/types/string.html) | Optional|PSA type|



### Type: [MessageFwdHeader](/API_docs/types/MessageFwdHeader.html)


### Example:

```
$messageFwdHeader = ['_' => 'messageFwdHeader', 'imported' => Bool, 'saved_out' => Bool, 'from_id' => Peer, 'from_name' => 'string', 'date' => int, 'channel_post' => int, 'post_author' => 'string', 'saved_from_peer' => Peer, 'saved_from_msg_id' => int, 'saved_from_id' => Peer, 'saved_from_name' => 'string', 'saved_date' => int, 'psa_type' => 'string'];
```  
