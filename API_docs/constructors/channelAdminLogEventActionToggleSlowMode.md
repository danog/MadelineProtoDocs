# channelAdminLogEventActionToggleSlowMode

> Slow mode setting for supergroups was changed

[Back to constructors index](/API_docs/constructors/index.html)



[Slow mode setting for supergroups was changed](../methods/channels.toggleSlowMode.html)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_value|[int](/API_docs/types/int.html) | Yes|Previous slow mode value|
|new\_value|[int](/API_docs/types/int.html) | Yes|New slow mode value|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionToggleSlowMode = ['_' => 'channelAdminLogEventActionToggleSlowMode', 'prev_value' => int, 'new_value' => int];
```
