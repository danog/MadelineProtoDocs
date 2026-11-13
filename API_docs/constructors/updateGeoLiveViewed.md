# updateGeoLiveViewed

> Live geoposition message was viewed

[Back to constructors index](/API_docs/constructors/index.html)



Live geoposition message was viewed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[long](/API_docs/types/long.html) | Yes|The user that viewed the live geoposition|
|msg\_id|[int](/API_docs/types/int.html) | Yes|Message ID of geoposition message|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateGeoLiveViewed = ['_' => 'updateGeoLiveViewed', 'peer' => long, 'msg_id' => int];
```
