import argparse
import functools
import json
import os
import random
import time

import requests

parser = argparse.ArgumentParser("PKU-fight-epidemic")
parser.add_argument("-u", "--user", type=str, required=True)
parser.add_argument("-p", "--password", type=str, required=True)
parser.add_argument("-f", "--form", type=str, required=True)
args = parser.parse_args()

SCKEY = os.getenv('SCKEY')


def log(log_type):
    def add_log(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            print('正在进行 {}......'.format(log_type))
            res = func(*args, **kwargs)
            end_time = time.time()
            if res == 200:
                print('{} 完成, 耗时 {:.3f}s.'.format(log_type, end_time - start_time))
            else:
                print('{} 失败. Status Code: {}'.format(log_type, res))
                raise Exception('{} 失败. HTTP Status Code: {}'.format(log_type, res))
            return res

        return wrapper

    return add_log


# 第一步：获得cookies
@log('获取cookies')
def get_cookie(session):
    r = session.get('https://iaaa.pku.edu.cn/iaaa/oauth.jsp', params={
        'appID': 'portal2017',
        'appName': '北京大学校内信息门户新版',
        'redirectUrl': 'https://portal.pku.edu.cn/portal2017/ssoLogin.do'
    })
    return r.status_code


# 第二步：进行oauth和ssologin认证
@log('获取oauth及ssologin认证')
def authenticate(session, user, password):
    r = session.post('https://iaaa.pku.edu.cn/iaaa/oauthlogin.do',
                     {'appid': 'portal2017', 'userName': user, 'password': password,
                      'redirUrl': 'https://portal.pku.edu.cn/portal2017/ssoLogin.do'})

    token = json.loads(r.text).get('token')
    _rand = random.random()

    r = session.get('https://portal.pku.edu.cn/portal2017/ssoLogin.do', params={'_rand': _rand, 'token': token})
    return r.status_code


# 第三步：获取ssop的cookies
@log('获取ssop的cookies')
def open_epidemic(session):
    r = session.get('https://portal.pku.edu.cn/portal2017/util/appSysRedir.do?appId=epidemic')
    return r.status_code


# 第四部：表单填写
@log('填写云战"疫"表单')
def fill_epidemic_form(session, arg):
    r = session.post('https://ssop.pku.edu.cn/stuAffair/edu/pku/stu/sa/jpf/yqfk/stu/saveMrtb.do',
                     data=json.loads(arg.form))
    return r.status_code


def main():
    try:
        s = requests.Session()
        get_cookie(s)
        authenticate(s, args.user, args.password)
        open_epidemic(s)
        fill_epidemic_form(s, args)

    except TimeoutError as e:
        desp = '由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。'
    except Exception as e:
        print(e)
        desp = str(e)
    else:
        desp = '战"疫"成功！'
    finally:
        requests.post('https://sc.ftqq.com/{}.send'.format(SCKEY), data={
            'text': '云战"疫"填报结果 {}'.format(time.strftime("%Y/%m/%d", time.localtime())),
            'desp': desp
        })


if __name__ == '__main__':
    main()
