# connectedBot

> Contains info about a connected business bot ».

[Back to constructors index](/API_docs/constructors/index.html)



Contains info about a [connected business bot »](https://core.telegram.org/api/bots/connected-business-bots).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|bot\_id|[long](/API_docs/types/long.html) | Yes|ID of the connected bot|
|recipients|[BusinessBotRecipients](/API_docs/types/BusinessBotRecipients.html) | Yes|Specifies the private chats that a [connected business bot »](https://core.telegram.org/api/bots/connected-business-bots) may receive messages and interact with.<br>|
|rights|[BusinessBotRights](/API_docs/types/BusinessBotRights.html) | Yes|Business bot rights.|
|device|[string](/API_docs/types/string.html) | Optional|
|date|[int](/API_docs/types/int.html) | Optional|
|location|[string](/API_docs/types/string.html) | Optional|



### Type: [ConnectedBot](/API_docs/types/ConnectedBot.html)


### Example:

```
$connectedBot = ['_' => 'connectedBot', 'bot_id' => long, 'recipients' => BusinessBotRecipients, 'rights' => BusinessBotRights, 'device' => 'string', 'date' => int, 'location' => 'string'];
```
