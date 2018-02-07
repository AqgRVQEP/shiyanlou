#!/usr/bin/env python3
'''
挑战2：完善工资计算器
'''
import sys


def 计算并且打印税后工资(员工号, 工资):
    应纳税额 = 工资 - 工资 * (0.08 + 0.02 + 0.005 + 0 + 0 + 0.06) - 3500
    if 0 < 应纳税额 <= 1500:
        到手工资 = 工资 * 0.835 - (应纳税额 * 0.03 - 0)
    elif 1500 < 应纳税额 <= 4500:
        到手工资 = 工资 * 0.835 - (应纳税额 * 0.1 - 105)
    elif 4500 < 应纳税额 <= 9000:
        到手工资 = 工资 * 0.835 - (应纳税额 * 0.2 - 555)
    elif 9000 < 应纳税额 <= 35000:
        到手工资 = 工资 * 0.835 - (应纳税额 * 0.25 - 1005)
    elif 35000 < 应纳税额 <= 55000:
        到手工资 = 工资 * 0.835 - (应纳税额 * 0.3 - 2755)
    elif 55000 < 应纳税额 <= 80000:
        到手工资 = 工资 * 0.835 - (应纳税额 * 0.35 - 5505)
    elif 应纳税额 > 80000:
        到手工资 = 工资 * 0.835 - (应纳税额 * 0.45 - 13505)
    else:
        到手工资 = 工资 * 0.835
    print(str(员工号) + ":" + format(到手工资, ".2f"))


if len(sys.argv) < 2:
    print("Parameter Error")
    exit()

for 参数 in sys.argv[1:]:
    参数列表 = 参数.strip().split(':')
    try:
        员工 = int(参数列表[0])
        税前工资 = int(参数列表[1])
        计算并且打印税后工资(员工, 税前工资)
    except Exception as e:
        print("Parameter Error")