# -*- coding: utf-8 -*-

routes_in = (
    # очень много запросов идут на эту иконку почемуто. ответ сервера 400(код ошибки) 50(миллисек?)
    (r'/favicon.ico', r'/icreator/static/images/favicon.png'),
    (r'/favicon.png', r'/icreator/static/images/favicon.png'),
    (r'/robots.txt', r'/icreator/static/robots.txt'),
    (r'/', r'/icreator/default/index/'),
    (r'/p/$anything', r'/icreator/default/p/$anything'),
    (r'/index/$anything', r'/icreator/default/index/$anything'),
    (r'/index', r'/icreator/default/index'),
    (r'/icreator/index', r'/icreator/default/index'),
    (r'/icreator', r'/icreator/default/index'),
    (r'/$anything', r'/icreator/$anything'),
    )

routes_out = [
    #(x, y) for (y, x) in routes_in
    (r'/icreator/static/images/favicon.png', r'/favicon.ico'),
    (r'/icreator/static/images/favicon.png', r'/favicon.png'),
    (r'/icreator/static/robots.txt', r'/robots.txt'),
    (r'/icreator/$anything', r'/$anything')
    ]
#routes_out.insert(0, )
#routes_out.insert(0, (r'/icreator', r'/'))
