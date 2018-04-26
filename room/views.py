from django.shortcuts import render
from django.http import HttpResponse
from .resources import DeskResource, DRUserResource
from .models import Room, DRUser, Computer, Desk, Software
from django.db.models import Count

from graphos.sources.simple import SimpleDataSource
from graphos.renderers.gchart import BarChart
from graphos.renderers.gchart import ColumnChart


# from graphos.renderers.yui import BarChart

# Create your views here.

def index(request):
    # r = DRUser.objects.order_by('-username',)[:5]
    c = Computer.objects.all()
    u = DRUser.objects.all()
    d = Desk.objects.all()

    # context = {'latest_question_list': latest_question_list}
    # return render(request, 'polls/index.html', context)
    return render(request, 'index.html', {'computers': c, 'users': u, 'desks': d})
    # return HttpResponse(r[0].desk_number)


def software(request, title):
    # s = Software.objects.values('title') \
    s = Software.objects.filter(title__icontains=title)
    # .annotate(num_title=Count('id'))

    return render(request, 'software_machine.html', {'software': s})


def software2(request):
    s = Software.objects.values('title', 'version') \
        .annotate(num_title=Count('id'))
    return render(request, 'software.html', {'software': s})


def desk(request, desk_number):
    return HttpResponse("View Desk: " + str(desk_number))


def computer(request, hostname):
    c = Computer.objects.get(hostname=hostname)
    return render(request, 'computer.html', {'computer': c})


def computers(request):
    c = Computer.objects.all()
    cpu = Computer.objects.values('cpu').annotate(Count('cpu')).order_by('-cpu__count')
    subnet = Computer.objects.values('address').annotate(Count('address')).order_by('-address__count')
    ram = Computer.objects.values('ram').annotate(Count('ram')).order_by('-ram')

    return render(request, 'computers.html', {'computers': c, 'cpu': cpu, 'subnet': subnet, 'ram': ram})


# Graphos doesn't like the Queryset result from .values, so turn it into a list it will swallow.
def mung_table(table):
    data = []
    data.append(['title', 'num_title'])
    for i, v in enumerate(table):
        data.append([v['title'], v['num_title']])

    return data


# Graphos doesn't like the Queryset result from .values, so turn it into a list it will swallow.
# expect headers to match column names
def listify_table_with_headers(headers, table):
    data = []
    data.append(headers)

    for i, v in enumerate(table):
        data.append([v[headers[0]], v[headers[1]]])

    return data


def graph(request):
    s = Software.objects.values('title').annotate(num_title=Count('title')).order_by('-num_title').filter(title__icontains='eikon') #[25:75]
    # s = Software.objects.all()
    print(s)
    if s.count():
        # data = mung_table(s)
        data = listify_table_with_headers(['title', 'num_title'], s)
        data_source = SimpleDataSource(data=data)
        # print (data)
        # data = ModelDataSource(s, fields=['title', 'num_title'])
        chart = BarChart(data_source, width='100%', options={
            'backgroundColor': 'grey',
            'title': 'SOFTWARE',
            'fontSize': '11'
        })
        # print (chart.as_html())

    return render(request, 'graph.html', {'chart': chart, 'software': s})
        # return HttpResponse(chart.as_html())

    # 1. create a Room()
    # 2. import desks
    # 3. import users
    # 4. import computers
    # 5. software


def import_desks(request):
    f = open('desks.csv', 'r')
    next(f)  # skip header row
    for line in f:
        line = line.split(',')
        druser = Desk()
        print(line)
        druser.desk_number = int(line[0])
        druser.description = int(line[1])
        druser.power_points = int(line[2])
        druser.data_points = int(line[3])
        druser.room = Room.objects.get(id=line[4])
        druser.save()
    f.close()
    return HttpResponse("IMPORTED DESKS")


def import_users(request):
    f = open('users.csv', 'r')
    next(f)  # skip header row
    for line in f:
        line = line.split(',')
        druser = DRUser()
        print(line)
        druser.firstname = str(line[0])
        druser.lastname = str(line[1])
        druser.username = str(line[2])
        druser.business_unit = line[3]
        _desk = Desk.objects.get(desk_number=line[4].strip())
        if _desk.count():
            print (_desk[0].hostname)
            druser.desk = _desk[0]
            druser.save()
    f.close()
    return HttpResponse("IMPORTED USERS")


def import_computers(request):
    f = open('machines.csv', 'r')
    next(f)  # skip header row
    for line in f:
        line = line.split(',')

        comp = Computer()
        comp.hostname = line[0].strip()
        comp.address = line[11]
        comp.cpu = line[2]
        comp.ram = int(line[8][:-3])  # -3 to remove MB text
        # if there's a listed user - link the desk.
        if line[7] != '<none>':
            desk = Desk.objects.filter(druser__username__contains=line[7].strip())
            if desk.count():
                # d = Desk.objects.get(desk_number=desk.desk_number)
                # d = Desk.objects.filter(druser__username__contains=line[7])
                print (Desk + " " + desk[0].desk_number)
                comp.desk = desk[0]

        print(comp)
        try:
            comp.save()
        except Exception as e:
            print("problem with user->mapping" + print(e))

    f.close()

    return HttpResponse("IMPORTED PCS")


def import_software(request):
    with open('software2.csv') as fp:
        fp.readline()
        line = fp.readline()
        computer_name = "get me out into scope so I'm remembered through while loop"
        print (line)
        while line:
            # print(line)
            line = line.split(',')

            if line[0]:  # hostname present in csv
                computer_name = line[0].strip()

            comp = Computer.objects.filter(hostname__contains=computer_name)
            if comp.count() > 0:
                name = str(line[1].strip())

                # split out name and version from string
                ver = line[1].split('|')
                name = ver[0]
                if len(ver) > 1:  # sometimes there isn't a version part
                    ver = str(ver[1].strip())
                else:
                    ver = "unknown"

                soft = Software(title=name, computer=comp[0], version=ver)
                print (comp[0].hostname + " +++ " + soft.title + ">>>>>" + soft.version)
                soft.save()
            else:
                print ("No matching PC " + line[0])
            line = fp.readline()

    # print (comp)
    #        else:
    #            print(line[1])

    return HttpResponse("IMPORTED SOFTWARE")
