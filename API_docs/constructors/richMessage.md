# richMessage

> richMessage attributes, type and example

[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|rtl|[Bool](/API_docs/types/Bool.html) | Optional|
|part|[Bool](/API_docs/types/Bool.html) | Optional|
|blocks|Array of [PageBlock](/API_docs/types/PageBlock.html) | Yes|
|photos|Array of [Photo](/API_docs/types/Photo.html) | Yes|
|documents|Array of [Document](/API_docs/types/Document.html) | Yes|



### Type: [RichMessage](/API_docs/types/RichMessage.html)


### Example:

```
$richMessage = ['_' => 'richMessage', 'rtl' => Bool, 'part' => Bool, 'blocks' => [PageBlock, PageBlock], 'photos' => [Photo, Photo], 'documents' => [Document, Document]];
```
