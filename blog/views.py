from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .port_scan import *
from .check_url import check
from .models import ip_port
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request,'index.html')

@csrf_exempt
def search(request):
    if request.method == 'POST':
        url = str(request.POST.get('url'))
        s_p = request.POST.get('s_p')
        e_p = request.POST.get('e_p')
        c = check(url)
        try:
            ip_port.objects.get(ip=url)
        except:
            ip_port.objects.create(ip=url,port='open:')
        # ip_port.objects.filter(ip=url).update(port='open')
        if c.check():
            ans = main(url,s_p,e_p)
            # return render(request,'page.html',{'dict':ans})
            txt = ''
            port_t = ''
            for i in ans:
                if ans[i]=='open':
                    txt += str(i)+':'+ans[i]+'\n'
                    port_t += ' '+str(i)
            port_obj = ip_port.objects.filter(ip=url)
            port_json = serializers.serialize("json",port_obj)
            port_dict = json.loads(port_json)[0]['fields']
            port_txt = port_dict['port']
            flag = '0'
            for i in port_t.split():
                for j in port_txt.split():
                    if i == j:
                        flag = '1'
                        break
                if flag != '1':
                    port_txt += ' '+i
                flag = '0'
            # port_txt += port_t
            ip_port.objects.filter(ip=url).update(port=port_txt)  # 更改
            return HttpResponse(txt)
        else:
            return JsonResponse({'result':'200','success':True,'msg':'ip input false'},url)
    return JsonResponse({'result':'405','success':False,'msg':'不被允许的请求方式'})