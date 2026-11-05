# photos.photos

> Full list of photos with auxiliary data.

[Back to constructors index](/API_docs/constructors/index.html)



Full list of photos with auxiliary data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|photos|Array of [Photo](/API_docs/types/Photo.html) | Yes|List of photos|
|users|Array of [User](/API_docs/types/User.html) | Yes|List of mentioned users|



### Type: [photos.Photos](/API_docs/types/photos.Photos.html)


### Example:

```
$photos_photos = ['_' => 'photos.photos', 'photos' => [Photo, Photo], 'users' => [User, User]];
```
