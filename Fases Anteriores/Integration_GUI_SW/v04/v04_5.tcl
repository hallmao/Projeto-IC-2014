#############################################################################
# Generated by PAGE version 4.3
# in conjunction with Tcl version 8.6
#    Jul 10, 2014 11:23:40 AM




#############################################################################
## vTcl Code to Load Stock Images


if {![info exist vTcl(sourcing)]} {
#############################################################################
## Procedure:  vTcl:rename

proc ::vTcl:rename {name} {
    ## This procedure may be used free of restrictions.
    ##    Exception added by Christian Gavin on 08/08/02.
    ## Other packages and widget toolkits have different licensing requirements.
    ##    Please read their license agreements for details.

    regsub -all "\\." $name "_" ret
    regsub -all "\\-" $ret "_" ret
    regsub -all " " $ret "_" ret
    regsub -all "/" $ret "__" ret
    regsub -all "::" $ret "__" ret

    return [string tolower $ret]
}

#############################################################################
## Procedure:  vTcl:image:create_new_image

proc ::vTcl:image:create_new_image {filename {description {no description}} {type {}} {data {}}} {
    ## This procedure may be used free of restrictions.
    ##    Exception added by Christian Gavin on 08/08/02.
    ## Other packages and widget toolkits have different licensing requirements.
    ##    Please read their license agreements for details.
    # Does the image already exist?
    if {[info exists ::vTcl(images,files)]} {
        if {[lsearch -exact $::vTcl(images,files) $filename] > -1} { return }
    }
    if {![info exists ::vTcl(sourcing)] && [string length $data] > 0} {
        set object [image create  [vTcl:image:get_creation_type $filename]  -data $data]
    } else {
        # Wait a minute... Does the file actually exist?
        if {! [file exists $filename] } {
            # Try current directory
            set script [file dirname [info script]]
            set filename [file join $script [file tail $filename] ]
        }

        if {![file exists $filename]} {
            set description "file not found!"
            ## will add 'broken image' again when img is fixed, for
            ## now create empty
            set object [image create photo -width 1 -height 1]
        } else {
            set object [image create  [vTcl:image:get_creation_type $filename]  -file $filename]
        }
    }

    set reference [vTcl:rename $filename]
    set ::vTcl(images,$reference,image)       $object
    set ::vTcl(images,$reference,description) $description
    set ::vTcl(images,$reference,type)        $type
    set ::vTcl(images,filename,$object)       $filename

    lappend ::vTcl(images,files) $filename
    lappend ::vTcl(images,$type) $object
    set ::vTcl(imagefile,$object) $filename   ;# Rozen
    # return image name in case caller might want it
    return $object
}

#############################################################################
## Procedure:  vTcl:image:get_image

proc ::vTcl:image:get_image {filename} {
    ## This procedure may be used free of restrictions.
    ##    Exception added by Christian Gavin on 08/08/02.
    ## Other packages and widget toolkits have different licensing requirements.
    ##    Please read their license agreements for details.

    set reference [vTcl:rename $filename]

    # Let's do some checking first
    if {![info exists ::vTcl(images,$reference,image)]} {
        # Well, the path may be wrong; in that case check
        # only the filename instead, without the path.

        set imageTail [file tail $filename]

        foreach oneFile $::vTcl(images,files) {
            if {[file tail $oneFile] == $imageTail} {
                set reference [vTcl:rename $oneFile]
                break
            }
        }
    }
    # Rozen. There follows a hack in case one wants to rerun a tcl
    # file which contains a file name where an image is expected.
    if {![info exists ::vTcl(images,$reference,image)]} {
        set ::vTcl(images,$reference,image)  [vTcl:image:create_new_image $filename]
    }
    return $::vTcl(images,$reference,image)
}

#############################################################################
## Procedure:  vTcl:image:get_creation_type

proc ::vTcl:image:get_creation_type {filename} {
    ## This procedure may be used free of restrictions.
    ##    Exception added by Christian Gavin on 08/08/02.
    ## Other packages and widget toolkits have different licensing requirements.
    ##    Please read their license agreements for details.

    switch [string tolower [file extension $filename]] {
        .ppm -
        .jpg -
        .bmp -
        .gif    {return photo}
        .xbm    {return bitmap}
        default {return photo}
    }
}

foreach img {


            } {
    eval set _file [lindex $img 0]
    vTcl:image:create_new_image\
        $_file [lindex $img 1] [lindex $img 2] [lindex $img 3]
}

}
#############################################################################
## vTcl Code to Load User Images

catch {package require Img}

