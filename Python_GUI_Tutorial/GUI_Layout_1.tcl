#############################################################################



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
    set site_4_0 .top36.tNo38.pg0 
    set site_4_0 $site_4_0
    set site_4_1 .top36.tNo38.pg1 
    set site_4_0 $site_4_1
    set site_3_0 $base.fra39
    set site_3_0 $base.fra40
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
    wm maxsize $top 3200 1058
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
        -menu "$top.m37" -relief ridge -background {#d9d9d9} \
        -highlightcolor {#000000} 
    wm focusmodel $top passive
    wm geometry $top 800x600+305+102; update
    wm maxsize $top 3200 1058
    wm minsize $top 72 1
    wm overrideredirect $top 0
    wm resizable $top 0 0
    wm title $top "Diff Eq Solver"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    bindtags $top "$top Toplevel all _TopLevel"
    menu $top.m37 \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#d9d9d9} -font TkMenuFont -foreground {#000000} \
        -tearoff 0 
    ttk::style configure TNotebook -background #d9d9d9
    ttk::style configure TNotebook.Tab -background #d9d9d9
    ttk::style configure TNotebook.Tab -foreground #000000
    ttk::style configure TNotebook.Tab -font TkDefaultFont
    ttk::style map TNotebook.Tab -background [list disabled #d9d9d9 selected #d9d9d9]
    ttk::notebook $top.tNo38 \
        -width 804 -height 260 -takefocus {} 
    vTcl:DefineAlias "$top.tNo38" "Abas" vTcl:WidgetProc "Toplevel1" 1
    frame .top36.tNo38.pg0 -background #d9d9d9
    $top.tNo38 add .top36.tNo38.pg0 \
        -padding 0 -sticky nsew -state normal -text {Solução Log} -image {} \
        -compound none -underline -1 
    set site_4_0  $top.tNo38.pg0
    message $site_4_0.mes42 \
        -background {#d9d9d9} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Message \
        -width -13 
    vTcl:DefineAlias "$site_4_0.mes42" "Message1" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.mes42 \
        -in $site_4_0 -x 100 -y 90 -width -13 -height -56 -anchor nw \
        -bordermode ignore 
    frame .top36.tNo38.pg1 -background #d9d9d9
    $top.tNo38 add .top36.tNo38.pg1 \
        -padding 0 -sticky nsew -state normal -text Gráficos -image {} \
        -compound none -underline -1 
    set site_4_1  $top.tNo38.pg1
    frame $site_4_1.fra41 \
        -borderwidth 2 -relief groove -background {#bad6d8} -height 205 \
        -width 755 
    vTcl:DefineAlias "$site_4_1.fra41" "graficos_plot" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_1.fra41 \
        -in $site_4_1 -x 0 -y 0 -width 755 -height 205 -anchor nw \
        -bordermode ignore 
    frame $top.fra39 \
        -borderwidth 2 -relief groove -background {#cfeaff} -height 135 \
        -highlightbackground {#b2e0ff} -width 815 
    vTcl:DefineAlias "$top.fra39" "EDO_Display" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra39
    entry $site_3_0.ent43 \
        -background white -font TkFixedFont -foreground {#000000} \
        -insertbackground black 
    vTcl:DefineAlias "$site_3_0.ent43" "Grau5" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent44 \
        -background white -font TkFixedFont -foreground {#000000} \
        -insertbackground black 
    vTcl:DefineAlias "$site_3_0.ent44" "Grau4" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent45 \
        -background white -font TkFixedFont -foreground {#000000} \
        -insertbackground black 
    vTcl:DefineAlias "$site_3_0.ent45" "Grau3" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent46 \
        -background white -font TkFixedFont -foreground {#000000} \
        -insertbackground black 
    vTcl:DefineAlias "$site_3_0.ent46" "Grau2" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent47 \
        -background white -font TkFixedFont -foreground {#000000} \
        -insertbackground black 
    vTcl:DefineAlias "$site_3_0.ent47" "Entry5" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent48 \
        -background white -font TkFixedFont -foreground {#000000} \
        -insertbackground black 
    vTcl:DefineAlias "$site_3_0.ent48" "Grau0" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent49 \
        -background white -font TkFixedFont -foreground {#000000} \
        -insertbackground black 
    vTcl:DefineAlias "$site_3_0.ent49" "Entry7" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent50 \
        -background white -font TkFixedFont -foreground {#000000} \
        -insertbackground black 
    vTcl:DefineAlias "$site_3_0.ent50" "xTEntryBox" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.ent43 \
        -in $site_3_0 -x 20 -y 50 -width 32 -height 27 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent44 \
        -in $site_3_0 -x 130 -y 50 -width 32 -height 27 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent45 \
        -in $site_3_0 -x 220 -y 50 -width 32 -height 27 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent46 \
        -in $site_3_0 -x 300 -y 50 -width 32 -height 27 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent47 \
        -in $site_3_0 -x 380 -y 50 -width 32 -height 27 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent48 \
        -in $site_3_0 -x 460 -y 50 -width 32 -height 27 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent49 \
        -in $site_3_0 -x 570 -y 50 -width 32 -height 27 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent50 \
        -in $site_3_0 -x 620 -y 50 -anchor nw -bordermode ignore 
    frame $top.fra40 \
        -borderwidth 2 -relief groove -background {#cfeaff} -height 85 \
        -width 805 
    vTcl:DefineAlias "$top.fra40" "Language_selection" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra40
    button $site_3_0.but55 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Button 
    vTcl:DefineAlias "$site_3_0.but55" "Button2" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but56 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Button 
    vTcl:DefineAlias "$site_3_0.but56" "Button3" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but57 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Button 
    vTcl:DefineAlias "$site_3_0.but57" "Button4" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but58 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Button 
    vTcl:DefineAlias "$site_3_0.but58" "Button5" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.but55 \
        -in $site_3_0 -x 30 -y 30 -width 30 -height 28 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but56 \
        -in $site_3_0 -x 80 -y 30 -width 30 -height 28 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but57 \
        -in $site_3_0 -x 130 -y 30 -width 30 -height 28 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but58 \
        -in $site_3_0 -x 750 -y 30 -width 30 -height 28 -anchor nw \
        -bordermode ignore 
    spinbox $top.spi51 \
        -activebackground {#f9f9f9} -background white \
        -buttonbackground {#d9d9d9} -foreground black -from 1.0 \
        -highlightbackground black -highlightcolor black -increment 1.0 \
        -insertbackground black -selectbackground {#c4c4c4} \
        -selectforeground black -textvariable {Precisão Decimal} -to 100.0 
    vTcl:DefineAlias "$top.spi51" "PrecisaoDecimal" vTcl:WidgetProc "Toplevel1" 1
    text $top.tex52 \
        -background {#c2e7ff} -font TkTextFont -foreground black -height 38 \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -selectbackground {#c4c4c4} \
        -selectforeground black -width 198 
    .top36.tex52 configure -font TkTextFont
    .top36.tex52 insert end text
    vTcl:DefineAlias "$top.tex52" "Precis_Dec_Text_box" vTcl:WidgetProc "Toplevel1" 1
    button $top.but53 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Mudar Notação} 
    vTcl:DefineAlias "$top.but53" "Mudar_Not" vTcl:WidgetProc "Toplevel1" 1
    listbox $top.lis54 \
        -background {#cfeaff} -font TkFixedFont -foreground {#000000} 
    .top36.lis54 configure -font TkFixedFont
    vTcl:DefineAlias "$top.lis54" "Notacao_Lista" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tNo38 \
        -in $top -x 0 -y 260 -width 804 -height 260 -anchor nw \
        -bordermode ignore 
    place $top.fra39 \
        -in $top -x 0 -y 0 -width 815 -height 135 -anchor nw \
        -bordermode ignore 
    place $top.fra40 \
        -in $top -x 0 -y 520 -width 805 -height 85 -anchor nw \
        -bordermode ignore 
    place $top.spi51 \
        -in $top -x 20 -y 170 -width 55 -height 38 -anchor nw \
        -bordermode ignore 
    place $top.tex52 \
        -in $top -x 80 -y 170 -width 198 -height 38 -anchor nw \
        -bordermode ignore 
    place $top.but53 \
        -in $top -x 340 -y 170 -width 120 -height 48 -anchor nw \
        -bordermode ignore 
    place $top.lis54 \
        -in $top -x 470 -y 140 -width 302 -height 112 -anchor nw \
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

