# updatePeerSettings

> Settings of a certain peer have changed

[Back to constructors index](/API_docs/constructors/index.html)



Settings of a certain peer have changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[long](/API_docs/types/long.html) | Yes|The peer|
|settings|[PeerSettings](/API_docs/types/PeerSettings.html) | Yes|Associated peer settings|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updatePeerSettings = ['_' => 'updatePeerSettings', 'peer' => long, 'settings' => PeerSettings];
```
