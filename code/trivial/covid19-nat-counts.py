#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python version 3.9
# created by pwz.wiki 2022


class NATCounter:

    @staticmethod
    def how_many_NAT_do_you_need(valid_period=72, report_delay=24, random_delay=False):
        """
        为了保证时刻拥有有效核酸报告，大概需要做多少次核酸检测
        :param valid_period:一次核酸的有效期限（小时）
        :param report_delay:核酸采样到出报告的延时（小时）
        :param random_delay: 随机延时（+-12小时）
        :return:
        """

        if valid_period < 0 or report_delay < 0 or valid_period < report_delay:
            print('invalid parameters')
            return

        print('_'*50)
        print(f'VALID_PERIOD: {valid_period}')
        print(f'DELAY: {report_delay}')
        print(f'RANDOM_DELAY: {random_delay}')

        def you_si_si(year_counts):
            print(f'NAT of YEAR: {year_counts}')
            print(f'NAT of MONS: {round(year_counts/12, 1)}')
            print(f'NAT of WEEK: {round(year_counts/(365/7), 1)}')
            print(f'NAT every: {round(365/year_counts, 1)}d')

        if not random_delay:
            hours_of_year = 24*365
            average = valid_period-report_delay
            you_si_si(hours_of_year//average)
        else:
            pass

        print('_'*50)


if __name__ == '__main__':
    NATCounter.how_many_NAT_do_you_need(72, 0)
    NATCounter.how_many_NAT_do_you_need(72, 24)
    NATCounter.how_many_NAT_do_you_need(72, 36)
    NATCounter.how_many_NAT_do_you_need(48, 24)
    NATCounter.how_many_NAT_do_you_need(48, 36)

