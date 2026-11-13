# payments.starGiftAuctionAcquiredGifts

> payments.starGiftAuctionAcquiredGifts attributes, type and example

[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|gifts|Array of [StarGiftAuctionAcquiredGift](/API_docs/types/StarGiftAuctionAcquiredGift.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|



### Type: [payments.StarGiftAuctionAcquiredGifts](/API_docs/types/payments.StarGiftAuctionAcquiredGifts.html)


### Example:

```
$payments_starGiftAuctionAcquiredGifts = ['_' => 'payments.starGiftAuctionAcquiredGifts', 'gifts' => [StarGiftAuctionAcquiredGift, StarGiftAuctionAcquiredGift], 'users' => [User, User], 'chats' => [Chat, Chat]];
```
