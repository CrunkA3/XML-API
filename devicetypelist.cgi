#!/bin/tclsh

#*******************************************************************************
# devicetypelist.cgi
# Erstellt die XML-Liste der verf�gbaren HomeMatic- Ger�tetypen.
#
# Pr�fix : DeviceTypeList
# Zugriff: g�ltige Session Id, unbeschr�nkt
#
# Autor      : Falk Werner
# Erstellt am: 02.05.2008
#*******************************************************************************

################################################################################
# Ressourcen                                                                   #
################################################################################

source once.tcl
 
sourceOnce cgi.tcl
#sourceOnce sessionid.tcl
sourceOnce DEVDB.tcl
sourceOnce xml.tcl

################################################################################
# Prozeduren und Funktionen                                                    #
################################################################################

#*******************************************************************************
# DeviceTypeList_getFormName { name }
# Entfernt die Hochkommas am Anfang und am Ende der Namen von Zeichenobjekten.
#
# Parameter:
#   name: Name des Zeichenobjekts mit f�hrendem und abschlie�endem Hochkomma.
#*******************************************************************************
proc DeviceTypeList_getFormName { name } {
  regexp {'(.*)'} $name dummy result
  return $result
}

#*******************************************************************************
# DeviceTypeList_putCircle { form }
# Gibt die XML-Beschreibung eines Zeichenobjekts vom Typ Kreis aus.
#*******************************************************************************
proc DeviceTypeList_putCircle { form } {
  set name   [lindex $form 0]
  set x      [lindex $form 2]
  set y      [lindex $form 3]
  set radius [lindex $form 4]
  
  puts -nonewline "<form type='circle'"
  puts -nonewline " name='[xml_escape $name]'"
  puts -nonewline " x='[xml_escape $x]</x>'"
  puts -nonewline " y='[xml_escape $y]</y>'"
  puts -nonewline " radius='[xml_escape $radius]'"
  puts -nonewline "/>"
  
}

#*******************************************************************************
# DeviceTypeList_putRectangle { form }
# Gibt die XML-Beschreibung eines Zeichenobjekts vom Typ Rechteck aus.
#*******************************************************************************
proc DeviceTypeList_putRectangle { form } {
  set name   [lindex $form 0]
  set x      [lindex $form 2]
  set y      [lindex $form 3]
  set width  [lindex $form 4]
  set height [lindex $form 5]
  
  puts -nonewline "<form type='rectangle'"
  puts -nonewline " name='[xml_escape $name]'"
  puts -nonewline " x='[xml_escape $x]'"
  puts -nonewline " y='[xml_escape $y]'"
  puts -nonewline " width='[xml_escape $width]'"
  puts -nonewline " height='[xml_escape $height]'"
  puts -nonewline "/>"
}

#*******************************************************************************
# DeviceTypeList_putText { form }
# Gibt die XML-Beschreibung eines Zeichenobjekts vom Typ Text aus.
#*******************************************************************************
proc DeviceTypeList_putText { form } {
  set name       [lindex $form 0]
  set x          [lindex $form 2]
  set y          [lindex $form 3]
  set value      [lindex $form 4]
  set size       [lindex $form 5]  
  set fontFamily [lindex $form 6]  
  set fontStyle  [lindex $form 7]  

  puts -nonewline "<form type='text'"
  puts -nonewline " name='[xml_escape $name]'"
  puts -nonewline " x='[xml_escape $x]'"
  puts -nonewline " y='[xml_escape $y]'"
  puts -nonewline " value=[xml_escape $value]"
  puts -nonewline " size='[xml_escape $size]'"
  puts -nonewline " fontFamily=[xml_escape $fontFamily]"
  puts -nonewline " fontStyle='[xml_escape $fontStyle]'"
  puts -nonewline "/>"
}

#*******************************************************************************
# DeviceTypeList_putEllipse { form }
# Gibt die XML-Beschreibung eines Zeichenobjekts vom Typ Ellipse aus.
#*******************************************************************************
proc DeviceTypeList_putEllipse { form } {
  set name   [lindex $form 0]
  set x      [lindex $form 2]
  set y      [lindex $form 3]
  set width  [lindex $form 4]
  set height [lindex $form 5]
  
  puts -nonewline "<form type='ellipse'"
  puts -nonewline " name='[xml_escape $name]'"
  puts -nonewline " x='[xml_escape $x]'"
  puts -nonewline " y='[xml_escape $y]'"
  puts -nonewline " width='[xml_escape $width]'"
  puts -nonewline " height='[xml_escape $height]'"
  puts -nonewline "/>"
}

