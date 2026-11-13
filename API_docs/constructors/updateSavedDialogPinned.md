# updateSavedDialogPinned

> A saved message dialog was pinned/unpinned

[Back to constructors index](/API_docs/constructors/index.html)



A [saved message dialog](https://core.telegram.org/api/saved-messages) was pinned/unpinned

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pinned|[Bool](/API_docs/types/Bool.html) | Optional|Whether the dialog was pinned|
|peer|[DialogPeer](/API_docs/types/DialogPeer.html) | Yes|The dialog|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateSavedDialogPinned = ['_' => 'updateSavedDialogPinned', 'pinned' => Bool, 'peer' => DialogPeer];
```
