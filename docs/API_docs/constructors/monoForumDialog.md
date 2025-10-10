---
title: "monoForumDialog"
description: "Represents a monoforum topic »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: monoForumDialog  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a [monoforum topic »](https://core.telegram.org/api/monoforum).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|unread\_mark|[Bool](/API_docs/types/Bool.html) | Optional|Whether this topic has a manually set (with [messages.markDialogUnread](../methods/messages.markDialogUnread.html)) unread mark.|
|nopaid\_messages\_exception|[Bool](/API_docs/types/Bool.html) | Optional|If set, an admin has exempted this peer from payment to send messages using [account.toggleNoPaidMessagesException](../methods/account.toggleNoPaidMessagesException.html).|
|peer|[long](/API_docs/types/long.html) | Yes|The peer associated to the topic, AKA the topic ID.|
|top\_message|[int](/API_docs/types/int.html) | Yes|The latest message ID|
|read\_inbox\_max\_id|[int](/API_docs/types/int.html) | Yes|Position up to which all incoming messages are read.|
|read\_outbox\_max\_id|[int](/API_docs/types/int.html) | Yes|Position up to which all outgoing messages are read.|
|unread\_count|[int](/API_docs/types/int.html) | Yes|Number of unread messages.|
|unread\_reactions\_count|[int](/API_docs/types/int.html) | Yes|Number of unread reactions.|
|draft|[DraftMessage](/API_docs/types/DraftMessage.html) | Optional|A pending message [draft](https://core.telegram.org/api/drafts).|



### Type: [SavedDialog](/API_docs/types/SavedDialog.html)


### Example:

```
$monoForumDialog = ['_' => 'monoForumDialog', 'unread_mark' => Bool, 'nopaid_messages_exception' => Bool, 'peer' => long, 'top_message' => int, 'read_inbox_max_id' => int, 'read_outbox_max_id' => int, 'unread_count' => int, 'unread_reactions_count' => int, 'draft' => DraftMessage];
```  
