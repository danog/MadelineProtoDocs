# channelAdminLogEventActionDefaultBannedRights

> The default banned rights were modified

[Back to constructors index](/API_docs/constructors/index.html)



The default banned rights were modified

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_banned\_rights|[ChatBannedRights](/API_docs/types/ChatBannedRights.html) | Yes|Previous global [banned rights](https://core.telegram.org/api/rights)|
|new\_banned\_rights|[ChatBannedRights](/API_docs/types/ChatBannedRights.html) | Yes|New global [banned rights](https://core.telegram.org/api/rights).|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionDefaultBannedRights = ['_' => 'channelAdminLogEventActionDefaultBannedRights', 'prev_banned_rights' => ChatBannedRights, 'new_banned_rights' => ChatBannedRights];
```
