# channelAdminLogEventActionChangePhoto

> The channel/supergroup's picture was changed

[Back to constructors index](/API_docs/constructors/index.html)



The channel/supergroup's picture was changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_photo|[Photo](/API_docs/types/Photo.html) | Optional|Previous picture|
|new\_photo|[Photo](/API_docs/types/Photo.html) | Optional|New picture|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionChangePhoto = ['_' => 'channelAdminLogEventActionChangePhoto', 'prev_photo' => Photo, 'new_photo' => Photo];
```
