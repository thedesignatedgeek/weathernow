#############################################################################
# Generated by PAGE version 4.24
#  in conjunction with Tcl version 8.6
#  Jul 27, 2019 05:39:33 PM CDT  platform: Linux
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

set desc "-family {DejaVu Sans} -size 10"
set vTcl(actual_gui_font_text_desc) $desc
set vTcl(actual_gui_font_text_name) [font create {*}$desc]
set desc "-family {DejaVu Sans Mono} -size 10"
set vTcl(actual_gui_font_fixed_desc) $desc
set vTcl(actual_gui_font_fixed_name) [font create {*}$desc]
set desc "-family {DejaVu Sans} -size 10"
set vTcl(actual_gui_font_menu_desc) $desc
set vTcl(actual_gui_font_menu_name) [font create {*}$desc]
set desc "-family {DejaVu Sans} -size 10"
set vTcl(actual_gui_font_tooltip_desc) $desc
set vTcl(actual_gui_font_tooltip_name) [font create {*}$desc]
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}

# vTcl Code to Load User Fonts

vTcl:font:add_font \
    "-family Ubuntu -size 12 -weight bold -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font15
vTcl:font:add_font \
    "-family Ubuntu -size 11 -weight bold -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font16
vTcl:font:add_font \
    "-family Ubuntu -size 10 -weight bold -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font17
vTcl:font:add_font \
    "-family Ubuntu -size 15 -weight bold -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font18


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top42
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top42
    }
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
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


proc vTclWindow.top42 {base} {
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background {#595959} -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 780x625+444+60
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1905 1050
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "FormAlerts" vTcl:Toplevel:WidgetProc "" 1
    vTcl::widgets::ttk::scrolledtext::CreateCmd $top.scr43 \
        -background {#d9d9d9} -height 75 -highlightcolor black -width 125 
    vTcl:DefineAlias "$top.scr43" "Scrolledtext1" vTcl:WidgetProc "FormAlerts" 1

    $top.scr43.01 configure -background #595959 \
        -font font16 \
        -foreground #ffffff \
        -height 3 \
        -highlightcolor black \
        -insertbackground black \
        -insertborderwidth 3 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10 \
        -wrap word
    button $top.but44 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -command on_btnExit -font TkDefaultFont \
        -foreground {#000000} -highlightcolor black -text Dismiss 
    vTcl:DefineAlias "$top.but44" "btnExit" vTcl:WidgetProc "FormAlerts" 1
    label $top.lab45 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#595959} -font $::vTcl(fonts,vTcl:font16,object) \
        -foreground {#ffffff} -highlightcolor black -relief sunken \
        -text {There are X alerts for this area} -textvariable AlertCount 
    vTcl:DefineAlias "$top.lab45" "lblAlertCount" vTcl:WidgetProc "FormAlerts" 1
    frame $top.fra46 \
        -borderwidth 2 -relief groove -background {#595959} -height 35 \
        -highlightcolor black -width 775 
    vTcl:DefineAlias "$top.fra46" "frmTitleBar" vTcl:WidgetProc "FormAlerts" 1
    set site_3_0 $top.fra46
    label $site_3_0.lab47 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#595959} -font $::vTcl(fonts,vTcl:font15,object) \
        -foreground {#ffffff} -highlightcolor black -text Label \
        -textvariable Title 
    vTcl:DefineAlias "$site_3_0.lab47" "lblTitle" vTcl:WidgetProc "FormAlerts" 1
    button $site_3_0.but42 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#595959} -command on_btnMinimize \
        -font $::vTcl(fonts,vTcl:font18,object) -foreground {#ff0000} \
        -highlightcolor black -text - 
    vTcl:DefineAlias "$site_3_0.but42" "btnMinimize" vTcl:WidgetProc "FormAlerts" 1
    place $site_3_0.lab47 \
        -in $site_3_0 -x 120 -y 7 -width 539 -relwidth 0 -height 31 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but42 \
        -in $site_3_0 -x 724 -y 7 -width 41 -relwidth 0 -height 31 \
        -relheight 0 -anchor nw -bordermode ignore 
    button $top.but48 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -command on_btnPrevious -font TkDefaultFont \
        -foreground {#000000} -highlightcolor black -text Prev 
    vTcl:DefineAlias "$top.but48" "btnPrevious" vTcl:WidgetProc "FormAlerts" 1
    button $top.but49 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -command on_btnNext -font TkDefaultFont \
        -foreground {#000000} -highlightcolor black -text Next 
    vTcl:DefineAlias "$top.but49" "btnNext" vTcl:WidgetProc "FormAlerts" 1
    label $top.lab50 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#595959} -font $::vTcl(fonts,vTcl:font17,object) \
        -foreground {#ffffff} -highlightcolor black -relief groove \
        -text Advisory -textvariable Severity 
    vTcl:DefineAlias "$top.lab50" "lblAlertSeverity" vTcl:WidgetProc "FormAlerts" 1
    message $top.mes51 \
        -anchor nw -background {#595959} \
        -font $::vTcl(fonts,vTcl:font16,object) -foreground {#ffffff} \
        -highlightcolor black -relief groove \
        -text {Bastrop, Caldwell, Hays, Travis, Williamson} \
        -textvariable Regions -width 742 
    vTcl:DefineAlias "$top.mes51" "msgRegions" vTcl:WidgetProc "FormAlerts" 1
    label $top.lab52 \
        -activebackground {#f9f9f9} -activeforeground black -anchor w \
        -background {#595959} -font $::vTcl(fonts,vTcl:font16,object) \
        -foreground {#ffffff} -highlightcolor black -relief groove \
        -text {Effective from Thu, 25 Jul 2019 19:10:00 GMT until Sun, 28 Jul 2019 00:00:00 GMT} \
        -textvariable Times 
    vTcl:DefineAlias "$top.lab52" "lblTimes" vTcl:WidgetProc "FormAlerts" 1
    label $top.lab42 \
        -activebackground {#f9f9f9} -activeforeground black -anchor w \
        -background {#595959} -font $::vTcl(fonts,vTcl:font17,object) \
        -foreground {#ffffff} -highlightcolor black -relief groove \
        -text Label -textvariable URL 
    vTcl:DefineAlias "$top.lab42" "lblUrl" vTcl:WidgetProc "FormAlerts" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.scr43 \
        -in $top -x 20 -y 215 -width 740 -relwidth 0 -height 347 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but44 \
        -in $top -x 350 -y 580 -width 80 -height 31 -anchor nw \
        -bordermode ignore 
    place $top.lab45 \
        -in $top -x 69 -y 55 -width 309 -relwidth 0 -height 31 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.fra46 \
        -in $top -x 0 -y 0 -width 780 -relwidth 0 -height 45 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but48 \
        -in $top -x 11 -y 55 -width 51 -relwidth 0 -height 31 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but49 \
        -in $top -x 384 -y 55 -width 51 -height 31 -anchor nw \
        -bordermode ignore 
    place $top.lab50 \
        -in $top -x 442 -y 56 -width 319 -relwidth 0 -height 31 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.mes51 \
        -in $top -x 20 -y 126 -width 740 -relwidth 0 -height 52 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab52 \
        -in $top -x 20 -y 93 -width 740 -relwidth 0 -height 31 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab42 \
        -in $top -x 20 -y 180 -width 740 -relwidth 0 -height 31 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}