foreach img {

        {{$[pwd]/images/Leibniz_order5.gif} {user image} user {}}
        {{$[pwd]/images/init_conditions.gif} {user image} user {}}

            } {
    eval set _file [lindex $img 0]
    vTcl:image:create_new_image\
        $_file [lindex $img 1] [lindex $img 2] [lindex $img 3]
}

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #d9d9d9
set vTcl(active_fg) #111111
#############################################################################
#############################################################################
# vTcl Code to Load User Fonts

vTcl:font:add_font \
    "-family Arial -size 18 -weight normal -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font10
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top36
    namespace eval ::widgets::$base {
        set set,origin 1
        set set,size 1
        set runvisible 1
    }
    set site_3_0 $base.m50
    set site_3_0 $base.m50
    set site_3_0 $base.m50
    set site_4_0 .top36.tNo36.pg0 
    set site_4_0 $site_4_0
    set site_4_1 .top36.tNo36.pg1 
    set site_4_0 $site_4_1
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# USER DEFINED PROCEDURES
#

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow. {base} {
    if {$base == ""} {
        set base .
    }
    ###################
    # CREATING WIDGETS
    ###################
    wm focusmodel $top passive
    wm geometry $top 1x1+5+27; update
    wm maxsize $top 1280 707
    wm minsize $top 72 15
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm withdraw $top
    wm title $top "page.tcl"
    bindtags $top "$top Page.tcl all"
    ###################
    # SETTING GEOMETRY
    ###################

    vTcl:FireEvent $base <<Ready>>
}

