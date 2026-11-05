# updateDialogPinned

> A dialog was pinned/unpinned

[Back to constructors index](/API_docs/constructors/index.html)



A dialog was pinned/unpinned

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pinned|[Bool](/API_docs/types/Bool.html) | Optional|Whether the dialog was pinned|
|folder\_id|[int](/API_docs/types/int.html) | Optional|[Peer folder ID, for more info click here](https://core.telegram.org/api/folders#peer-folders)|
|peer|[DialogPeer](/API_docs/types/DialogPeer.html) | Yes|The dialog|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateDialogPinned = ['_' => 'updateDialogPinned', 'pinned' => Bool, 'folder_id' => int, 'peer' => DialogPeer];
```
