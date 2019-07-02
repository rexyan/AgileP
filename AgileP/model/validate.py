import re


class Validate:
    reglist = {
        'CH': r'[^\u0000-\u00FF]*',  # 纯文字
        'number': r'([-]?[0-9]+(\.[0-9]+){0,1})',  # 正负数，小数
        'positive': r'([0-9]+(\.[0-9]+){0,1})',  # 正数
        'positive_integer': r'([0-9]+)',  # 正整数

        'month': r'(0?[1-9]|1[0-2])',  # 月份
        'day': r'((0?[1-9])|((1|2)[0-9])|(3[01]))',  # 天数
        'time': r'(0?[1-9]|1[0-9]|2[0-4])((:|-|\/|\\)(0?[0-9]|[1-5][0-9])){2}',

        'username': r'[a-zA-Z0-9_\-]{1,}',  # 用户名：长度至少为1，包含大小写字母、数字、_、-
        'password': r'[a-zA-Z0-9]{6,}',  # 密码：大小写字母或数字，长度至少6位
        'password_easy': r'.{6,16}',  # 密码：6到16位的任意（除开斜线）
        'password_hard': r'(?=.*[0-9])(?=.*[a-zA-Z])(.{6,12})',  # 密码：数字 + 字母（大写或小写） + 长度6到12位
        'password_hard1': r'(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z])(.{8,})',  # 密码：数字 + 字母（大写和小写） + 长度6到12位

        'date': r'[1-9][0-9]{0,3}(?:年|\||\\|\/|\s|,|、|-)(0?[1-9]|1[0-2])(?:月|\||\\|\/|\s|,|、|-)((0?[1-9])|((1|2)[0-9])|(3[01]))日?',
        'birthday': r'(19|20)[0-9]{2}(:|-|\/|\\)(((0?[1-9]|1[0-2])(:|-|\/|\\)(0?[1-9]|1[0-9]|2[0-9]))|((0?[13-9]|1[0-2])(:|-|\/|\\)(30))|((0?[13578]|1[02])(:|-|\/|\\)(31)))',
        'birthday_hard': r'(([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8]))))|((([0-9]{2})(0[48]|[2468][048]|[13579][26])|((0[48]|[2468][048]|[3579][26])00))-02-29)',

        'credit': '[1-9][0-9]{5}[1-9][0-9]{3}((0[0-9])|(1[0-2]))(([0|1|2][0-9])|3[0-1])[0-9]{3}([0-9]|x|X)',
        'carcode': '[\u4E00-\u9FA5]{1}[A-Z]{1}[A-Z0-9]{5}',  # 车牌

        'qq': r'[1-9][0-9]{4,}',
        'fax': r'^[+]{0,1}([0-9]){1,3}[ ]?([-]?(([0-9])|[ ]){1,12})+',  # 传真
        'phone_common': r'([0-9]{3}-[0-9]{8}|[0-9]{4}-[0-9]{7}|[0-9]{8}|1[0-9]{10})',
        'phone': r'(\(((010)|(021)|(0\d{3,4}))\)( ?)([0-9]{7,8}))|((010|021|0\d{3,4}))([- ]{1,2})([0-9]{7,8})',
        'mobile': r'((13[0-9])|147|(15[0-35-9])|180|182|(18[5-9]))[0-9]{8}',  # 手机
        'email': r'([a-zA-Z0-9_\.\-])+\@([a-zA-Z0-9\-])+(\.([a-zA-Z0-9]{2,6}))+',  # 邮件
        'url': r'(([a-zA-Z]+)(:\/\/))?([a-zA-Z]+)\.(\w+)\.([\w.]+)(\/([\w]+)\/?)*(\/[a-zA-Z0-9]+\.(\w+))*(\/([\w]+)\/?)*(\?(\w+=?[\w]*))*((&?\w+=?[\w]*))*',
        # URL1
        'URL': r'((http|ftp|https)://)?(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}(\.[0-9]{1,3}){3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?',
        # URL2
        'ipv4Agent': r'(192\.168\.|169\.254\.|10\.|172\.(1[6-9]|2[0-9]|3[01]))',  # ipv4私有地址
        'ipv4': r'[0-9]{1,3}(\.[0-9]{1,3}){3}',  # ipv4地址
        'ipv6': r'[a-f0-9]{1,4}(:[a-f0-9]{1,4}){7})',  # ipv6地址
        'json_header': r'application/x-www-form-urlencoded',  # json_header
        'request_header': r'httputil',  # request_header
        'all': r'.*',  # 所有
    }

    @classmethod
    def _find_reg(self, reg_type):
        if reg_type in self.reglist:
            return self.reglist[reg_type]
        else:
            return False

    @classmethod
    def check(cls, value, reg_type="all"):
        try:
            # print re.match(r'^{0}$'.format(cls._find_reg(reg_type)), value, re.M).group()
            return re.match(r'^{0}$'.format(cls._find_reg(reg_type)), value, re.M) is not None
        except TypeError:
            return False

    @classmethod
    def has(cls, value, reg_type="all"):
        try:
            return re.search(r'{0}'.format(cls._find_reg(reg_type)), value, re.M) is not None
        except TypeError:
            return False


if __name__ == '__main__':
    print(Validate.check("17615153175", reg_type="mobile"))
