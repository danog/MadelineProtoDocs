# updates.channelDifferenceEmpty

> There are no new updates

[Back to constructors index](/API_docs/constructors/index.html)



There are no new updates

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|final|[Bool](/API_docs/types/Bool.html) | Optional|Whether there are more updates that must be fetched (always false)|
|pts|[int](/API_docs/types/int.html) | Yes|The latest [PTS](https://core.telegram.org/api/updates)|
|timeout|[int](/API_docs/types/int.html) | Optional|Clients are supposed to refetch the channel difference after timeout seconds have elapsed, if the user is [currently viewing the chat, see here »](https://core.telegram.org/api/updates#subscribing-to-updates-of-channels-supergroups) for more info.|



### Type: [updates.ChannelDifference](/API_docs/types/updates.ChannelDifference.html)


### Example:

```
$updates_channelDifferenceEmpty = ['_' => 'updates.channelDifferenceEmpty', 'final' => Bool, 'pts' => int, 'timeout' => int];
```
