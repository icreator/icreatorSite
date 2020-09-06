# -*- coding: utf-8 -*-

# выдача файлов на экран по стримингу - вместо загрузки из полей записей БД
def stream():
    f = request.folder + 'views/' + '/'.join(request.args)
    #print f
    return response.stream(f, request=request)

def u(h, url, cls='col-sm-4'):
    return DIV(DIV(P(h, _class='btn_mc2'), _class='btn_mc1', _onclick="location.href='%s'" % url), _class='btn_mc ' + cls)

def old_ver(i=12):
    return DIV(
        u(T('Старая версия сайта'),
          #'http://i-creator.azurewebsites.net/',
          URL('static', 'icreator/index.htm'),
          'col-sm-%s' % i),
            _class='row')

## вызывается по AJAX из soc_share
def like():
    r = db.pg[ request.args(0) ]
    r.update_record (lke = (r.lke or 0) + 1)
    pass

def soc_share(r):
    ### ссылка по Лайку от АИ - http://icreator.site/default/p/philos/main_aim?fbclid=IwAR0yn18lvfc5lYDqFulLBOmH4t8OaT1tB56T7h2L2DztQyTKUJeSE8y_lBw
    url = URL(args=request.args, host=True) ## , vars=request.vars - от фейсбука параметр вставляет свой
    path = URL('static','images')
    title = r.name
    twit = 'http://twitter.com/home?status='+title+'%20'+url
    facebook = 'http://www.facebook.com/sharer.php?u='+url
    gplus = 'https://plus.google.com/share?url='+url
    cl = ' onclick="ajax(\'%s\');" ' % URL('like', args=[r.id])
    tbar = '<div class="center"'+cl+'><a target="_blank" href="'+twit+'" id="twit" title="Share on twitter"><img src="'+path+'/twitter.png"  alt="Share on Twitter" width="42" height="42" /></a> <a target="_blank" href="'+facebook+'" id="facebook" title="Share on Facebook"> <img src="'+path+'/facebook.png"  alt="Share on facebook" width="42" height="42" /></a> <a target="_blank" href="'+gplus+'" id="gplus" title="Share on Google Plus"> <img src="'+path+'/gplus-32.png"  alt="Share on Google Plus" width="42" height="42" /></a> <i class="fa fa-eye gold">'+'%s' % (r.see or  '')+'</i> <i class="fa fa-heart red">'+'%s' % (r.lke or  '')+'</i></div>'
    
    return XML(tbar)

def dance():
    response.nsf = True
    h = CAT(H3('Танец хастл - социальный парный танец'),
        BR(),
        'Танцуем с женой на набережной в Нескучном саду (г.Москва):', BR(),
        IFRAME(
            _width=560, _height=315,
            _src="https://www.youtube.com/embed/1Inei1pfWb4",
            _frameborder=0, _allowfullscreen=''), BR(),
        BR(),
        'Экспромт и ипровизация под настроение:',BR(),
        A(_href='http://vk.com/video4587762_162717352'),BR(),
        #IFRAME(_width=560, _height=315,
        #    _src="//vk.com/video_ext.php?oid=4587762&id=162717352&hash=b080754e8ba6d2d4&hd=2",
        #    _frameborder=0),
        XML('<iframe src="//vk.com/video_ext.php?oid=4587762&id=162717352&hash=b080754e8ba6d2d4&hd=1" \
         width="560", height="315", \
         frameborder="0"></iframe>'), # width="640" height="360"
        BR(),
        BR(),
        'Танцуем Екатериниском саду (г.Москва):',BR(),
        A(_href='http://vk.com/video4587762_164283297'),BR(),
        IFRAME(
            _width=560, _height=315,
            #_width=560, _height=315,
            _src="//vk.com/video_ext.php?oid=4587762&id=164283297&hash=1e1e199526ec7cae&hd=2",
            _frameborder=0), BR(),
        )
    h += DIV(
            u(T('Назад'), URL('index') , 'col-sm-12'),
            _class='row')
    return dict(h=DIV(h, _class='container',
                _style='padding-bottom:25px;background-color:indianred;'))

def bitcoin():
    response.nsf = True
    h = CAT(
        DIV(
            u(CAT(IMG(_src=URL('static','images/currs_BTC.png')),' ', T('Что такое Биткойн? Почему он лучше современных денег?')), 'http://7pay.in/crypto' , 'col-sm-12'),
            _class='row'),
        DIV(
            u(T('Назад'), URL('index') , 'col-sm-12'),
            _class='row')
        )
    return dict(h=DIV(h, _class='container',
                _style='padding-bottom:25px;background-color:indianred;'))

