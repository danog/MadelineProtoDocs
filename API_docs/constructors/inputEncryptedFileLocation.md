# inputEncryptedFileLocation

> Location of encrypted secret chat file.

[Back to constructors index](/API_docs/constructors/index.html)



Location of encrypted secret chat file.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|File ID, **id** parameter value from [encryptedFile](../constructors/encryptedFile.html)|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Checksum, **access\_hash** parameter value from [encryptedFile](../constructors/encryptedFile.html)|



### Type: [InputFileLocation](/API_docs/types/InputFileLocation.html)


### Example:

```
$inputEncryptedFileLocation = ['_' => 'inputEncryptedFileLocation', 'id' => long, 'access_hash' => long];
```
