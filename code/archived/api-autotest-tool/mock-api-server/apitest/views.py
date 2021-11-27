import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import generic

from .models import MockApi
import logging

logger = logging.getLogger('main')


class IndexView(generic.ListView):
    template_name = 'apitest/index.html'
    context_object_name = 'mockapi_list'

    def get_queryset(self):
        return MockApi.objects.order_by('-pub_date')


def do_mock(request, mock_api_name='', mock_api_id=''):
    """
    根据mock_api的id或者name查找请求及响应，若请求体匹配则给出响应，不然则给出404
    :param request: Http请求
    :param mock_api_name: mock名称
    :param mock_api_id: mock id
    :return: 对应mock的响应体或者404
    """
    logger.info(
        'Do mock with: mock_api_id=' + str(mock_api_id) + ', mock_api_name=' + mock_api_name)
    logger.info('The request detail is:\n'
                + 'request.method: ' + str(request.method) + '\n'
                + 'request.body: ' + str(request.body, 'utf-8') + '\n')

    try:
        if mock_api_id != '':
            logger.info('Finding mock api by api id.')
            mock_api = get_object_or_404(MockApi, pk=mock_api_id)
        elif mock_api_name != '':
            logger.info('Finding mock api by api name.')
            mock_api = get_object_or_404(MockApi, api_name=mock_api_name)
        else:
            # 没有可能走到这个分支，这样写只是为了消除后面的可能未定义警告
            raise Exception(
                'Parameter error, both mock api id and name are empty!')
    except Exception as e:
        logger.error('No MockApi matches the given query.\n')
        logger.error(e)
        return HttpResponse('Error, MockApi Not Found!')
    else:
        mock_response = mock_api.api_response
        res_type = mock_api.api_response_type

        # 如果是post请求，则校验请求体是否与预设一致，不一致则返回报错信息
        if request.method == 'POST':
            if str(request.body, 'utf-8') != mock_api.api_request:
                logger.error('The request body does not match the setting.')
                return HttpResponse(
                    'MockApi {0}\'s request body need to be:\n{1}\n'.format(
                        mock_api.api_name, mock_api.api_request
                    ))
        # 如果是GET请求则直接给出响应
        elif request.method == 'GET':
            pass
        # 如果是GET与POST之外的请求类型，直接返回报错信息
        else:
            logger.error('Request method is not supported.')
            return HttpResponse('Request method is not yet supported')

        # 以上对于请求方法的筛选通过之后，开始处理响应
        if 'json' in res_type:
            logger.info('Got json response.')
            return HttpResponse(json.dumps(mock_response))
        elif 'text' in res_type:
            logger.info('Got text response.')
            return HttpResponse(mock_response)
        else:
            logger.error('Content-type is not supported')
            return HttpResponse(
                'MockApi {0}\'s content-type {1} is not yet supported.'.format(
                    mock_api.api_name, mock_api.api_response_type
                ))
