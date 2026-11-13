# chatlists.exportedChatlistInvite

> Info about an exported chat folder deep link ».

[Back to constructors index](/API_docs/constructors/index.html)



Info about an exported [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|filter|[DialogFilter](/API_docs/types/DialogFilter.html) | Yes|Folder ID|
|invite|[ExportedChatlistInvite](/API_docs/types/ExportedChatlistInvite.html) | Yes|The exported [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links).|



### Type: [chatlists.ExportedChatlistInvite](/API_docs/types/chatlists.ExportedChatlistInvite.html)


### Example:

```
$chatlists_exportedChatlistInvite = ['_' => 'chatlists.exportedChatlistInvite', 'filter' => DialogFilter, 'invite' => ExportedChatlistInvite];
```
