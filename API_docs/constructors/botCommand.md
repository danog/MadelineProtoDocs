# botCommand

> Describes a bot command that can be used in a chat

[Back to constructors index](/API_docs/constructors/index.html)



Describes a bot command that can be used in a chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|ephemeral|[Bool](/API_docs/types/Bool.html) | Optional|
|command|[string](/API_docs/types/string.html) | Yes|`/command` name|
|description|[string](/API_docs/types/string.html) | Yes|Description of the command|



### Type: [BotCommand](/API_docs/types/BotCommand.html)


### Example:

```
$botCommand = ['_' => 'botCommand', 'ephemeral' => Bool, 'command' => 'string', 'description' => 'string'];
```
