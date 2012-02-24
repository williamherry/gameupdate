#!/usr/bin/env python
# -*- coding: utf-8 -*-

dns_dx = '8.8.8.8'
dns_lt = '202.106.196.115'
location_file = 'location_data.txt'
dns_retry = 5
dns_timeout = 15
MAX_THREAD = 200

data_head = '\n;--------%s F--------\n\n'
data_body = {
'ping': """
Method      = %(method)s
;--- Common properties --
;DestFolder = Root\趣游监控系统\%(name)s\\%(platform)s\%(location_short)s
Title       = %(platform)s-%(name)s%(server)s-%(server)sF-%(ip)s-%(location)s
Comment     =
RelatedURL  = 
CmntPattern = %%path%%
ScheduleMode= Regular
Schedule    = 
Interval    = 30
Alerts      = %(alerts)s
ReverseAlert= No
UnknownIsBad= Yes
WarningIsBad= Yes
UseCommonLog= Yes
PrivLogMode = Default
CommLogMode = Default
;--- Test specific properties ---
Host        = %(ip)s
Timeout     = 2000
Retries     = 4
MaxLostRatio= 100
DisplayMode = time
DontFragment= No
""",

'tcp': """
Method      = Tcp
;--- Common properties ---
;DestFolder = Root\趣游监控系统\%(name)s\\%(platform)s\%(location_short)s
Title       = %(platform)s-%(name)s%(server)s-%(server)sF-%(ip)s-%(location)s
Comment     = port: %(port)s
RelatedURL  = "
CmntPattern = port: %%TargetPort%%
ScheduleMode= Regular
Schedule    = 
Interval    = 30
Alerts      = %(alerts)s
ReverseAlert= No
UnknownIsBad= Yes
WarningIsBad= Yes
UseCommonLog= Yes
PrivLogMode = Default
CommLogMode = Default
;--- Test specific properties ---
Host    = %(ip)s
Port    = %(port)s
""",

'url': """
Method      = Url
;--- Common properties ---
;DestFolder = Root\趣游监控系统\%(name)s\\%(platform)s\%(location_short)s
Title       = %(platform)s-%(name)s%(server)s-%(server)sF-%(ip)s-%(location)s
Comment     = http://%(ip)s/crossdomain.xml
RelatedURL  = 
CmntPattern = %%path%%
ScheduleMode= Regular
Schedule    = 
Interval    = 30
Alerts      = %(alerts)s
ReverseAlert= No
UnknownIsBad= Yes
WarningIsBad= Yes
UseCommonLog= Yes
PrivLogMode = Default
CommLogMode = Default
;--- Test specific properties ---
URL         = http://%(ip)s/crossdomain.xml
UrlUseMacros= No
is302ok     = Yes
IgnoreUnknCA= No
UseFrames   = No
UseImages   = No
""",

}

