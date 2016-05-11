MODULE = {
    'api': [
        'coredhcp.views.api',
    ],
    'hooks': {
        'agent.network.delete': ['coredhcp.hooks.network'],
    },
}
