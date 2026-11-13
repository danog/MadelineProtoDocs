# updatePeerLocated

> List of peers near you was updated

[Back to constructors index](/API_docs/constructors/index.html)



List of peers near you was updated

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peers|Array of [PeerLocated](/API_docs/types/PeerLocated.html) | Yes|Geolocated peer list update|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updatePeerLocated = ['_' => 'updatePeerLocated', 'peers' => [PeerLocated, PeerLocated]];
```
