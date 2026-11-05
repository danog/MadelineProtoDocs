# updateNotifySettings

> Changes in notification settings.

[Back to constructors index](/API_docs/constructors/index.html)



Changes in notification settings.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[NotifyPeer](/API_docs/types/NotifyPeer.html) | Yes|Notification source|
|notify\_settings|[PeerNotifySettings](/API_docs/types/PeerNotifySettings.html) | Yes|New notification settings|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateNotifySettings = ['_' => 'updateNotifySettings', 'peer' => NotifyPeer, 'notify_settings' => PeerNotifySettings];
```
