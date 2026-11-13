# updateBotDeleteBusinessMessage

> A message was deleted in a connected business chat ».

[Back to constructors index](/API_docs/constructors/index.html)



A message was deleted in a [connected business chat »](https://core.telegram.org/api/bots/connected-business-bots).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|connection\_id|[string](/API_docs/types/string.html) | Yes|Business connection ID.|
|peer|[long](/API_docs/types/long.html) | Yes|[Peer](https://core.telegram.org/api/peers) where the messages were deleted.|
|messages|Array of [int](/API_docs/types/int.html) | Yes|IDs of the messages that were deleted.|
|qts|[int](/API_docs/types/int.html) | Yes|New **qts** value, see [updates »](https://core.telegram.org/api/updates) for more info.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateBotDeleteBusinessMessage = ['_' => 'updateBotDeleteBusinessMessage', 'connection_id' => 'string', 'peer' => long, 'messages' => [int, int], 'qts' => int];
```