#*******************************************************************************
# DeviceTypeList_putFormset { form }
# Gibt die XML-Beschreibung eines Zeichenobjekts vom Typ Formset aus.
#*******************************************************************************
proc DeviceTypeList_putFormset { form } {
  set name     [lindex $form 0]
  set formName [DeviceTypeList_getFormName [lindex $form 2]]
  puts -nonewline "<form type='formset'"
  puts -nonewline " name='[xml_escape $name]'"
  puts -nonewline " formList=\"[xml_escape $formName]"
  for { set i 3 } { $i < [llength $form] } { incr i } {
    set formName [DeviceTypeList_getFormName [lindex $form $i]]
    puts -nonewline ",[xml_escape $formName]"
  }
  puts -nonewline "\" />"
}

#*******************************************************************************
# DeviceTypeList_putLine { form }
# Gibt die XML-Beschreibung eines Zeichenobjekts vom  Typ Linie aus.
#*******************************************************************************
proc DeviceTypeList_putLine { form } {
  set name     [lindex $form 0]
  set x1       [lindex $form 2]
  set y1       [lindex $form 3]  
  set x2       [lindex $form 4]
  set y2       [lindex $form 5]  
  set stroke   [lindex $form 6]  
  
  puts -nonewline "<form type='line'"
  puts -nonewline " name='[xml_escape $name]'"
  puts -nonewline " x1='[xml_escape $x1]'"
  puts -nonewline " y1='[xml_escape $y1]'"
  puts -nonewline " x2='[xml_escape $x2]'"
  puts -nonewline " y2='[xml_escape $y2]'"
  puts -nonewline " stroke='[xml_escape $stroke]'"
  puts -nonewline "/>"
}

#*******************************************************************************
# DeviceTypeList_putOffset { form }
# Gibt die XML-Beschreibung eines Zeichenobjekts vom Typ Offset aus.
#*******************************************************************************
proc DeviceTypeList_putOffset { form } {
  set name     [lindex $form 0]
  set formName [DeviceTypeList_getFormName [lindex $form 2]]
  set x        [lindex $form 3]
  set y        [lindex $form 4]
  
  puts -nonewline "<form type='offset'"
  puts -nonewline " name='[xml_escape $name]'"
  puts -nonewline " formName=\"[xml_escape $formName]\""
  puts -nonewline " x='[xml_escape $x]'"
  puts -nonewline " y='[xml_escape $y]'"
  puts -nonewline "/>"
}

#*******************************************************************************
# DeviceTypeList_putXML { }
# Gibt die Liste der verf�gbaren HomeMatic Ger�te als XML-Datei aus.
#*******************************************************************************
proc DeviceTypeList_putXML { } {
  global DEV_LIST DEV_DESCRIPTION DEV_HIGHLIGHT
  
  puts -nonewline "<?xml version='1.0' ?>"
  puts -nonewline "<deviceTypeList>"
  foreach device $DEV_LIST {
    puts -nonewline "<deviceType "
    puts -nonewline " name='[xml_escape $device]'"
    puts -nonewline " description='[xml_escape $DEV_DESCRIPTION($device)]'"
    puts -nonewline " thumbnailPath='[xml_escape [DEV_getImagePath $device 50]]'"
    puts -nonewline " imagePath='[xml_escape [DEV_getImagePath $device 250]]'"
    puts -nonewline ">"
    
    foreach form $DEV_HIGHLIGHT($device) {
      set type [lindex $form 1]
      switch -exact $type {
        1 { DeviceTypeList_putCircle    $form }
        2 { DeviceTypeList_putRectangle $form }
        3 { DeviceTypeList_putText      $form }
        4 { DeviceTypeList_putEllipse   $form }
        5 { DeviceTypeList_putFormset   $form }
        6 { DeviceTypeList_putLine      $form }
        7 { DeviceTypeList_putOffset    $form }      
      }
   }
    
    puts -nonewline "</deviceType>"
  }
  puts -nonewline "</deviceTypeList>"
}

#*******************************************************************************
# DeviceTypeList_putEmptyXML
# Gibt eine Leere Liste von HomeMatic Ger�tetypen als XML-Datei aus.
#
# Diese Liste wird ausgegeben, wenn die Session Id ung�ltig ist.
#*******************************************************************************
proc DeviceTypeList_putEmptyXML { } {
  puts -nonewline "<?xml version='1.0' ?>"
  puts -nonewline "<deviceTypeList>"
  puts -nonewline "</deviceTypeList>"
}

################################################################################
# Einsprungpunkt                                                               #
################################################################################

cgi_eval {

  cgi_input
  cgi_content_type "text/xml"
  cgi_http_head
#  if { 0 < [SessionId_isValid $SessionId_UPL(GUEST)] } then {
#    DeviceTypeList_putXML
#  } else {
#    DeviceTypeList_putEmptyXML
#  }

# ohne Pr�fen der SessionId
  DeviceTypeList_putXML
  
}
