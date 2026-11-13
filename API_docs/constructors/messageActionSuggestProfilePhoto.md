# messageActionSuggestProfilePhoto

> A new profile picture was suggested using photos.uploadContactProfilePhoto.

[Back to constructors index](/API_docs/constructors/index.html)



A new profile picture was suggested using [photos.uploadContactProfilePhoto](../methods/photos.uploadContactProfilePhoto.html).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|photo|[Photo](/API_docs/types/Photo.html) | Optional|The photo that the user suggested we set as profile picture.|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionSuggestProfilePhoto = ['_' => 'messageActionSuggestProfilePhoto', 'photo' => Photo];
```
