# botVerification

> Describes a bot verification icon ».

[Back to constructors index](/API_docs/constructors/index.html)



Describes a [bot verification icon »](https://core.telegram.org/api/bots/verification).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|bot\_id|[long](/API_docs/types/long.html) | Yes|ID of the bot that verified this peer|
|icon|[long](/API_docs/types/long.html) | Yes|Verification icon|
|description|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Yes|



### Type: [BotVerification](/API_docs/types/BotVerification.html)


### Example:

```
$botVerification = ['_' => 'botVerification', 'bot_id' => long, 'icon' => long, 'description' => TextWithEntities];
```
