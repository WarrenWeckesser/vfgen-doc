

def test_id_assignment(m, ident):
    k = 0
    for mitem in m:
        print(mitem[0], ' assigned ', [ident, k])
        if len(mitem) > 3:
            test_id_assignment(mitem[3], [ident, k])
        k = k + 1


def is_in_chain(idchild, idparent):
    if len(idparent) > len(idchild):
        return False
    if len(idparent) == len(idchild):
        return idparent == idchild
    t = idchild
    while len(t) > len(idparent):
        t = t[0]
    return t == idparent


def test_menu_list(m, rootident, my_ident):
    print('test_menu_list: ', rootident, ',', my_ident)
    filler = "-----------------"
    n = len(rootident) - 1
    fill = filler[0:n] + ' '
    k = 0
    for mitem in m:
        if my_ident == [rootident, k]:
            print(fill, mitem[1], '(strong)')
        else:
            print(fill, mitem[1])
        if len(mitem) > 3:
            test_menu_list(mitem[3], [rootident, k], my_ident)
        k = k + 1


def test_menu_gen(m, sm, ident):
    k = 0
    for mitem in sm:
        filename = mitem[0] + '.html'
        print('Creating ' + filename)
        test_menu_list(m, [0], [ident, k])
        if len(mitem) > 3:
            test_menu_gen(m, mitem[3], [ident, k])
        k = k + 1


def write_menu_list(f, m, rootident, my_ident):
    # print 'write_menu_list(...,...,',rootident,my_ident,')'
    # print 'write_menu_list: ',rootident,'=',my_ident,' is ',rootident==my_ident
    # if (not match_root(my_ident,rootident)):
    #     return

    k = 0
    for mitem in m:
        link_filename = mitem[0] + '.html'
        if my_ident == [rootident, k]:
            f.write('            <li class="strong"><a href="'+link_filename+'">'+mitem[1]+'</a></li>\n')
        else:
            f.write('            <li><a href="'+link_filename+'">'+mitem[1]+'</a></li>\n')
        if len(mitem) > 3:
            write_menu_list(f, mitem[3], [rootident, k], my_ident)
        k = k + 1


def write_menu_files(m, sm, ident):
    # print 'write_menu_files(...,...,',ident,')'
    k = 0
    for mitem in sm:
        filename = mitem[0] + '.html'
        print('Creating ' + filename)
        f = open(filename, 'w')
        #f.write('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">\n')
        f.write('<!doctype html>\n')
        f.write('<html lang="en">\n')
        f.write('<head>\n')
        f.write('<title>VFGEN ' + mitem[1] + '</title>\n')
        f.write('<meta http-equiv="content-type" content="text/html;charset=iso-8859-1" />\n')
#         f.write("""
# <script type="text/x-mathjax-config">
#   MathJax.Hub.Config({
#     tex2jax: {inlineMath: [["$","$"],["\\(","\\)"]],
#               processEscapes: true}
#   });
# </script>
        f.write("""
<script type="text/javascript" src="MathJax/MathJax.js?config=TeX-AMS_HTML-full"></script>
""")
        #f.write('<link rel="stylesheet" href="menulayout.css" type="text/css" />\n')
        #f.write('<link rel="stylesheet" href="menucontent.css" type="text/css" />\n')
        f.write('<link rel="stylesheet" href="menulayout.css">\n')
        f.write('<link rel="stylesheet" href="menucontent.css">\n')
        f.write('</head>\n')
        f.write('<body>\n')
        f.write('<div id="menu-side">\n')
        f.write('    <img width=145 src="images/VFGENbrown.png" alt="VFGEN">\n')
        f.write('    <ul id="menu-side-nav">\n')
        write_menu_list(f, m, [0], [ident, k])
        f.write('    </ul>\n')
        f.write('</div>\n')
        f.write('<div id="menu-page-content">\n')
        f.write('<!-- * * * Contents of '+mitem[2]+' * * * -->\n')
        cf = open(mitem[2], 'r')
        s = cf.readline()
        while s:
            f.write(s)
            s = cf.readline()
        f.write('<!-- * * * End of '+mitem[2]+' * * * -->\n')
        f.write('</div>\n')
        f.write('<div id="menu-footer">\n')
        f.write('Copyright &copy; 2005-2015 <a href="http://www.warrenweckesser.net/">Warren Weckesser</a>\n')
        f.write('</div>\n')
        f.write('</body>\n')
        f.write('</html>\n')
        f.close()
        if len(mitem) > 3:
            print('Recursing with')
            print(mitem[3])
            write_menu_files(m, mitem[3], [ident, k])
        k = k + 1

