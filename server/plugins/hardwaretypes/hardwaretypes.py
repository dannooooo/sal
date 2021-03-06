from yapsy.IPlugin import IPlugin
from yapsy.PluginManager import PluginManager
from django.template import loader, Context
from django.db.models import Count
from server.models import *
from django.shortcuts import get_object_or_404
import server.utils as utils

class HardwareTypes(IPlugin):
    def show_widget(self, page, machines=None, theid=None):
        # The data is data is pulled from the database and passed to a template.
        
        # we're not linking anywhere, so the template will be the same for all
        t = loader.get_template('hardwaretypes/templates/front.html')
        if page == 'front':
            if not machines:
                machines = Machine.objects.all()
        
        if page == 'bu_dashboard':
            if not machines:
                machines = utils.getBUmachines(theid)
        
        if page == 'group_dashboard':
            if not machines:
                machine_group = get_object_or_404(MachineGroup, pk=theid)
                machines = Machine.objects.filter(machine_group=machine_group)
        
        if machines:
            machines = machines.values('machine_model').annotate(count=Count('machine_model'))
        else:
            machines = None
        
        out = []
        if machines:
            for machine in machines:
                if machine['machine_model']:
                    found = False
                    nodigits=''.join(i for i in machine['machine_model'] if i.isalpha())
                    machine['machine_model']=nodigits
                    for item in out:
                        if item['machine_model'] == machine['machine_model']:
                            item['count'] = item['count']+machine['count']
                            found = True
                            break
                    #if we get this far, it's not been seen before
                    if found == False:
                        out.append(machine)

        c = Context({
            'title': 'Hardware Types',
            'machines': out,
            'theid': theid,
            'page': page
        })
        return t.render(c), 4
    
    def filter_machines(self, machines, data):
        # You will be passed a QuerySet of machines, you then need to perform some filtering based on the 'data' part of the url from the show_widget output. Just return your filtered list of machines and the page title.
        
        machines = machines.filter(operating_system__exact=data)
        
        return machines, 'Machines running '+data
        