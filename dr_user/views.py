from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from tablib import Dataset


# Create your views here.

def index(request):
    my_users = DR_User.objects.order_by('lastname')
    context = {'my_users': my_users}
    return render(request, 'dr_user\index.html', context)


def import_user(request):
    if request.method == 'POST':
        user_resource = DR_UserResource()
        dataset = Dataset()
        new_users = request.FILES['myfile']

        imported_data = dataset.load(new_users.read().decode('utf-8'), format='csv')
        result = user_resource.import_data(dataset, dry_run=True)  # Test the data import
        if not result.has_errors():
            user_resource.import_data(dataset, dry_run=False)  # Actually import now
    return render(request, 'dr_user\import_user.html')


def detail(request):
    return HttpResponse("VIEW USER:" """+ str(user_id)""")


def query_user(request):
    import ldap

    l = ldap.initialize("ldap://sydwisads01")
    try:
        l.protocol_version = ldap.VERSION3
        l.set_option(ldap.OPT_REFERRALS, 0)

        bind = l.simple_bind_s("dshanaha", "Janu2018!")

        base = "dc=global,dc=thenational, dc=com"
        criteria = "(&(objectClass=user)(sAMAccountName=username))"
        attributes = ['displayName', 'company']
        result = l.search_s(base, ldap.SCOPE_SUBTREE, criteria, attributes)

        results = [entry for dn, entry in result if isinstance(entry, dict)]
        print(results)
    finally:
        l.unbind()
    return HttpResponse("QUERY USER")
# return render(request, 'users\ldap_query.html', results)