proc vTclWindow.top36 {base} {
    if {$base == ""} {
        set base .top36
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl:toplevel $top -class Toplevel \
        -menu "$top.m50" -background {} -highlightbackground {#d9d9d9} \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 800x600+142+81; update
    wm maxsize $top 800 724
    wm minsize $top 72 1
    wm overrideredirect $top 0
    wm resizable $top 0 0
    wm title $top "EDO Solver"
    vTcl:DefineAlias "$top" "EDO_main_window" vTcl:Toplevel:WidgetProc "" 1
    bindtags $top "$top Toplevel all _TopLevel"
    label $top.lab37 \
        -activebackground white -activeforeground black -anchor s \
        -background white -borderwidth 5 -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -image [vTcl:image:get_image [file join / Users Michael Desktop {Projeto IC 2014} Integration_GUI_SW v04 images Leibniz_order5.gif]] \
        -relief ridge -text {Diff Equation Here} -width 800 
    vTcl:DefineAlias "$top.lab37" "EDO_viewer" vTcl:WidgetProc "EDO_main_window" 1
    label $top.lab40 \
        -activebackground white -activeforeground black -anchor nw \
        -background white -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -image [vTcl:image:get_image [file join / Users Michael Desktop {Projeto IC 2014} Integration_GUI_SW v04 images init_conditions.gif]] \
        -relief ridge -text Init.Conditions 
    vTcl:DefineAlias "$top.lab40" "Label2" vTcl:WidgetProc "EDO_main_window" 1
    label $top.lab41 \
        -activebackground {#f9f9f9} -activeforeground black -anchor w \
        -background {#ffffff} -font font10 -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -relief ridge \
        -text {Input x(t) = } 
    vTcl:DefineAlias "$top.lab41" "Label3" vTcl:WidgetProc "EDO_main_window" 1
    menu $top.m50 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -font TkMenuFont -foreground {#000000} \
        -tearoff 0 
    $top.m50 add cascade \
        -menu "$top.m50.men52" -activebackground {#d9d9d9} \
        -activeforeground {#111111} -background {#d9d9d9} -font TkMenuFont \
        -foreground {#000000} -label Idioma 
    set site_3_0 $top.m50
    menu $site_3_0.men52 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font menu -foreground black -tearoff 0 
    $site_3_0.men52 add radiobutton \
        -value Espanhol -activebackground {#d9d9d9} \
        -activeforeground {#000000} -background {#d9d9d9} -command TODO \
        -font TkMenuFont -foreground {#000000} -label Espanhol 
    $site_3_0.men52 add radiobutton \
        -value Inglês -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command TODO -font TkMenuFont \
        -foreground {#000000} -label Inglês 
    $site_3_0.men52 add radiobutton \
        -value Português -activebackground {#d9d9d9} \
        -activeforeground {#000000} -background {#d9d9d9} -command TODO \
        -font TkMenuFont -foreground {#000000} -label Português 
    $top.m50 add cascade \
        -menu "$top.m50.men53" -activebackground {#d9d9d9} \
        -activeforeground {#111111} -background {#d9d9d9} -font TkMenuFont \
        -foreground {#000000} -label Notacao 
    set site_3_0 $top.m50
    menu $site_3_0.men53 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font menu -foreground black -tearoff 0 
    $site_3_0.men53 add radiobutton \
        -value Linha -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command TODO -font TkMenuFont \
        -foreground {#000000} -label Linha 
    $site_3_0.men53 add radiobutton \
        -value Leibniz -activebackground {#d9d9d9} \
        -activeforeground {#000000} -background {#d9d9d9} -command TODO \
        -font TkMenuFont -foreground {#000000} -label Leibniz 
    $site_3_0.men53 add radiobutton \
        -value Newton -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command TODO -font TkMenuFont \
        -foreground {#000000} -label Newton 
    $site_3_0.men53 add radiobutton \
        -value Heavside -activebackground {#d9d9d9} \
        -activeforeground {#000000} -background {#d9d9d9} -command TODO \
        -font TkMenuFont -foreground {#000000} -label Heavside 
    $top.m50 add cascade \
        -menu "$top.m50.men54" -activebackground {#d9d9d9} \
        -activeforeground {#111111} -background {#d9d9d9} -font TkMenuFont \
        -foreground {#000000} -label DigitosFracionarios 
    set site_3_0 $top.m50
    menu $site_3_0.men54 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font menu -foreground black -tearoff 0 
    $site_3_0.men54 add radiobutton \
        -value {2 digitos} -activebackground {#d9d9d9} \
        -activeforeground {#000000} -background {#d9d9d9} -command TODO \
        -font TkMenuFont -foreground {#000000} -label {2 digitos} 
    $site_3_0.men54 add radiobutton \
        -value {3 digitos} -activebackground {#d9d9d9} \
        -activeforeground {#000000} -background {#d9d9d9} -command TODO \
        -font TkMenuFont -foreground {#000000} -label {3 digitos} 
    $site_3_0.men54 add radiobutton \
        -value {4 digitos} -activebackground {#d9d9d9} \
        -activeforeground {#000000} -background {#d9d9d9} -command TODO \
        -font TkMenuFont -foreground {#000000} -label {4 digitos} 
    frame $top.fra37 \
        -borderwidth 3 -relief ridge -background white -height 65 \
        -highlightbackground {#d9d9d9} -highlightcolor black -width 805 
    vTcl:DefineAlias "$top.fra37" "plotOptions_frame" vTcl:WidgetProc "EDO_main_window" 1
    ttk::style configure TNotebook -background #d9d9d9
    ttk::style configure TNotebook.Tab -background #d9d9d9
    ttk::style configure TNotebook.Tab -foreground #000000
    ttk::style configure TNotebook.Tab -font TkDefaultFont
    ttk::style map TNotebook.Tab -background [list disabled #d9d9d9 selected #d9d9d9]
    ttk::notebook $top.tNo36 \
        -width 804 -height 370 -takefocus {} 
    vTcl:DefineAlias "$top.tNo36" "Abas" vTcl:WidgetProc "EDO_main_window" 1
    frame .top36.tNo36.pg0 -background #d9d9d9
    $top.tNo36 add .top36.tNo36.pg0 \
        -padding 0 -sticky nsew -state normal -text Relatorio -image {} \
        -compound none -underline -1 
    set site_4_0  $top.tNo36.pg0
    message $site_4_0.mes38 \
        -background white -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -width 747 
    vTcl:DefineAlias "$site_4_0.mes38" "Output_relatorio" vTcl:WidgetProc "EDO_main_window" 1
    place $site_4_0.mes38 \
        -in $site_4_0 -x 0 -y 0 -width 747 -height 314 -anchor nw \
        -bordermode ignore 
    frame .top36.tNo36.pg1 -background #d9d9d9
    $top.tNo36 add .top36.tNo36.pg1 \
        -padding 0 -sticky nsew -state normal -text Gráfico -image {} \
        -compound none -underline -1 
    set site_4_1  $top.tNo36.pg1
    frame $site_4_1.fra36 \
        -borderwidth 2 -relief groove -background White -height 315 \
        -highlightbackground {#d9d9d9} -highlightcolor black -width 755 
    vTcl:DefineAlias "$site_4_1.fra36" "output_plots" vTcl:WidgetProc "EDO_main_window" 1
    place $site_4_1.fra36 \
        -in $site_4_1 -x 0 -y 0 -width 755 -height 315 -anchor nw \
        -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab37 \
        -in $top -x 0 -y 0 -width 800 -height 100 -anchor nw \
        -bordermode ignore 
    place $top.lab40 \
        -in $top -x 0 -y 100 -width 310 -height 82 -anchor nw \
        -bordermode ignore 
    place $top.lab41 \
        -in $top -x 310 -y 100 -width 490 -height 82 -anchor nw \
        -bordermode ignore 
    place $top.fra37 \
        -in $top -x 0 -y 560 -width 805 -height 65 -anchor nw \
        -bordermode ignore 
    place $top.tNo36 \
        -in $top -x 0 -y 190 -width 804 -height 370 -anchor nw \
        -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

Window show .
Window show .top36

