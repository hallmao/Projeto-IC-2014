#############################################################################
# Generated by PAGE version 4.3
# in conjunction with Tcl version 8.6
#    Jul 07, 2014 06:47:27 PM


set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #d9d9d9
set vTcl(active_fg) #111111
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
    set site_3_0 $base.m41
    set site_3_0 $base.m41
    set site_3_0 $base.m41
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
    wm maxsize $top 3200 1036
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
        -menu "$top.m41" -background {#d9d9d9} -highlightbackground {#d9d9d9} \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 800x600+1778+296; update
    wm maxsize $top 1280 703
    wm minsize $top 72 1
    wm overrideredirect $top 0
    wm resizable $top 0 0
    wm title $top "EDO_Solver"
    vTcl:DefineAlias "$top" "EDO_mainWindow" vTcl:Toplevel:WidgetProc "" 1
    bindtags $top "$top Toplevel all _TopLevel"
    menu $top.m41 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -font TkMenuFont -foreground {#000000} \
        -tearoff 0 
    $top.m41 add cascade \
        -menu "$top.m41.men42" -activebackground {#d9d9d9} \
        -activeforeground {#111111} -background {#d9d9d9} -font TkMenuFont \
        -foreground {#000000} -label Idiomas 
    set site_3_0 $top.m41
    menu $site_3_0.men42 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font menu -foreground black -tearoff 0 
    $site_3_0.men42 add radiobutton \
        -value EN -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command TODO -font TkMenuFont \
        -foreground {#000000} -label English 
    $site_3_0.men42 add radiobutton \
        -value ES -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command TODO -font TkMenuFont \
        -foreground {#000000} -label Español 
    $site_3_0.men42 add radiobutton \
        -value PT -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command TODO -font TkMenuFont \
        -foreground {#000000} -label Português 
    $top.m41 add cascade \
        -menu "$top.m41.men43" -activebackground {#d9d9d9} \
        -activeforeground {#111111} -background {#d9d9d9} -font TkMenuFont \
        -foreground {#000000} -label Notação 
    set site_3_0 $top.m41
    menu $site_3_0.men43 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font menu -foreground black -tearoff 0 
    $site_3_0.men43 add radiobutton \
        -value Newton -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command TODO -font TkMenuFont \
        -foreground {#000000} -label Newton 
    $site_3_0.men43 add radiobutton \
        -value Leibniz -activebackground {#d9d9d9} \
        -activeforeground {#000000} -background {#d9d9d9} -command TODO \
        -font TkMenuFont -foreground {#000000} -label Leibniz 
    $site_3_0.men43 add radiobutton \
        -value Heavside -activebackground {#d9d9d9} \
        -activeforeground {#000000} -background {#d9d9d9} -command TODO \
        -font TkMenuFont -foreground {#000000} -label Heavside 
    $site_3_0.men43 add radiobutton \
        -value Linha -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command TODO -font TkMenuFont \
        -foreground {#000000} -label Linha 
    $top.m41 add cascade \
        -menu "$top.m41.men44" -activebackground {#d9d9d9} \
        -activeforeground {#111111} -background {#d9d9d9} -font TkMenuFont \
        -foreground {#000000} -label {Digitos Fracionários} 
    set site_3_0 $top.m41
    menu $site_3_0.men44 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font menu -foreground black -tearoff 0 
    $site_3_0.men44 add radiobutton \
        -value {2 Digitos} -activebackground {#d9d9d9} \
        -activeforeground {#000000} -background {#d9d9d9} -command TODO \
        -font TkMenuFont -foreground {#000000} -label {2 Digitos} 
    $site_3_0.men44 add radiobutton \
        -value {3 Digitos} -activebackground {#d9d9d9} \
        -activeforeground {#000000} -background {#d9d9d9} -command TODO \
        -font TkMenuFont -foreground {#000000} -label {3 Digitos} 
    $site_3_0.men44 add radiobutton \
        -value {4 Digitos} -activebackground {#d9d9d9} \
        -activeforeground {#000000} -background {#d9d9d9} -command TODO \
        -font TkMenuFont -foreground {#000000} -label {4 Digitos} 
    ttk::label $top.tLa53 \
        -background {#d9d9d9} -foreground {#000000} -relief flat -takefocus 0 \
        -text Image -width 800 
    vTcl:DefineAlias "$top.tLa53" "TLabel1" vTcl:WidgetProc "EDO_mainWindow" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tLa53 \
        -in $top -x 0 -y 0 -width 800 -height 90 -anchor nw \
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

