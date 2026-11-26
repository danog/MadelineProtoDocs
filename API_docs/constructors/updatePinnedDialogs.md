# updatePinnedDialogs

> Pinned dialogs were updated

[Back to constructors index](/API_docs/constructors/index.html)



Pinned dialogs were updated

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|folder\_id|[int](/API_docs/types/int.html) | Optional|[Peer folder ID, for more info click here](https://core.telegram.org/api/folders#peer-folders)|
|order|Array of [DialogPeer](/API_docs/types/DialogPeer.html) | Optional|New order of pinned dialogs|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updatePinnedDialogs = ['_' => 'updatePinnedDialogs', 'folder_id' => int, 'order' => [DialogPeer, DialogPeer]];
```
