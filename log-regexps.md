# Log regexps

This is a reference of the log lines and the corresponding regexps that are used in Jilo for events tracking.

Work in progress: 2024.06.24

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

regex

```Jicofo\ ([0-9-]+\ [0-9:.]+)\ ([A-Z]+):.*Main\.main.*:\ Starting\ Jicofo\.```

### jicofo registered to xmpp
needed: *timestamp, loglevel*

regex

```Jicofo\ ([0-9-]+\ [0-9:.]+)\ ([A-Z]+):.*\[xmpp_connection=client\]\ XmppProvider\$connectionListener\$1\.authenticated.*:\ Registered\.```

### jicofo started
needed: *timestamp, loglevel*

regex

```Jicofo\ ([0-9-]+\ [0-9:.]+)\ ([A-Z]+):.*\JicofoServices\.\<init\>.*\ Registering\ GlobalMetrics\ periodic\ updates\.```

### jvb added
needed: *timestamp, loglevel, jvbID, jvb version, jvb region*

log

```Jicofo 2024-06-18 18:38:07.378 INFO: [33] BridgeSelector.addJvbAddress#96: Added new videobridge: Bridge[jid=jvbbrewery@internal.auth.meet.example.com/87531df0-4018-420a-bfb3-cb2f8d48ba08, version=2.3.105-ge155b81e, relayId=null, region=null, stress=0.00]```

regex

```Jicofo\ ([0-9-]+\ [0-9:.]+)\ ([A-Z]+):.*\BridgeSelector\.addJvbAddress.*:\ Added\ new\ videobridge:\ Bridge\[jid=.*@.*\/(.*),\ version=(.*),.*region=(.*),```

### jvb removed
needed: *timestamp, loglevel, jvbID*

log

```Jicofo 2024-06-22 12:20:38.713 INFO: [1401] BridgeSelector.removeJvbAddress#109: Removing JVB: jvbbrewery@internal.auth.meet.example.com/87531df0-4018-420a-bfb3-cb2f8d48ba08```

regex

```Jicofo\ ([0-9-]+\ [0-9:.]+)\ ([A-Z]+):.*\BridgeSelector\.removeJvbAddress.*:\ Removing\ JVB:\ .*@.*\/(.*)```

### jvb lost (just in case the removal was not detected)
needed: *timestamp, loglevel, jvbID*

log

```Jicofo 2024-06-22 12:20:38.713 WARNING: [1401] BridgeSelector.removeJvbAddress#112: Lost a bridge: jvbbrewery@internal.auth.meet.example.com/87531df0-4018-420a-bfb3-cb2f8d48ba08```

regex

```Jicofo\ ([0-9-]+\ [0-9:.]+)\ ([A-Z]+):.*\BridgeSelector\.removeJvbAddress.*:\ Lost\ a\ bridge:\ .*@.*\/(.*)```

### jvb health-check scheduled
needed: *timestamp, loglevel, jvbID, jvb version, jvb region*

log

```Jicofo 2024-06-22 12:22:03.707 INFO: [40] JvbDoctor.bridgeAdded#128: Scheduled health-check task for: Bridge[jid=jvbbrewery@internal.auth.meet.example.com/87531df0-4018-420a-bfb3-cb2f8d48ba08, version=2.3.105-ge155b81e, relayId=null, region=null, stress=0.00]```

regex

```Jicofo\ ([0-9-]+\ [0-9:.]+)\ ([A-Z]+):.*\JvbDoctor\.bridgeAdded.*:\ Scheduled\ health-check\ task\ for:\ Bridge\[jid=.*@.*\/(.*),\ version=(.*),\ .*\ region=(.*),```

### jvb health-check stopped
needed: *timestamp, loglevel, jvbID, jvb version, jvb region*

log

```Jicofo 2024-06-22 12:20:38.733 INFO: [40] JvbDoctor.bridgeRemoved#105: Stopping health-check task for: Bridge[jid=jvbbrewery@internal.auth.meet.example.com/87531df0-4018-420a-bfb3-cb2f8d48ba08, version=2.3.105-ge155b81e, relayId=null, region=null, stress=0.00]```

regex

```Jicofo\ ([0-9-]+\ [0-9:.]+)\ ([A-Z]+):.*\JvbDoctor\.bridgeRemoved.*:\ Stopping\ health-check\ task\ for:\ Bridge\[jid=.*@.*\/(.*),\ version=(.*),\ .*\ region=(.*),```

### Warning: no operational bridges
needed: *timestamp, loglevel*

log

```Jicofo 2024-06-25 10:44:18.727 WARNING: [2505] BridgeSelector.selectBridge#182: There are no operational bridges.```

regex

```Jicofo\ ([0-9-]+\ [0-9:.]+)\ ([A-Z]+):.*BridgeSelector\.selectBridge.*\ There\ are\ no\ operational\ bridges\.```

### Severe: no bridge available
needed: *timestamp, loglevel, conferenceID*

log

```Jicofo 2024-06-25 10:44:18.727 SEVERE: [2505] [room=fewfewf-wfwegf@conference.meet.example.com meeting_id=750c7bcc-d9fb-4b8b-a085-dcf6b5c99546 participant=49e3837d] ParticipantInviteRunnable.doRun#218: Can not invite participant, no bridge available.```

regex

```Jicofo\ ([0-9-]+\ [0-9:.]+)\ ([A-Z]+):.*\[room=([^ ]+)@.*\ meeting_id=([a-zA-Z0-9-]+).*:\ Can\ not\ invite\ participant,\ no\ bridge\ available\.```

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
