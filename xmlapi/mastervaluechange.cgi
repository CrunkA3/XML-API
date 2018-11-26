#!/bin/tclsh
load tclrega.so
load tclrpc.so
source common.tcl

puts -nonewline {Content-Type: text/xml
Access-Control-Allow-Origin: *

<?xml version="1.0" encoding="ISO-8859-1" ?><mastervalue>}

set device_id ""
set name ""
set value ""

catch {
    set input $env(QUERY_STRING)
    set pairs [split $input &]
    foreach pair $pairs {
        if {0 != [regexp "^(\[^=]*)=(.*)$" $pair dummy varname val]} {
            set $varname $val
        }
    }
}

read_interfaces

set rec_devids [split $device_id "\,"]
set rec_mvaluename [split $name "\,"]
set rec_mvaluevalue [split $value "\,"]

for {set counter 0} {$counter<[llength $rec_devids]} {incr counter} {
    set devid [lindex $rec_devids $counter]

    set item [lindex $rec_mvaluename $counter]
    set val [lindex $rec_mvaluevalue $counter]
    set cmd "{$item {string $val}}"

    array set values [rega_script {
        integer iseId = "} $devid {";
        var oDevice = dom.GetObject(iseId);
        var address = oDevice.Address();
        var deviceType = oDevice.HssType();
        Write("<device");
        Write(" name='");
        WriteXML(oDevice.Name());
        Write("'");
        Write(" ise_id='" # iseId # "'");
        Write(" device_type='");
        WriteXML(deviceType);                                        
        Write("'");                                                  
        Write(" >");                                                 
    }]                                                               
    set deviceAddress $values(address)                               
    set deviceType $values(deviceType)        
                                              
    puts -nonewline $values(STDOUT)           

    if {[string compare -nocase -length 9 "HM-CC-VG-" $deviceType] == 0} {
        set ausgabe [xmlrpc $interfaces(VirtualDevices) putParamset [list string $deviceAddress] [list string "MASTER"] [list struct $cmd]]
    } elseif {[string compare -nocase -length 5 "HMIP-" $deviceType] == 0} {
        set ausgabe [xmlrpc $interfaces(HmIP-RF) putParamset [list string $deviceAddress] [list string "MASTER"] [list struct $cmd]]
    } else {
        set ausgabe [xmlrpc $interfaces(BidCos-RF) putParamset [list string $deviceAddress] [list string "MASTER"] [list struct $cmd]]
    }                                                                                                                                       
    puts -nonewline {<mastervalue name='}                                                                                                   
    puts -nonewline $item                                                                                                                   
    puts -nonewline {' value='}                                                                                                             
    puts -nonewline $val                                                                                                                    
    puts -nonewline {'/>}                                                                                                                   
    puts -nonewline {</device>}                                                                                                             
}                                                                                                                                           
puts -nonewline {</mastervalue>}
