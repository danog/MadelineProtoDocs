# messagePeerVote

> How a peer voted in a poll

[Back to constructors index](/API_docs/constructors/index.html)



How a peer voted in a poll

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[long](/API_docs/types/long.html) | Yes|Peer ID|
|option|[bytes](/API_docs/types/bytes.html) | Yes|The option chosen by the peer|
|date|[int](/API_docs/types/int.html) | Yes|When did the peer cast the vote|



### Type: [MessagePeerVote](/API_docs/types/MessagePeerVote.html)


### Example:

```
$messagePeerVote = ['_' => 'messagePeerVote', 'peer' => long, 'option' => 'bytes', 'date' => int];
```
