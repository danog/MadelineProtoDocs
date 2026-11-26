# messages.preparedInlineMessage

> Represents a prepared inline message received via a bot's mini app, that can be sent to some chats »

[Back to constructors index](/API_docs/constructors/index.html)



Represents a [prepared inline message received via a bot's mini app, that can be sent to some chats »](https://core.telegram.org/api/bots/inline#21-using-a-prepared-inline-message)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|query\_id|[long](/API_docs/types/long.html) | Yes|The `query_id` to pass to [messages.sendInlineBotResult](../methods/messages.sendInlineBotResult.html)|
|result|[BotInlineResult](/API_docs/types/BotInlineResult.html) | Yes|The contents of the message, to be shown in a preview|
|peer\_types|Array of [InlineQueryPeerType](/API_docs/types/InlineQueryPeerType.html) | Yes|Types of chats where this message can be sent|
|cache\_time|[int](/API_docs/types/int.html) | Yes|Caching validity of the results|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users mentioned in the results|



### Type: [messages.PreparedInlineMessage](/API_docs/types/messages.PreparedInlineMessage.html)


### Example:

```
$messages_preparedInlineMessage = ['_' => 'messages.preparedInlineMessage', 'query_id' => long, 'result' => BotInlineResult, 'peer_types' => [InlineQueryPeerType, InlineQueryPeerType], 'cache_time' => int, 'users' => [User, User]];
```
