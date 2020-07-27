from hoshino import Service
from hoshino.typing import CQEvent

import json, time, requests

sv = Service('clanrank', bundle='pcr公会战', help_='''
clanrank <公会名> [all] | 查看该公会最新或者全部的会战名次记录
'''.strip())


def second2time(second):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(second))


def get_default_data():
    request_url = 'https://service-kjcbcnmw-1254119946.gz.apigw.tencentcs.com//default'
    request_headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'service-kjcbcnmw-1254119946.gz.apigw.tencentcs.com',
            'Origin': 'https://kengxxiao.github.io',
            'Referer': 'https://kengxxiao.github.io/Kyouka/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            }
    response = requests.get(url=request_url, headers=request_headers)
    return response.text


def get_clan_data(history, clanName):
    request_url = 'https://service-kjcbcnmw-1254119946.gz.apigw.tencentcs.com//name/0'
    payload_data = json.dumps({'history': history, 'clanName': clanName,})
    request_headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            #'Accept-Encoding': 'gzip, deflate, br',         加上这行会导致响应文本乱码
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Length': '48',
            'Content-Type': 'application/json',
            'Host': 'service-kjcbcnmw-1254119946.gz.apigw.tencentcs.com',
            'Origin': 'https://kengxxiao.github.io',
            'Referer': 'https://kengxxiao.github.io/Kyouka/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            }
    response = requests.session().post(url=request_url, data=payload_data, headers=request_headers)
    return response.text


@sv.on_prefix('clanrank')
async def search_clanrank(bot, ev: CQEvent):
    try:
        s = ev.message.extract_plain_text().split(' ')
        if not ((len(s)==1 and s[0]!='') or (len(s)==2 and s[1]=='all')):
            await bot.send(ev, '参数错误，请重试')
            return
        clan_name = s[0]
        default_data_dict = json.loads(get_default_data())
        history_list = default_data_dict['history']
        history_list.sort(reverse = True)
        result_list = []
        for history in history_list:
            clan_data_dict = json.loads(get_clan_data(history, clan_name))
            data = clan_data_dict['data']
            if len(data) != 0:
                name = data[0]['clan_name']
                rank = data[0]['rank']
                if name == clan_name:
                    result_list.append(f'{rank}名, 记录时间: {second2time(history)}')
        if len(s) == 1:
            msg_head = f'{clan_name}公会最新的会战名次为:\n'
            msg_part = result_list[0] if len(result_list)!=0 else ''
        else:
            msg_head = f'{clan_name}公会记录在档的会战名次为:\n'
            msg_part = '\n'.join(result_list)
        await bot.send(ev, msg_head + msg_part)
    except:
        await bot.send(ev, '指令发生错误，请重试')