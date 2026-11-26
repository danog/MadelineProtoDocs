# updateDialogUnreadMark

> The manual unread mark of a chat was changed

[Back to constructors index](/API_docs/constructors/index.html)



The manual unread mark of a chat was changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|unread|[Bool](/API_docs/types/Bool.html) | Optional|Was the chat marked or unmarked as read|
|peer|[DialogPeer](/API_docs/types/DialogPeer.html) | Yes|The dialog|
|saved\_peer\_id|[Peer](/API_docs/types/Peer.html) | Optional|If set, the mark is related to the specified [monoforum topic ID »](https://core.telegram.org/api/monoforum).|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateDialogUnreadMark = ['_' => 'updateDialogUnreadMark', 'unread' => Bool, 'peer' => DialogPeer, 'saved_peer_id' => Peer];
```
