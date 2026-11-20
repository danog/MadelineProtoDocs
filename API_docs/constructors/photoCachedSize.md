# photoCachedSize

> Description of an image and its content.

[Back to constructors index](/API_docs/constructors/index.html)



Description of an image and its content.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[string](/API_docs/types/string.html) | Yes|Thumbnail type|
|w|[int](/API_docs/types/int.html) | Yes|Image width|
|h|[int](/API_docs/types/int.html) | Yes|Image height|
|bytes|[bytes](/API_docs/types/bytes.html) | Yes|Binary data, file content|



### Type: [PhotoSize](/API_docs/types/PhotoSize.html)


### Example:

```
$photoCachedSize = ['_' => 'photoCachedSize', 'type' => 'string', 'w' => int, 'h' => int, 'bytes' => 'bytes'];
```
