# pollAnswer

> A possible answer of a poll

[Back to constructors index](/API_docs/constructors/index.html)



A possible answer of a poll

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Yes|Textual representation of the answer (only [Premium](https://core.telegram.org/api/premium) users can use [custom emoji entities](https://core.telegram.org/api/custom-emoji) here).|
|option|[bytes](/API_docs/types/bytes.html) | Yes|The param that has to be passed to [messages.sendVote](../methods/messages.sendVote.html).|
|media|[MessageMedia](/API_docs/types/MessageMedia.html) | Optional|
|added\_by|[Peer](/API_docs/types/Peer.html) | Optional|
|date|[int](/API_docs/types/int.html) | Optional|



### Type: [PollAnswer](/API_docs/types/PollAnswer.html)


### Example:

```
$pollAnswer = ['_' => 'pollAnswer', 'text' => TextWithEntities, 'option' => 'bytes', 'media' => MessageMedia, 'added_by' => Peer, 'date' => int];
```
