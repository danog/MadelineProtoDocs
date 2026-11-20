# botCommandScopePeerAdmins

> The specified bot commands will be valid for all admins of the specified group or supergroup.

[Back to constructors index](/API_docs/constructors/index.html)



The specified bot commands will be valid for all admins of the specified [group or supergroup](https://core.telegram.org/api/channel).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[InputPeer](/API_docs/types/InputPeer.html) | Optional|The chat|



### Type: [BotCommandScope](/API_docs/types/BotCommandScope.html)


### Example:

```
$botCommandScopePeerAdmins = ['_' => 'botCommandScopePeerAdmins', 'peer' => InputPeer];
```
