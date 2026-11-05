# inputMediaPhoto

> Forwarded photo

[Back to constructors index](/API_docs/constructors/index.html)



Forwarded photo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|spoiler|[Bool](/API_docs/types/Bool.html) | Optional|Whether this media should be hidden behind a spoiler warning|
|live\_photo|[Bool](/API_docs/types/Bool.html) | Optional|
|id|[MessageMedia, Message, Update or InputPhoto](/API_docs/types/InputPhoto.html) | Optional|Photo to be forwarded|
|ttl\_seconds|[int](/API_docs/types/int.html) | Optional|Time to live in seconds of self-destructing photo|
|video|[MessageMedia, Message, Update or InputDocument](/API_docs/types/InputDocument.html) | Optional|



### Type: [InputMedia](/API_docs/types/InputMedia.html)


### Example:

```
$inputMediaPhoto = ['_' => 'inputMediaPhoto', 'spoiler' => Bool, 'live_photo' => Bool, 'id' => InputPhoto, 'ttl_seconds' => int, 'video' => InputDocument];
```
