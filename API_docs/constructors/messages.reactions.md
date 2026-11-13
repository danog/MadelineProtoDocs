# messages.reactions

> List of message reactions

[Back to constructors index](/API_docs/constructors/index.html)



List of [message reactions](https://core.telegram.org/api/reactions)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[long](/API_docs/types/long.html) | Yes|Hash used for caching, can also be locally regenerated using the algorithm specified [here »](https://core.telegram.org/api/reactions#recent-reactions).|
|reactions|Array of [Reaction](/API_docs/types/Reaction.html) | Yes|Reactions|



### Type: [messages.Reactions](/API_docs/types/messages.Reactions.html)


### Example:

```
$messages_reactions = ['_' => 'messages.reactions', 'hash' => long, 'reactions' => [Reaction, Reaction]];
```
