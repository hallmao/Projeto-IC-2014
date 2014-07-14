#############################################################################
# Generated by PAGE version 4.3
# in conjunction with Tcl version 8.6
#    Jul 14, 2014 02:12:43 PM


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
    "-family {Al Nile} -size 13 -weight bold -slant roman -underline 0 -overstrike 0" \
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
    set site_3_0 $base.m39
    set site_3_0 $base.m39
    set site_3_0 $base.m39
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
    wm maxsize $top 1280 703
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
        -menu "$top.m39" -background {#d9d9d9} 
    wm focusmodel $top passive
    wm geometry $top 1024x706+138+35; update
    wm maxsize $top 1024 768
    wm minsize $top 72 15
    wm overrideredirect $top 0
    wm resizable $top 0 0
    wm deiconify $top
    wm title $top "EDO Solver"
    vTcl:DefineAlias "$top" "Solver_main_window" vTcl:Toplevel:WidgetProc "" 1
    bindtags $top "$top Toplevel all _TopLevel"
    label $top.lab38 \
        -anchor nw -background white -borderwidth 4 -font font10 \
        -foreground {#000000} -relief ridge -text Texto.Aqui -width 1030 
    vTcl:DefineAlias "$top.lab38" "EDO_image_notacao" vTcl:WidgetProc "Solver_main_window" 1
    menu $top.m39 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -font TkMenuFont -foreground {#000000} \
        -tearoff 0 
    $top.m39 add cascade \
        -activebackground {#d9d9d9} -activeforeground {#111111} \
        -background {#d9d9d9} -command {} -font TkMenuFont \
        -foreground {#000000} -label Idiomas -state disabled 
    set site_3_0 $top.m39
    menu $site_3_0.men40 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font menu -foreground black -tearoff 0 
    $site_3_0.men40 add radiobutton \
        -variable selectedButton -activebackground {#d9d9d9} \
        -activeforeground {#000000} -background {#d9d9d9} -command TODO \
        -font TkMenuFont -foreground {#000000} -label Português 
    $site_3_0.men40 add radiobutton \
        -variable selectedButton -activebackground {#d9d9d9} \
        -activeforeground {#000000} -background {#d9d9d9} -command TODO \
        -font TkMenuFont -foreground {#000000} -label Espanhol 
    $site_3_0.men40 add radiobutton \
        -variable selectedButton -activebackground {#d9d9d9} \
        -activeforeground {#000000} -background {#d9d9d9} -command TODO \
        -font TkMenuFont -foreground {#000000} -label Inglês 
    $top.m39 add cascade \
        -activebackground {#d9d9d9} -activeforeground {#111111} \
        -background {#d9d9d9} -command {} -font TkMenuFont \
        -foreground {#000000} -label Notacao -state normal 
    set site_3_0 $top.m39
    menu $site_3_0.men41 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font menu -foreground black -tearoff 0 
    $site_3_0.men41 add radiobutton \
        -variable selectedButton -activebackground {#d9d9d9} \
        -activeforeground {#000000} -background {#d9d9d9} -command TODO \
        -font TkMenuFont -foreground {#000000} -label Newton 
    $site_3_0.men41 add radiobutton \
        -variable selectedButton -activebackground {#d9d9d9} \
        -activeforeground {#000000} -background {#d9d9d9} -command TODO \
        -font TkMenuFont -foreground {#000000} -label Leibniz 
    $site_3_0.men41 add radiobutton \
        -variable selectedButton -activebackground {#d9d9d9} \
        -activeforeground {#000000} -background {#d9d9d9} -command TODO \
        -font TkMenuFont -foreground {#000000} -label Heaviside 
    $site_3_0.men41 add radiobutton \
        -variable selectedButton -activebackground {#d9d9d9} \
        -activeforeground {#000000} -background {#d9d9d9} -command TODO \
        -font TkMenuFont -foreground {#000000} -label Lagrange 
    $top.m39 add cascade \
        -activebackground {#d9d9d9} -activeforeground {#111111} \
        -background {#d9d9d9} -command {} -font TkMenuFont \
        -foreground {#000000} -label DigitosDecimais -state disabled 
    set site_3_0 $top.m39
    menu $site_3_0.men43 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font menu -foreground black -tearoff 0 
    $site_3_0.men43 add radiobutton \
        -variable selectedButton -activebackground {#d9d9d9} \
        -activeforeground {#000000} -background {#d9d9d9} -command TODO \
        -font TkMenuFont -foreground {#000000} -label {2 Digitos} 
    $site_3_0.men43 add radiobutton \
        -variable selectedButton -activebackground {#d9d9d9} \
        -activeforeground {#000000} -background {#d9d9d9} -command TODO \
        -font TkMenuFont -foreground {#000000} -label {3 Digitos} 
    $site_3_0.men43 add radiobutton \
        -variable selectedButton -activebackground {#d9d9d9} \
        -activeforeground {#000000} -background {#d9d9d9} -command TODO \
        -font TkMenuFont -foreground {#000000} -label {4 Digitos} 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab38 \
        -in $top -x 0 -y 0 -width 1030 -height 70 -anchor nw \
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

