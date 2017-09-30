MODULE = {
    'api': [
        'coredhcp.views.api',
    ],
    'agents': [
        {'type': 'dhcp', 'module': 'coredhcp.agents.dhcp', 'count': 2},
    ],
    'hooks': {
        'agent.network.delete': ['coredhcp.hooks.network'],
    },
    'cli': {
        'coredhcp': 'corecluster.cli.agent',
    }
}