def me():
    response.nsf = True
    h = CAT(
        H1('Ермолаев Дмитрий Сергеевич, д.р. 1966.08.21'),
        P('Список моих научных статей и изобретений', ': ',
         A('на Elibrary.ru', _href='http://elibrary.ru/author_items.asp?authorid=819474', _target='blank')),
        H2('Биография'),
    )
    odd = None
    
    for rec in [
        ['1966-08-21',0, 'Родился во Владивостоке', ''],
        [1975,1982,'Школьные городские олимпиады по математике',''],
        [1983,1988,'Высшее техническое образование',
                'Дальневосточный Политехнический Институт (ныне Университет). Увлекся программированием'],
        [1984,1986,'Участвовал во Всероссийских олимпиадах по физике','От Приморского края. Занимал стабильно места по середине всего списка участников (Томск, Самара)'],
        [1988,1991, 'Аспирантура','Началась перестройка и аспирантура была заменена работой на себя'],
        [1993,1998, 'Свободная работа','До кризиса 1998г работал и занимался коммерцией'],
        [1996,2000, 'Усилители мощности','Изобретаю усилители мощности звуковой частоты на базе цифровых и импульсных решений'],
        [1998,2006, 'Система поиска','Разработка программной Системы осмысленного поиска в текстовой информации'],
        [2000,2010, 'Электродвигатель','Изобретаю электродвигаль-электрогенератор повышенной мощности с КПД 0.95'],
        [2013,2015, 'Биткоин','Изучение биткоин-технологии и создание платежных сервисов на нём - 7Pay.in (поалат услуг и обмен) и LITE.cash (органнизация приёма биткоинов на сайтах'],
        [2013,'...', 'Блокчейн', 'Изучаю блокчейн технологии - изобретаю цепочки данных - datachains.world'],
        ]:
        odd = not odd
        h += DIV(
            DIV(rec[0], rec[1] and ' - ' or '', rec[1] or '', _class='col-sm-2'),
            DIV(B(rec[2]), BR(), rec[3], _class='col-sm-10'),
            _class='row' + (odd and ' odd' or ''),
            _style='padding:5px 0;'
            )
    h += DIV(
            u(T('Назад'), URL('index') , 'col-sm-12'),
            _class='row')
    return dict(h=DIV(h, _class='container',
                _style='padding-bottom:25px;background-color:indianred;'))

def all():
    response.nsf = True
    h = CAT()
    odd = None
    for rec in db(db.pg).select(orderby=~db.pg.dte):
        odd = not odd
        cat = db.cat[ rec.cat_id]
        see = rec.see and CAT(' ', TAG.i(_class='fa fa-eye'), rec.see) or ''
        lke = rec.lke and CAT(' ', TAG.i(_class='fa fa-heart'), rec.lke) or ''
        h += DIV(
            DIV(rec.dte, ' ', cat.name, _class='col-sm-3'),
            DIV(A(rec.name, _href=URL('p', args= rec.arg and [cat.folder, rec.arg] or [rec.id])), see, lke, _class='col-sm-9'),
            _class='row' + (odd and ' odd' or ''),
            _style='padding:10px 0;'
            )
    return dict(h=DIV(h, _class='container',
                _style='padding-bottom:25px;background-color:indianred;'))

# выдаем либо весь каталог либо страницу по 1-2 аргументам
def p():
    response.nsf = True
    if not request.args: return 'emty args'

    arg_1 = request.args(0)
    cat = page = None
    if len(request.args) == 1:
        if arg_1.isdigit():
            page_id = arg_1
            page = db.pg[page_id]
            cat = page and db.cat[page.cat_id]
            cat_folder = cat and cat.folder
        else:
            cat_folder = arg_1
            cat = db(db.cat.folder == cat_folder).select().first()
    else:
        cat_folder = arg_1
        cat = db(db.cat.folder == cat_folder).select().first()

    if not cat:
        
        return dict(h=old_ver())

    if not page:
        page_arg = cat and request.args(1)
        if page_arg:
            page = db((db.pg.arg == page_arg)
                 & (db.pg.cat_id == cat.id)).select().first()


    h = CAT()
    h += H2(cat.name)
    if page:
        page.update_record( see = (page.see or 0) +1 )
        f = DIV(
            soc_share(page) if page else '',
            u(CAT(T('Назад в раздел'), ' ', cat.name), URL(args=[cat_folder]), 'col-sm-12'),
            _class='row')
        if page.descr:
            h += DIV(XML(page.descr))
        else:
            # тут ссылки включаются как вызовы на контроллер
            # поэтому через download
            #spath = 'views/default/pages/' + cat.folder + '/'
            #spath1 = '/' + request.application + '/default/stream/' + spath
            #return dict(page=request.folder + spath + page.arg, sp=spath1, h=h, f=f)
            up = cat_folder + '/'
            sp = 'default/pages/' + up
            response.view = sp + page_arg + '.html'
            return dict(sp= '/' + request.application + '/default/stream/' + sp,
                       h = h, f = f)
    else:
        recs = db(db.pg.cat_id == cat.id).select(orderby=~db.pg.dte)

        h += H2(T('Важные, ценные, основные'))
        for r in db((db.pg.cat_id == cat.id)
                      & (db.pg.vip >0)).select(orderby=~db.pg.vip):
            see = r.see and CAT(' ', TAG.i(_class='fa fa-eye'), ' ',r.see) or ''
            lke = r.lke and CAT(' ', TAG.i(_class='fa fa-heart'), ' ',r.lke) or ''
            h += H3(A(r.name, _href=URL(args=r.arg and [cat_folder, r.arg] or [r.id])), see, lke)

        h += H3(T('Все по дате опубликования'))
        
        # если страница лежит в БД то у нее нет arg - имени файла
        for r in recs:
            see = r.see and CAT(' ', TAG.i(_class='fa fa-eye'), ' ',r.see) or ''
            lke = r.lke and CAT(' ', TAG.i(_class='fa fa-heart'), ' ',r.lke) or ''
            h += H4(A(r.dte, ' ', r.name, _href=URL(
                    args=r.arg and [cat_folder, r.arg] or [r.id])), see, lke)

        if not recs:
            h += old_ver()

    h += DIV(
            page and CAT(
                soc_share(page) if page else '',
                u(CAT(T('Назад в раздел'),' ',cat.name), URL(args=[cat_folder]), 'col-sm-12'))
            or u(T('Назад'), URL('index') , 'col-sm-12'),
            _class='row')
    return dict(h=DIV(h, _class='container',
                _style='padding-bottom:25px;background-color:maroon;'))

