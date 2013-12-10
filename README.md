riemann-ocsp
============

## a simple gateway from nagios to riemann

riemann-ocsp hooks in nagios's ["Obsessive Compulsive Service Processor" facility](http://nagios.sourceforge.net/docs/3_0/configmain.html#ocsp_command), transforms nagios *service* events into riemann events, and submits them to a riemann instance.


Example usage:

```
$ grep submit_ocsp /etc/nagios/nagios.cfg
ocsp_command=/usr/local/bin/submit_ocsp
```

```
$ cat /usr/local/bin/submit_ocsp
#!/bin/sh

printf "%b" "$1\t$2\t$3\t$4\n" | send_nsca -H nagios.example.com -c /etc/nagios/send_nsca.cfg

TTL=600
riemann_ocsp "$1" "$2" "$3" "$4" "$TTL" "riemann.example.com:5555"
```

```
$ irb -rriemann/client
>> r = Riemann::Client.new(:host => "riemann.example.com")
>> r['tagged = "nagios"'].first
=> <Riemann::Event time: 1386088432, state: "ok", service: "Load Average", host: "node.example.com", description: "OK - load average: 0.00, 0.01, 0.00", tags: ["nagios"], ttl: 600.0>
```


## golang

riemann-ocsp is written in golang because legacy linux distros come with very old versions of the protobuf lib, which makes installing riemann's python/ruby/perl/etc client library a nuisance. Using a compiled binary shifts the annoyance onto the person having to install golang on the legacy distro to build the tool, but then makes distribution a breeze.

riemann-ocsp is barely more than a copy-paste of [raidman's (riemann lib for golang) example](https://github.com/amir/raidman).

