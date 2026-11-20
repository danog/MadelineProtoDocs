# upload.file

> File content.

[Back to constructors index](/API_docs/constructors/index.html)



File content.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[storage.FileType](/API_docs/constructors/storage.FileType.html) | Yes|File type|
|mtime|[int](/API_docs/types/int.html) | Yes|Modification time|
|bytes|[bytes](/API_docs/types/bytes.html) | Yes|Binary data, file content|



### Type: [upload.File](/API_docs/types/upload.File.html)


### Example:

```
$upload_file = ['_' => 'upload.file', 'type' => storage.FileType, 'mtime' => int, 'bytes' => 'bytes'];
```