def page_old__(ee):
    response.nsf = True
    cat_id = request.args(0)
    cat = cat_id and db.cat[cat_id]
    if not cat:
        redirect(URL('default', 'index'))

    response.title = ''
    id = request.args(1)
    rec = id and db.pg[id]
    h = CAT()
    h += H2(cat.name)
    f = DIV(
        soc_share(rec) if rec else '',
        u(CAT(T('Назад в раздел'), ' ', cat.name), URL(args=[request.args[0]]), 'col-sm-12'),
        _class='row')
    #h += DIV('test data-role', data={ 'role':'collapsible'})
    #h += DIV('text', **{'_data-role': 'collapsible'})
    if rec:
        if rec.descr:
            h += DIV(XML(rec.descr))
        else:
            if False:
                from gluon.fileutils import read_file
                spath = 'static/pages/' + cat.folder + '/'
                spath1 = '/' + request.application + '/' + spath
                h += XML(response.render(request.folder + spath + rec.arg + '.html', dict(sp=spath1)))
            else:
                # тут ссылки включаются как вызовы на контроллер
                # поэтому через download
                spath = 'views/default/pages/' + cat.folder + '/'
                spath1 = '/' + request.application + '/default/stream/' + spath
                return dict(page=request.folder + spath + rec.arg + '.html', sp=spath1, h=h, f=f)

    else:
        h += H2(T('Важные, ценные, основные'))
        for rec in db((db.pg.cat_id == cat_id)
                      & (db.pg.vip >0)).select():
            h += H3(A(rec.dte, ' ', rec.name, _href=URL(args=[cat_id, rec.id])))
        h += H3(T('Все по дате опубликования'))
        for rec in db(db.pg.cat_id == cat_id).select(orderby=~db.pg.dte):
            h += H4(A(rec.dte, ' ', rec.name, _href=URL(args=[cat_id, rec.id])))

    return dict(h=h)

def index():
    response.nsf = True
    h = CAT()
    h += H2(T('Мои Достижения'), _class='header')
    h += H4(T('Для вего мира и общества'), _class='header')
    h += DIV(
            u(T('Физика'),URL('p', args=['physics'])),
            u(T('Экономика'),URL('p', args=['econ'])),
            u(T('Философия'),URL('p', args=['philos'])),
            u(T('Общество'),URL('p', args=['soc'])),
            u(T('Финансы'),URL('p', args=['finance'])),
            u(T('Госуправление'),URL('p', args=['gov'])),
            _class='row')
    h += BR()
    h += H2(T('Мои Идеи, Изобретения и Разработки'), _class='header')
    h += H4(T('Инновации для инвесторов и бизнеса'), _class='header')
    h += DIV(
            u(T('Электрические машины, элекродвигатели'),URL('p', args=['ed'])),
            u(T('Смысловой поиск текстовой информации'),URL('p', args=['isearch'])),
            u(T('Идеи для бизнеса и жизни'),URL('p', args=['ideas'])),
            u(T('Искусственный Интеллект'),URL('p', args=['ii'])),
            u(T('Усилители мощности звуковой частоты'),URL('p', args=['amplif'])),
            u(T('Энергия'),URL('p', args=['energy'])),
            _class='row')
    h += BR()
    h += H2(T('Мои Увлечения'), _class='header')
    h += H4(T('Для себя лично'), _class='header')
    h += DIV(
            u(T('Программирование'),URL('p', args=['prog'])),
            u(T('Танцы'),URL('dance')),
            u(CAT(IMG(_src=URL('static','images/currs_BTC.png')),' Bitcoin, ',
                  T('Биткойн')),URL('bitcoin')),
            _class='row')
    h += BR()
    h += H2(T('Сайт'), _class='header')
    h += DIV(
            u(T('О Себе'),URL('me')),
            u(T('В Начало'),URL('default', 'index')),
            u(T('Всё по дате'),URL('all')),
            _class='row')
    h += old_ver()
    
    return dict(content=DIV(h, _class='container',
                _style='padding-bottom:25px;background-color:darkslategrey;'))

def wiki():
    return auth.wiki()

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
