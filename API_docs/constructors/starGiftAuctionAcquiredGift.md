# starGiftAuctionAcquiredGift

> starGiftAuctionAcquiredGift attributes, type and example

[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|name\_hidden|[Bool](/API_docs/types/Bool.html) | Optional|
|peer|[long](/API_docs/types/long.html) | Yes|
|date|[int](/API_docs/types/int.html) | Yes|
|bid\_amount|[long](/API_docs/types/long.html) | Yes|
|round|[int](/API_docs/types/int.html) | Yes|
|pos|[int](/API_docs/types/int.html) | Yes|
|message|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Optional|
|gift\_num|[int](/API_docs/types/int.html) | Optional|



### Type: [StarGiftAuctionAcquiredGift](/API_docs/types/StarGiftAuctionAcquiredGift.html)


### Example:

```
$starGiftAuctionAcquiredGift = ['_' => 'starGiftAuctionAcquiredGift', 'name_hidden' => Bool, 'peer' => long, 'date' => int, 'bid_amount' => long, 'round' => int, 'pos' => int, 'message' => TextWithEntities, 'gift_num' => int];
```
