# inputDocument

> Defines a document for subsequent interaction.

[Back to constructors index](/API_docs/constructors/index.html)



Defines a document for subsequent interaction.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|Document ID|
|access\_hash|[long](/API_docs/types/long.html) | Yes|**access\_hash** parameter from the [document](../constructors/document.html) constructor|
|file\_reference|[bytes](/API_docs/types/bytes.html) | Yes|[File reference](https://core.telegram.org/api/file-references)|



### Type: [InputDocument](/API_docs/types/InputDocument.html)


### Example:

```
$inputDocument = ['_' => 'inputDocument', 'id' => long, 'access_hash' => long, 'file_reference' => 'bytes'];
```
