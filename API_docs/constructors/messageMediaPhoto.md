# messageMediaPhoto

> Attached photo.

[Back to constructors index](/API_docs/constructors/index.html)



Attached photo.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|spoiler|[Bool](/API_docs/types/Bool.html) | Optional|Whether this media should be hidden behind a spoiler warning|
|live\_photo|[Bool](/API_docs/types/Bool.html) | Optional|
|photo|[Photo](/API_docs/types/Photo.html) | Optional|Photo|
|ttl\_seconds|[int](/API_docs/types/int.html) | Optional|Time to live in seconds of self-destructing photo|
|video|[Document](/API_docs/types/Document.html) | Optional|



### Type: [MessageMedia](/API_docs/types/MessageMedia.html)


### Example:

```
$messageMediaPhoto = ['_' => 'messageMediaPhoto', 'spoiler' => Bool, 'live_photo' => Bool, 'photo' => Photo, 'ttl_seconds' => int, 'video' => Document];
```
