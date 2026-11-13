# channelAdminLogEventActionEditMessage

> A message was edited

[Back to constructors index](/API_docs/constructors/index.html)



A message was edited

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_message|[Message](/API_docs/types/Message.html) | Optional|Old message|
|new\_message|[Message](/API_docs/types/Message.html) | Optional|New message|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionEditMessage = ['_' => 'channelAdminLogEventActionEditMessage', 'prev_message' => Message, 'new_message' => Message];
```
