# inputReplyToMonoForum

> Used to send messages to a monoforum topic.

[Back to constructors index](/API_docs/constructors/index.html)



Used to send messages to a [monoforum topic](https://core.telegram.org/api/monoforum).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|monoforum\_peer\_id|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|The topic ID.|



### Type: [InputReplyTo](/API_docs/types/InputReplyTo.html)


### Example:

```
$inputReplyToMonoForum = ['_' => 'inputReplyToMonoForum', 'monoforum_peer_id' => InputPeer];
```
