# inputMediaDocumentExternal

> Document that will be downloaded by the telegram servers

[Back to constructors index](/API_docs/constructors/index.html)



Document that will be downloaded by the telegram servers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|spoiler|[Bool](/API_docs/types/Bool.html) | Optional|Whether this media should be hidden behind a spoiler warning|
|url|[string](/API_docs/types/string.html) | Yes|URL of the document|
|ttl\_seconds|[int](/API_docs/types/int.html) | Optional|Self-destruct time to live of document|
|video\_cover|[MessageMedia, Message, Update or InputPhoto](/API_docs/types/InputPhoto.html) | Optional|Custom video cover.|
|video\_timestamp|[int](/API_docs/types/int.html) | Optional|Start playing the video at the specified timestamp (seconds).|



### Type: [InputMedia](/API_docs/types/InputMedia.html)


### Example:

```
$inputMediaDocumentExternal = ['_' => 'inputMediaDocumentExternal', 'spoiler' => Bool, 'url' => 'string', 'ttl_seconds' => int, 'video_cover' => InputPhoto, 'video_timestamp' => int];
```
