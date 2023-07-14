---
title: "danog\\MadelineProto\\Namespace\\Stats: "
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\Namespace\Stats`
[Back to index](../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

  




## Method list:
* [`getBroadcastStats(array|int|string $channel, bool $dark = false): array{_: \"stats.broadcastStats", period: array{_: \"statsDateRangeDays", min_date: int, max_date: int}, followers: array{_: \"statsAbsValueAndPrev", current: float, previous: float}, views_per_post: array{_: \"statsAbsValueAndPrev", current: float, previous: float}, shares_per_post: array{_: \"statsAbsValueAndPrev", current: float, previous: float}, enabled_notifications: array{_: \"statsPercentValue", part: float, total: float}, growth_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, followers_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, mute_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, top_hours_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, interactions_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, iv_interactions_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, views_by_source_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, new_followers_by_source_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, languages_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, recent_message_interactions: \list<array{_: "messageInteractionCounters", msg_id: int, views: int, forwards: int}>} @see https://docs.madelineproto.xyz/API_docs/types/stats.BroadcastStats.htm}`](#getbroadcaststats-array-int-string-channel-bool-dark-false-array-_-stats-broadcaststats-period-array-_-statsdaterangedays-min_date-int-max_date-int-followers-array-_-statsabsvalueandprev-current-float-previous-float-views_per_post-array-_-statsabsvalueandprev-current-float-previous-float-shares_per_post-array-_-statsabsvalueandprev-current-float-previous-float-enabled_notifications-array-_-statspercentvalue-part-float-total-float-growth_graph-array-_-statsgraphasync-token-string-array-_-statsgrapherror-error-string-array-_-statsgraph-json-mixed-zoom_token-string-followers_graph-array-_-statsgraphasync-token-string-array-_-statsgrapherror-error-string-array-_-statsgraph-json-mixed-zoom_token-string-mute_graph-array-_-statsgraphasync-token-string-array-_-statsgrapherror-error-string-array-_-statsgraph-json-mixed-zoom_token-string-top_hours_graph-array-_-statsgraphasync-token-string-array-_-statsgrapherror-error-string-array-_-statsgraph-json-mixed-zoom_token-string-interactions_graph-array-_-statsgraphasync-token-string-array-_-statsgrapherror-error-string-array-_-statsgraph-json-mixed-zoom_token-string-iv_interactions_graph-array-_-statsgraphasync-token-string-array-_-statsgrapherror-error-string-array-_-statsgraph-json-mixed-zoom_token-string-views_by_source_graph-array-_-statsgraphasync-token-string-array-_-statsgrapherror-error-string-array-_-statsgraph-json-mixed-zoom_token-string-new_followers_by_source_graph-array-_-statsgraphasync-token-string-array-_-statsgrapherror-error-string-array-_-statsgraph-json-mixed-zoom_token-string-languages_graph-array-_-statsgraphasync-token-string-array-_-statsgrapherror-error-string-array-_-statsgraph-json-mixed-zoom_token-string-recent_message_interactions-list-array-_-messageinteractioncounters-msg_id-int-views-int-forwards-int-see-https-docs-madelineproto-xyz-api_docs-types-stats-broadcaststats-htm)
* [`loadAsyncGraph(string $token = '', int $x = 0): array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: \string} @see https://docs.madelineproto.xyz/API_docs/types/StatsGraph.htm}`](#loadasyncgraph-string-token-int-x-0-array-_-statsgraphasync-token-string-array-_-statsgrapherror-error-string-array-_-statsgraph-json-mixed-zoom_token-string-see-https-docs-madelineproto-xyz-api_docs-types-statsgraph-htm)
* [`getMegagroupStats(array|int|string $channel, bool $dark = false): array{_: \"stats.megagroupStats", period: array{_: \"statsDateRangeDays", min_date: int, max_date: int}, members: array{_: \"statsAbsValueAndPrev", current: float, previous: float}, messages: array{_: \"statsAbsValueAndPrev", current: float, previous: float}, viewers: array{_: \"statsAbsValueAndPrev", current: float, previous: float}, posters: array{_: \"statsAbsValueAndPrev", current: float, previous: float}, growth_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, members_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, new_members_by_source_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, languages_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, messages_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, actions_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, top_hours_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, weekdays_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, top_posters: list<array{_: \"statsGroupTopPoster", user_id: int, messages: int, avg_chars: int}>, top_admins: list<array{_: \"statsGroupTopAdmin", user_id: int, deleted: int, kicked: int, banned: int}>, top_inviters: list<array{_: \"statsGroupTopInviter", user_id: int, invitations: int}>, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/stats.MegagroupStats.htm}`](#getmegagroupstats-array-int-string-channel-bool-dark-false-array-_-stats-megagroupstats-period-array-_-statsdaterangedays-min_date-int-max_date-int-members-array-_-statsabsvalueandprev-current-float-previous-float-messages-array-_-statsabsvalueandprev-current-float-previous-float-viewers-array-_-statsabsvalueandprev-current-float-previous-float-posters-array-_-statsabsvalueandprev-current-float-previous-float-growth_graph-array-_-statsgraphasync-token-string-array-_-statsgrapherror-error-string-array-_-statsgraph-json-mixed-zoom_token-string-members_graph-array-_-statsgraphasync-token-string-array-_-statsgrapherror-error-string-array-_-statsgraph-json-mixed-zoom_token-string-new_members_by_source_graph-array-_-statsgraphasync-token-string-array-_-statsgrapherror-error-string-array-_-statsgraph-json-mixed-zoom_token-string-languages_graph-array-_-statsgraphasync-token-string-array-_-statsgrapherror-error-string-array-_-statsgraph-json-mixed-zoom_token-string-messages_graph-array-_-statsgraphasync-token-string-array-_-statsgrapherror-error-string-array-_-statsgraph-json-mixed-zoom_token-string-actions_graph-array-_-statsgraphasync-token-string-array-_-statsgrapherror-error-string-array-_-statsgraph-json-mixed-zoom_token-string-top_hours_graph-array-_-statsgraphasync-token-string-array-_-statsgrapherror-error-string-array-_-statsgraph-json-mixed-zoom_token-string-weekdays_graph-array-_-statsgraphasync-token-string-array-_-statsgrapherror-error-string-array-_-statsgraph-json-mixed-zoom_token-string-top_posters-list-array-_-statsgrouptopposter-user_id-int-messages-int-avg_chars-int-top_admins-list-array-_-statsgrouptopadmin-user_id-int-deleted-int-kicked-int-banned-int-top_inviters-list-array-_-statsgrouptopinviter-user_id-int-invitations-int-users-list-array-int-string-see-https-docs-madelineproto-xyz-api_docs-types-stats-megagroupstats-htm)
* [`getMessagePublicForwards(array|int|string $channel, array|int|string $offset_peer, int $msg_id = 0, int $offset_rate = 0, int $offset_id = 0, int $limit = 0): array{_: \"messages.messages", messages: list<array>, chats: list<array>, users: list<array>}|array{_: \"messages.messagesSlice", inexact: array, count: array, next_rate: array, offset_id_offset: array, messages: list<array>, chats: list<array>, users: list<array>}|array{_: \"messages.channelMessages", inexact: array, pts: array, count: array, offset_id_offset: array, messages: list<array>, topics: list<array>, chats: list<array>, users: list<array>}|array{_: \"messages.messagesNotModified", count: \array} @see https://docs.madelineproto.xyz/API_docs/types/messages.Messages.htm}`](#getmessagepublicforwards-array-int-string-channel-array-int-string-offset_peer-int-msg_id-0-int-offset_rate-0-int-offset_id-0-int-limit-0-array-_-messages-messages-messages-list-array-chats-list-array-users-list-array-array-_-messages-messagesslice-inexact-array-count-array-next_rate-array-offset_id_offset-array-messages-list-array-chats-list-array-users-list-array-array-_-messages-channelmessages-inexact-array-pts-array-count-array-offset_id_offset-array-messages-list-array-topics-list-array-chats-list-array-users-list-array-array-_-messages-messagesnotmodified-count-array-see-https-docs-madelineproto-xyz-api_docs-types-messages-messages-htm)
* [`getMessageStats(array|int|string $channel, bool $dark = false, int $msg_id = 0): array{_: \"stats.messageStats", views_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: \string}} @see https://docs.madelineproto.xyz/API_docs/types/stats.MessageStats.ht}}`](#getmessagestats-array-int-string-channel-bool-dark-false-int-msg_id-0-array-_-stats-messagestats-views_graph-array-_-statsgraphasync-token-string-array-_-statsgrapherror-error-string-array-_-statsgraph-json-mixed-zoom_token-string-see-https-docs-madelineproto-xyz-api_docs-types-stats-messagestats-ht)

## Methods:
### `getBroadcastStats(array|int|string $channel, bool $dark = false): array{_: \"stats.broadcastStats", period: array{_: \"statsDateRangeDays", min_date: int, max_date: int}, followers: array{_: \"statsAbsValueAndPrev", current: float, previous: float}, views_per_post: array{_: \"statsAbsValueAndPrev", current: float, previous: float}, shares_per_post: array{_: \"statsAbsValueAndPrev", current: float, previous: float}, enabled_notifications: array{_: \"statsPercentValue", part: float, total: float}, growth_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, followers_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, mute_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, top_hours_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, interactions_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, iv_interactions_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, views_by_source_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, new_followers_by_source_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, languages_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, recent_message_interactions: \list<array{_: "messageInteractionCounters", msg_id: int, views: int, forwards: int}>} @see https://docs.madelineproto.xyz/API_docs/types/stats.BroadcastStats.htm}`

Get [channel statistics](https://core.telegram.org/api/stats)


Parameters:

* `$channel`: `array|int|string` The channel @see https://docs.madelineproto.xyz/API_docs/types/InputChannel.html  
* `$dark`: `bool` Whether to enable dark theme for graph colors  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/stats.BroadcastStats.html


### `loadAsyncGraph(string $token = '', int $x = 0): array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: \string} @see https://docs.madelineproto.xyz/API_docs/types/StatsGraph.htm}`

Load [channel statistics graph](https://core.telegram.org/api/stats) asynchronously


Parameters:

* `$token`: `string` Graph token from [statsGraphAsync](https://docs.madelineproto.xyz/API_docs/constructors/statsGraphAsync.html) constructor  
* `$x`: `int` Zoom value, if required  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/StatsGraph.html


### `getMegagroupStats(array|int|string $channel, bool $dark = false): array{_: \"stats.megagroupStats", period: array{_: \"statsDateRangeDays", min_date: int, max_date: int}, members: array{_: \"statsAbsValueAndPrev", current: float, previous: float}, messages: array{_: \"statsAbsValueAndPrev", current: float, previous: float}, viewers: array{_: \"statsAbsValueAndPrev", current: float, previous: float}, posters: array{_: \"statsAbsValueAndPrev", current: float, previous: float}, growth_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, members_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, new_members_by_source_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, languages_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, messages_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, actions_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, top_hours_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, weekdays_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: string}, top_posters: list<array{_: \"statsGroupTopPoster", user_id: int, messages: int, avg_chars: int}>, top_admins: list<array{_: \"statsGroupTopAdmin", user_id: int, deleted: int, kicked: int, banned: int}>, top_inviters: list<array{_: \"statsGroupTopInviter", user_id: int, invitations: int}>, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/stats.MegagroupStats.htm}`

Get [supergroup statistics](https://core.telegram.org/api/stats)


Parameters:

* `$channel`: `array|int|string` [Supergroup ID](https://core.telegram.org/api/channel) @see https://docs.madelineproto.xyz/API_docs/types/InputChannel.html  
* `$dark`: `bool` Whether to enable dark theme for graph colors  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/stats.MegagroupStats.html


### `getMessagePublicForwards(array|int|string $channel, array|int|string $offset_peer, int $msg_id = 0, int $offset_rate = 0, int $offset_id = 0, int $limit = 0): array{_: \"messages.messages", messages: list<array>, chats: list<array>, users: list<array>}|array{_: \"messages.messagesSlice", inexact: array, count: array, next_rate: array, offset_id_offset: array, messages: list<array>, chats: list<array>, users: list<array>}|array{_: \"messages.channelMessages", inexact: array, pts: array, count: array, offset_id_offset: array, messages: list<array>, topics: list<array>, chats: list<array>, users: list<array>}|array{_: \"messages.messagesNotModified", count: \array} @see https://docs.madelineproto.xyz/API_docs/types/messages.Messages.htm}`

Obtains a list of messages, indicating to which other public channels was a channel message forwarded.
Will return a list of [messages](https://docs.madelineproto.xyz/API_docs/constructors/message.html) with `peer_id` equal to the public channel to which this message was forwarded.

Parameters:

* `$channel`: `array|int|string` Source channel @see https://docs.madelineproto.xyz/API_docs/types/InputChannel.html  
* `$offset_peer`: `array|int|string` [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) @see https://docs.madelineproto.xyz/API_docs/types/InputPeer.html  
* `$msg_id`: `int` Source message ID  
* `$offset_rate`: `int` Initially 0, then set to the `next_rate` parameter of [messages.messagesSlice](https://docs.madelineproto.xyz/API_docs/constructors/messages.messagesSlice.html)  
* `$offset_id`: `int` [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets)  
* `$limit`: `int` Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets)  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/messages.Messages.html


### `getMessageStats(array|int|string $channel, bool $dark = false, int $msg_id = 0): array{_: \"stats.messageStats", views_graph: array{_: \"statsGraphAsync", token: string}|array{_: \"statsGraphError", error: string}|array{_: \"statsGraph", json: mixed, zoom_token: \string}} @see https://docs.madelineproto.xyz/API_docs/types/stats.MessageStats.ht}}`

Get [message statistics](https://core.telegram.org/api/stats)


Parameters:

* `$channel`: `array|int|string` Channel ID @see https://docs.madelineproto.xyz/API_docs/types/InputChannel.html  
* `$dark`: `bool` Whether to enable dark theme for graph colors  
* `$msg_id`: `int` Message ID  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/stats.MessageStats.html


---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
