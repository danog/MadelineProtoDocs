---
title: Working with updates in MTProto
description: Apart from the basic operations required to work with MTProto update sequences, implementations also have to take care to postpone updates received via the socket while filling gaps in the event and Update sequences, as well as avoid filling gaps in the same sequence.
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---

# Working with updates in MTProto

Apart from the basic operations [required to work with MTProto update sequences](https://core.telegram.org/api/updates), implementations also have to take care to postpone updates received via the socket while filling gaps in the event and Update sequences, as well as avoid filling gaps in the same sequence.

An interesting and easy way this can be implemented, instead of using various locks, is by running background threads, like in [MadelineProto](https://github.com/danog/MadelineProto/tree/v8/src/Loop/Update).

* A background _feeder_ thread for each [sequence](#event-sequences), associated to a FIFO queue is initialized and then paused ([event sequence FeedLoop](https://github.com/danog/MadelineProto/blob/2672728fe3b7ddbc03c59299e2483e6708919896/src/Loop/Update/FeedLoop.php), [common sequence SeqLoop](https://github.com/danog/MadelineProto/blob/2672728fe3b7ddbc03c59299e2483e6708919896/src/Loop/Update/SeqLoop.php)).
* Another set of _updater_ threads is started: one for the common [sequence](#event-sequences), one for each channel [sequence](#event-sequences) ([UpdateLoop](https://github.com/danog/MadelineProto/blob/2672728fe3b7ddbc03c59299e2483e6708919896/src/Loop/Update/UpdateLoop.php)).

When a getDifference is requested, a signal resumes the _updater_ thread, which starts fetching difference until the gap is filled, then it pauses itself again.

When a new Updates constructor or event is received, it is added to the FIFO queue of the correspondent _feeder_ thread, and a signal is sent to said thread.
The signal wakes up the thread, which starts parsing the queued events: as per [update handling](#update-handling), duplicates are eliminated, correct events are accepted and the [state](#fetching-state) is updated.
When a gap is encountered, the _updater_ thread is resumed: the _feeder_ thread waits until the _updater_ thread is paused again.
Finally, the manually fetched difference is prepended to the _feeder_ FIFO queue, to parse it before any additional update that was fetched from the socket while fetching the difference.

The simplicity of this approach is in its sequentiality: 

* Each thread can only execute one action at a time.
* Each event is fetched one by one from the FIFO queue
* Threads cannot start handling a new event received from the socket while fetching the difference, or while still handling the previous one
* Only one part of the application at a time can trigger a getDifference, to avoid re-fetching and re-saving the same difference twice.
