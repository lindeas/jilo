# Log regexps

This is a reference of the log lines and the corresponding regexps that are used in Jilo for events tracking.

Work in progress: 2024.06.16

----

## JVB

### conference start
needed: *timestamp, loglevel, conferenceID, conferenceName, conferenceDomain*

log

```JVB 2024-04-01 04:08:55.124 INFO: [19046] [confId=4c14584fce9a5970 conf_name=someroom123@conference.meet.example.com meeting_id=177c43a3] EndpointConnectionStatusMonitor.start#58: Starting connection status monitor```

regex

```JVB\ ([0-9-]+\ [0-9:.]+)\ ([A-Z]+):.*\[confId=([a-zA-Z]+)\ conf_name=(.*)@([a-zA-Z0-9-_.]+)\ meeting_id=.*\]\ EndpointConnectionStatusMonitor\.start.*:\ Starting\ connection\ status\ monitor```

### conference end
needed: *timestamp, loglevel, conferenceID* (optionally in case we don't have the starting event: *conferenceName, conferenceDomain*)

log

```JVB 2024-04-01 03:04:24.339 INFO: [18981] [confId=4c14584fce9a5970 conf_name=someroom123@conference.meet.example.com meeting_id=177c43a3] EndpointConnectionStatusMonitor.stop#66: Stopped```

## participant joining
needed: *timestamp, loglevel, conferenceID, endpointID, statsID*

regex

```JVB ([0-9-]+\ [0-9:.]+)\ [A-Z]+:.*\[confId=${conference_id}\ .*epId=([a-zA-Z0-9-]+)\ stats_id=([a-zA-Z0-9-]+)\ .*Starting\ the\ Agent\ without\ remote\ candidates```

### pair selection
needed: *timestamp, loglevel, conferenceID, endpointID, statsID, participant IP address*

regex

```JVB ([0-9-]+\ [0-9:.]+)\ [A-Z]+:.*\[confId=${conference_id}\ .*epId=${participant_endpoint_id}\ stats_id=${participant_stats_id}\ .*Selected\ pair\ for\ stream\ .*([0-9.]+):10000/udp/srflx\ \-\>\ ([0-9.]+):[0-9]+/udp/prflx```

### participant leaving
needed: *timestamp, loglevel, conferenceID, endpointID, statsID*

regex

```JVB ([0-9-]+\ [0-9:.]+)\ [A-Z]+:.*\[confId=${conference_id}\ .*epId=${participant_endpoint_id}\ stats_id=${participant_stats_id}\]\ Endpoint\.expire.*:\ Expired\.```

----

## JICOFO

### jicofo starting
needed: *timestamp, loglevel* (it's good to find a way to diferentiate the jicofo by some id (IP, hostname, etc.)

regex:

```Jicofo\ ([0-9-]+\ [0-9:.]+)\ ([A-Z]+):.*Main\.main.*:\ Starting\ Jicofo\.```

### jicofo registered to xmpp
needed: *timestamp, loglevel*

regex

```Jicofo\ ([0-9-]+\ [0-9:.]+)\ ([A-Z]+):.*\[xmpp_connection=client\]\ XmppProvider\$connectionListener\$1\.authenticated.*:\ Registered\.```

### jicofo started
needed: *timestamp, loglevel*

regex

```Jicofo\ ([0-9-]+\ [0-9:.]+)\ ([A-Z]+):.*\JicofoServices\.\<init\>.*\ Registering\ GlobalMetrics\ periodic\ updates\.```

### conference start
needed: *timestamp, loglevel, conferenceName,* (**FIXME**: we don't have *conferenceID* here, it's good to have it)

regex

```Jicofo ([0-9-]+\ [0-9:.]+)\ [A-Z]+:.*\[room=([^ ]+)@.*\]\ JitsiMeetConferenceImpl\.joinTheRoom```

### participant joining
needed: *timestamp, loglevel, conferenceID, conferenceName, participantID, statsID*

regex

```Jicofo ([0-9-]+\ [0-9:.]+)\ [A-Z]+:.*\[room=([^ ]+)@.*\ meeting_id=([a-zA-Z0-9-]+)\]\ .*\.onMemberJoined.*:\ Member\ joined:([a-zA-Z0-9]+)\ stats-id=([a-zA-Z0-9-]+)```

### bridge selection
needed: *timestamp, loglevel, bridgeID*

regex

```Jicofo ([0-9-]+\ [0-9:.]+)\ [A-Z]+:.*BridgeSelectionStrategy.select#.*:\ Selected.*\[jid=[a-z]@.*\/(.*),\ ```

### participant leaving
needed: *timestamp, loglevel, conferenceID, participantID*

regex

```Jicofo ([0-9-]+\ [0-9:.]+)\ [A-Z]+:.*\[room=${conference_name}@.*\ meeting_id=${conference_id}\]\ .*\.removeParticipant#.*:\ Removing\ ([a-zA-Z0-9]+)```

### conference end
needed: *timestamp, loglevel, conferenceID*

regex

```Jicofo ([0-9-]+\ [0-9:.]+)\ [A-Z]+:.*\[room=([^ ]+)@.*\ meeting_id=([a-zA-Z0-9-]+)\]\ JitsiMeetConferenceImpl\.stop```
