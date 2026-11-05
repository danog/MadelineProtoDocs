# notificationSoundLocal

> Indicates a specific local notification sound should be used

[Back to constructors index](/API_docs/constructors/index.html)



Indicates a specific local notification sound should be used

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|title|[string](/API_docs/types/string.html) | Yes|Notification sound title|
|data|[string](/API_docs/types/string.html) | Yes|Notification sound identifier (arbitrary data used by the client to identify a specific local notification sound)|



### Type: [NotificationSound](/API_docs/types/NotificationSound.html)


### Example:

```
$notificationSoundLocal = ['_' => 'notificationSoundLocal', 'title' => 'string', 'data' => 'string'];
```
