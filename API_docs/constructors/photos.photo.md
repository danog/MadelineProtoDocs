# photos.photo

> Photo with auxiliary data.

[Back to constructors index](/API_docs/constructors/index.html)



Photo with auxiliary data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|photo|[Photo](/API_docs/types/Photo.html) | Optional|Photo|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users|



### Type: [photos.Photo](/API_docs/types/photos.Photo.html)


### Example:

```
$photos_photo = ['_' => 'photos.photo', 'photo' => Photo, 'users' => [User, User]];
```
