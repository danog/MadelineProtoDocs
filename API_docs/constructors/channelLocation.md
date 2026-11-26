# channelLocation

> Geographical location of supergroup (geogroups)

[Back to constructors index](/API_docs/constructors/index.html)



Geographical location of supergroup (geogroups)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo\_point|[GeoPoint](/API_docs/types/GeoPoint.html) | Optional|Geographical location of supergroup|
|address|[string](/API_docs/types/string.html) | Yes|Textual description of the address|



### Type: [ChannelLocation](/API_docs/types/ChannelLocation.html)


### Example:

```
$channelLocation = ['_' => 'channelLocation', 'geo_point' => GeoPoint, 'address' => 'string'];
```
