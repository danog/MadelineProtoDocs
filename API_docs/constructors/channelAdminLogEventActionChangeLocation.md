# channelAdminLogEventActionChangeLocation

> The geogroup location was changed

[Back to constructors index](/API_docs/constructors/index.html)



The geogroup location was changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_value|[ChannelLocation](/API_docs/types/ChannelLocation.html) | Optional|Previous location|
|new\_value|[ChannelLocation](/API_docs/types/ChannelLocation.html) | Optional|New location|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionChangeLocation = ['_' => 'channelAdminLogEventActionChangeLocation', 'prev_value' => ChannelLocation, 'new_value' => ChannelLocation];
```
