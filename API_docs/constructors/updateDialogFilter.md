# updateDialogFilter

> A new folder was added

[Back to constructors index](/API_docs/constructors/index.html)



A new [folder](https://core.telegram.org/api/folders) was added

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](/API_docs/types/int.html) | Yes|[Folder](https://core.telegram.org/api/folders) ID|
|filter|[DialogFilter](/API_docs/types/DialogFilter.html) | Optional|[Folder](https://core.telegram.org/api/folders) info|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateDialogFilter = ['_' => 'updateDialogFilter', 'id' => int, 'filter' => DialogFilter];
```
