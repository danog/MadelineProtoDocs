# inputFolderPeer

> Peer in a folder

[Back to constructors index](/API_docs/constructors/index.html)



Peer in a folder

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|Peer|
|folder\_id|[int](/API_docs/types/int.html) | Yes|[Peer folder ID, for more info click here](https://core.telegram.org/api/folders#peer-folders)|



### Type: [InputFolderPeer](/API_docs/types/InputFolderPeer.html)


### Example:

```
$inputFolderPeer = ['_' => 'inputFolderPeer', 'peer' => InputPeer, 'folder_id' => int];
```
