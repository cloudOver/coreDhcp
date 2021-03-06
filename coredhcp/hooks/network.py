"""
Copyright (C) 2014-2017 cloudover.io ltd.
This file is part of the CloudOver.org project

Licensee holding a valid commercial license for this software may
use it in accordance with the terms of the license agreement
between cloudover.io ltd. and the licensee.

Alternatively you may use this software under following terms of
GNU Affero GPL v3 license:

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version. For details contact
with the cloudover.io company: https://cloudover.io/


This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.


You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


from corenetwork.network_mixin import NetworkMixin
from corenetwork.os_mixin import OsMixin
from corenetwork.api_mixin import ApiMixin
from corenetwork.hook_interface import HookInterface
from corenetwork.utils.logger import log
import subprocess


class Hook(NetworkMixin, OsMixin, ApiMixin, HookInterface):
    task = None

    def start(self):
        super(Hook, self).finish()
        network = self.task.get_obj('Subnet')

        try:
            dnsmasq_procs = [int(x) for x in subprocess.check_output(['pgrep', 'dnsmasq']).splitlines()]
            ns_procs = [int(x) for x in subprocess.check_output(['sudo', 'ip', 'netns', 'pids', network.netns_name]).splitlines()]

            for pid in ns_procs:
                if pid in dnsmasq_procs:
                    try:
                        #os.kill(pid, 15)
                        subprocess.call(['sudo', 'ip', 'netns', 'exec', network.netns_name, 'kill', '-15', str(pid)])
                    except:
                        pass
        except Exception, e:
            log(msg="Failed to kill DHCP process: " + str(e), tags=('agent', 'dhcp', 'network'))

        network.set_prop('dhcp_running', False)
        network.save()