guide_submenu = [
    ['menu_fileformat',  '&sect; &nbsp; Vector Field File', 'content_vfxmlfmt.html'],
    ['menu_adolc',       '&sect; &nbsp; ADOL-C',      'content_adolc.html'],
    ['menu_auto',        '&sect; &nbsp; AUTO',        'content_auto.html'],
    ['menu_boostodeint', '&sect; &nbsp; Boost Odeint','content_boostodeint.html'],
    ['menu_check',       '&sect; &nbsp; Check',       'content_check.html'],
    ['menu_cvode',       '&sect; &nbsp; CVODE',       'content_cvode.html'],
    ['menu_dde23',       '&sect; &nbsp; DDE23',       'content_dde23.html'],
    ['menu_ddebiftool',  '&sect; &nbsp; DDE-BIFTOOL', 'content_ddebiftool.html'],
    ['menu_dde_solver',  '&sect; &nbsp; DDE_SOLVER',  'content_dde_solver.html'],
    ['menu_delay2ode',   '&sect; &nbsp; Delay2ODE',   'content_delay2ode.html'],
    ['menu_dstool',      '&sect; &nbsp; DSTool',      'content_dstool.html'],
    ['menu_evf',         '&sect; &nbsp; EVF',         'content_evf.html'],
    ['menu_gsl',         '&sect; &nbsp; GSL',         'content_gsl.html'],
    ['menu_help',        '&sect; &nbsp; Help',        'content_help.html'],
    ['menu_javascript',  '&sect; &nbsp; Javascript',  'content_javascript.html'],
    ['menu_latex',       '&sect; &nbsp; LaTeX',       'content_latex.html'],
    ['menu_lsoda',       '&sect; &nbsp; LSODA',       'content_lsoda.html'],
    ['menu_matcont',     '&sect; &nbsp; MATCONT',     'content_matcont.html'],
    ['menu_matlab',      '&sect; &nbsp; MATLAB',      'content_matlab.html'],
    ['menu_octave',      '&sect; &nbsp; Octave',      'content_octave.html'],
    ['menu_pddecont',    '&sect; &nbsp; PDDE-CONT',   'content_pddecont.html'],
    ['menu_pydstool',    '&sect; &nbsp; PyDSTool',    'content_pydstool.html'],
    ['menu_pygsl',       '&sect; &nbsp; PyGSL',       'content_pygsl.html'],
    ['menu_r',           '&sect; &nbsp; R',           'content_r.html'],
    ['menu_radau5',      '&sect; &nbsp; RADAU5',      'content_radau5.html'],
    ['menu_scilab',      '&sect; &nbsp; Scilab',      'content_scilab.html'],
    ['menu_scipy',       '&sect; &nbsp; SciPy',       'content_scipy.html'],
    ['menu_taylor',      '&sect; &nbsp; Taylor',      'content_taylor.html'],
    ['menu_xpp',         '&sect; &nbsp; XPP',         'content_xpp.html']
]

m = [['index', 'Home', 'content_home.html'],
     ['menu_download', 'Download', 'content_download.html'],
     ['menu_support', 'Support', 'content_support.html'],
     ['menu_guide', "User's Guide", 'content_guide.html', guide_submenu]]

# test_id_assignment(m, [0])
# test_menu_gen(m, m, [0])
write_menu_files(m, m, [0])
