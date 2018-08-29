---
title: getChannelMembers
description: Returns information about channel members or banned users. Can be used only if channel_full->can_get_members == true. Administrator privileges may be additionally needed for some filters
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: getChannelMembers  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Returns information about channel members or banned users. Can be used only if channel_full->can_get_members == true. Administrator privileges may be additionally needed for some filters

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel\_id|[int](../types/int.md) | Identifier of the channel | Yes|
|filter|[ChannelMembersFilter](../types/ChannelMembersFilter.md) | Kind of channel users to return, defaults to channelMembersRecent | Yes|
|offset|[int](../types/int.md) | Number of channel users to skip | Yes|
|limit|[int](../types/int.md) | Maximum number of users be returned, can't be greater than 200 | Yes|


### Return type: [ChatMembers](../types/ChatMembers.md)

